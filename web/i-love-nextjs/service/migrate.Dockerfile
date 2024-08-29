FROM node:18-alpine AS base

WORKDIR /app

COPY migrate.sh package.json package-lock.json ./
COPY prisma ./prisma

RUN npm ci && npx prisma generate

CMD ["npx", "prisma", "migrate", "deploy"]
