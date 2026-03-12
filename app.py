<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dream Home Realty · Premium AI</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=DM+Sans:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root {
  --gold: #d4a843;
  --gold2: #f5d272;
  --gold3: #ffeca0;
  --amber: #b8791a;
  --deep: #070810;
  --panel: rgba(12,14,22,0.95);
  --glass: rgba(255,255,255,0.028);
  --border: rgba(212,168,67,0.18);
  --border2: rgba(212,168,67,0.06);
  --text: #e8e2d5;
  --muted: #4a4638;
  --glow: rgba(212,168,67,0.5);
  --cyan: #40d0e8;
  --green: #00e664;
}

*{margin:0;padding:0;box-sizing:border-box;}

body {
  font-family: 'DM Sans', sans-serif;
  background: var(--deep);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

/* ─── SCENE ─────────────────────────────────── */
#scene { position: fixed; inset: 0; z-index: 0; }
#bgCanvas { position: absolute; inset: 0; width: 100%; height: 100%; }

/* ─── HOLOGRAPHIC GRID ───────────────────────── */
.holo-grid {
  position: fixed; inset: 0; z-index: 1; pointer-events: none;
  background-image:
    linear-gradient(rgba(212,168,67,0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(212,168,67,0.03) 1px, transparent 1px);
  background-size: 60px 60px;
  animation: gridShift 20s linear infinite;
}
@keyframes gridShift { from{background-position:0 0} to{background-position:60px 60px} }

/* ─── PARTICLES ──────────────────────────────── */
.orb-field { position: fixed; inset: 0; z-index: 1; pointer-events: none; overflow: hidden; }
.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(60px);
  animation: orbDrift linear infinite;
  opacity: 0;
}
@keyframes orbDrift {
  0%{transform:translate(0,100vh) scale(0.5);opacity:0}
  8%{opacity:1}
  92%{opacity:0.5}
  100%{transform:translate(var(--ox),calc(-100px)) scale(1.2);opacity:0}
}
.spark {
  position: absolute;
  width: 2px; height: 2px;
  border-radius: 50%;
  background: var(--gold2);
  box-shadow: 0 0 6px var(--gold);
  animation: sparkFloat linear infinite;
  opacity: 0;
}
@keyframes sparkFloat {
  0%{transform:translateY(0) rotate(0deg);opacity:0}
  10%{opacity:1}
  90%{opacity:0.6}
  100%{transform:translateY(-100vh) rotate(360deg);opacity:0}
}

/* ─── WRAPPER ────────────────────────────────── */
.scene-wrapper {
  position: relative; z-index: 10;
  width: 100%; max-width: 520px;
  padding: 16px;
  min-height: 100vh;
  display: flex; align-items: center; justify-content: center;
}

/* ─── 3D CARD STAGE ──────────────────────────── */
.card-stage {
  width: 100%;
  transform-style: preserve-3d;
  animation: stageEntrance 1.2s cubic-bezier(0.16,1,0.3,1) forwards;
  transition: transform 0.1s ease-out;
  position: relative;
}
@keyframes stageEntrance {
  from {
    opacity: 0;
    transform: perspective(1000px) rotateX(25deg) rotateY(-15deg) translateY(80px) scale(0.85);
  }
  to {
    opacity: 1;
    transform: perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0) scale(1);
  }
}

/* ─── REFRACTION LAYERS ──────────────────────── */
.refraction-wrap { position: relative; }
.ref-shadow {
  position: absolute; inset: -2px;
  border-radius: 34px;
  background: linear-gradient(135deg,
    rgba(212,168,67,0.12) 0%,
    rgba(212,168,67,0.04) 30%,
    rgba(64,208,232,0.04) 60%,
    rgba(212,168,67,0.08) 100%);
  filter: blur(12px);
  animation: refShift 6s ease-in-out infinite alternate;
}
@keyframes refShift {
  from { opacity: 0.6; transform: scale(1.01); }
  to { opacity: 1; transform: scale(1.03); }
}

/* ─── MAIN CHAT CARD ─────────────────────────── */
.chat-card {
  position: relative;
  background: linear-gradient(160deg,
    rgba(14,17,28,0.98) 0%,
    rgba(9,11,19,0.99) 40%,
    rgba(11,13,22,0.98) 100%);
  border-radius: 32px;
  overflow: hidden;
  display: flex; flex-direction: column;
  height: min(740px, 90vh);
  border: 1px solid rgba(212,168,67,0.2);
  box-shadow:
    0 0 0 1px rgba(212,168,67,0.06),
    0 30px 80px rgba(0,0,0,0.9),
    0 0 100px rgba(212,168,67,0.06),
    inset 0 1px 0 rgba(255,255,255,0.06),
    inset 0 -1px 0 rgba(212,168,67,0.05);
  transform-style: preserve-3d;
}

/* Inner glass sheen */
.chat-card::before {
  content: '';
  position: absolute; inset: 0;
  background:
    radial-gradient(ellipse 80% 30% at 50% 0%, rgba(212,168,67,0.07) 0%, transparent 60%),
    radial-gradient(ellipse 40% 20% at 20% 0%, rgba(255,255,255,0.03) 0%, transparent 50%),
    radial-gradient(ellipse 60% 40% at 80% 100%, rgba(64,208,232,0.02) 0%, transparent 50%);
  pointer-events: none; z-index: 0; border-radius: 32px;
}

