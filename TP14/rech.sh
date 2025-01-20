echo "$(date +"%Y%m%d") + $(debsecan --suite $(lsb_release --codename --short) | wc -l)" >> faille.txt

if [ "$(debsecan --suite $(lsb_release --codename --short) --only-fixed | wc -l)" -gt 0 ]; then 
    sudo apt update
fi

