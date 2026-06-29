# HTML 设计参考 — 多主题阅读报告

本文档包含完整的 HTML/CSS/JS 模板和设计规范。生成报告时，**先根据书籍内容选择主题**，再将分析数据填入模板。

---

## 主题系统（Theme System）

根据书籍的内容、时代背景和文化语境自动选择最匹配的主题风格。**主题决定了整个报告的气质**。

### 主题选择规则

分析书籍的题材、时代、文化背景，选择最匹配的主题：

| 主题 | 适用书籍 | 判定关键词 |
|------|---------|-----------|
| apple-modern | 科技传记、硅谷、现代商业、互联网 | 苹果、谷歌、硅谷、创业、科技、互联网 |
| classical-chinese | 中国历史人物、古典文学、传统文化 | 曾国藩、李白、论语、三国、朝代、皇帝 |
| warm-memoir | 个人回忆录、女性成长、家庭故事、人生感悟 | 回忆、自传、人生、成长、母亲、家庭 |
| literary-novel | 文学小说、散文、诗歌 | 小说、散文、虚构、文学 |
| dark-dramatic | 战争、犯罪、惊悚、暗黑主题 | 战争、犯罪、悬疑、惊悚 |

**默认**：如果无法判定，使用 `apple-modern`。

### 主题 CSS 变量集

生成 HTML 时，将对应主题的 CSS 变量替换到 `:root` 中：

#### 1. apple-modern（科技现代）

```css
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f5f5f7;
  --bg-card: #ffffff;
  --text-primary: #1d1d1f;
  --text-secondary: #6e6e73;
  --text-tertiary: #86868b;
  --accent-primary: #0071e3;
  --accent-secondary: #6e3bff;
  --accent-gradient: linear-gradient(135deg, #0071e3 0%, #6e3bff 100%);
  --border-light: rgba(0, 0, 0, 0.06);
  --shadow-card: 0 2px 12px rgba(0, 0, 0, 0.04);
  --shadow-card-hover: 0 8px 30px rgba(0, 0, 0, 0.08);
  --shadow-elevated: 0 12px 40px rgba(0, 0, 0, 0.12);
  --radius-sm: 12px;
  --radius-md: 18px;
  --radius-lg: 24px;
  --font-sans: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Helvetica Neue", "Noto Sans SC", sans-serif;
  --font-serif: "Noto Serif SC", Georgia, serif;
}
```
**Hero 风格**：大留白，渐变浅灰背景，封面居中投影

#### 2. classical-chinese（中国古典）

```css
:root {
  --bg-primary: #f7f3eb;
  --bg-secondary: #ede7d9;
  --bg-card: #fdfbf6;
  --text-primary: #2c1810;
  --text-secondary: #5c4033;
  --text-tertiary: #8b7355;
  --accent-primary: #8b1a1a;
  --accent-secondary: #c5a355;
  --accent-gradient: linear-gradient(135deg, #8b1a1a 0%, #c5a355 100%);
  --border-light: rgba(139, 26, 26, 0.1);
  --shadow-card: 0 2px 8px rgba(44, 24, 16, 0.06);
  --shadow-card-hover: 0 6px 24px rgba(44, 24, 16, 0.1);
  --shadow-elevated: 0 8px 32px rgba(44, 24, 16, 0.12);
  --radius-sm: 4px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --font-sans: "Noto Sans SC", "PingFang SC", sans-serif;
  --font-serif: "Noto Serif SC", "STSong", "SimSun", serif;
}
```
**Hero 风格**：暖色纸纹背景，竖排书名（可选），朱红印章装饰元素
**特殊装饰**：section-label 使用竖排文字或方印章样式；卡片边角方正，不用大圆角

#### 3. warm-memoir（温暖回忆录）

