export type Json = string | number | boolean | null | { [key: string]: Json | undefined } | Json[];

export interface Database {
  public: {
    Tables: {
      profile: {
        Row: {
          id: number;
          full_name: string;
          headline: string | null;
          bio: string | null;
          location: string | null;
          email: string | null;
          phone: string | null;
          avatar_url: string | null;
          resume_url: string | null;
          display_order: number;
          created_at: string;
          updated_at: string;
        };
        Insert: {
          id?: number;
          full_name: string;
          headline?: string | null;
          bio?: string | null;
          location?: string | null;
          email?: string | null;
          phone?: string | null;
          avatar_url?: string | null;
          resume_url?: string | null;
          display_order?: number;
          created_at?: string;
          updated_at?: string;
        };
        Update: Partial<Database['public']['Tables']['profile']['Insert']>;
      };
      skills: {
        Row: {
          id: number;
          name: string;
          category: string | null;
          proficiency: string | null;
          display_order: number;
          created_at: string;
          updated_at: string;
        };
        Insert: {
          id?: number;
          name: string;
          category?: string | null;
          proficiency?: string | null;
          display_order?: number;
          created_at?: string;
          updated_at?: string;
        };
        Update: Partial<Database['public']['Tables']['skills']['Insert']>;
      };
      projects: {
        Row: {
          id: number;
          title: string;
          description: string | null;
          tech_stack: string[] | null;
          repo_url: string | null;
          live_url: string | null;
          image_url: string | null;
          display_order: number;
          created_at: string;
          updated_at: string;
        };
        Insert: {
          id?: number;
          title: string;
          description?: string | null;
          tech_stack?: string[] | null;
          repo_url?: string | null;
          live_url?: string | null;
          image_url?: string | null;
          display_order?: number;
          created_at?: string;
          updated_at?: string;
        };
        Update: Partial<Database['public']['Tables']['projects']['Insert']>;
      };
      certificates: {
        Row: {
          id: number;
          title: string;
          issuer: string | null;
          issue_date: string | null;
          credential_url: string | null;
          display_order: number;
          created_at: string;
          updated_at: string;
        };
        Insert: {
          id?: number;
          title: string;
          issuer?: string | null;
          issue_date?: string | null;
          credential_url?: string | null;
          display_order?: number;
          created_at?: string;
          updated_at?: string;
        };
        Update: Partial<Database['public']['Tables']['certificates']['Insert']>;
      };
      achievements: {
        Row: {
          id: number;
          title: string;
          description: string | null;
          award_date: string | null;
          display_order: number;
          created_at: string;
          updated_at: string;
        };
        Insert: {
          id?: number;
          title: string;
          description?: string | null;
          award_date?: string | null;
          display_order?: number;
          created_at?: string;
          updated_at?: string;
        };
        Update: Partial<Database['public']['Tables']['achievements']['Insert']>;
      };
      contact_messages: {
        Row: {
          id: number;
          name: string;
          email: string;
          subject: string | null;
          message: string;
          is_read: boolean;
          created_at: string;
        };
        Insert: {
          id?: number;
          name: string;
          email: string;
          subject?: string | null;
          message: string;
          is_read?: boolean;
          created_at?: string;
        };
        Update: Partial<Database['public']['Tables']['contact_messages']['Insert']>;
      };
    };
    Views: Record<string, never>;
    Functions: Record<string, never>;
    Enums: Record<string, never>;
  };
}

export type PublicTable<T extends keyof Database['public']['Tables']> = Database['public']['Tables'][T]['Row'];
