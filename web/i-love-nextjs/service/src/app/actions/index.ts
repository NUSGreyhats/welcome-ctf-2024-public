'use server'

import { PrismaClient, Prisma } from '@prisma/client'
import { z } from 'zod'

const prisma = new PrismaClient()

export async function getTagline(username: string) {
  const user = await prisma.user.findFirst({
    where: {
      name: username,
    },
  })

  if (!user) return `User ${username} does not exist!`

  return user.tagline
}

export async function addTagline(
  prevState: { message: string },
  formData: FormData
) {
  const schema = z.object({
    username: z.string().min(1),
    tagline: z.string().min(1),
  })

  const parse = schema.safeParse({
    username: formData.get('username'),
    tagline: formData.get('tagline'),
  })

  if (!parse.success) return { message: 'Failed to create tagline!' }

  const data = parse.data

  try {
    await prisma.user.create({
      data: {
        name: data.username,
        tagline: data.tagline,
      },
    })
  } catch (e) {
    if (e instanceof Prisma.PrismaClientKnownRequestError && e.code === 'P2002')
      return { message: 'Username already exists in database :(' }
    return { message: 'Error occurred when creating tagline :(' }
  }
  return { message: 'Successfully created tagline!' }
}
