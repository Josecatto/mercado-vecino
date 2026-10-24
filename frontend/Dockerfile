# syntax=docker/dockerfile:1

# ---------- Etapa 1: compilación ----------
FROM node:22-alpine AS build
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
# Las variables VITE_* quedan incrustadas en el JavaScript público: nunca un secreto
ARG VITE_API_URL=/api
RUN npm run build

# ---------- Etapa 2: servidor estático ----------
FROM nginxinc/nginx-unprivileged:1.27-alpine AS runtime
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 8080
