'use client';

import { useEffect, useState } from 'react';

import { getProfile, type Profile } from '@/services';

export function ProfileSection() {
  const [profile, setProfile] = useState<Profile | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadProfile() {
      try {
        setLoading(true);
        setError(null);
        const data = await getProfile();
        setProfile(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load profile.');
      } finally {
        setLoading(false);
      }
    }

    loadProfile();
  }, []);

  if (loading) return <p>Loading profile...</p>;
  if (error) return <p role="alert">Could not load profile: {error}</p>;
  if (!profile) return <p>No profile content published yet.</p>;

  return (
    <section>
      <h1>{profile.full_name}</h1>
      {profile.headline ? <p>{profile.headline}</p> : null}
      {profile.bio ? <p>{profile.bio}</p> : null}
    </section>
  );
}
