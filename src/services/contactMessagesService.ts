import { supabaseClient } from '@/lib/supabaseClient';
import type { PublicTable } from '@/lib/database.types';

export type ContactMessage = PublicTable<'contact_messages'>;
export type NewContactMessage = Omit<ContactMessage, 'id' | 'created_at' | 'is_read'>;

export async function getContactMessages() {
  const { data, error } = await supabaseClient
    .from('contact_messages')
    .select('*')
    .order('created_at', { ascending: false });

  if (error) {
    throw new Error(error.message);
  }

  return data ?? [];
}

export async function createContactMessage(payload: NewContactMessage) {
  const { data, error } = await supabaseClient
    .from('contact_messages')
    .insert({ ...payload, is_read: false })
    .select('*')
    .single();

  if (error) {
    throw new Error(error.message);
  }

  return data;
}