/* Scan beam */
.scan-beam {
  position: absolute; top: 0; left: 0; right: 0; height: 3px; z-index: 20;
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(212,168,67,0.0) 20%,
    rgba(245,210,114,0.9) 45%,
    rgba(255,236,160,1) 50%,
    rgba(245,210,114,0.9) 55%,
    rgba(212,168,67,0.0) 80%,
    transparent 100%);
  animation: scanBeam 4s ease-in-out infinite;
  filter: blur(1px);
}
@keyframes scanBeam {
  0%{transform:translateX(-100%)} 50%,100%{transform:translateX(200%)}
}
.scan-beam-glow {
  position: absolute; top: 0; left: 0; right: 0; height: 40px; z-index: 19;
  background: linear-gradient(180deg, rgba(212,168,67,0.06) 0%, transparent 100%);
  animation: scanBeam 4s ease-in-out infinite;
  transform: translateX(-100%);
  filter: blur(10px);
}

/* ─── CORNERS ────────────────────────────────── */
.corner-fx {
  position: absolute; z-index: 30; pointer-events: none;
}
.corner-fx::before, .corner-fx::after {
  content: ''; position: absolute;
  background: var(--gold2);
  border-radius: 2px;
}
.cfx-tl { top: 14px; left: 14px; }
.cfx-tl::before { width: 24px; height: 2px; top: 0; left: 0; box-shadow: 0 0 8px var(--glow); }
.cfx-tl::after  { width: 2px; height: 24px; top: 0; left: 0; box-shadow: 0 0 8px var(--glow); }
.cfx-tr { top: 14px; right: 14px; }
.cfx-tr::before { width: 24px; height: 2px; top: 0; right: 0; box-shadow: 0 0 8px var(--glow); }
.cfx-tr::after  { width: 2px; height: 24px; top: 0; right: 0; box-shadow: 0 0 8px var(--glow); }
.cfx-bl { bottom: 14px; left: 14px; }
.cfx-bl::before { width: 24px; height: 2px; bottom: 0; left: 0; box-shadow: 0 0 8px var(--glow); }
.cfx-bl::after  { width: 2px; height: 24px; bottom: 0; left: 0; box-shadow: 0 0 8px var(--glow); }
.cfx-br { bottom: 14px; right: 14px; }
.cfx-br::before { width: 24px; height: 2px; bottom: 0; right: 0; box-shadow: 0 0 8px var(--glow); }
.cfx-br::after  { width: 2px; height: 24px; bottom: 0; right: 0; box-shadow: 0 0 8px var(--glow); }

/* Animated corners */
.corner-fx::before { animation: cornerPulse 3s ease-in-out infinite; }
.corner-fx::after  { animation: cornerPulse 3s ease-in-out infinite 0.3s; }
@keyframes cornerPulse {
  0%,100%{opacity:0.6; box-shadow: 0 0 6px var(--glow);}
  50%{opacity:1; box-shadow: 0 0 16px var(--glow), 0 0 30px var(--glow);}
}

/* ─── HEADER ─────────────────────────────────── */
.header {
  padding: 24px 22px 18px;
  position: relative; z-index: 5; flex-shrink: 0;
}

.header-row { display: flex; align-items: center; gap: 14px; }

