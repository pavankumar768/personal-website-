"use client";

import { useMutation, useQuery, useQueryClient } from "@tanstack/react-query";
import { supabase } from "@/lib/supabase-client";
import type { AdminTable, EntityMap } from "@/lib/types";

export function useAdminCrud<T extends AdminTable>(table: T) {
  const queryClient = useQueryClient();

  const listQuery = useQuery({
    queryKey: ["admin", table],
    queryFn: async () => {
      const { data, error } = await supabase.from(table).select("*").order("id", { ascending: true });
      if (error) throw error;
      return (data ?? []) as EntityMap[T][];
    }
  });

  const createMutation = useMutation({
    mutationFn: async (payload: Partial<EntityMap[T]>) => {
      const { data, error } = await supabase.from(table).insert(payload).select().single();
      if (error) throw error;
      return data as EntityMap[T];
    },
    onMutate: async (newItem) => {
      await queryClient.cancelQueries({ queryKey: ["admin", table] });
      const previous = queryClient.getQueryData<EntityMap[T][]>(["admin", table]) ?? [];
      queryClient.setQueryData(["admin", table], [...previous, { ...newItem, id: `temp-${Date.now()}` }]);
      return { previous };
    },
    onError: (_, __, context) => {
      queryClient.setQueryData(["admin", table], context?.previous);
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["admin", table] });
    }
  });

  const updateMutation = useMutation({
    mutationFn: async (payload: Partial<EntityMap[T]> & { id: string }) => {
      const { id, ...updates } = payload;
      const { data, error } = await supabase.from(table).update(updates).eq("id", id).select().single();
      if (error) throw error;
      return data as EntityMap[T];
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["admin", table] });
    }
  });

  const deleteMutation = useMutation({
    mutationFn: async (id: string) => {
      const { error } = await supabase.from(table).delete().eq("id", id);
      if (error) throw error;
      return id;
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["admin", table] });
    }
  });

  return { listQuery, createMutation, updateMutation, deleteMutation };
}