```css
:root {
  --bg-primary: #fefcf8;
  --bg-secondary: #f9f0e8;
  --bg-card: #ffffff;
  --text-primary: #2d2926;
  --text-secondary: #6b5e57;
  --text-tertiary: #9c8b82;
  --accent-primary: #c17f6e;
  --accent-secondary: #d4a574;
  --accent-gradient: linear-gradient(135deg, #c17f6e 0%, #d4a574 100%);
  --border-light: rgba(193, 127, 110, 0.1);
  --shadow-card: 0 2px 12px rgba(45, 41, 38, 0.05);
  --shadow-card-hover: 0 8px 30px rgba(45, 41, 38, 0.08);
  --shadow-elevated: 0 12px 40px rgba(45, 41, 38, 0.1);
  --radius-sm: 12px;
  --radius-md: 20px;
  --radius-lg: 28px;
  --font-sans: -apple-system, "Helvetica Neue", "Noto Sans SC", sans-serif;
  --font-serif: "Noto Serif SC", "Lora", Georgia, serif;
}
```
**Hero 风格**：奶油色暖调背景，封面柔光投影，整体温柔优雅
**特殊装饰**：idea-card 的编号用 accent 色而非渐变；quote 引用使用手写体风格

#### 4. literary-novel（文学小说）

```css
:root {
  --bg-primary: #fafaf8;
  --bg-secondary: #f0efe8;
  --bg-card: #ffffff;
  --text-primary: #1a1a1a;
  --text-secondary: #555555;
  --text-tertiary: #888888;
  --accent-primary: #2d5f3e;
  --accent-secondary: #6b8f71;
  --accent-gradient: linear-gradient(135deg, #2d5f3e 0%, #6b8f71 100%);
  --border-light: rgba(0, 0, 0, 0.08);
  --shadow-card: 0 2px 10px rgba(0, 0, 0, 0.04);
  --shadow-card-hover: 0 6px 24px rgba(0, 0, 0, 0.08);
  --shadow-elevated: 0 10px 36px rgba(0, 0, 0, 0.1);
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --font-sans: -apple-system, "Helvetica Neue", "Noto Sans SC", sans-serif;
  --font-serif: "Noto Serif SC", Georgia, "Palatino", serif;
}
```
**Hero 风格**：素雅背景，书籍封面搭配一段精选引文

#### 5. dark-dramatic（暗色戏剧）

```css
:root {
  --bg-primary: #1a1a1a;
  --bg-secondary: #252525;
  --bg-card: #2a2a2a;
  --text-primary: #e8e8e8;
  --text-secondary: #a0a0a0;
  --text-tertiary: #707070;
  --accent-primary: #e63946;
  --accent-secondary: #f4a261;
  --accent-gradient: linear-gradient(135deg, #e63946 0%, #f4a261 100%);
  --border-light: rgba(255, 255, 255, 0.06);
  --shadow-card: 0 2px 12px rgba(0, 0, 0, 0.3);
  --shadow-card-hover: 0 8px 30px rgba(0, 0, 0, 0.4);
  --shadow-elevated: 0 12px 40px rgba(0, 0, 0, 0.5);
  --radius-sm: 8px;
  --radius-md: 14px;
  --radius-lg: 20px;
  --font-sans: -apple-system, "Helvetica Neue", "Noto Sans SC", sans-serif;
  --font-serif: "Noto Serif SC", Georgia, serif;
}
```
**Hero 风格**：深色背景，封面高对比投影，戏剧性渐变光效

### 主题应用方式

1. 在 SKILL.md 阶段 2 增加一个**主题判定步骤**（可与 2a/2b 并行）
2. 分析书籍元数据和正文前 500 字，判定主题类别
3. 生成 HTML 时，用对应主题的 CSS 变量替换 `:root`
4. Hero 区和装饰元素根据主题微调（见上方各主题说明）

---

## 基础设计系统（所有主题共享）

### 颜色变量

```css
:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f5f5f7;
  --bg-card: #ffffff;
  --text-primary: #1d1d1f;
  --text-secondary: #6e6e73;
  --text-tertiary: #86868b;
  --accent-blue: #0071e3;
  --accent-purple: #6e3bff;
  --accent-gradient: linear-gradient(135deg, #0071e3 0%, #6e3bff 100%);
  --border-light: rgba(0, 0, 0, 0.06);
  --shadow-card: 0 2px 12px rgba(0, 0, 0, 0.04);
  --shadow-card-hover: 0 8px 30px rgba(0, 0, 0, 0.08);
  --shadow-elevated: 0 12px 40px rgba(0, 0, 0, 0.12);
  --radius-sm: 12px;
  --radius-md: 18px;
  --radius-lg: 24px;
}
```

### 字体栈

```css
--font-sans: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text",
             "Helvetica Neue", "Noto Sans SC", sans-serif;
--font-serif: "Noto Serif SC", "Source Han Serif SC", Georgia, serif;
--font-mono: "SF Mono", "Fira Code", "Consolas", monospace;
```

