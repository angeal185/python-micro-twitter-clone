def index():
    if auth.user: redirect(URL('home'))
    return locals()

@auth.requires_login()
def home():
    '''First point of call, contains all weets and all weets of those you follow'''

    db.weets.posted_by.default = me
    db.weets.posted_on.default = request.now

    crud.settings.formstyle = 'table2cols'
    form = crud.create(db.weets)
    my_followees = db(db.followers.follower==me)
    me_and_my_followees = [me]+[row.followee for row in my_followees.select(db.followers.followee)]
    weets = db(db.weets.posted_by.belongs(me_and_my_followees)).select(orderby=~db.weets.posted_on,limitby=(0,100))
    return locals()

def wall():
    user = db.auth_user(request.args(0) or me)
    if not user:
        redirect(URL('home'))
    weets = db(db.weets.posted_by==user.id).select(orderby=~db.weets.posted_on,limitby=(0,100))
    return locals()

@auth.requires_login()
def search():
    form = SQLFORM.factory(Field('name',requires=IS_NOT_EMPTY()))
    if form.accepts(request):
        tokens = form.vars.name.split()
        query = reduce(lambda a,b:a&b,
                       [db.auth_user.first_name.contains(k)|db.auth_user.last_name.contains(k) \
                            for k in tokens])
        people = db(query).select(orderby=db.auth_user.first_name|db.auth_user.last_name,left=db.followers.on(db.followers.followee==db.auth_user.id))        
    else:
        people = []        
    return locals()

@auth.requires_login()
def follow():
    if request.env.request_method!='POST': raise HTTP(400)
    if request.args(0) =='follow' and not db.followers(follower=me,followee=request.args(1)):
        db.followers.insert(follower=me,followee=request.args(1))
    elif request.args(0)=='unfollow':
        db(db.followers.follower==me)(db.followers.followee==request.args(1)).delete()




def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
