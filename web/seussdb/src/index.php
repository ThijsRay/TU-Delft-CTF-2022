<?php

error_reporting(E_ERROR | E_PARSE);

function performQuery($query) {
    $db = new SQLite3('./books.db', SQLITE3_OPEN_READONLY);
    $result = $db->query($query);
    if ($result == FALSE) {
        echo "There was an error executing the following SQLite query: $query<br>";
        echo "The error was: " . $db->lastErrorMsg();
        die();
    }
    return $result;
}

$books = [];

if (isset($_GET["year"])) {
    $year = $_GET["year"];
    if (preg_match("/^[0-9]/", $year)) { // intentionally only checking for prefix, not entire string
        $books = performQuery("SELECT * FROM books WHERE year = $year");
    } else {
        echo "Invalid year: " . $_GET["year"] . ". Must start with a digit.";
        die();
    }
} else {
    $books = performQuery("SELECT * FROM books");
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/water.css@2/out/light.css">
    <title>Dr. Seuss Fanclub</title>
</head>
<body>
    <h1>Dr. Seuss Fanclub - SeussDB</h1>
    <p>Do you like Dr. Seuss as much as we do? Ran out of things to read? Find your next Dr. Seuss book in our interactive Dr. Seuss book database! Now featuring a filter for finding books released in a specific year!</p>


    <hr>

    <h2>Books</h2>

    <table>
        <thead>
            <tr>
                <th>Title</th>
                <th>Year</th>
            </tr>
        </thead>
        <tbody>
            <?php while ($row = $books->fetchArray()) { ?>
                <tr>
                    <td><?php echo $row["title"] ?></td>
                    <td><?php echo $row["year"] ?></td>
                </tr>
            <?php } ?>
        </tbody>
    </table>

    <hr>

    <h2>Filter by Year</h2>

    <form>
        <label for="year">Year</label>
        <input type="text" name="year" placeholder="1900">
        <input type="submit" value="Filter">
    </form>
</body>
</html>
