export default function ContactSection() {
  return (
    <section id="contact" className="bg-slate-50 py-20">
      <div className="mx-auto w-full max-w-6xl px-4 md:px-8">
        <h2 className="text-3xl font-bold text-slate-900">Contact</h2>
        <p className="mt-4 text-slate-700">Let&apos;s connect for opportunities, collaborations, or project ideas.</p>
        <a href="mailto:hello@example.com" className="mt-6 inline-flex rounded-lg bg-indigo-600 px-5 py-3 font-medium text-white hover:bg-indigo-700">
          hello@example.com
        </a>
      </div>
    </section>
  )
}
