import Link from 'next/link'

export default function Home() {
  return (
    <main>
      <div>Hi this is my revolutionary tagline page</div>
      <Link href="/tagline">View taglines</Link>
      <br />
      <Link href="/add">Register</Link>
    </main>
  )
}
