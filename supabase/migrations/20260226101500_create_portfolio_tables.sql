create table if not exists public.profile (
  id bigint generated always as identity primary key,
  full_name text not null,
  headline text,
  bio text,
  location text,
  email text,
  phone text,
  avatar_url text,
  resume_url text,
  display_order int not null default 0,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.skills (
  id bigint generated always as identity primary key,
  name text not null,
  category text,
  proficiency text,
  display_order int not null default 0,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.projects (
  id bigint generated always as identity primary key,
  title text not null,
  description text,
  tech_stack text[] default '{}',
  repo_url text,
  live_url text,
  image_url text,
  display_order int not null default 0,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.certificates (
  id bigint generated always as identity primary key,
  title text not null,
  issuer text,
  issue_date date,
  credential_url text,
  display_order int not null default 0,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.achievements (
  id bigint generated always as identity primary key,
  title text not null,
  description text,
  award_date date,
  display_order int not null default 0,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create table if not exists public.contact_messages (
  id bigint generated always as identity primary key,
  name text not null,
  email text not null,
  subject text,
  message text not null,
  is_read boolean not null default false,
  created_at timestamptz not null default now()
);

create index if not exists profile_display_order_idx on public.profile (display_order, id);
create index if not exists skills_display_order_idx on public.skills (display_order, id);
create index if not exists projects_display_order_idx on public.projects (display_order, id);
create index if not exists certificates_display_order_idx on public.certificates (display_order, id);
create index if not exists achievements_display_order_idx on public.achievements (display_order, id);
create index if not exists contact_messages_created_at_idx on public.contact_messages (created_at desc);
