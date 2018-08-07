$(function(){
	if ($.cookie("realtime-chat-nickname")){
		window.location = "/"
	} else{
		$("#frm-login").submit(function(event){
			event.preventDefault();
			if ($("#nickname").val() !==''){
				$.cookie("realtime-chat-nickname", $("#nickname").val());
				window.location = "/";
			}
		})
	}
})
