import { supabaseClient } from '@/lib/supabaseClient';
import type { PublicTable } from '@/lib/database.types';

export type Profile = PublicTable<'profile'>;

export async function getProfile() {
  const { data, error } = await supabaseClient
    .from('profile')
    .select('*')
    .order('display_order', { ascending: true })
    .limit(1)
    .maybeSingle();

  if (error) {
    throw new Error(error.message);
  }

  return data;
}