### 间距系统

```css
--space-xs: 8px;
--space-sm: 16px;
--space-md: 24px;
--space-lg: 40px;
--space-xl: 64px;
--space-2xl: 96px;
```

### 响应式断点

| 名称 | 断点 | 容器宽度 |
|------|------|---------|
| 手机 | < 768px | 100% - 32px |
| 平板 | 768px - 1024px | 720px |
| 桌面 | > 1024px | 980px |

---

## 完整 HTML 模板

以下是完整的单文件 HTML 模板。`{{变量}}` 为数据占位符，生成时替换为实际内容。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{{title}} — 深度阅读报告</title>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;600;700&display=swap" rel="stylesheet">
<style>
/* ===== Reset & Base ===== */
*, *::before, *::after { margin: 0; padding: 0; box-sizing: border-box; }

:root {
  --bg-primary: #ffffff;
  --bg-secondary: #f5f5f7;
  --bg-card: #ffffff;
  --text-primary: #1d1d1f;
  --text-secondary: #6e6e73;
  --text-tertiary: #86868b;
  --accent-blue: #0071e3;
  --accent-purple: #6e3bff;
  --accent-gradient: linear-gradient(135deg, #0071e3 0%, #6e3bff 100%);
  --border-light: rgba(0, 0, 0, 0.06);
  --shadow-card: 0 2px 12px rgba(0, 0, 0, 0.04);
  --shadow-card-hover: 0 8px 30px rgba(0, 0, 0, 0.08);
  --radius-sm: 12px;
  --radius-md: 18px;
  --radius-lg: 24px;
  --font-sans: -apple-system, BlinkMacSystemFont, "SF Pro Display", "SF Pro Text",
               "Helvetica Neue", "Noto Sans SC", sans-serif;
  --font-serif: "Noto Serif SC", "Source Han Serif SC", Georgia, serif;
}

html { scroll-behavior: smooth; }

body {
  font-family: var(--font-sans);
  color: var(--text-primary);
  background: var(--bg-primary);
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
}

.container {
  max-width: 980px;
  margin: 0 auto;
  padding: 0 24px;
}

/* ===== Animations ===== */
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(30px); }
  to { opacity: 1; transform: translateY(0); }
}

.fade-in {
  animation: fadeInUp 0.8s ease-out both;
}

.fade-in-delay-1 { animation-delay: 0.15s; }
.fade-in-delay-2 { animation-delay: 0.3s; }
.fade-in-delay-3 { animation-delay: 0.45s; }
.fade-in-delay-4 { animation-delay: 0.6s; }

/* ===== Section Common ===== */
section {
  padding: 80px 0;
}

.section-label {
  font-size: 14px;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--accent-blue);
  margin-bottom: 12px;
}

.section-title {
  font-family: var(--font-serif);
  font-size: 40px;
  font-weight: 700;
  line-height: 1.2;
  color: var(--text-primary);
  margin-bottom: 16px;
}

.section-subtitle {
  font-size: 18px;
  color: var(--text-secondary);
  max-width: 640px;
  line-height: 1.6;
}

/* ===== Hero Section ===== */
.hero {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(180deg, #f5f5f7 0%, #ffffff 100%);
  padding: 120px 0 80px;
}

.hero-inner {
  text-align: center;
  max-width: 680px;
  margin: 0 auto;
  padding: 0 24px;
}

.hero-cover {
  width: 220px;
  height: 320px;
  object-fit: cover;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-elevated);
  margin-bottom: 40px;
}

/* Fallback cover when no image */
.hero-cover-fallback {
  width: 220px;
  height: 320px;
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-elevated);
  margin: 0 auto 40px;
  background: var(--accent-gradient);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-family: var(--font-serif);
  font-size: 28px;
  font-weight: 700;
  line-height: 1.3;
  padding: 24px;
}

.hero-title {
  font-family: var(--font-serif);
  font-size: 52px;
  font-weight: 700;
  line-height: 1.15;
  margin-bottom: 12px;
  color: var(--text-primary);
}

.hero-author {
  font-size: 20px;
  color: var(--text-secondary);
  margin-bottom: 24px;
}

