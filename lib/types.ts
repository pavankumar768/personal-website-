export type Role = "admin" | "editor" | "viewer";

export interface Profile {
  id: string;
  full_name: string;
  headline: string;
  bio: string;
}

export interface Skill {
  id: string;
  name: string;
  level: string;
}

export interface Project {
  id: string;
  title: string;
  description: string;
  url?: string;
}

export interface Certificate {
  id: string;
  title: string;
  file_path: string;
}

export interface Achievement {
  id: string;
  title: string;
  description: string;
}

export type EntityMap = {
  profiles: Profile;
  skills: Skill;
  projects: Project;
  certificates: Certificate;
  achievements: Achievement;
};

export type AdminTable = keyof EntityMap;
