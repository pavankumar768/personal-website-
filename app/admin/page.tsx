"use client";

import Link from "next/link";
import { AdminDashboard } from "@/components/admin/admin-dashboard";
import { useAdminAuth } from "@/hooks/use-admin-auth";

export default function AdminPage() {
  const { loading, signedIn, role, error } = useAdminAuth();

  if (loading) {
    return <main style={{ padding: "2rem" }}>Checking session...</main>;
  }

  if (!signedIn) {
    return (
      <main style={{ padding: "2rem" }}>
        <h1>Admin</h1>
        <p>You must sign in first.</p>
        <Link href="/">Return Home</Link>
      </main>
    );
  }

  if (role !== "admin") {
    return (
      <main style={{ padding: "2rem" }}>
        <h1>Admin</h1>
        <p>Forbidden: your role does not have admin access.</p>
      </main>
    );
  }

  return (
    <main style={{ padding: "2rem", maxWidth: 980, margin: "0 auto" }}>
      <h1>Admin Console</h1>
      <p>Manage your profile content across all portfolio modules.</p>
      {error ? <p style={{ color: "crimson" }}>{error}</p> : null}
      <AdminDashboard />
    </main>
  );
}
