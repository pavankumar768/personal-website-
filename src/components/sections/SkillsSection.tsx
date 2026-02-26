'use client';

import { useEffect, useState } from 'react';

import { getSkills, type Skill } from '@/services';

export function SkillsSection() {
  const [skills, setSkills] = useState<Skill[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadSkills() {
      try {
        setLoading(true);
        setError(null);
        const data = await getSkills();
        setSkills(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load skills.');
      } finally {
        setLoading(false);
      }
    }

    loadSkills();
  }, []);

  if (loading) return <p>Loading skills...</p>;
  if (error) return <p role="alert">Could not load skills: {error}</p>;
  if (skills.length === 0) return <p>No skills published yet.</p>;

  return (
    <section>
      <h2>Skills</h2>
      <ul>
        {skills.map((skill) => (
          <li key={skill.id}>
            {skill.name}
            {skill.category ? ` — ${skill.category}` : ''}
          </li>
        ))}
      </ul>
    </section>
  );
}
