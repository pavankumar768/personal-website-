import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom'
import App from './App'
import './index.css'

function AdminPage() {
  return <div className="p-8 text-xl font-semibold">Admin module placeholder</div>
}

function ProjectDetailPage() {
  return <div className="p-8 text-xl font-semibold">Project detail placeholder</div>
}

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/admin" element={<AdminPage />} />
        <Route path="/projects/:id" element={<ProjectDetailPage />} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  </StrictMode>,
)
