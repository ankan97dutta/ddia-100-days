# Day 038: Avro

Chapter 5 | Avro lab

Use writer/reader schemas to evolve records safely.

## Summary

Avro embeds no field names on the wire; the reader's schema reconciles against the writer's schema at decode time. Added fields with defaults fill missing values; removed fields are ignored when the reader still knows them. Schema resolution rules define safe evolution paths and reject incompatible type changes. This simulation uses JSON schema metadata plus a compact field-order payload.

> These notes and diagrams are original study aids for this repo, not copies of DDIA figures or prose. Read the matching section in your own copy of the book.

## Key points

- Writer and reader each carry a schema; resolution happens at read time.
- Fields omitted on the wire can be supplied from reader defaults.
- Field order in the binary payload follows the writer schema order.
- Incompatible type changes fail resolution instead of silently coercing.

## Diagram

Avro-style writer bytes resolved through the reader schema.

```mermaid
flowchart LR
WS[Writer schema] --> WB[Write columnar bytes]
WB --> RS[Reader schema resolves]
RS --> RD[Record dict]
```

## Today

1. Read the matching DDIA section in your own copy of the book.
2. Skim [WORKFLOW.md](../WORKFLOW.md) if you need the shared checklist.
3. Run the starter, then do Try this / Break it / Measure.

### Run the starter

```bash
cd workbook/starter
python3 main.py --help
python3 main.py
```

See [workbook/starter/README.md](./workbook/starter/README.md).

### Try this

Write Avro with schema A; read with schema B (added field with default). Then try a conflicting change.

### Break it

Drop a field without a default on the reader. What error do you get?

### Measure

Which evolutions Avro accepts vs rejects in your tests.

## Done when

- [ ] You can explain the idea simply
- [ ] You ran the starter and captured output
- [ ] You changed one variable or failure mode and noted what happened
- [ ] You wrote one trade-off you would defend in a design review

Workbook: [workbook/exercise.md](./workbook/exercise.md)
