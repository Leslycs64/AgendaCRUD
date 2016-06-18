$(document).ready(function() {
  $('.button').on('click', function() {
    $('.content').toggleClass('isOpen');
  });
});

function isEmptyField(campo){
	var field = document.getElementById(campo).value;
	if(field.length == 0){
		return false;
	}else{
		return true;
	}
}

function enablePaterno(){                     
    var campo = document.getElementById("id_apaterno");
    if (isEmptyField("id_nombre")){
    	campo.disabled = false;	
    	campo.focus();
    }
    
}

function enableMaterno(){
    var campo = document.getElementById("id_amaterno");
    if (isEmptyField("id_apaterno")){
    	campo.disabled = false;	
    	campo.focus();
    }
}

function enableCorreo(){
	var campo = document.getElementById("id_correo");
    if (isEmptyField("id_amaterno")){
    	campo.disabled = false;	
    	campo.focus();
    }	
}

function enableTelefono(){
	var campo = document.getElementById("id_telefono");
    if (isEmptyField("id_correo")){
    	campo.disabled = false;	
    	campo.focus();
    }	
}
/*.removeAttr("disabled");*/