import { supabaseClient } from '@/lib/supabaseClient';
import type { PublicTable } from '@/lib/database.types';

export type Certificate = PublicTable<'certificates'>;

export async function getCertificates() {
  const { data, error } = await supabaseClient
    .from('certificates')
    .select('*')
    .order('display_order', { ascending: true })
    .order('id', { ascending: true });

  if (error) {
    throw new Error(error.message);
  }

  return data ?? [];
}
