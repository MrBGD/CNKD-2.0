
$source = 'https://github.com/Endermanch/MalwareDatabase/blob/master/ransomwares/Petya.A.zip'
$destination = 'D:\python\CNKD\petya'
Invoke-WebRequest -Uri $source -Outfile $destination