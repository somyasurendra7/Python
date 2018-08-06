$(function(){
	$.ajax({
		url: '/getWish',
		type: 'GET',
		success: function(res){

			var wishObj = JSON.parse(res);

			$('#listTemplate').tmpl(wishObj).appendTo('#ulist');
		},
		error: function(error){
			console.log(error);
		}
	});
});
