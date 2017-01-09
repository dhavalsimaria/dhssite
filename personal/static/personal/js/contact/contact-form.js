$(function(){
	//alert("Script loaded.");
	$(document).on('submit', '#ContactForm', function(event){
		event.preventDefault();
		//alert("Alert entered function.");
		$.ajax({
			type: 'POST',
			url: '/contact/add/',
			data: $("#ContactForm").serialize(),
			//csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
			success: function(data){
				if(data.status == 'error'){
					$("#message_post").html("<div class='errorMessage'>ERROR: " + data.msg + "!</div>"); 
					document.ContactForm.submitf.value='Resend >>';
					document.ContactForm.submitf.disabled=false;
				}else {
					$("#message_post").html("<div class='successMessage'>Hi " + data.welcome_name + "! Glad to meet you. I'll definitely contact you shortly.</div>"); 
					$("#submitf").value='Send >>';
				}
			}
		}, "json");

		return false;
	});
});

/*$(function(){
	$("#ContactForm").submit(function(){
		$("#submitf").value='Please wait...';
		alert("Control reached the script.");
		$.post("/contact/add/", $("#ContactForm").serialize(),
		function(data){ 
			alert("Alert entered function.");
			if(data.status == 'error'){ 
					$("#message_post").html("<div class='errorMessage'>ERROR: " + data.msg + "!</div>"); 
					document.ContactForm.submitf.value='Resend >>';
					document.ContactForm.submitf.disabled=false;
			} else {
				$("#message_post").html("<div class='successMessage'>Hi! Glad to meet you. I'll definitely contact you shortly.</div>"); 
				$("#submitf").value='Send >>';
				}
		}, "json");
		
		return false;
		
	});
});
*/
/*
$(function(){
	$("#ContactForm").submit(function(){
		$("#submitf").value='Please wait...';
		csrfmiddlewaretoken: $('input[name = csrfmiddlewaretoken]').val();
		//$.post("process.php?send=comments", $("#ContactForm").serialize(),
		$.post("/contact/add/", $("#ContactForm").serialize(),
		function(data){ 
			if(data.frm_check == 'error'){ 
			
					$("#message_post").html("<div class='errorMessage'>ERROR: " + data.msg + "!</div>"); 
					document.ContactForm.submitf.value='Resend >>';
					document.ContactForm.submitf.disabled=false;
			} else {
				$("#message_post").html("<div class='successMessage'>Your message has been sent successfully!</div>"); 
				$("#submitf").value='Send >>';
				}
		}, "json");
		
		return false;
		
	});
});
*/