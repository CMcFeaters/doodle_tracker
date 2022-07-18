<?php
$val=exec("python3 doodle_sort.py",$output,$retval);
//echo "most recent doodle: ".$val;

$fileurl='/mnt/raid1/shared/doodle/'.$val;
//echo($fileurl);

//header('Content-Type: image/jpeg');
//header('Content-Length: '.filesize($fileurl));
//readfile($fileurl);
header('Content-Type: image/jpeg');
header('Content-Length: '.filesize($fileurl));
readfile($fileurl);

?>
