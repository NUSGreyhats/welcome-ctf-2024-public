import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Revolutionary login',
  description: 'Powered by vercel!',
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
