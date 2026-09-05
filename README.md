# diwwergg Agent Toolkit

คลังรวม Agent Skills และ Claude Code Plugins สำหรับใช้งานร่วมกันหลาย agent

## Install skills

ติดตั้ง skill ทั้งหมด:

```bash
npx skills add diwwergg/agent-toolkit
```

ติดตั้งเฉพาะ skill:

```bash
npx skills add diwwergg/agent-toolkit --skill graph-engineering
```

## Install Claude Code plugins

เพิ่ม marketplace:

```text
/plugin marketplace add diwwergg/agent-toolkit
```

ติดตั้งหมวด engineering:

```text
/plugin install engineering@diwwergg-toolkit
```

## Repository layout

```text
skills/<category>/<skill>/SKILL.md  # Canonical skills; discovered by npx skills
plugins/<plugin>/                    # Full Claude Code plugins
.claude-plugin/marketplace.json      # Claude marketplace catalog
```

เพิ่ม skill ใหม่ไว้ใต้ `skills/<category>/<skill>/` โดยต้องมี `SKILL.md` พร้อม YAML frontmatter ที่มี `name` และ `description`.

ใช้ `plugins/<plugin>/` เมื่อจำเป็นต้องรวม skills, agents, hooks, MCP servers หรือคำสั่งเฉพาะของ Claude Code ใน package เดียว

## Current categories

- `engineering`: graph-engineering, graph-driven-engineering

