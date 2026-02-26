'use client';

import { useEffect, useState } from 'react';

import { getCertificates, type Certificate } from '@/services';

export function CertificatesSection() {
  const [certificates, setCertificates] = useState<Certificate[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    async function loadCertificates() {
      try {
        setLoading(true);
        setError(null);
        const data = await getCertificates();
        setCertificates(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Failed to load certificates.');
      } finally {
        setLoading(false);
      }
    }

    loadCertificates();
  }, []);

  if (loading) return <p>Loading certificates...</p>;
  if (error) return <p role="alert">Could not load certificates: {error}</p>;
  if (certificates.length === 0) return <p>No certificates published yet.</p>;

  return (
    <section>
      <h2>Certificates</h2>
      <ul>
        {certificates.map((certificate) => (
          <li key={certificate.id}>
            {certificate.title}
            {certificate.issuer ? ` — ${certificate.issuer}` : ''}
          </li>
        ))}
      </ul>
    </section>
  );
}
