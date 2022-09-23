<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP Practical</title>
</head>
<body><br><br>
    <?php
        echo "Hello! <b>".$_REQUEST["name"]."</b>. <br>".
        "You are a <b>".$_REQUEST["gender"]."</b>. <br>
        And your hobbies are <br>";
        echo "<b>";
        if (isset($_REQUEST["Cricket"]))
            echo $_REQUEST["Cricket"], "<br>";

        if (isset($_REQUEST["Soccer"]))
            echo $_REQUEST["Soccer"], "<br>";
            
        if (isset($_REQUEST["Hockey"]))
            echo $_REQUEST["Hockey"], "<br>";
        echo "</b>";
    ?>
</body>
</html>