.hero-tagline {
  font-size: 22px;
  color: var(--text-primary);
  line-height: 1.5;
  font-family: var(--font-serif);
  font-weight: 400;
  max-width: 520px;
  margin: 0 auto;
}

/* ===== Ideas Section ===== */
.ideas-section {
  background: var(--bg-primary);
}

.ideas-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
  margin-top: 48px;
}

.idea-card {
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 32px;
  box-shadow: var(--shadow-card);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.idea-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-card-hover);
}

.idea-card .idea-number {
  font-size: 48px;
  font-weight: 700;
  background: var(--accent-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  line-height: 1;
  margin-bottom: 16px;
}

.idea-card h3 {
  font-size: 20px;
  font-weight: 600;
  margin-bottom: 8px;
  color: var(--text-primary);
}

.idea-card .idea-explanation {
  font-size: 15px;
  color: var(--text-secondary);
  margin-bottom: 16px;
  line-height: 1.6;
}

.idea-card .idea-quote {
  font-family: var(--font-serif);
  font-size: 14px;
  color: var(--text-tertiary);
  font-style: italic;
  border-left: 3px solid var(--accent-blue);
  padding-left: 16px;
  line-height: 1.6;
}

.unique-insight {
  margin-top: 32px;
  background: var(--bg-secondary);
  border-radius: var(--radius-md);
  padding: 40px;
  text-align: center;
}

.unique-insight h3 {
  font-size: 18px;
  font-weight: 600;
  color: var(--accent-blue);
  margin-bottom: 12px;
}

.unique-insight p {
  font-family: var(--font-serif);
  font-size: 20px;
  color: var(--text-primary);
  line-height: 1.6;
  max-width: 600px;
  margin: 0 auto;
}

/* ===== Characters Section ===== */
.characters-section {
  background: var(--bg-secondary);
}

.characters-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 20px;
  margin-top: 48px;
}

.character-card {
  background: var(--bg-card);
  border-radius: var(--radius-md);
  padding: 32px;
  box-shadow: var(--shadow-card);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.character-card:hover {
  transform: translateY(-4px);
  box-shadow: var(--shadow-card-hover);
}

.character-avatar {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  background: var(--accent-gradient);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #fff;
  font-size: 24px;
  font-weight: 700;
  margin-bottom: 20px;
}

.character-card h3 {
  font-size: 22px;
  font-weight: 600;
  margin-bottom: 4px;
}

.character-role {
  font-size: 14px;
  color: var(--text-tertiary);
  margin-bottom: 16px;
}

.character-traits {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin-bottom: 16px;
}

.trait-tag {
  font-size: 12px;
  font-weight: 500;
  padding: 4px 12px;
  border-radius: 100px;
  background: var(--bg-secondary);
  color: var(--text-secondary);
}

.character-belief {
  font-size: 14px;
  color: var(--text-secondary);
  line-height: 1.6;
}

/* Character detail overlay */
.character-detail {
  display: none;
  margin-top: 20px;
  padding-top: 20px;
  border-top: 1px solid var(--border-light);
  font-size: 14px;
  line-height: 1.7;
  color: var(--text-secondary);
}

.character-detail.open { display: block; }

.character-detail h4 {
  font-size: 13px;
  font-weight: 600;
  color: var(--text-primary);
  margin-top: 16px;
  margin-bottom: 6px;
}

.relationship-item {
  display: flex;
  align-items: baseline;
  gap: 8px;
  margin-bottom: 6px;
}

.relationship-item .rel-name {
  font-weight: 600;
  color: var(--text-primary);
  white-space: nowrap;
}

.relationship-item .rel-type {
  font-size: 12px;
  color: var(--accent-blue);
  white-space: nowrap;
}

.character-card .expand-hint {
  font-size: 12px;
  color: var(--text-tertiary);
  text-align: center;
  margin-top: 16px;
}

/* ===== Dialogue Section ===== */
.dialogue-section {
  background: var(--bg-primary);
}

.dialogue-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 20px;
  margin-top: 48px;
}

.dialogue-card {
  background: var(--bg-card);
  border: 1px solid var(--border-light);
  border-radius: var(--radius-md);
  padding: 36px;
  box-shadow: var(--shadow-card);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.dialogue-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-card-hover);
}

.dialogue-topic {
  font-size: 13px;
  font-weight: 600;
  color: var(--accent-blue);
  letter-spacing: 0.04em;
  margin-bottom: 8px;
}

