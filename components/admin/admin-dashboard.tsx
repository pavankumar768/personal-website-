"use client";

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";
import { useState } from "react";
import { AdminModule } from "@/components/admin/admin-module";

const queryClient = new QueryClient();

export function AdminDashboard() {
  const [active, setActive] = useState<"profile" | "skills" | "projects" | "certificates" | "achievements">("profile");

  return (
    <QueryClientProvider client={queryClient}>
      <div style={{ display: "grid", gap: 16 }}>
        <nav style={{ display: "flex", gap: 8, flexWrap: "wrap" }}>
          {["profile", "skills", "projects", "certificates", "achievements"].map((tab) => (
            <button key={tab} onClick={() => setActive(tab as typeof active)} style={{ padding: "8px 10px" }}>
              {tab}
            </button>
          ))}
        </nav>

        {active === "profile" ? (
          <AdminModule
            table="profiles"
            title="Profile Editor"
            fields={[
              { key: "full_name", label: "Full Name", required: true },
              { key: "headline", label: "Headline", required: true },
              { key: "bio", label: "Bio", required: true }
            ]}
          />
        ) : null}

        {active === "skills" ? (
          <AdminModule
            table="skills"
            title="Skills CRUD"
            fields={[
              { key: "name", label: "Skill Name", required: true },
              { key: "level", label: "Level", required: true }
            ]}
          />
        ) : null}

        {active === "projects" ? (
          <AdminModule
            table="projects"
            title="Project CRUD"
            fields={[
              { key: "title", label: "Project Title", required: true },
              { key: "description", label: "Description", required: true },
              { key: "url", label: "URL" }
            ]}
          />
        ) : null}

        {active === "certificates" ? (
          <AdminModule
            table="certificates"
            title="Certificate Upload/Manage"
            fields={[
              { key: "title", label: "Certificate Title", required: true },
              { key: "file_path", label: "Supabase Storage Path", required: true }
            ]}
          />
        ) : null}

        {active === "achievements" ? (
          <AdminModule
            table="achievements"
            title="Achievements CRUD"
            fields={[
              { key: "title", label: "Achievement Title", required: true },
              { key: "description", label: "Description", required: true }
            ]}
          />
        ) : null}
      </div>
    </QueryClientProvider>
  );
}
