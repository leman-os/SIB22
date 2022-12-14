if (Test-Path $args[0]) {
    $ftype = Get-Item $args[0]
    if($ftype.PSIsContainer) {
    echo "dir"
    }
    else {echo "file"}
}
else {echo "not exist"}

