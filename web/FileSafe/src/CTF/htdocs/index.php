<!DOCTYPE html>
<html lang="en">
  <head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
    <title>FileSafe</title>
    <link href="cover.css" rel="stylesheet">
    <meta charset="UTF-8">
  </head>
<body class="text-center vsc-initialized">

    <div class="cover-container d-flex w-100 h-100 p-3 mx-auto flex-column">
      <header class="masthead mb-auto">
        <div class="inner">
          <h3 class="masthead-brand">FileSafe</h3>
          <nav class="nav nav-masthead justify-content-center">
            <a class="nav-link active" href="#">Home</a>
          </nav>
        </div>
      </header>

      <main role="main" class="inner cover">
        <h1 class="cover-heading">Share your Files</h1>
        <p class="lead">FileSafe is a top of the line file storage/sharing service you can use with ease. Don't worry, you files are totally safe with us!</p>

        <form action="upload.php" method="post" enctype="multipart/form-data">
            <?php
               echo '<input type="hidden" id="filename" name="filename" value="'.  uniqid() . '.png">'
            ?>
            <div class="mb-3">
              <label for="formFile" class="form-label">Upload a file to store</label>
              <input class="form-control" type="file" id="fileUploaded" name="fileUploaded"> 
            </div>
            <button type="submit" class="btn btn-lg btn-secondary">Submit</button>
        </form>
      </main>

      <footer class="mastfoot mt-auto">
        <div class="inner">
          <p>Made with &lt;3 by Y33t</a></p>
        </div>
      </footer>

    </div>
</body>
</html>
