<?php


$fileName = $_FILES['userfile']['name'];
$fileSize = $_FILES['userfile']['size'];
$fileType = $_FILES['userfile']['type'];
$fileNameCmps = explode(".", $fileName);
$fileExtension = strtolower(end($fileNameCmps));

$allowedfileExtensions = array('jpg', 'gif', 'png', 'zip', 'txt', 'xls', 'doc', 'php', 'svg');

if (in_array($fileExtension, $allowedfileExtensions))
    {

 	if (move_uploaded_file($_FILES['userfile']['tmp_name'],  $fileName)){
      		echo "El archivo ha sido cargado correctamente.";
   	}else{
      		echo "Ocurrió algún error al subir el fichero. No pudo guardarse.";
   	}
}else{
	echo "Ocurrió algún error al subir el fichero. extension no permitida.";
}
?>