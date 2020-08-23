<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Intro to Data Science</title>

    <link rel="stylesheet" href="style.css">
</head>

<body>
    <div class="container">
        <h1>Hasil prediksi</h1>
        <p class="center-text"><b><?= $page_data["hasil"]; ?></b></p>
        
        <?php if (isset($page_data["img"])) {?>
            <img src="<?= $page_data['img']; ?>" alt="">
        <?php }?>
        <br>
        <a href="index.php">&larr; Kembali ke Beranda</a>
    </div>
</body>

</html>