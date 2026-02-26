const skills = ['React', 'TypeScript', 'Tailwind CSS', 'Node.js', 'Testing', 'UI/UX']

export default function SkillsSection() {
  return (
    <section id="skills" className="bg-slate-50 py-20">
      <div className="mx-auto w-full max-w-6xl px-4 md:px-8">
        <h2 className="text-3xl font-bold text-slate-900">Skills</h2>
        <div className="mt-6 flex flex-wrap gap-3">
          {skills.map((skill) => (
            <span key={skill} className="rounded-full bg-white px-4 py-2 text-sm font-medium text-slate-800 shadow-sm ring-1 ring-slate-200">
              {skill}
            </span>
          ))}
        </div>
      </div>
    </section>
  )
}
