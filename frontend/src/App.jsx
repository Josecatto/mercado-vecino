import { useEffect, useState } from 'react'

export default function App() {
  const [tiendas, setTiendas] = useState([])
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch('/api/tiendas')
      .then((r) => r.json())
      .then(setTiendas)
      .catch(() => setError('La API no está disponible todavía'))
  }, [])

  return (
    <main style={{ fontFamily: 'sans-serif', padding: 24 }}>
      <h1>Mercado Vecino</h1>
      <h2>Catálogo de tiendas</h2>
      {error && <p>{error}</p>}
      <ul>
        {tiendas.map((t) => (
          <li key={t.id}>{t.nombre} ({t.barrio})</li>
        ))}
      </ul>
    </main>
  )
}
