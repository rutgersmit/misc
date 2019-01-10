<?php
error_reporting(-1);
ini_set('display_errors', 'On');

// Load the stamp and the photo to apply the watermark to
$imageurl = $_GET["source"];
//echo $imageurl;

if(empty($imageurl)){
	return;
}
$stamp = imagecreatefrompng($_SERVER["DOCUMENT_ROOT"]."/".$_GET["overlay"].".png");

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $imageurl); 
curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1); // good edit, thanks!
curl_setopt($ch, CURLOPT_BINARYTRANSFER, 1); // also, this seems wise considering output is image.
$data = curl_exec($ch);
curl_close($ch);

$im = imagecreatefromstring($data);


// Set the margins for the stamp and get the height/width of the stamp image
$marge_right = 0;
$marge_bottom = 0;
$sx = imagesx($stamp);
$sy = imagesy($stamp);

// Copy the stamp image onto our photo using the margin offsets and the photo 
// width to calculate positioning of the stamp. 
imagecopy($im, $stamp, imagesx($im) - $sx - $marge_right, imagesy($im) - $sy - $marge_bottom, 0, 0, imagesx($stamp), imagesy($stamp));

// Output and free memory
header('Content-type: image/png');

imagepng($im);
imagedestroy($im);
?>
