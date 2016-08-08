<?php

$handle = fopen ("php://stdin","r");
fscanf($handle,"%d %d",$n,$m);

echo $m % $n == 0 ? 0 : $n - ($m % $n)
?>
