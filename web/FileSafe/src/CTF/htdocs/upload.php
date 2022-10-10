<?php
$target_dir = "uploads/";
$target_file = $target_dir . basename($_POST["filename"]);
$uploadOk = 1;
$imageFileType = strtolower(pathinfo($target_file,PATHINFO_EXTENSION));

if (file_exists($target_file)) {
    echo "Sorry, file already exists.";
    $uploadOk = 0;
}

if ($_FILES["fileUploaded"]["size"] > 500000) {
    echo "Sorry, your file is too large.";
    $uploadOk = 0;
}

if ($uploadOk == 1){
    move_uploaded_file($_FILES["fileUploaded"]["tmp_name"], $target_file);
    header('Location: file.php?file='.basename($_POST["filename"]));
}
?>
