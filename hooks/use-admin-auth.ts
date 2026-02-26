"use client";

import { useEffect, useState } from "react";
import { supabase } from "@/lib/supabase-client";
import type { Role } from "@/lib/types";

interface AuthState {
  loading: boolean;
  signedIn: boolean;
  role: Role | null;
  error?: string;
}

export function useAdminAuth() {
  const [state, setState] = useState<AuthState>({ loading: true, signedIn: false, role: null });

  useEffect(() => {
    let active = true;

    const loadSession = async () => {
      const {
        data: { session }
      } = await supabase.auth.getSession();

      if (!active) return;
      if (!session?.user) {
        setState({ loading: false, signedIn: false, role: null });
        return;
      }

      const { data: profile, error } = await supabase
        .from("profiles")
        .select("role")
        .eq("id", session.user.id)
        .single();

      if (!active) return;
      if (error) {
        setState({ loading: false, signedIn: true, role: null, error: error.message });
        return;
      }

      setState({ loading: false, signedIn: true, role: (profile?.role as Role) ?? null });
    };

    loadSession();

    const {
      data: { subscription }
    } = supabase.auth.onAuthStateChange(() => {
      loadSession();
    });

    return () => {
      active = false;
      subscription.unsubscribe();
    };
  }, []);

  return state;
}
