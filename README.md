# Personal Website Admin

This repository now includes a Next.js-based admin console at `/admin` using Supabase Auth session + role checks.

## Features

- `/admin` route guard validates signed-in session and checks `profiles.role === 'admin'`.
- Admin modules:
  - Profile editor
  - Skills CRUD
  - Project CRUD
  - Certificate upload/manage metadata
  - Achievements CRUD
- Reusable form components powered by **React Hook Form + Zod**.
- Data behavior includes optimistic create updates and refetch-on-save/delete via TanStack Query.

## Environment Variables

Copy `.env.example` to `.env.local` and configure:

- `NEXT_PUBLIC_SUPABASE_URL`
- `NEXT_PUBLIC_SUPABASE_ANON_KEY`

## Run

```bash
npm install
npm run dev
```
