<?php
error_reporting(E_ERROR | E_PARSE);

function r($u, $p){
    $s = getenv("SECRET_USER");
    if($u === $s) {
        $a = 0x1337;
    } else {
        $a = 0xb451c;
    }
    $q = pack("i$p", $a, $u);
    return base64_encode(md5($q.$s).$q);
}

function a($t) {
    $s = getenv("SECRET_USER");
    $r = unpack("a32h/a*d", base64_decode($t));
    $d = $r["d"];
    if(md5($d.$s) !== $r["h"]) {
        return false;
    }
    return unpack("ia/a*u", $d);
}

function g($d, $p) {
    if($d["a"] == 0x1337) {
        $r = "/pro";
    } else if($d["a"] == 0xb451c) {
        $r = "/basic";
    } else {
        return "Invalid permissions!";
    }
    if(strpos($p, "../") !== false) {
        return "Go away hacker!";
    }
    if(!file_exists($r.$p) || !is_file($r.$p)){
        return "File not exist!";
    }
    $c = file_get_contents($r . $p);
    if($c === false){
        return "File not exist!";
    }
    $u = htmlspecialchars($d["u"]);
    return "<h2>Hello, $u!</h2><br>$c";
}


$a = $_GET["a"];
if($a == "r") {
    $u = $_GET["u"];
    $p = $_GET["p"];
    if(!$u || !$p) {
        die("Inval");
    }
    die(r($u, $p));
}

if($a == "g") {
    $t = $_GET["t"];
    $p = $_GET["p"];
    if(!$t || !$p) {
        die("Inval");
    }
    $d = a($t);
    if(!$d) {
        die("Inval");
    }
    die(g($d, $p));
}

show_source("api.php");