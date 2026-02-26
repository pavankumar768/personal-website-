import { supabaseClient } from '@/lib/supabaseClient';
import type { PublicTable } from '@/lib/database.types';

export type Project = PublicTable<'projects'>;

export async function getProjects() {
  const { data, error } = await supabaseClient
    .from('projects')
    .select('*')
    .order('display_order', { ascending: true })
    .order('id', { ascending: true });

  if (error) {
    throw new Error(error.message);
  }

  return data ?? [];
}