/* Logo 3D cube */
.logo-cube-wrap {
  position: relative; width: 58px; height: 58px; flex-shrink: 0;
  transform-style: preserve-3d;
}
.logo-cube {
  width: 58px; height: 58px;
  background: linear-gradient(145deg, #2d2212 0%, #1a1508 60%, #241c0a 100%);
  border-radius: 18px;
  border: 1px solid rgba(212,168,67,0.5);
  display: flex; align-items: center; justify-content: center;
  font-size: 26px;
  position: relative; z-index: 1;
  box-shadow:
    0 12px 40px rgba(212,168,67,0.25),
    0 4px 12px rgba(0,0,0,0.7),
    inset 0 1px 0 rgba(255,255,255,0.12),
    inset 0 -2px 0 rgba(0,0,0,0.4),
    inset 1px 0 0 rgba(255,255,255,0.05);
  animation: cubeFloat 4s ease-in-out infinite;
  cursor: pointer;
  transition: transform 0.3s;
}
.logo-cube:hover { transform: rotateY(180deg) scale(1.05); }
@keyframes cubeFloat {
  0%,100%{transform:translateY(0) rotateZ(0deg) rotateY(0deg)}
  25%{transform:translateY(-4px) rotateZ(1deg) rotateY(5deg)}
  75%{transform:translateY(-3px) rotateZ(-1deg) rotateY(-4deg)}
}
/* Cube sides for 3D illusion */
.cube-left {
  position: absolute; top: 6px; left: -8px; width: 8px; height: 46px;
  background: linear-gradient(180deg, rgba(180,130,40,0.6), rgba(80,60,15,0.8));
  border-radius: 3px 0 0 3px;
  transform: skewY(-8deg);
  filter: brightness(0.7);
}
.cube-bottom {
  position: absolute; bottom: -8px; left: 4px; right: 4px; height: 8px;
  background: linear-gradient(90deg, rgba(130,95,30,0.8), rgba(80,60,15,0.6));
  border-radius: 0 0 4px 4px;
  transform: skewX(-8deg);
  filter: brightness(0.5);
}
.orbit-ring {
  position: absolute; inset: -8px;
  border: 1px solid transparent;
  border-top-color: rgba(212,168,67,0.5);
  border-right-color: rgba(212,168,67,0.2);
  border-radius: 50%;
  animation: ringOrbit 3s linear infinite;
}
.orbit-ring2 {
  position: absolute; inset: -14px;
  border: 1px solid transparent;
  border-bottom-color: rgba(64,208,232,0.3);
  border-left-color: rgba(64,208,232,0.15);
  border-radius: 50%;
  animation: ringOrbit 5s linear infinite reverse;
}
@keyframes ringOrbit { from{transform:rotate(0deg)} to{transform:rotate(360deg)} }

.brand-info { flex: 1; }
.brand-name {
  font-family: 'Playfair Display', serif;
  font-size: 1.18rem; font-weight: 900;
  color: #fff; letter-spacing: 0.03em;
  text-shadow: 0 0 30px rgba(212,168,67,0.4);
  line-height: 1.2;
}
.brand-name em {
  font-style: normal;
  background: linear-gradient(90deg, var(--gold), var(--gold2), var(--gold3));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.brand-sub {
  font-family: 'Space Mono', monospace;
  font-size: 0.58rem; color: var(--muted);
  letter-spacing: 0.2em; text-transform: uppercase; margin-top: 3px;
}

/* Live badge */
.live-wrap { display: flex; flex-direction: column; align-items: flex-end; gap: 5px; }
.live-chip {
  display: flex; align-items: center; gap: 7px;
  background: rgba(0,230,100,0.07);
  border: 1px solid rgba(0,230,100,0.22);
  border-radius: 100px; padding: 5px 12px;
  position: relative; overflow: hidden;
}
.live-chip::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(90deg, transparent, rgba(0,230,100,0.07), transparent);
  animation: chipSheen 3s ease-in-out infinite;
}
@keyframes chipSheen { 0%,100%{transform:translateX(-100%)} 50%{transform:translateX(100%)} }
.ldot {
  width: 7px; height: 7px; border-radius: 50%;
  background: var(--green); position: relative;
  box-shadow: 0 0 12px var(--green);
}
.ldot::before {
  content: ''; position: absolute;
  inset: -4px; border-radius: 50%;
  background: rgba(0,230,100,0.2);
  animation: dotRipple 1.5s ease-in-out infinite;
}
@keyframes dotRipple {
  0%{transform:scale(0.8);opacity:1} 100%{transform:scale(2.5);opacity:0}
}
.ltext { font-size: 0.68rem; font-weight: 700; color: var(--green); letter-spacing: 0.1em; }
.ai-badge {
  font-size: 0.6rem; color: rgba(212,168,67,0.5);
  font-family: 'Space Mono', monospace; letter-spacing: 0.12em;
  border: 1px solid rgba(212,168,67,0.12); border-radius: 4px; padding: 2px 6px;
}

/* ─── STATS BAR ──────────────────────────────── */
.stats-row {
  display: grid; grid-template-columns: repeat(4, 1fr);
  gap: 8px; margin-top: 16px;
}
.stat {
  background: linear-gradient(145deg, rgba(212,168,67,0.07) 0%, rgba(212,168,67,0.02) 100%);
  border: 1px solid var(--border2); border-radius: 14px; padding: 10px 6px;
  text-align: center; cursor: default; position: relative; overflow: hidden;
  transition: all 0.3s ease;
  transform-style: preserve-3d;
}
.stat::before {
  content: ''; position: absolute; inset: 0; border-radius: 14px;
  background: linear-gradient(135deg, rgba(255,255,255,0.04) 0%, transparent 60%);
  pointer-events: none;
}
.stat::after {
  content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(212,168,67,0.1), transparent);
  transition: left 0.5s ease;
}
.stat:hover::after { left: 100%; }
.stat:hover {
  border-color: rgba(212,168,67,0.35);
  transform: translateY(-3px) scale(1.03);
  box-shadow: 0 12px 30px rgba(212,168,67,0.15), 0 0 0 1px rgba(212,168,67,0.1);
}
.stat-n {
  font-family: 'Playfair Display', serif; font-size: 1rem; font-weight: 700;
  background: linear-gradient(135deg, var(--gold2), var(--gold3));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.stat-l { font-size: 0.57rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.08em; margin-top: 2px; }

/* ─── DIVIDER ────────────────────────────────── */
.hdiv {
  height: 1px; margin: 0 20px; flex-shrink: 0;
  background: linear-gradient(90deg, transparent, rgba(212,168,67,0.15), rgba(64,208,232,0.08), rgba(212,168,67,0.15), transparent);
  position: relative;
}
.hdiv::after {
  content: ''; position: absolute; top: -1px; left: 50%; transform: translateX(-50%);
  width: 60px; height: 3px; border-radius: 2px;
  background: linear-gradient(90deg, rgba(212,168,67,0.4), rgba(245,210,114,0.8), rgba(212,168,67,0.4));
  filter: blur(2px);
}

/* ─── MESSAGES ───────────────────────────────── */
.messages {
  flex: 1; overflow-y: auto; padding: 18px 16px 10px;
  display: flex; flex-direction: column; gap: 14px;
  position: relative; z-index: 2;
  scroll-behavior: smooth;
}
.messages::-webkit-scrollbar { width: 2px; }
.messages::-webkit-scrollbar-thumb { background: rgba(212,168,67,0.25); border-radius: 2px; }

.mrow { display: flex; gap: 10px; animation: msgPop 0.45s cubic-bezier(0.16,1,0.3,1) forwards; }
.mrow.user { flex-direction: row-reverse; }
@keyframes msgPop {
  from{opacity:0;transform:scale(0.88) translateY(14px)}
  to{opacity:1;transform:scale(1) translateY(0)}
}

.mav {
  width: 36px; height: 36px; border-radius: 12px;
  display: flex; align-items: center; justify-content: center;
  font-size: 17px; flex-shrink: 0; align-self: flex-end;
  position: relative;
}
.mav-bot {
  background: linear-gradient(145deg, #2d2212, #1a1508);
  border: 1px solid rgba(212,168,67,0.35);
  box-shadow: 0 6px 20px rgba(212,168,67,0.2), inset 0 1px 0 rgba(255,255,255,0.1);
}
.mav-bot::after {
  content: ''; position: absolute; inset: -3px; border-radius: 15px;
  border: 1px solid rgba(212,168,67,0.15);
  animation: avatarPulse 2s ease-in-out infinite;
}
@keyframes avatarPulse {
  0%,100%{transform:scale(1);opacity:0.5} 50%{transform:scale(1.08);opacity:1}
}
.mav-usr {
  background: linear-gradient(145deg, #0e1f10, #081008);
  border: 1px solid rgba(80,200,100,0.22);
  box-shadow: 0 4px 14px rgba(0,230,100,0.1);
}

.mbody { max-width: 82%; display: flex; flex-direction: column; gap: 4px; }
.mrow.user .mbody { align-items: flex-end; }

/* Bubbles */
.bubble-bot {
  background: linear-gradient(145deg, #181c2c 0%, #111420 100%);
  border: 1px solid rgba(212,168,67,0.14);
  border-bottom-left-radius: 4px;
  border-radius: 18px 18px 18px 4px;
  padding: 13px 16px;
  font-size: 0.875rem; line-height: 1.7; color: var(--text);
  position: relative; overflow: hidden;
  box-shadow: 0 6px 24px rgba(0,0,0,0.45), inset 0 1px 0 rgba(255,255,255,0.04);
}
.bubble-bot::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(212,168,67,0.3), transparent);
}
.bubble-usr {
  background: linear-gradient(135deg, #e0b348 0%, #c8912a 50%, #d4a030 100%);
  border-radius: 18px 18px 4px 18px;
  padding: 13px 16px;
  font-size: 0.875rem; line-height: 1.7; color: #1a0f00; font-weight: 500;
  box-shadow:
    0 8px 28px rgba(212,168,67,0.35),
    inset 0 1px 0 rgba(255,255,255,0.22),
    inset 0 -2px 0 rgba(0,0,0,0.18);
  position: relative; overflow: hidden;
}
.bubble-usr::before {
  content: ''; position: absolute; top: 0; left: -100%; width: 60%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255,255,255,0.12), transparent);
  animation: usrSheen 4s ease-in-out infinite;
}
@keyframes usrSheen { 0%,100%{left:-100%} 50%{left:200%} }

.mtime { font-size: 0.59rem; color: var(--muted); padding: 0 5px; letter-spacing: 0.04em; font-family: 'Space Mono', monospace; }

/* Welcome card */
.welcome-card {
  background: linear-gradient(145deg,
    rgba(212,168,67,0.08) 0%,
    rgba(212,168,67,0.03) 50%,
    rgba(64,208,232,0.02) 100%);
  border: 1px solid rgba(212,168,67,0.2);
  border-radius: 20px 20px 20px 4px;
  padding: 18px 18px 16px;
  position: relative; overflow: hidden;
  box-shadow: 0 12px 40px rgba(0,0,0,0.35), inset 0 1px 0 rgba(255,255,255,0.06);
}
.welcome-card::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(212,168,67,0.5), rgba(64,208,232,0.2), rgba(212,168,67,0.5), transparent);
}
.wc-title {
  font-family: 'Playfair Display', serif;
  font-size: 1rem; font-weight: 700;
  background: linear-gradient(90deg, var(--gold2), var(--gold3));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text; margin-bottom: 12px;
}
.wc-items { display: flex; flex-direction: column; gap: 8px; }
.wc-item {
  display: flex; align-items: center; gap: 10px;
  font-size: 0.8rem; color: #8a8470;
  animation: itemFadeIn 0.5s ease forwards;
  opacity: 0;
}
.wc-item:nth-child(1){animation-delay:0.3s}
.wc-item:nth-child(2){animation-delay:0.5s}
.wc-item:nth-child(3){animation-delay:0.7s}
.wc-item:nth-child(4){animation-delay:0.9s}
@keyframes itemFadeIn { from{opacity:0;transform:translateX(-8px)} to{opacity:1;transform:translateX(0)} }
.wc-icon {
  width: 28px; height: 28px; border-radius: 9px;
  background: rgba(212,168,67,0.1);
  border: 1px solid rgba(212,168,67,0.2);
  display: flex; align-items: center; justify-content: center;
  font-size: 13px; flex-shrink: 0;
  box-shadow: 0 4px 12px rgba(212,168,67,0.1), inset 0 1px 0 rgba(255,255,255,0.08);
  transition: all 0.3s;
}
.wc-item:hover .wc-icon {
  background: rgba(212,168,67,0.18);
  transform: scale(1.1) rotate(5deg);
  box-shadow: 0 6px 20px rgba(212,168,67,0.2);
}

