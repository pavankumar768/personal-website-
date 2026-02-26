import { supabaseClient } from '@/lib/supabaseClient';
import type { PublicTable } from '@/lib/database.types';

export type Skill = PublicTable<'skills'>;

export async function getSkills() {
  const { data, error } = await supabaseClient
    .from('skills')
    .select('*')
    .order('display_order', { ascending: true })
    .order('id', { ascending: true });

  if (error) {
    throw new Error(error.message);
  }

  return data ?? [];
}
