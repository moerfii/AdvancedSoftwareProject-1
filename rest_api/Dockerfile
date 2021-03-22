# start rest api
FROM node:14.16.0
ENV NODE_ENV=production

WORKDIR /app

COPY ["package.json", "package-lock.json*", "./"]

RUN npm install --production

COPY . .

ENV POSTGRES_USER=ase_user
ENV POSTGRES_PASSWORD=aseisgreat

CMD [ "node", "src/server.js" ]