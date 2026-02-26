'use client';

import { useEffect, useState } from 'react';

import { getProjects, type Project } from '@/services';

export function ProjectsSection() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadProjects() {
      try {
        setLoading(true);
        setError(null);
        const data = await getProjects();
        setProjects(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load projects.');
      } finally {
        setLoading(false);
      }
    }

    loadProjects();
  }, []);

  if (loading) return <p>Loading projects...</p>;
  if (error) return <p role="alert">Could not load projects: {error}</p>;
  if (projects.length === 0) return <p>No projects published yet.</p>;

  return (
    <section>
      <h2>Projects</h2>
      {projects.map((project) => (
        <article key={project.id}>
          <h3>{project.title}</h3>
          {project.description ? <p>{project.description}</p> : null}
        </article>
      ))}
    </section>
  );
}
