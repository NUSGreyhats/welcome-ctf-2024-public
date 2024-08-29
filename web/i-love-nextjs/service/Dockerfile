FROM node:18-alpine AS base

WORKDIR /app

COPY . .

RUN npm ci && npx prisma generate
RUN npm run build

CMD ["npm", "run", "start"]