/* ─── TYPING ─────────────────────────────────── */
.typing-row { display: none; gap: 10px; }
.typing-row.on { display: flex; animation: msgPop 0.3s ease; }
.typing-bub {
  background: linear-gradient(145deg, #181c2c, #111420);
  border: 1px solid rgba(212,168,67,0.14);
  border-radius: 18px 18px 18px 4px;
  padding: 14px 18px; display: flex; gap: 6px; align-items: center;
  box-shadow: 0 6px 24px rgba(0,0,0,0.4);
}
.td { width: 8px; height: 8px; border-radius: 50%; background: var(--gold); }
.td:nth-child(1){animation:tdBounce 1.4s ease-in-out infinite}
.td:nth-child(2){animation:tdBounce 1.4s ease-in-out infinite 0.2s}
.td:nth-child(3){animation:tdBounce 1.4s ease-in-out infinite 0.4s}
@keyframes tdBounce {
  0%,100%{transform:translateY(0) scale(1);opacity:0.3;background:var(--gold)}
  50%{transform:translateY(-8px) scale(1.15);opacity:1;background:var(--gold3);box-shadow:0 4px 12px var(--glow)}
}

/* ─── QUICK BUTTONS ──────────────────────────── */
.quick-strip {
  padding: 8px 16px 10px; display: flex; gap: 7px;
  flex-wrap: wrap; flex-shrink: 0; position: relative; z-index: 2;
}
.qb {
  background: linear-gradient(145deg, rgba(212,168,67,0.07), rgba(212,168,67,0.02));
  border: 1px solid rgba(212,168,67,0.2); color: var(--gold2);
  padding: 7px 13px; border-radius: 100px;
  font-size: 0.73rem; font-family: 'DM Sans', sans-serif; font-weight: 500;
  cursor: pointer; transition: all 0.25s; white-space: nowrap;
  letter-spacing: 0.02em; position: relative; overflow: hidden;
}
.qb::before {
  content: ''; position: absolute; inset: 0; border-radius: 100px;
  background: linear-gradient(135deg, rgba(255,255,255,0.06) 0%, transparent 50%);
  pointer-events: none;
}
.qb::after {
  content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(212,168,67,0.12), transparent);
  transition: left 0.35s;
}
.qb:hover::after { left: 100%; }
.qb:hover {
  border-color: rgba(212,168,67,0.45);
  transform: translateY(-3px) scale(1.04);
  box-shadow: 0 8px 24px rgba(212,168,67,0.2), 0 0 0 1px rgba(212,168,67,0.1);
  background: rgba(212,168,67,0.11);
  color: var(--gold3);
}
.qb:active { transform: scale(0.96); }

