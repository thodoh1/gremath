"use client";

import { useEffect, useState } from "react";
import { Button } from "@/components/ui/button";
import {
  loadMastery,
  masteryLabel,
  setMastery,
  type Mastery,
} from "@/lib/progress";

export function MasteryControl({ id }: { id: string }) {
  const [value, setValue] = useState<Mastery>(0);

  useEffect(() => {
    setValue((loadMastery()[id] as Mastery) || 0);
  }, [id]);

  return (
    <div className="rounded-lg border border-rule bg-paper-dark/40 p-4">
      <p className="mb-2 text-[11px] uppercase tracking-[0.18em] text-ink/45">
        Mastery · {masteryLabel(value)}
      </p>
      <p className="mb-3 text-sm text-ink/70">
        0 unseen · 1 learned · 2 can solve standard problems · 3 can solve
        unfamiliar timed GRE-style problems
      </p>
      <div className="flex flex-wrap gap-2">
        {([0, 1, 2, 3] as Mastery[]).map((n) => (
          <Button
            key={n}
            size="sm"
            variant={value === n ? "default" : "outline"}
            onClick={() => {
              setMastery(id, n);
              setValue(n);
            }}
          >
            {n}
          </Button>
        ))}
      </div>
    </div>
  );
}
