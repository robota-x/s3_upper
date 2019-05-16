source secrets.sh

get_upload_url() {
    curl "$APIURL?filename=$1&bucketname=$BUCKETNAME" 2>/dev/null
}
export -f get_upload_url

upload_file() {
    curl -X PUT -T $1 -L $2
}

for file in $(ls -p | grep -v /)
do
    echo uploading $file .......
    upload_url=$(get_upload_url $file)
    upload_file $file $upload_url
done