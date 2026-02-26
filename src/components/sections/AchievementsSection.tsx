'use client';

import { useEffect, useState } from 'react';

import { getAchievements, type Achievement } from '@/services';

export function AchievementsSection() {
  const [achievements, setAchievements] = useState<Achievement[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadAchievements() {
      try {
        setLoading(true);
        setError(null);
        const data = await getAchievements();
        setAchievements(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load achievements.');
      } finally {
        setLoading(false);
      }
    }

    loadAchievements();
  }, []);

  if (loading) return <p>Loading achievements...</p>;
  if (error) return <p role="alert">Could not load achievements: {error}</p>;
  if (achievements.length === 0) return <p>No achievements published yet.</p>;

  return (
    <section>
      <h2>Achievements</h2>
      <ul>
        {achievements.map((achievement) => (
          <li key={achievement.id}>
            <strong>{achievement.title}</strong>
            {achievement.description ? ` — ${achievement.description}` : ''}
          </li>
        ))}
      </ul>
    </section>
  );
}
