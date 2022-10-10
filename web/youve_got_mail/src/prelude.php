<?php
require_once("config.php");
require_once("db.php");
session_start();

echo "<head>
<title>eMailers - Online community for mail and stamp enthousiasts</title>
<style>
  html {
    max-width: 70ch;
    padding: 3em 1em;
    margin: auto;
    line-height: 1.75;
    font-size: 1.25em;
    font-family: Helvetica, 'Trebuchet MS', Verdana, sans-serif;
  }
  h1,h2,h3,h4,h5,h6 {
    margin: 1em 0 0.5em;
  }
  p,ul,ol {
    margin-bottom: 2em;
  }
</style>
</head>
<h1><a href='/'>eMailers</a></h1>";
