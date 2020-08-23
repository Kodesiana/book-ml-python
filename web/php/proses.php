<?php

if ($_SERVER['REQUEST_METHOD'] !== "POST") {
    die("Harus POST!");
}

function send_curl($url, $body)
{
    $ch = curl_init();
    $options = array(
        CURLOPT_URL => $url,
        CURLOPT_HEADER => true,
        CURLOPT_FOLLOWLOCATION => true,
        CURLOPT_POST => 1,
        CURLOPT_HTTPHEADER => array('Content-Type: multipart/form-data'),
        CURLOPT_POSTFIELDS => $body,
        CURLOPT_RETURNTRANSFER => true,
        CURLOPT_FAILONERROR => true
    );
    curl_setopt_array($ch, $options);

    $response = curl_exec($ch);
    $header_size = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
    $header = substr($response, 0, $header_size);
    $body = substr($response, $header_size);

    curl_close($ch);
    return json_decode($body, true);
}

function predict_regression()
{
    if (!isset($_POST["ruangan"])) {
        $data["hasil"] = "Tidak diinputkan.";
        return $data;
    }

    $req = array("rm" => (int)$_POST["ruangan"]);
    $response = send_curl("http://localhost:3001/predict", $req);

    $data["hasil"] = $response["predicted"];
    return $data;
}

function predict_classification() 
{
    if (!isset($_FILES["file"])) {
        $data["hasil"] = "Gambar tidak diinputkan.";
        return $data;
    }

    if (!getimagesize($_FILES["file"]["tmp_name"])) {
        $data["hasil"] = "File bukan gambar.";
        return $data;
    }

    $target = tempnam(sys_get_temp_dir(), 'gm');
    move_uploaded_file($_FILES['file']['tmp_name'], $target);

    $req = array('file' => new CURLFile($target));        
    $response = send_curl("http://localhost:3002/predict", $req);

    $img_data = file_get_contents($target);
    $img_encoded = 'data:image/jpg;base64,' . base64_encode($img_data);
    unlink($target);

    $data["hasil"] = $response["predicted"];
    $data["img"] = $img_encoded;
    return $data;
}

$page_data = array();
if ($_POST["predict_mode"] == "regresi")
{
    $page_data = predict_regression();
}
else 
{
    $page_data = predict_classification();
}

require('hasil.php');
