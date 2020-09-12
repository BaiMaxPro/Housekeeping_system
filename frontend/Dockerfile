FROM node:lts-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install @vue/cli-service --no-save --registry=https://registry.npm.taobao.org && \
    npm install --registry=https://registry.npm.taobao.org --only=prod
COPY . .
RUN npm run build

FROM nginx:stable-alpine as production
RUN mkdir /app
COPY --from=build /app/dist /app
COPY nginx.conf /etc/nginx/nginx.conf
