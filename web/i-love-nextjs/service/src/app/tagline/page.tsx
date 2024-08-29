'use client'

import { getTagline } from '@/app/actions'
import { ChangeEventHandler, FormEventHandler, useState } from 'react'

export default function GetTagline() {
  const [username, setUsername] = useState('')
  const [output, setOutput] = useState<string | null>(null)

  const handleChange: ChangeEventHandler<HTMLInputElement> = (event) => {
    setUsername(event.target.value)
  }

  const handleSubmit: FormEventHandler<HTMLFormElement> = async (event) => {
    event.preventDefault()
    const tagline = await getTagline(username)
    setOutput(tagline)
  }

  return (
    <main>
      <div>Retrieve your very own tagline!</div>
      <form onSubmit={handleSubmit}>
        <input type="text" value={username} onChange={handleChange} />
        <button type="submit">Retrieve</button>
      </form>
      {output !== null && output}
    </main>
  )
}
