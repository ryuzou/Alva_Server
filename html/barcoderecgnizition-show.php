<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Refresh" content="1">
    <title>Barcode-Watcher</title>
</head>
<body>
<?php
$bookid = 0;
$barcode = 0;
$link = new mysqli("db", "root", "password", "Alva_Server");
if ($link->connect_errno) {
    printf("Connect failed: %s\n", $link->connect_error);
    exit();
}
$barcodelog_result = $link->query("SELECT barcode, id FROM D_Barcode_log");
if (!$barcodelog_result) {
    throw new Exception("Database Error [{$link->errno}] {$link->error}");
}
while ($row = $barcodelog_result->fetch_assoc()) {
    $barcode = $row["barcode"];
}
$barcode_result = $link->query("SELECT Barcode, Number FROM D_Barcode");
if (!$barcode_result) {
    throw new Exception("Database Error [{$link->errno}] {$link->error}");
}
while ($row = $barcode_result->fetch_assoc()) {
    if (strcmp($barcode, $row["Barcode"]) == 0) {
        $bookid = $row["Number"];
    }
}
$book_result = $link->query("SELECT id, AdvancedbookdataDIR, book_title, book_genre, book_author FROM D_Bookdata");
if (!$book_result) {
    throw new Exception("Database Error [{$link->errno}] {$link->error}");
}
while ($row = $book_result->fetch_assoc()) {
    if (strcmp($bookid, $row["id"]) == 0) {
        $AdvancedbookdataDIR = $row["AdvancedbookdataDIR"];
        $book_title = $row["book_title"];
        $book_genre = $row["book_genre"];
        $book_author = $row["book_author"];
    }
}
?>
<img src=<?php echo $bookpath; ?>>
<br>
本のタイトル：<?php echo $book_title; ?>
<br>
本のジャンル：<?php echo $book_genre; ?>
<br>
<?php
if (empty($AdvancedbookdataDIR) == false) {
    $bookdatapath = "AdvancedBookDatas/" . $AdvancedbookdataDIR + "/index.html";
    echo "本について";
    echo "<br />";
    readfile($bookdatapath);
}
?>
</body>
</html>