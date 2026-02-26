"use client";

import { zodResolver } from "@hookform/resolvers/zod";
import { useForm } from "react-hook-form";
import { z } from "zod";
import { FormField } from "@/components/forms/form-field";

export interface EntityField {
  key: string;
  label: string;
  required?: boolean;
}

interface EntityFormProps {
  fields: EntityField[];
  defaultValues?: Record<string, string>;
  onSubmit: (values: Record<string, string>) => Promise<void> | void;
  submitLabel: string;
}

export function EntityForm({ fields, defaultValues, onSubmit, submitLabel }: EntityFormProps) {
  const schema = z.object(
    fields.reduce<Record<string, z.ZodTypeAny>>((acc, field) => {
      acc[field.key] = field.required
        ? z.string().trim().min(1, `${field.label} is required`)
        : z.string().trim().optional().default("");
      return acc;
    }, {})
  );

  type FormValues = z.infer<typeof schema>;

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors, isSubmitting }
  } = useForm<FormValues>({
    resolver: zodResolver(schema),
    defaultValues: defaultValues as FormValues
  });

  return (
    <form
      onSubmit={handleSubmit(async (values) => {
        await onSubmit(values as Record<string, string>);
        if (!defaultValues) reset();
      })}
      style={{ display: "grid", gap: 12, padding: 16, border: "1px solid #ddd", borderRadius: 8 }}
    >
      {fields.map((field) => (
        <FormField key={field.key} label={field.label} error={errors[field.key]?.message as string | undefined}>
          <input
            {...register(field.key as keyof FormValues)}
            style={{ border: "1px solid #ccc", padding: 8, borderRadius: 6 }}
          />
        </FormField>
      ))}
      <button disabled={isSubmitting} style={{ width: "fit-content", padding: "8px 14px" }}>
        {isSubmitting ? "Saving..." : submitLabel}
      </button>
    </form>
  );
}
