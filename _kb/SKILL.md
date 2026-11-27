---
name: teardown-100-kb
description: 100 个 AI 产品拆解的知识库（Slack / Taskade 已入库）。当需要查「某个产品怎么定位、由哪些原子能力组成、工作流怎么拼、靠什么渠道获客、有哪些模板可参考（适合谁/什么场景/怎么用）」时使用。数据在 db/kb.sqlite 与同名 CSV/MD。
---

# Teardown-100 知识库

## 数据在哪
- **主库（推荐查询）**：`db/kb.sqlite`（SQLite，含 7 张表 + 全文检索表 search_fts）
- 分表 CSV：`01-products` / `02-atoms` / `03-workflows` / `04-channels` / `05-resources` / `08-template-modules` / `11-template-fit`
- 可读索引：`06-problem-to-component.md`（问题→组件）、`10-template-picker.md`（按模块反查模板）、`09-template-anatomy.md`（逐模板结构）
- 原始底稿：`raw/*.md`（每条带 URL）

## 表结构（列名即字段）
- `products`：no, slug, name, category, one_liner, icp_primary, icp_secondary, jtbd, core_scenarios, ai_mode, pricing_model, free_tier, paid_tiers, atoms_count, workflows_count, primary_channels, moat_hypothesis, evidence_urls, updated_at
- `atoms`：atom_id, product, atom_name, atom_type, what_it_does, composable_with, evidence_url
- `workflows`：workflow_id, product, workflow_name, input, atoms_used, steps, output, who_uses, evidence_url
- `channels`：channel_id, product, channel_type, mechanics, url_pattern, scale_note, replicable_score, evidence_url
- `resources`：resource_id, product, resource_name, resource_type, problem_solved, how_to_access, reuse_form, reuse_score, migration_cost, evidence_strength, evidence_url
- `template_modules`：template_id, product, template_name, template_one_liner, module_no, module_name, module_type, detail, composition, evidence_url
- `template_fit`：template_id, product, template_name, for_whom, scenario, how_to_use, value, what_it_is, composition, evidence_url, fit_basis
- `search_fts`：tbl, rid, title, body, url（FTS5）

## 查询套路
```sql
-- 1) 我要做 X 功能，别人怎么拼的
SELECT workflow_name, input, atoms_used, steps, output FROM workflows WHERE steps LIKE '%关键词%';
-- 2) 我要参考一个模板（先看适合谁/场景/怎么用）
SELECT template_name, for_whom, scenario, how_to_use FROM template_fit WHERE scenario LIKE '%关键词%';
-- 3) 这个模板由哪些模块组成
SELECT module_name, module_type, detail FROM template_modules WHERE template_id = ?;
-- 4) 某种原子能力谁有
SELECT product, atom_name, what_it_does, composable_with FROM atoms WHERE atom_type = '工具';
-- 5) 全文检索
SELECT tbl, title, url FROM search_fts WHERE search_fts MATCH 'MCP OR 工作流' LIMIT 20;
```

## 规则
1. 回答必须带 `evidence_url`；查不到出处就说「库里没有」。
2. `fit_basis` / `evidence_strength` 标了「推断」的，不能当事实陈述。
3. 先查 `template_fit`（人/场景/怎么用）→ 再查 `template_modules`（模块）→ 再查 `atoms/workflows`（实现）。
4. 需要原文时去 `raw/` 找对应产品的底稿。
