import { PrismaClient } from '@prisma/client'

const prisma = new PrismaClient()

function makeId(length: number) {
  let result = ''
  const characters =
    'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
  const charactersLength = characters.length
  let counter = 0
  while (counter < length) {
    result += characters.charAt(Math.floor(Math.random() * charactersLength))
    counter += 1
  }
  return result
}

async function main() {
  console.log(JSON.stringify(process.env))
  await prisma.user.create({
    data: {
      name: makeId(99),
      tagline: `Damn how did you get this? ${process.env.FLAG}`,
    },
  })
}

main()
  .then(async () => {
    await prisma.$disconnect()
  })
  .catch(async (e) => {
    console.error(e)
    await prisma.$disconnect()
    process.exit(1)
  })
