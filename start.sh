cd qr-front
npm install
npm run build

cd ..

docker-compose build
docker-compose up -d


cp nginx.conf /etc/nginx/sites-available/easymenu2.kz.conf

symlink_path="/etc/nginx/sites-enabled/easymenu2.kz.conf"

if [ -e "$symlink_path" ]; then
    echo "Symbolic link exists: $symlink_path"
else
    sudo ln -s /etc/nginx/sites-available/easymenu2.kz.conf /etc/nginx/sites-enabled/easymenu2.kz.conf
fi