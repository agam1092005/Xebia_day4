import './globals.css'

export const metadata = {
  title: 'Auth App',
  description: 'Minimalist Registration and Login',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
