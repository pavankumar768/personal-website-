export default function Footer() {
  return (
    <footer className="border-t border-slate-200 bg-slate-50">
      <div className="mx-auto flex w-full max-w-6xl flex-col items-center justify-between gap-3 px-4 py-6 text-sm text-slate-600 md:flex-row md:px-8">
        <p>© {new Date().getFullYear()} Portfolio. All rights reserved.</p>
        <a href="#hero" className="font-medium text-indigo-600 hover:text-indigo-700">
          Back to top
        </a>
      </div>
    </footer>
  )
}
