# Claude Code plugins

ใช้โฟลเดอร์นี้สำหรับ plugin ที่ต้องมีองค์ประกอบมากกว่า `SKILL.md` เดี่ยว เช่น agents, hooks, MCP servers หรือ commands

โครงสร้าง plugin ขั้นต่ำ:

```text
plugins/<plugin-name>/
├── .claude-plugin/
│   └── plugin.json
└── skills/
    └── <skill-name>/
        └── SKILL.md
```

เมื่อเพิ่ม plugin ให้เพิ่มรายการใน `.claude-plugin/marketplace.json` ด้วย source แบบ relative path เช่น `./plugins/<plugin-name>`.