.dialogue-card h3 {
  font-size: 22px;
  font-weight: 600;
  margin-bottom: 8px;
}

.dialogue-context {
  font-size: 15px;
  color: var(--text-secondary);
  margin-bottom: 20px;
  line-height: 1.6;
}

.guiding-questions {
  list-style: none;
  margin-bottom: 24px;
}

.guiding-questions li {
  position: relative;
  padding-left: 24px;
  margin-bottom: 10px;
  font-size: 15px;
  color: var(--text-primary);
  line-height: 1.5;
}

.guiding-questions li::before {
  content: "";
  position: absolute;
  left: 0;
  top: 8px;
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: var(--accent-gradient);
}

/* ===== Footer ===== */
footer {
  padding: 48px 0;
  text-align: center;
  color: var(--text-tertiary);
  font-size: 13px;
  border-top: 1px solid var(--border-light);
}

footer .footer-brand {
  font-weight: 600;
  background: var(--accent-gradient);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* ===== Responsive ===== */
@media (max-width: 768px) {
  .hero-title { font-size: 36px; }
  .hero-tagline { font-size: 18px; }
  .section-title { font-size: 28px; }
  .ideas-grid { grid-template-columns: 1fr; }
  .characters-grid { grid-template-columns: 1fr; }
  section { padding: 48px 0; }
  .hero { min-height: auto; padding: 80px 0 48px; }
}

@media (min-width: 769px) and (max-width: 1024px) {
  .container { max-width: 720px; }
  .hero-title { font-size: 44px; }
}
</style>
</head>
<body>

<!-- ===== HERO ===== -->
<section class="hero">
  <div class="hero-inner">
    <!-- 使用搜索结果封面，或渐变色备选 -->
    <!-- 有封面时： -->
    <img class="hero-cover fade-in" src="{{cover_url}}" alt="{{title}}">
    <!-- 无封面时使用以下 div 替代：
    <div class="hero-cover-fallback fade-in">{{title}}</div>
    -->
    <h1 class="hero-title fade-in fade-in-delay-1">{{title}}</h1>
    <p class="hero-author fade-in fade-in-delay-2">{{author}}</p>
    <p class="hero-tagline fade-in fade-in-delay-3">{{one_liner}}</p>
  </div>
</section>

<!-- ===== IDEAS ===== -->
<section class="ideas-section">
  <div class="container">
    <p class="section-label fade-in">Core Ideas</p>
    <h2 class="section-title fade-in">核心观念</h2>
    <p class="section-subtitle fade-in">{{core_thesis}}</p>

    <div class="ideas-grid">
      <!-- 为每个 key_idea 生成一张卡片 -->
      <div class="idea-card fade-in">
        <div class="idea-number">01</div>
        <h3>{{idea.title}}</h3>
        <p class="idea-explanation">{{idea.explanation}}</p>
        <blockquote class="idea-quote">{{idea.quote}}</blockquote>
      </div>
      <!-- 重复 02, 03, 04, 05 -->
    </div>

    <div class="unique-insight fade-in">
      <h3>独特洞见</h3>
      <p>{{unique_insight}}</p>
    </div>
  </div>
</section>

<!-- ===== CHARACTERS ===== -->
<section class="characters-section">
  <div class="container">
    <p class="section-label fade-in">Characters</p>
    <h2 class="section-title fade-in">核心人物</h2>
    <p class="section-subtitle fade-in">点击人物卡片，展开详细关系与信念体系</p>

    <div class="characters-grid">
      <!-- 为每个 character 生成一张卡片 -->
      <div class="character-card fade-in" onclick="toggleDetail(this)">
        <div class="character-avatar">{{character.name[0]}}</div>
        <h3>{{character.name}}</h3>
        <p class="character-role">{{character.role}}</p>
        <div class="character-traits">
          <!-- 为每个 trait 生成 tag -->
          <span class="trait-tag">{{trait}}</span>
        </div>
        <p class="character-belief">{{character.belief_system}}</p>
        <div class="character-detail">
          <h4>决策模式</h4>
          <p>{{character.decision_pattern}}</p>
          <h4>说话风格</h4>
          <p>{{character.dialogue_style}}</p>
          <h4>人物关系</h4>
          <!-- 为每个 relationship 生成 item -->
          <div class="relationship-item">
            <span class="rel-name">{{rel.target}}</span>
            <span class="rel-type">{{rel.type}}</span>
            <span>{{rel.description}}</span>
          </div>
        </div>
        <p class="expand-hint">点击展开详情 ↓</p>
      </div>
      <!-- 重复其他人物 -->
    </div>
  </div>
</section>

<!-- ===== DIALOGUE ===== -->
<section class="dialogue-section">
  <div class="container">
    <p class="section-label fade-in">Dialogue</p>
    <h2 class="section-title fade-in">与{{character_name}}对话</h2>
    <p class="section-subtitle fade-in">选择一个话题方向，直接在对话中向{{character_name}}提问即可。</p>

    <div class="dialogue-grid">
      <!-- 为每个 topic 生成一张卡片 -->
      <div class="dialogue-card fade-in">
        <p class="dialogue-topic">{{topic.topic}}</p>
        <h3>和{{character_name}}聊聊「{{topic.topic}}」</h3>
        <p class="dialogue-context">{{topic.context}}</p>
        <ul class="guiding-questions">
          <!-- 为每个 guiding_question 生成 li -->
          <li>{{question}}</li>
        </ul>
      </div>
      <!-- 重复其他话题 -->
    </div>
  </div>
</section>

<!-- ===== FOOTER ===== -->
<footer>
  <div class="container">
    <p>由 <span class="footer-brand">Book Reader</span> 生成 · {{generated_date}}</p>
  </div>
</footer>

<!-- ===== JavaScript ===== -->
<script>
function toggleDetail(card) {
  const detail = card.querySelector('.character-detail');
  const hint = card.querySelector('.expand-hint');
  if (detail) {
    detail.classList.toggle('open');
    if (hint) hint.textContent = detail.classList.contains('open') ? '收起 ↑' : '点击展开详情 ↓';
  }
}

// Intersection Observer for scroll animations
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.animationPlayState = 'running';
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.1 });

