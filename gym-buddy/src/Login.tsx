import { useCallback, useState } from '@lynx-js/react'

export function LoginPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [user, setUser] = useState<any>(null)
  const [error, setError] = useState<string | null>(null)

  const handleLogin = useCallback(async () => {
    try {
      const res = await fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      })

      const data = await res.json()
      if (!res.ok) {
        throw new Error(data.error?.message || 'Login failed')
      }

      setUser(data.user)
      setError(null)

      // Optionally, store token in localStorage for later use
      localStorage.setItem('access_token', data.access_token)

    } catch (err: any) {
      setError(err.message)
      setUser(null)
    }
  }, [email, password])

  return (
    <view>
        <text>Hello</text>
    </view>
  )
}
