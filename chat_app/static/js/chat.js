var channel="/chat";
var socket = io.connect('http://'+document.domain+':'+location.port+channel);
socket.on('connect',function(){
	socket.emit('my_connection',{data:'I\'m connected!'});
});

socket.on("message", function(message){
	refreshMessages(message);
});
function refreshMessages(message){
	$(".media-list").append('<li class="media"><div class="media-body"><div class="media"><div class="media-body">'+message.message+'<br/><small class="text-muted">'+message.author+' | '+message.createDate+'</small><hr/></div></div</li>');
}

$(function(){
	if (typeof $.cookie("realtime-chat-nickname") === 'undefined'){
		window.location ="/login"
	}else{
		$("#sendMessage").on("click", function(){
			sendMessage()
		});

		$('#messageText').keyup(function(e){
			if(e.keyCode == 13)
			{
				sendMessage();
			}
		});
	}

	function sendMessage(){
		$container=$('.media-list');
		$container[0].scrollTop = $container[0].scrollHeight;
		var messsage = $("#messageText").val();
		var author = $.cookie("realtime-chat-nickname");
		socket.emit('message', {data:{message: message, author: author}});
		$("#messageText").val("");
		$conatiner.animate({scrollTop: $container[0].scrollHeight},"slow");
	}
})


