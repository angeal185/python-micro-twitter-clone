jQuery(function(){var e=jQuery('script[src*="share.js"]').attr("src"),t=function(t,o){var i=RegExp("[?&]"+t+"=([^&]*)").exec(e);return i&&decodeURIComponent(i[1].replace(/\+/g," "))||o},o=t("static","social"),i=encodeURIComponent(window.location.href),r=(window.location.hostname,escape(jQuery("title").text())),a="http://twitter.com/home?status="+r+"%20"+i,p="http://www.facebook.com/sharer.php?u="+i,d="https://plus.google.com/share?url="+i,s='<div id="socialdrawer"><span>Share<br/></span><div id="sicons"><a href="'+a+'" id="twit" title="Share on twitter"><img src="'+o+'/twitter.png"  alt="Share on Twitter" width="32" height="32" /></a><a href="'+p+'" id="facebook" title="Share on Facebook"><img src="'+o+'/facebook.png"  alt="Share on facebook" width="32" height="32" /></a><a href="'+d+'" id="gplus" title="Share on Google Plus"><img src="'+o+'/gplus-32.png"  alt="Share on Google Plus" width="32" height="32" /></a></div></div>';jQuery("body").append(s);var h=jQuery("#socialdrawer");h.css({opacity:".7","z-index":"3000",background:"#FFF",border:"solid 1px #666","border-width":" 1px 0 0 1px",height:"20px",width:"40px",position:"fixed",bottom:"0",right:"0",padding:"2px 5px",overflow:"hidden","-webkit-border-top-left-radius":" 12px","-moz-border-radius-topleft":" 12px","border-top-left-radius":" 12px","-moz-box-shadow":" -3px -3px 3px rgba(0,0,0,0.5)","-webkit-box-shadow":" -3px -3px 3px rgba(0,0,0,0.5)","box-shadow":" -3px -3px 3px rgba(0,0,0,0.5)"}),jQuery("#socialdrawer a").css({"float":"left",width:"32px",margin:"3px 2px 2px 2px",padding:"0",cursor:"pointer"}),jQuery("#socialdrawer span").css({"float":"left",margin:"2px 3px","text-shadow":" 1px 1px 1px #FFF",color:"#444","font-size":"12px","line-height":"1em"}),jQuery("#socialdrawer img").hide(),h.click(function(){jQuery(this).animate({height:"40px",width:"160px",opacity:.95},300),jQuery("#socialdrawer img").show()}),h.mouseleave(function(){return h.animate({height:"20px",width:"40px",opacity:.7},300),jQuery("#socialdrawer img").hide(),!1})});