import Link from "next/link";

export default function HomePage() {
  return (
    <main style={{ padding: "2rem", maxWidth: 920, margin: "0 auto" }}>
      <h1>Portfolio Admin</h1>
      <p>This project now includes an authenticated admin area backed by Supabase.</p>
      <Link href="/admin">Go to /admin</Link>
    </main>
  );
}
