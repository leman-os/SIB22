if ($args[2])
{
    echo "Error. More than 2 parameters."
    Exit
}
else
{
    if($args[0] -eq "crypt")
    {
        echo "Encrypting..."
        $res = [Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes($args[1]))
    }
    elseif($args[0] -eq "decrypt")
    {
        echo "Decrypting..."
        $res = [Text.Encoding]::Utf8.GetString([Convert]::FromBase64String($args[1]))
    }
    else 
    {
        echo "Bad parameters"
        Exit
    }
}

echo $res