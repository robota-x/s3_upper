source secrets.sh

get_upload_url() {
    curl "$APIURL?filename=$1&bucketname=$BUCKETNAME"
}

upload_file() {
    curl -X PUT -T $1 -L $2
}


a=$(get_upload_url testfile.jpg)

echo done
echo $a