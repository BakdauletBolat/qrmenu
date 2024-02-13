cd qr-front
npm install
npm run build

cd ..

docker compose build
docker compose up -d