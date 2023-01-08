provider=$1
version=$2

if [ -z "$provider" ]; then
    echo "provider (arg 1) must be set"
    exit 1
fi

if [ -z "$version" ]; then
    echo "version (arg 2) must be set"
    exit 1
fi

echo "building docs for: $provider $version"


# install packages

pip install -q -r requirements.txt

# download and unzip stackql binary

if [ ! -f stackql ]
then
    wget -q https://releases.stackql.io/stackql/latest/stackql_linux_amd64.zip
    unzip stackql_linux_amd64.zip
fi

chmod +x stackql

# clear .stackql folder
rm -rf ./.stackql

# start server if not running
echo "checking if server is running"
if [ -z "$(ps | grep stackql)" ]; then
    echo "starting server..."
    nohup ./stackql --pgsrv.port=5444 srv &
    sleep 15
else
    echo "server is already running"
fi

python3 docgen/generate_docs.py $provider $version
