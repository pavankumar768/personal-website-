"use client";

import { EntityForm, type EntityField } from "@/components/forms/entity-form";
import { useAdminCrud } from "@/hooks/use-admin-crud";
import type { AdminTable, EntityMap } from "@/lib/types";

interface AdminModuleProps<T extends AdminTable> {
  table: T;
  title: string;
  fields: EntityField[];
}

export function AdminModule<T extends AdminTable>({ table, title, fields }: AdminModuleProps<T>) {
  const { listQuery, createMutation, updateMutation, deleteMutation } = useAdminCrud(table);

  return (
    <section style={{ marginBottom: 28 }}>
      <h2>{title}</h2>
      <EntityForm
        fields={fields}
        submitLabel={`Create ${title}`}
        onSubmit={async (values) => {
          await createMutation.mutateAsync(values as Partial<EntityMap[T]>);
        }}
      />

      <div style={{ marginTop: 16, display: "grid", gap: 10 }}>
        {listQuery.isLoading ? <p>Loading...</p> : null}
        {listQuery.data?.map((item) => (
          <div
            key={item.id}
            style={{ border: "1px solid #ddd", borderRadius: 8, padding: 12, display: "grid", gap: 8 }}
          >
            <pre style={{ margin: 0, overflow: "auto" }}>{JSON.stringify(item, null, 2)}</pre>
            <div style={{ display: "flex", gap: 8 }}>
              <button
                onClick={() => updateMutation.mutate({ ...(item as EntityMap[T]), id: item.id })}
                style={{ padding: "6px 10px" }}
              >
                Save (Refetch)
              </button>
              <button onClick={() => deleteMutation.mutate(item.id)} style={{ padding: "6px 10px" }}>
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}
