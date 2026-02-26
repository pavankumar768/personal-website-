export default function HeroSection() {
  return (
    <section id="hero" className="bg-gradient-to-br from-slate-900 via-slate-800 to-indigo-900 py-28 text-white">
      <div className="mx-auto w-full max-w-6xl px-4 md:px-8">
        <p className="mb-4 text-sm uppercase tracking-[0.2em] text-indigo-200">Welcome</p>
        <h1 className="max-w-3xl text-4xl font-bold leading-tight md:text-6xl">Hi, I&apos;m Your Name — Frontend Developer</h1>
        <p className="mt-6 max-w-2xl text-base text-slate-200 md:text-lg">
          I design and build responsive web experiences with React, TypeScript, and modern UI systems.
        </p>
        <a href="#projects" className="mt-8 inline-flex rounded-lg bg-white px-6 py-3 font-semibold text-slate-900 transition hover:bg-slate-200">
          View Projects
        </a>
      </div>
    </section>
  )
}
