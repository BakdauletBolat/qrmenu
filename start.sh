cd qr-front
npm install
npm run build

cd ..

docker-compose build
docker-compose up -d


cp nginx.conf /etc/nginx/sites-available/easymenu.kz.conf

symlink_path="/etc/nginx/sites-enabled/easymenu.kz.conf"

f [ -e "$symlink_path" ]; then
    echo "Symbolic link exists: $symlink_path"
else
    sudo ln -s /etc/nginx/sites-available/easymenu.kz.conf /etc/nginx/sites-enabled/easymenu.kz.conf
fi