document.querySelectorAll('.fade-in').forEach(el => {
  el.style.animationPlayState = 'paused';
  observer.observe(el);
});
</script>
</body>
</html>
```

---

## 数据填充指南

### 变量映射

从阶段 2 的 JSON 输出映射到 HTML 模板：

| HTML 占位符 | 数据来源 |
|------------|---------|
| `{{title}}` | `metadata.title` |
| `{{author}}` | `metadata.author` |
| `{{cover_url}}` | ImageSearch 结果 |
| `{{one_liner}}` | `core_thesis.one_liner` |
| `{{core_thesis}}` | `core_thesis.core_thesis` |
| `{{idea.title}}` | `key_ideas[n].title` |
| `{{idea.explanation}}` | `key_ideas[n].explanation` |
| `{{idea.quote}}` | `key_ideas[n].quote` |
| `{{unique_insight}}` | `core_thesis.unique_insight` |
| `{{character.name}}` | `characters[n].name` |
| `{{character.role}}` | `characters[n].role` |
| `{{character.belief_system}}` | `characters[n].belief_system` |
| `{{trait}}` | `characters[n].core_traits[i]` |
| `{{character.decision_pattern}}` | `characters[n].decision_pattern` |
| `{{character.dialogue_style}}` | `characters[n].dialogue_style` |
| `{{rel.target/type/description}}` | `characters[n].relationships[i]` |
| `{{topic.topic/context}}` | `topics[n].topic / context` |
| `{{question}}` | `topics[n].guiding_questions[i]` |
| `{{generated_date}}` | 当前日期 |

### 动态生成逻辑

1. **Idea Cards**：遍历 `key_ideas` 数组，编号用 `01` `02` ... 格式
2. **Character Cards**：遍历 `characters` 数组，头像取名字首字
3. **Dialogue Cards**：遍历 `topics` 数组，每个 topic 对应一张卡
4. **Relationship Items**：嵌套在 character-detail 内，遍历 `relationships`

### 特殊情况处理

- **无封面**：用 `.hero-cover-fallback` div 替代 `<img>`，渐变背景 + 书名
- **无人物**（工具书/科普书）：跳过 Characters 板块，改为"核心概念图"
- **单一主角**（自传）：Dialogue section 标题用主角名，所有话题指向同一角色
- **key_ideas < 2**：ideas-grid 改为单列布局
