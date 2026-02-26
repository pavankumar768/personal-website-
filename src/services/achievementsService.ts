import { supabaseClient } from '@/lib/supabaseClient';
import type { PublicTable } from '@/lib/database.types';

export type Achievement = PublicTable<'achievements'>;

export async function getAchievements() {
  const { data, error } = await supabaseClient
    .from('achievements')
    .select('*')
    .order('display_order', { ascending: true })
    .order('id', { ascending: true });

  if (error) {
    throw new Error(error.message);
  }

  return data ?? [];
}
