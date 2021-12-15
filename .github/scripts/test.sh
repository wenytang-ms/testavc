while ! echo "$password" | grep -P ...
do
    read -r -s -p "Please enter a password: " password
done