/* ─── INPUT ZONE ─────────────────────────────── */
.input-zone {
  padding: 8px 14px 18px; flex-shrink: 0; position: relative; z-index: 2;
}
.input-wrap {
  display: flex; align-items: center; gap: 10px;
  background: linear-gradient(145deg, #141820, #0f1218);
  border: 1px solid rgba(212,168,67,0.2); border-radius: 20px;
  padding: 8px 8px 8px 18px; transition: all 0.3s;
  box-shadow: 0 6px 24px rgba(0,0,0,0.45), inset 0 1px 0 rgba(255,255,255,0.04);
  position: relative; overflow: hidden;
}
.input-wrap::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 1px;
  background: linear-gradient(90deg, transparent, rgba(212,168,67,0.15), transparent);
}
.input-wrap:focus-within {
  border-color: rgba(212,168,67,0.5);
  box-shadow:
    0 6px 24px rgba(0,0,0,0.45),
    0 0 0 3px rgba(212,168,67,0.08),
    0 0 40px rgba(212,168,67,0.07),
    inset 0 1px 0 rgba(255,255,255,0.05);
}
.input-wrap:focus-within::before {
  background: linear-gradient(90deg, transparent, rgba(212,168,67,0.4), transparent);
  animation: inputScan 2s ease-in-out infinite;
}
@keyframes inputScan {
  0%{transform:translateX(-100%)} 100%{transform:translateX(200%)}
}
.inp-field {
  flex: 1; background: transparent; border: none; outline: none;
  font-size: 0.88rem; font-family: 'DM Sans', sans-serif;
  color: var(--text); padding: 8px 0; letter-spacing: 0.01em;
}
.inp-field::placeholder { color: #302c22; }

/* Send button */
.send-btn {
  width: 46px; height: 46px; border-radius: 15px;
  background: linear-gradient(145deg, #e0b045 0%, #c88c28 50%, #b07820 100%);
  border: none; cursor: pointer; display: flex; align-items: center; justify-content: center;
  transition: all 0.2s; flex-shrink: 0; position: relative; overflow: hidden;
  box-shadow:
    0 8px 24px rgba(212,168,67,0.4),
    inset 0 1px 0 rgba(255,255,255,0.28),
    inset 0 -2px 0 rgba(0,0,0,0.25),
    inset 1px 0 0 rgba(255,255,255,0.12);
}
.send-btn::before {
  content: ''; position: absolute; top: 1px; left: 4px; right: 4px; height: 45%;
  background: linear-gradient(rgba(255,255,255,0.24), transparent);
  border-radius: 12px 12px 0 0; pointer-events: none;
}
.send-btn::after {
  content: ''; position: absolute; inset: 0;
  background: radial-gradient(circle at 50% 0%, rgba(255,255,255,0.15), transparent 60%);
  pointer-events: none;
}
.send-btn:hover {
  transform: translateY(-3px) scale(1.06);
  box-shadow:
    0 14px 36px rgba(212,168,67,0.5),
    inset 0 1px 0 rgba(255,255,255,0.28),
    inset 0 -2px 0 rgba(0,0,0,0.25);
}
.send-btn:active { transform: translateY(1px) scale(0.97); }
.send-btn svg { width: 19px; height: 19px; fill: #1a0e00; position: relative; z-index: 1; }

.input-footer {
  display: flex; justify-content: center; gap: 16px; margin-top: 9px;
}
.ifitem {
  font-size: 0.61rem; color: #252218; display: flex; align-items: center; gap: 5px;
  font-family: 'Space Mono', monospace; letter-spacing: 0.04em;
}
.ifdot { width: 3px; height: 3px; border-radius: 50%; background: #252218; }
</style>
</head>
<body>

<div id="scene">
  <canvas id="bgCanvas"></canvas>
</div>
<div class="holo-grid"></div>
<div class="orb-field" id="orbField"></div>

<div class="scene-wrapper">
  <div class="card-stage" id="cardStage">
    <div class="refraction-wrap">
      <div class="ref-shadow"></div>
      <div class="chat-card">
        <div class="scan-beam"></div>
        <div class="scan-beam-glow"></div>

        <div class="corner-fx cfx-tl"></div>
        <div class="corner-fx cfx-tr"></div>
        <div class="corner-fx cfx-bl"></div>
        <div class="corner-fx cfx-br"></div>

        <!-- HEADER -->
        <div class="header">
          <div class="header-row">
            <div class="logo-cube-wrap">
              <div class="orbit-ring"></div>
              <div class="orbit-ring2"></div>
              <div class="logo-cube">🏛️</div>
              <div class="cube-left"></div>
              <div class="cube-bottom"></div>
            </div>

            <div class="brand-info">
              <div class="brand-name">Dream Home <em>Realty</em></div>
              <div class="brand-sub">Premium Properties · Ahmedabad</div>
            </div>

            <div class="live-wrap">
              <div class="live-chip">
                <div class="ldot"></div>
                <span class="ltext">LIVE AI</span>
              </div>
              <div class="ai-badge">GPT · CLAUDE</div>
            </div>
          </div>

          <div class="stats-row">
            <div class="stat"><div class="stat-n">500+</div><div class="stat-l">Properties</div></div>
            <div class="stat"><div class="stat-n">15+</div><div class="stat-l">Areas</div></div>
            <div class="stat"><div class="stat-n">24/7</div><div class="stat-l">Support</div></div>
            <div class="stat"><div class="stat-n">₹25L</div><div class="stat-l">Starting</div></div>
          </div>
        </div>

        <div class="hdiv"></div>

        <!-- MESSAGES -->
        <div class="messages" id="msgs">
          <div class="mrow bot">
            <div class="mav mav-bot">🏛️</div>
            <div class="mbody">
              <div class="welcome-card">
                <div class="wc-title">✨ Welcome to Dream Home Realty</div>
                <div class="wc-items">
                  <div class="wc-item"><div class="wc-icon">🏠</div>Buy, sell or rent residential &amp; commercial property</div>
                  <div class="wc-item"><div class="wc-icon">📍</div>Premium locations across Ahmedabad</div>
                  <div class="wc-item"><div class="wc-icon">🏦</div>Free home loan assistance — SBI, HDFC, ICICI</div>
                  <div class="wc-item"><div class="wc-icon">📅</div>Free site visits arranged within 24 hours</div>
                </div>
              </div>
              <div class="mtime" id="wtime"></div>
            </div>
          </div>
        </div>

        <!-- TYPING -->
        <div class="typing-row" id="typing">
          <div class="mav mav-bot">🏛️</div>
          <div class="typing-bub">
            <div class="td"></div><div class="td"></div><div class="td"></div>
          </div>
        </div>

        <!-- QUICK BUTTONS -->
        <div class="quick-strip" id="quickStrip">
          <button class="qb" onclick="qs('I want to buy a property')">🏠 Buy</button>
          <button class="qb" onclick="qs('Show me rental options')">🔑 Rent</button>
          <button class="qb" onclick="qs('What are your price ranges?')">💰 Prices</button>
          <button class="qb" onclick="qs('Help with home loan')">🏦 Loan</button>
          <button class="qb" onclick="qs('Book a free site visit')">📅 Visit</button>
        </div>

        <!-- INPUT -->
        <div class="input-zone">
          <div class="input-wrap">
            <input class="inp-field" id="inp" type="text"
              placeholder="Ask about properties in Ahmedabad…"
              autocomplete="off"
              onkeypress="if(event.key==='Enter')doSend()"/>
            <button class="send-btn" onclick="doSend()">
              <svg viewBox="0 0 24 24"><path d="M2 21L23 12 2 3v7l15 2-15 2v7z"/></svg>
            </button>
          </div>
          <div class="input-footer">
            <span class="ifitem">🔒 Private</span>
            <span class="ifdot"></span>
            <span class="ifitem">⚡ Instant</span>
            <span class="ifdot"></span>
            <span class="ifitem">🤖 AI Powered</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
/* ─── BACKGROUND CITY SCENE ─────────────────── */
const canvas = document.getElementById('bgCanvas');
const ctx = canvas.getContext('2d');
let W, H, stars=[], buildings=[], frame=0;

function resize(){
  W = canvas.width = window.innerWidth;
  H = canvas.height = window.innerHeight;
  initScene();
}

function initScene(){
  stars = Array.from({length:160},()=>({
    x:Math.random()*W, y:Math.random()*H*0.72,
    r:Math.random()*1.5+0.3, a:Math.random()*Math.PI*2,
    speed:Math.random()*0.006+0.002,
    cx:Math.random()>0.3?'255,240,200':'212,200,255'
  }));

  buildings=[];
  let x=0;
  while(x<W+80){
    const w=28+Math.random()*70, h=55+Math.random()*240;
    const hue = Math.random()>0.7;
    const b={x,w,h,accent:hue,windows:[]};
    for(let wy=12;wy<h-12;wy+=20)
      for(let wx=7;wx<w-7;wx+=16)
        b.windows.push({x:wx,y:wy,lit:Math.random()>0.38,flicker:Math.random()>0.82,warm:Math.random()>0.4});
    buildings.push(b);
    x+=w+3+Math.random()*12;
  }
}

function drawCity(){
  ctx.clearRect(0,0,W,H); frame++;
  // Sky gradient
  const sky=ctx.createLinearGradient(0,0,0,H);
  sky.addColorStop(0,'#020408');
  sky.addColorStop(0.5,'#040610');
  sky.addColorStop(1,'#080c18');
  ctx.fillStyle=sky; ctx.fillRect(0,0,W,H);

  // Moon atmosphere glow
  const mx=W*0.76, my=H*0.14;
  const atm=ctx.createRadialGradient(mx,my,0,mx,my,160);
  atm.addColorStop(0,'rgba(212,168,67,0.10)');
  atm.addColorStop(0.5,'rgba(212,168,67,0.03)');
  atm.addColorStop(1,'transparent');
  ctx.fillStyle=atm; ctx.fillRect(0,0,W,H);

  // Moon
  ctx.beginPath(); ctx.arc(mx,my,26,0,Math.PI*2);
  const mg=ctx.createRadialGradient(mx-5,my-5,0,mx,my,26);
  mg.addColorStop(0,'rgba(255,248,200,0.95)');
  mg.addColorStop(0.5,'rgba(220,175,60,0.8)');
  mg.addColorStop(1,'rgba(180,130,40,0.2)');
  ctx.fillStyle=mg; ctx.fill();
  // Moon halo
  ctx.beginPath(); ctx.arc(mx,my,36,0,Math.PI*2);
  const mh=ctx.createRadialGradient(mx,my,26,mx,my,36);
  mh.addColorStop(0,'rgba(212,168,67,0.15)');
  mh.addColorStop(1,'transparent');
  ctx.fillStyle=mh; ctx.fill();

  // Stars
  stars.forEach(s=>{
    s.a+=s.speed;
    const alpha=0.2+Math.abs(Math.sin(s.a))*0.75;
    ctx.beginPath(); ctx.arc(s.x,s.y,s.r,0,Math.PI*2);
    ctx.fillStyle=`rgba(${s.cx},${alpha})`; ctx.fill();
    // Occasional sparkle cross
    if(s.r>1.2 && Math.sin(s.a*0.3)>0.8){
      ctx.strokeStyle=`rgba(${s.cx},${alpha*0.5})`;
      ctx.lineWidth=0.5;
      ctx.beginPath(); ctx.moveTo(s.x-4,s.y); ctx.lineTo(s.x+4,s.y); ctx.stroke();
      ctx.beginPath(); ctx.moveTo(s.x,s.y-4); ctx.lineTo(s.x,s.y+4); ctx.stroke();
    }
  });

  const groundY=H*0.72;

  // Atmospheric haze
  const haze=ctx.createLinearGradient(0,groundY-80,0,groundY);
  haze.addColorStop(0,'transparent');
  haze.addColorStop(1,'rgba(212,168,67,0.04)');
  ctx.fillStyle=haze; ctx.fillRect(0,groundY-80,W,80);

  // Buildings
  buildings.forEach(b=>{
    const bx=b.x, by=groundY-b.h;

    // Building body
    const bg=ctx.createLinearGradient(bx,by,bx+b.w,by+b.h);
    bg.addColorStop(0,'rgba(18,20,32,0.97)');
    bg.addColorStop(0.5,'rgba(12,14,22,0.99)');
    bg.addColorStop(1,'rgba(8,10,16,0.99)');
    ctx.fillStyle=bg; ctx.fillRect(bx,by,b.w,b.h);

    // Building edge highlight
    ctx.strokeStyle='rgba(212,168,67,0.07)'; ctx.lineWidth=1;
    ctx.strokeRect(bx,by,b.w,b.h);

    // Left face 3D depth
    ctx.beginPath();
    ctx.moveTo(bx,by); ctx.lineTo(bx-6,by+10);
    ctx.lineTo(bx-6,groundY+10); ctx.lineTo(bx,groundY);
    ctx.fillStyle='rgba(6,8,14,0.8)'; ctx.fill();

    // Windows
    b.windows.forEach(win=>{
      if(win.flicker && frame%200===0) win.lit=!win.lit;
      if(!win.lit) return;
      const wx=bx+win.x, wy=by+win.y;
      const wg=ctx.createRadialGradient(wx+4,wy+5,0,wx+4,wy+5,10);
      if(win.warm){
        wg.addColorStop(0,'rgba(255,220,100,0.95)');
        wg.addColorStop(0.5,'rgba(212,168,67,0.4)');
      } else {
        wg.addColorStop(0,'rgba(180,220,255,0.9)');
        wg.addColorStop(0.5,'rgba(100,180,230,0.3)');
      }
      wg.addColorStop(1,'transparent');
      ctx.fillStyle=wg; ctx.fillRect(wx,wy,9,12);
    });

    // Rooftop antenna light
    ctx.beginPath(); ctx.arc(bx+b.w/2, by+2, 2.5, 0, Math.PI*2);
    const blinkAlpha = 0.4+0.55*Math.sin(frame*0.04+b.x*0.01);
    ctx.fillStyle=`rgba(255,80,80,${blinkAlpha})`; ctx.fill();
    ctx.shadowBlur=b.accent?12:6; ctx.shadowColor='rgba(255,80,80,0.5)';
    ctx.fill(); ctx.shadowBlur=0;
  });

  // Ground / road
  ctx.fillStyle='#050710'; ctx.fillRect(0,groundY,W,H-groundY);

  // Road lines
  for(let rx=0;rx<W;rx+=80){
    const rl=ctx.createLinearGradient(rx,groundY,rx,H);
    rl.addColorStop(0,'rgba(212,168,67,0.08)');
    rl.addColorStop(1,'transparent');
    ctx.fillStyle=rl; ctx.fillRect(rx,groundY,1,H-groundY);
  }

  // Ground glow
  const gg=ctx.createLinearGradient(0,groundY,0,groundY+50);
  gg.addColorStop(0,'rgba(212,168,67,0.07)');
  gg.addColorStop(1,'transparent');
  ctx.fillStyle=gg; ctx.fillRect(0,groundY,W,50);

  // Reflection strip
  const ref=ctx.createLinearGradient(0,groundY,W,groundY);
  ref.addColorStop(0,'transparent');
  ref.addColorStop(0.5,'rgba(212,168,67,0.06)');
  ref.addColorStop(1,'transparent');
  ctx.fillStyle=ref; ctx.fillRect(0,groundY-1,W,2);

  requestAnimationFrame(drawCity);
}

window.addEventListener('resize',resize);
resize(); drawCity();

/* ─── ORB PARTICLES ──────────────────────────── */
const of=document.getElementById('orbField');
// Large ambient orbs
['rgba(212,168,67','rgba(64,208,232','rgba(212,168,67'].forEach((c,i)=>{
  const o=document.createElement('div');
  o.className='orb';
  const s=80+i*40;
  o.style.cssText=`width:${s}px;height:${s}px;background:radial-gradient(circle,${c},0.15),transparent);left:${20+i*30}%;animation-duration:${18+i*6}s;animation-delay:${i*5}s;--ox:${(Math.random()-0.5)*200}px;`;
  of.appendChild(o);
});
// Sparks
for(let i=0;i<40;i++){
  const sp=document.createElement('div');
  sp.className='spark';
  sp.style.cssText=`left:${Math.random()*100}%;top:${50+Math.random()*50}%;animation-duration:${6+Math.random()*10}s;animation-delay:${Math.random()*12}s;width:${1+Math.random()*2}px;height:${1+Math.random()*2}px;`;
  of.appendChild(sp);
}

/* ─── 3D TILT ────────────────────────────────── */
const cardStage=document.getElementById('cardStage');
let tiltTarget={x:0,y:0}, tiltCurrent={x:0,y:0};
document.addEventListener('mousemove',e=>{
  const dx=(e.clientX-window.innerWidth/2)/(window.innerWidth/2);
  const dy=(e.clientY-window.innerHeight/2)/(window.innerHeight/2);
  tiltTarget={x:dx*5,y:-dy*3.5};
});
document.addEventListener('mouseleave',()=>{tiltTarget={x:0,y:0};});
function tiltLoop(){
  tiltCurrent.x+=(tiltTarget.x-tiltCurrent.x)*0.08;
  tiltCurrent.y+=(tiltTarget.y-tiltCurrent.y)*0.08;
  cardStage.style.transform=`perspective(1400px) rotateY(${tiltCurrent.x}deg) rotateX(${tiltCurrent.y}deg)`;
  requestAnimationFrame(tiltLoop);
}
tiltLoop();

/* ─── CHAT LOGIC ─────────────────────────────── */
let history=[];
document.getElementById('wtime').textContent=getTime();

function getTime(){
  return new Date().toLocaleTimeString('en-IN',{hour:'2-digit',minute:'2-digit'});
}

async function doSend(){
  const inp=document.getElementById('inp');
  const msg=inp.value.trim(); if(!msg) return;
  document.getElementById('quickStrip').style.display='none';
  addMsg(msg,'user'); inp.value=''; setTyping(true);

  try {
    const res = await fetch('https://api.anthropic.com/v1/messages',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body: JSON.stringify({
        model:'claude-sonnet-4-20250514',
        max_tokens:1000,
        system:`You are a warm, professional AI assistant for Dream Home Realty — a premium real estate agency in Ahmedabad, India. Help users with:
- Property buying, selling, renting (residential & commercial)
- Areas: Satellite, Bodakdev, Prahlad Nagar, Thaltej, Bopal, SG Highway, Vastrapur, Navrangpura, and more
- Pricing guidance (₹25L–₹5Cr+)
- Home loan assistance (SBI, HDFC, ICICI, Axis)
- Site visit bookings (free, within 24 hrs)
Keep responses concise, friendly, and helpful. Use bullet points when listing properties or features. Always offer next steps.`,
        messages:[...history,{role:'user',content:msg}]
      })
    });
    const data=await res.json();
    const reply=data.content?.[0]?.text || 'I apologize, I had trouble generating a response. Please try again.';
    setTyping(false); addMsg(reply,'bot');
    history.push({role:'user',content:msg},{role:'assistant',content:reply});
  } catch(err){
    setTyping(false);
    addMsg('Connection issue — please try again in a moment.','bot');
  }
}

function qs(msg){ document.getElementById('inp').value=msg; doSend(); }

function addMsg(text,type){
  const msgs=document.getElementById('msgs');
  const row=document.createElement('div'); row.className=`mrow ${type}`;
  const av=document.createElement('div');
  av.className=`mav ${type==='bot'?'mav-bot':'mav-usr'}`;
  av.textContent=type==='bot'?'🏛️':'👤';
  const body=document.createElement('div'); body.className='mbody';
  if(type==='user') body.style.alignItems='flex-end';
  const bub=document.createElement('div');
  bub.className=`bubble-${type==='bot'?'bot':'usr'}`;
  bub.textContent=text;
  const t=document.createElement('div'); t.className='mtime'; t.textContent=getTime();
  body.appendChild(bub); body.appendChild(t);
  if(type==='bot'){row.appendChild(av);row.appendChild(body);}
  else{row.appendChild(body);row.appendChild(av);}
  msgs.appendChild(row);
  row.scrollIntoView({behavior:'smooth',block:'end'});
}

function setTyping(show){
  const t=document.getElementById('typing');
  t.classList.toggle('on',show);
  if(show) t.scrollIntoView({behavior:'smooth',block:'end'});
}
</script>
</body>
</html>
