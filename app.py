<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dream Home Realty</title>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;700;900&family=Nunito:wght@300;400;500;600;700&family=Fira+Code:wght@300;400;500&display=swap" rel="stylesheet">
<style>
/* ═══════════════════════════════════════════════
   ROOT VARIABLES
═══════════════════════════════════════════════ */
:root {
  --g1: #f5c842;
  --g2: #e8a820;
  --g3: #d4881a;
  --g4: #ffea90;
  --glow: rgba(245,200,66,0.45);
  --glow2: rgba(245,200,66,0.15);
  --dark: #04060d;
  --dark2: #080b15;
  --dark3: #0c1020;
  --panel: rgba(8,11,20,0.92);
  --glass: rgba(255,255,255,0.025);
  --border: rgba(245,200,66,0.2);
  --border2: rgba(245,200,66,0.08);
  --text: #ede8de;
  --muted: #3d3928;
  --cyan: #3dd6f5;
  --red: #ff5555;
  --green: #00e676;
  --r: 32px;
}

/* ═══════════════════════════════════════════════
   RESET & BASE
═══════════════════════════════════════════════ */
*, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }

html, body {
  width: 100%; height: 100%;
  overflow: hidden;
  background: var(--dark);
  font-family: 'Nunito', sans-serif;
  cursor: none;
}

/* ═══════════════════════════════════════════════
   CUSTOM CURSOR
═══════════════════════════════════════════════ */
#cursor-dot {
  position: fixed; z-index: 9999; pointer-events: none;
  width: 8px; height: 8px; border-radius: 50%;
  background: var(--g1);
  box-shadow: 0 0 16px var(--glow), 0 0 40px var(--glow2);
  transform: translate(-50%, -50%);
  transition: transform 0.05s, width 0.2s, height 0.2s;
}
#cursor-ring {
  position: fixed; z-index: 9998; pointer-events: none;
  width: 36px; height: 36px; border-radius: 50%;
  border: 1px solid rgba(245,200,66,0.5);
  transform: translate(-50%, -50%);
  transition: transform 0.12s ease-out, width 0.3s, height 0.3s, border-color 0.3s;
}
body:has(button:hover) #cursor-dot { width: 16px; height: 16px; }
body:has(button:hover) #cursor-ring { width: 60px; height: 60px; border-color: var(--g1); }

/* ═══════════════════════════════════════════════
   CANVAS LAYERS
═══════════════════════════════════════════════ */
#city-canvas {
  position: fixed; inset: 0; z-index: 0;
  width: 100%; height: 100%;
}
#particle-canvas {
  position: fixed; inset: 0; z-index: 1; pointer-events: none;
  width: 100%; height: 100%;
}

/* ═══════════════════════════════════════════════
   HOLOGRAPHIC OVERLAY
═══════════════════════════════════════════════ */
.holo-overlay {
  position: fixed; inset: 0; z-index: 2; pointer-events: none;
  background:
    repeating-linear-gradient(
      0deg,
      transparent,
      transparent 3px,
      rgba(245,200,66,0.008) 3px,
      rgba(245,200,66,0.008) 4px
    );
  animation: holoShift 8s linear infinite;
}
@keyframes holoShift { from{background-position:0 0} to{background-position:0 100px} }

.grid-overlay {
  position: fixed; inset: 0; z-index: 2; pointer-events: none;
  background-image:
    linear-gradient(rgba(245,200,66,0.025) 1px, transparent 1px),
    linear-gradient(90deg, rgba(245,200,66,0.025) 1px, transparent 1px);
  background-size: 80px 80px;
  mask-image: radial-gradient(ellipse 80% 80% at 50% 50%, black 30%, transparent 100%);
  animation: gridDrift 25s linear infinite;
}
@keyframes gridDrift { from{transform:perspective(600px) rotateX(20deg) translateY(0)} to{transform:perspective(600px) rotateX(20deg) translateY(80px)} }

/* ═══════════════════════════════════════════════
   SCENE WRAPPER
═══════════════════════════════════════════════ */
.scene {
  position: fixed; inset: 0; z-index: 10;
  display: flex; align-items: center; justify-content: center;
  padding: 12px;
}

/* ═══════════════════════════════════════════════
   CARD WRAPPER WITH DEPTH
═══════════════════════════════════════════════ */
.card-wrapper {
  position: relative;
  width: 100%; max-width: 500px;
  animation: floatIn 1.3s cubic-bezier(0.16,1,0.3,1) forwards;
  transform-style: preserve-3d;
  will-change: transform;
}
@keyframes floatIn {
  0%  { opacity:0; transform:perspective(1200px) rotateX(30deg) rotateY(-20deg) translateY(100px) scale(0.8); }
  60% { opacity:1; }
  100%{ opacity:1; transform:perspective(1200px) rotateX(0) rotateY(0) translateY(0) scale(1); }
}

/* Glow halo behind card */
.card-halo {
  position: absolute; inset: -40px;
  border-radius: 60px;
  background: radial-gradient(ellipse at 50% 50%,
    rgba(245,200,66,0.12) 0%,
    rgba(245,200,66,0.05) 40%,
    transparent 70%);
  filter: blur(30px);
  animation: haloPulse 4s ease-in-out infinite;
  pointer-events: none;
}
@keyframes haloPulse {
  0%,100%{opacity:0.7;transform:scale(1)}
  50%{opacity:1;transform:scale(1.05)}
}

/* Depth shadow slices */
.card-depth {
  position: absolute; inset: 0;
  border-radius: var(--r);
  transform: translateZ(-30px) translateY(20px) scale(0.96);
  background: rgba(0,0,0,0.7);
  filter: blur(24px);
  pointer-events: none;
}
.card-depth2 {
  position: absolute; inset: 0;
  border-radius: var(--r);
  transform: translateZ(-15px) translateY(10px) scale(0.98);
  background: rgba(245,200,66,0.04);
  filter: blur(12px);
  pointer-events: none;
}

/* ═══════════════════════════════════════════════
   MAIN CHAT CARD
═══════════════════════════════════════════════ */
.chat-card {
  position: relative;
  border-radius: var(--r);
  overflow: hidden;
  display: flex; flex-direction: column;
  height: min(760px, 92vh);
  background:
    linear-gradient(160deg,
      rgba(14,18,30,0.97) 0%,
      rgba(8,11,20,0.99) 45%,
      rgba(10,13,22,0.97) 100%);
  border: 1px solid var(--border);
  box-shadow:
    0 0 0 1px var(--border2),
    0 0 80px rgba(245,200,66,0.07),
    0 40px 120px rgba(0,0,0,0.95),
    inset 0 1px 0 rgba(255,255,255,0.07),
    inset 0 -1px 0 rgba(245,200,66,0.06),
    inset 1px 0 0 rgba(255,255,255,0.03),
    inset -1px 0 0 rgba(255,255,255,0.02);
  transform-style: preserve-3d;
}

/* Top glass sheen */
.chat-card::before {
  content: '';
  position: absolute; top: 0; left: 0; right: 0; height: 160px;
  background: linear-gradient(180deg,
    rgba(255,255,255,0.05) 0%,
    rgba(255,255,255,0.02) 40%,
    transparent 100%);
  border-radius: var(--r) var(--r) 0 0;
  pointer-events: none; z-index: 0;
}

/* ═══════════════════════════════════════════════
   SCAN BEAM
═══════════════════════════════════════════════ */
.scan-wrap {
  position: absolute; top: 0; left: 0; right: 0; z-index: 50;
  overflow: hidden; height: 3px; border-radius: var(--r) var(--r) 0 0;
}
.scan-beam {
  position: absolute; top: 0; left: -100%; width: 120%; height: 100%;
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(245,200,66,0.0) 25%,
    rgba(245,200,66,0.8) 45%,
    rgba(255,240,140,1) 50%,
    rgba(245,200,66,0.8) 55%,
    rgba(245,200,66,0.0) 75%,
    transparent 100%);
  animation: scanBeam 3.5s ease-in-out infinite;
  filter: blur(0.5px);
}
.scan-glow {
  position: absolute; top: 0; left: -100%; width: 120%; height: 60px;
  background: linear-gradient(90deg,
    transparent 30%, rgba(245,200,66,0.07) 50%, transparent 70%);
  animation: scanBeam 3.5s ease-in-out infinite;
  filter: blur(15px);
}
@keyframes scanBeam {
  0%   { transform: translateX(-30%); }
  50%  { transform: translateX(130%); }
  100% { transform: translateX(130%); }
}

/* ═══════════════════════════════════════════════
   CORNER BRACKETS
═══════════════════════════════════════════════ */
.cbr { position: absolute; z-index: 60; width: 22px; height: 22px; }
.cbr span {
  position: absolute; background: var(--g2);
  box-shadow: 0 0 10px var(--glow), 0 0 24px var(--glow2);
  border-radius: 2px;
  animation: cbrPulse 2.5s ease-in-out infinite;
}
.cbr span:first-child { width: 22px; height: 2px; }
.cbr span:last-child  { width: 2px; height: 22px; }
@keyframes cbrPulse {
  0%,100%{opacity:0.55;box-shadow:0 0 8px var(--glow)}
  50%{opacity:1;box-shadow:0 0 20px var(--glow),0 0 40px var(--glow2)}
}
.cbr-tl { top:12px; left:12px; }
.cbr-tl span:first-child { top:0; left:0; }
.cbr-tl span:last-child  { top:0; left:0; }
.cbr-tr { top:12px; right:12px; }
.cbr-tr span:first-child { top:0; right:0; }
.cbr-tr span:last-child  { top:0; right:0; }
.cbr-bl { bottom:12px; left:12px; }
.cbr-bl span:first-child { bottom:0; left:0; }
.cbr-bl span:last-child  { bottom:0; left:0; }
.cbr-br { bottom:12px; right:12px; }
.cbr-br span:first-child { bottom:0; right:0; }
.cbr-br span:last-child  { bottom:0; right:0; }

/* ═══════════════════════════════════════════════
   HEADER
═══════════════════════════════════════════════ */
.header {
  padding: 22px 22px 16px;
  position: relative; z-index: 5; flex-shrink: 0;
}

.hdr-top { display: flex; align-items: center; gap: 14px; }

/* LOGO */
.logo-rig {
  position: relative; width: 60px; height: 60px; flex-shrink: 0;
  transform-style: preserve-3d;
}
.logo-face {
  position: relative; z-index: 3;
  width: 60px; height: 60px; border-radius: 20px;
  background:
    linear-gradient(145deg, #2e2410 0%, #1c1508 60%, #271d0c 100%);
  border: 1px solid rgba(245,200,66,0.55);
  display: flex; align-items: center; justify-content: center;
  font-size: 26px;
  box-shadow:
    0 0 0 1px rgba(245,200,66,0.12),
    0 14px 40px rgba(245,200,66,0.3),
    0 4px 16px rgba(0,0,0,0.8),
    inset 0 1px 0 rgba(255,255,255,0.14),
    inset 0 -2px 0 rgba(0,0,0,0.4);
  animation: logoRock 5s ease-in-out infinite;
  cursor: default;
}
@keyframes logoRock {
  0%,100%{transform:translateY(0) rotateY(0deg) rotateZ(0deg)}
  20%{transform:translateY(-4px) rotateY(8deg) rotateZ(1deg)}
  70%{transform:translateY(-3px) rotateY(-6deg) rotateZ(-1deg)}
}

/* 3D cube sides */
.logo-left {
  position: absolute; top: 8px; left: -7px;
  width: 7px; height: 44px;
  background: linear-gradient(180deg, rgba(160,120,30,0.7) 0%, rgba(80,58,10,0.9) 100%);
  border-radius: 3px 0 0 3px;
  transform: skewY(-10deg);
  z-index: 2;
}
.logo-bot {
  position: absolute; bottom: -7px; left: 5px; right: 5px;
  height: 7px;
  background: linear-gradient(90deg, rgba(120,90,20,0.8) 0%, rgba(70,50,10,0.7) 100%);
  border-radius: 0 0 5px 5px;
  transform: skewX(-10deg);
  z-index: 2;
}

/* Orbit rings */
.orb1 {
  position: absolute; inset: -8px; border-radius: 50%;
  border: 1.5px solid transparent;
  border-top-color: rgba(245,200,66,0.6);
  border-right-color: rgba(245,200,66,0.2);
  animation: orb1Spin 2.8s linear infinite;
  z-index: 4;
}
.orb2 {
  position: absolute; inset: -15px; border-radius: 50%;
  border: 1px solid transparent;
  border-bottom-color: rgba(61,214,245,0.4);
  border-left-color: rgba(61,214,245,0.15);
  animation: orb1Spin 5s linear infinite reverse;
  z-index: 4;
}
.orb3 {
  position: absolute; inset: -22px; border-radius: 50%;
  border: 1px dashed rgba(245,200,66,0.1);
  animation: orb1Spin 12s linear infinite;
  z-index: 4;
}
@keyframes orb1Spin { from{transform:rotate(0deg)} to{transform:rotate(360deg)} }

/* Pulse dot */
.logo-pulse {
  position: absolute; top: -4px; right: -4px; z-index: 10;
  width: 12px; height: 12px; border-radius: 50%;
  background: var(--green);
  box-shadow: 0 0 16px var(--green);
}
.logo-pulse::after {
  content: ''; position: absolute; inset: -4px; border-radius: 50%;
  border: 1px solid rgba(0,230,100,0.4);
  animation: pulseRipple 1.8s ease-out infinite;
}
@keyframes pulseRipple {
  0%{transform:scale(0.6);opacity:1}
  100%{transform:scale(2.2);opacity:0}
}

/* Brand text */
.brand { flex: 1; }
.brand-name {
  font-family: 'Cinzel', serif;
  font-size: 1.08rem; font-weight: 700;
  letter-spacing: 0.06em;
  line-height: 1.2;
  color: #fff;
  text-shadow: 0 0 30px rgba(245,200,66,0.35);
}
.brand-name b {
  background: linear-gradient(90deg, var(--g1) 0%, var(--g4) 50%, var(--g1) 100%);
  background-size: 200% auto;
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: shimmerText 4s linear infinite;
}
@keyframes shimmerText {
  from{background-position:0% 50%} to{background-position:200% 50%}
}
.brand-sub {
  font-family: 'Fira Code', monospace;
  font-size: 0.6rem; color: var(--muted);
  letter-spacing: 0.2em; text-transform: uppercase; margin-top: 4px;
}

/* Live / status */
.status-col {
  display: flex; flex-direction: column; align-items: flex-end; gap: 6px;
}
.live-pill {
  display: flex; align-items: center; gap: 7px;
  padding: 5px 12px;
  background: rgba(0,230,100,0.07);
  border: 1px solid rgba(0,230,100,0.25);
  border-radius: 100px;
  position: relative; overflow: hidden;
}
.live-pill::before {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(90deg, transparent, rgba(0,230,100,0.06), transparent);
  animation: pillSheen 3s ease-in-out infinite;
}
@keyframes pillSheen { 0%,100%{transform:translateX(-100%)} 60%{transform:translateX(100%)} }
.ldot {
  width: 8px; height: 8px; border-radius: 50%;
  background: var(--green); position: relative;
  box-shadow: 0 0 14px var(--green);
  animation: ldotBeat 1.6s ease-in-out infinite;
}
@keyframes ldotBeat {
  0%,100%{transform:scale(1);opacity:1}
  50%{transform:scale(1.5);opacity:0.7}
}
.ldot::after {
  content: ''; position: absolute; inset: -5px; border-radius: 50%;
  border: 1px solid rgba(0,230,100,0.3);
  animation: ldotRing 1.6s ease-out infinite;
}
@keyframes ldotRing {
  0%{transform:scale(0.5);opacity:1}
  100%{transform:scale(2.5);opacity:0}
}
.live-txt { font-size: 0.67rem; font-weight: 700; color: var(--green); letter-spacing: 0.12em; font-family:'Fira Code',monospace; }
.model-tag {
  font-family:'Fira Code',monospace; font-size:0.57rem;
  color:rgba(245,200,66,0.45); letter-spacing:0.1em;
  border:1px solid rgba(245,200,66,0.1); border-radius:5px; padding:2px 7px;
}

/* ═══════════════════════════════════════════════
   STATS GRID
═══════════════════════════════════════════════ */
.stats {
  display: grid; grid-template-columns: repeat(4,1fr);
  gap: 8px; margin-top: 14px;
}
.stat {
  background: linear-gradient(145deg, rgba(245,200,66,0.07) 0%, rgba(245,200,66,0.02) 100%);
  border: 1px solid var(--border2);
  border-radius: 14px; padding: 10px 6px;
  text-align: center; cursor: default;
  position: relative; overflow: hidden;
  transition: all 0.3s ease;
  transform-style: preserve-3d;
}
/* glass top reflection */
.stat::before {
  content: ''; position: absolute; top: 0; left: 0; right: 0; height: 50%;
  background: linear-gradient(180deg, rgba(255,255,255,0.05) 0%, transparent 100%);
  border-radius: 14px 14px 0 0; pointer-events: none;
}
/* hover sweep */
.stat::after {
  content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(245,200,66,0.1), transparent);
  transition: left 0.45s;
}
.stat:hover::after { left: 100%; }
.stat:hover {
  border-color: rgba(245,200,66,0.35);
  transform: translateY(-4px) rotateX(8deg) scale(1.04);
  box-shadow: 0 16px 36px rgba(245,200,66,0.15), 0 0 0 1px rgba(245,200,66,0.08);
}
.sn {
  font-family: 'Cinzel', serif; font-size: 1.0rem; font-weight: 700;
  background: linear-gradient(135deg, var(--g1), var(--g4));
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  background-clip: text;
}
.sl { font-size: 0.57rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.09em; margin-top: 2px; }

/* ═══════════════════════════════════════════════
   DIVIDER
═══════════════════════════════════════════════ */
.divider {
  height: 1px; margin: 0 18px; flex-shrink: 0;
  background: linear-gradient(90deg,
    transparent,
    rgba(245,200,66,0.18) 30%,
    rgba(61,214,245,0.1) 50%,
    rgba(245,200,66,0.18) 70%,
    transparent);
  position: relative;
}
.divider::after {
  content: ''; position: absolute;
  top: -1px; left: 50%; transform: translateX(-50%);
  width: 80px; height: 3px; border-radius: 3px;
  background: linear-gradient(90deg, rgba(245,200,66,0.5), rgba(255,240,140,1), rgba(245,200,66,0.5));
  filter: blur(2px);
  animation: divGlow 3s ease-in-out infinite;
}
@keyframes divGlow {
  0%,100%{opacity:0.5;width:40px}
  50%{opacity:1;width:120px}
}

/* ═══════════════════════════════════════════════
   MESSAGES
═══════════════════════════════════════════════ */
.messages {
  flex: 1; overflow-y: auto;
  padding: 16px 16px 8px;
  display: flex; flex-direction: column; gap: 14px;
  position: relative; z-index: 2;
  scroll-behavior: smooth;
}
.messages::-webkit-scrollbar { width: 2px; }
.messages::-webkit-scrollbar-thumb {
  background: linear-gradient(var(--g1), var(--g3)); border-radius: 2px;
}

/* Row */
.mrow { display: flex; gap: 10px; animation: rowIn 0.5s cubic-bezier(0.16,1,0.3,1) forwards; }
.mrow.usr { flex-direction: row-reverse; }
@keyframes rowIn {
  from{opacity:0;transform:translateY(18px) scale(0.93)}
  to{opacity:1;transform:translateY(0) scale(1)}
}

/* Avatar */
.mav {
  width: 38px; height: 38px; border-radius: 13px;
  display: flex; align-items: center; justify-content: center;
  font-size: 18px; flex-shrink: 0; align-self: flex-end;
  position: relative; cursor: default;
}
.mav-bot {
  background: linear-gradient(145deg, #2e2410, #1c1508);
  border: 1px solid rgba(245,200,66,0.4);
  box-shadow: 0 8px 24px rgba(245,200,66,0.2), inset 0 1px 0 rgba(255,255,255,0.12);
  animation: avFloat 3s ease-in-out infinite;
}
@keyframes avFloat {
  0%,100%{transform:translateY(0)}
  50%{transform:translateY(-3px)}
}
.mav-bot::after {
  content:''; position:absolute; inset:-4px; border-radius:16px;
  border:1px solid rgba(245,200,66,0.15);
  animation: avRing 2s ease-in-out infinite;
}
@keyframes avRing { 0%,100%{opacity:0.4;transform:scale(1)} 50%{opacity:0.9;transform:scale(1.06)} }
.mav-usr {
  background: linear-gradient(145deg, #0d1f0e, #080f08);
  border: 1px solid rgba(80,200,100,0.25);
  box-shadow: 0 6px 18px rgba(0,230,100,0.12);
}

/* Body */
.mbody { max-width: 82%; display:flex; flex-direction:column; gap:4px; }
.mrow.usr .mbody { align-items:flex-end; }

/* Bot bubble */
.bbot {
  background: linear-gradient(145deg, #171b2c 0%, #101420 100%);
  border: 1px solid rgba(245,200,66,0.13);
  border-bottom-left-radius: 4px;
  border-radius: 18px 18px 18px 4px;
  padding: 13px 16px;
  font-size: 0.875rem; line-height: 1.72; color: var(--text);
  position: relative; overflow: hidden;
  box-shadow:
    0 8px 30px rgba(0,0,0,0.5),
    inset 0 1px 0 rgba(255,255,255,0.05),
    0 0 0 1px rgba(245,200,66,0.04);
}
.bbot::before {
  content:''; position:absolute; top:0; left:0; right:0; height:1px;
  background:linear-gradient(90deg,transparent,rgba(245,200,66,0.35),rgba(61,214,245,0.15),rgba(245,200,66,0.35),transparent);
}
/* Usr bubble */
.busr {
  background: linear-gradient(145deg, #e8b83a 0%, #c8901e 55%, #d4a020 100%);
  border-radius: 18px 18px 4px 18px;
  padding: 13px 16px;
  font-size: 0.875rem; line-height: 1.72; color: #1a0e00; font-weight: 600;
  position: relative; overflow: hidden;
  box-shadow:
    0 10px 32px rgba(245,200,66,0.4),
    inset 0 1px 0 rgba(255,255,255,0.3),
    inset 0 -2px 0 rgba(0,0,0,0.2);
}
.busr::before {
  content:''; position:absolute; top:0; left:-100%; width:60%; height:100%;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,0.15),transparent);
  animation:usrSheen 5s ease-in-out infinite;
}
@keyframes usrSheen { 0%,100%{left:-100%} 50%{left:200%} }

.mtime {
  font-size:0.59rem; color:var(--muted); padding:0 5px;
  letter-spacing:0.05em; font-family:'Fira Code',monospace;
}

/* ═══════════════════════════════════════════════
   WELCOME CARD
═══════════════════════════════════════════════ */
.welcome {
  background: linear-gradient(145deg,
    rgba(245,200,66,0.08) 0%,
    rgba(245,200,66,0.03) 50%,
    rgba(61,214,245,0.025) 100%);
  border: 1px solid rgba(245,200,66,0.22);
  border-radius: 20px 20px 20px 4px;
  padding: 18px 18px 16px;
  position: relative; overflow: hidden;
  box-shadow: 0 16px 50px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.07);
}
.welcome::before {
  content:''; position:absolute; top:0; left:0; right:0; height:1px;
  background:linear-gradient(90deg,
    transparent,
    rgba(245,200,66,0.6) 25%,
    rgba(61,214,245,0.3) 50%,
    rgba(245,200,66,0.6) 75%,
    transparent);
}
/* Diagonal shine */
.welcome::after {
  content:''; position:absolute;
  top:-50%; left:-50%; width:60%; height:200%;
  background:linear-gradient(105deg,transparent 40%,rgba(255,255,255,0.03) 50%,transparent 60%);
  animation:wShine 6s ease-in-out infinite;
}
@keyframes wShine { 0%,100%{transform:translateX(-100%) rotate(15deg)} 50%{transform:translateX(300%) rotate(15deg)} }

.w-title {
  font-family:'Cinzel',serif; font-size:0.95rem; font-weight:700;
  background:linear-gradient(90deg,var(--g1),var(--g4),var(--g1));
  background-size:200% auto;
  -webkit-background-clip:text; -webkit-text-fill-color:transparent;
  background-clip:text; margin-bottom:13px;
  animation:shimmerText 4s linear infinite;
}
.w-items { display:flex; flex-direction:column; gap:9px; }
.w-item {
  display:flex; align-items:center; gap:11px;
  font-size:0.8rem; color:#8a8472;
  opacity:0; animation:wItemIn 0.5s ease forwards;
}
.w-item:nth-child(1){animation-delay:0.4s}
.w-item:nth-child(2){animation-delay:0.65s}
.w-item:nth-child(3){animation-delay:0.9s}
.w-item:nth-child(4){animation-delay:1.15s}
@keyframes wItemIn {
  from{opacity:0;transform:translateX(-12px)}
  to{opacity:1;transform:translateX(0)}
}
.w-icon {
  width:30px; height:30px; border-radius:10px; flex-shrink:0;
  background:rgba(245,200,66,0.1);
  border:1px solid rgba(245,200,66,0.2);
  display:flex; align-items:center; justify-content:center; font-size:14px;
  box-shadow:0 4px 16px rgba(245,200,66,0.1),inset 0 1px 0 rgba(255,255,255,0.1);
  transition:all 0.3s;
}
.w-item:hover .w-icon {
  background:rgba(245,200,66,0.18);
  transform:scale(1.15) rotate(8deg);
  box-shadow:0 8px 24px rgba(245,200,66,0.25);
}

/* ═══════════════════════════════════════════════
   TYPING INDICATOR
═══════════════════════════════════════════════ */
.typing-row { display:none; gap:10px; }
.typing-row.on { display:flex; animation:rowIn 0.35s ease; }
.typing-bub {
  background:linear-gradient(145deg,#171b2c,#101420);
  border:1px solid rgba(245,200,66,0.13);
  border-radius:18px 18px 18px 4px;
  padding:15px 18px; display:flex; gap:6px; align-items:center;
  box-shadow:0 8px 28px rgba(0,0,0,0.45);
}
.td {
  width:9px; height:9px; border-radius:50%;
  background:var(--g1);
}
.td:nth-child(1){animation:tdBounce 1.4s ease-in-out infinite}
.td:nth-child(2){animation:tdBounce 1.4s ease-in-out infinite 0.18s}
.td:nth-child(3){animation:tdBounce 1.4s ease-in-out infinite 0.36s}
@keyframes tdBounce {
  0%,100%{transform:translateY(0) scale(1);opacity:0.3;background:var(--g2)}
  50%{transform:translateY(-9px) scale(1.2);opacity:1;background:var(--g4);box-shadow:0 4px 14px var(--glow)}
}

/* ═══════════════════════════════════════════════
   QUICK CHIPS
═══════════════════════════════════════════════ */
.qstrip {
  padding:8px 16px 10px; display:flex; gap:7px;
  flex-wrap:wrap; flex-shrink:0; position:relative; z-index:2;
}
.qchip {
  background:linear-gradient(145deg, rgba(245,200,66,0.08), rgba(245,200,66,0.02));
  border:1px solid rgba(245,200,66,0.22); color:var(--g1);
  padding:7px 14px; border-radius:100px;
  font-size:0.73rem; font-family:'Nunito',sans-serif; font-weight:600;
  cursor:pointer; white-space:nowrap; letter-spacing:0.02em;
  transition:all 0.25s; position:relative; overflow:hidden;
}
.qchip::before {
  content:''; position:absolute; inset:0; border-radius:100px;
  background:linear-gradient(135deg,rgba(255,255,255,0.06) 0%,transparent 55%);
  pointer-events:none;
}
.qchip::after {
  content:''; position:absolute; top:0; left:-100%; width:100%; height:100%;
  background:linear-gradient(90deg,transparent,rgba(245,200,66,0.14),transparent);
  transition:left 0.4s;
}
.qchip:hover::after { left:100%; }
.qchip:hover {
  border-color:rgba(245,200,66,0.5);
  transform:translateY(-3px) scale(1.05);
  box-shadow:0 10px 28px rgba(245,200,66,0.22), 0 0 0 1px rgba(245,200,66,0.1);
  color:var(--g4);
}
.qchip:active{transform:scale(0.96);}

/* ═══════════════════════════════════════════════
   INPUT ZONE
═══════════════════════════════════════════════ */
.input-zone {
  padding:8px 14px 20px; flex-shrink:0; position:relative; z-index:2;
}
.input-shell {
  display:flex; align-items:center; gap:10px;
  background:linear-gradient(145deg,#131720,#0e1118);
  border:1px solid rgba(245,200,66,0.22); border-radius:20px;
  padding:8px 8px 8px 18px;
  transition:all 0.35s;
  box-shadow:0 6px 28px rgba(0,0,0,0.5),inset 0 1px 0 rgba(255,255,255,0.04);
  position:relative; overflow:hidden;
}
.input-shell::before {
  content:''; position:absolute; top:0; left:0; right:0; height:1px;
  background:linear-gradient(90deg,transparent,rgba(245,200,66,0.2),transparent);
  transition:all 0.3s;
}
.input-shell:focus-within {
  border-color:rgba(245,200,66,0.55);
  box-shadow:
    0 6px 28px rgba(0,0,0,0.5),
    0 0 0 3px rgba(245,200,66,0.09),
    0 0 50px rgba(245,200,66,0.08);
}
.input-shell:focus-within::before {
  background:linear-gradient(90deg,transparent,rgba(245,200,66,0.55),rgba(61,214,245,0.2),rgba(245,200,66,0.55),transparent);
  animation:inputScan 2.5s ease-in-out infinite;
}
@keyframes inputScan { 0%,100%{opacity:0.4} 50%{opacity:1} }
.ifield {
  flex:1; background:transparent; border:none; outline:none;
  font-size:0.88rem; font-family:'Nunito',sans-serif;
  color:var(--text); padding:8px 0; letter-spacing:0.01em;
}
.ifield::placeholder { color:#282418; }

/* Send button */
.send-btn {
  width:48px; height:48px; border-radius:16px; flex-shrink:0;
  background:linear-gradient(145deg, #ecbe40 0%, #c8911e 50%, #b07a18 100%);
  border:none; cursor:pointer;
  display:flex; align-items:center; justify-content:center;
  transition:all 0.2s; position:relative; overflow:hidden;
  box-shadow:
    0 10px 28px rgba(245,200,66,0.45),
    inset 0 1px 0 rgba(255,255,255,0.3),
    inset 0 -2px 0 rgba(0,0,0,0.25),
    inset 1px 0 0 rgba(255,255,255,0.12);
}
.send-btn::before {
  content:''; position:absolute; top:1px; left:4px; right:4px; height:44%;
  background:linear-gradient(rgba(255,255,255,0.22),transparent);
  border-radius:14px 14px 0 0; pointer-events:none;
}
.send-btn::after {
  content:''; position:absolute; inset:0;
  background:radial-gradient(circle at 50% 0%,rgba(255,255,255,0.18),transparent 60%);
  pointer-events:none;
}
.send-btn:hover {
  transform:translateY(-3px) scale(1.07);
  box-shadow:0 18px 40px rgba(245,200,66,0.55),inset 0 1px 0 rgba(255,255,255,0.3);
}
.send-btn:active{transform:translateY(1px) scale(0.97);}
.send-btn svg { width:20px; height:20px; fill:#1a0e00; position:relative; z-index:1; }

/* Footer */
.input-foot {
  display:flex; justify-content:center; gap:16px; margin-top:8px;
}
.ifoot-item {
  font-size:0.6rem; color:#201e14; display:flex; align-items:center; gap:5px;
  font-family:'Fira Code',monospace; letter-spacing:0.05em;
}
.ifoot-sep { width:3px; height:3px; border-radius:50%; background:#201e14; }

/* ═══════════════════════════════════════════════
   NOTIFICATION TOAST
═══════════════════════════════════════════════ */
.toast {
  position:fixed; bottom:30px; left:50%; transform:translateX(-50%) translateY(100px);
  background:linear-gradient(135deg, rgba(14,18,30,0.98), rgba(8,11,20,0.99));
  border:1px solid var(--border); border-radius:14px; padding:12px 20px;
  font-size:0.8rem; color:var(--text);
  box-shadow:0 16px 50px rgba(0,0,0,0.7), 0 0 0 1px var(--border2);
  z-index:9000; transition:transform 0.4s cubic-bezier(0.16,1,0.3,1);
  pointer-events:none; white-space:nowrap;
}
.toast.show { transform:translateX(-50%) translateY(0); }
</style>
</head>
<body>

<!-- Custom cursor -->
<div id="cursor-dot"></div>
<div id="cursor-ring"></div>

<!-- Canvas layers -->
<canvas id="city-canvas"></canvas>
<canvas id="particle-canvas"></canvas>

<!-- Overlays -->
<div class="holo-overlay"></div>
<div class="grid-overlay"></div>

<!-- MAIN SCENE -->
<div class="scene">
  <div class="card-wrapper" id="cardWrapper">
    <div class="card-halo"></div>
    <div class="card-depth"></div>
    <div class="card-depth2"></div>

    <div class="chat-card">
      <!-- Scan beam -->
      <div class="scan-wrap">
        <div class="scan-beam"></div>
        <div class="scan-glow"></div>
      </div>

      <!-- Corner brackets -->
      <div class="cbr cbr-tl"><span></span><span></span></div>
      <div class="cbr cbr-tr"><span></span><span></span></div>
      <div class="cbr cbr-bl"><span></span><span></span></div>
      <div class="cbr cbr-br"><span></span><span></span></div>

      <!-- ── HEADER ── -->
      <div class="header">
        <div class="hdr-top">
          <div class="logo-rig">
            <div class="orb1"></div>
            <div class="orb2"></div>
            <div class="orb3"></div>
            <div class="logo-face">🏛️</div>
            <div class="logo-left"></div>
            <div class="logo-bot"></div>
            <div class="logo-pulse"></div>
          </div>

          <div class="brand">
            <div class="brand-name">Dream Home <b>Realty</b></div>
            <div class="brand-sub">Premium Properties &middot; Ahmedabad</div>
          </div>

          <div class="status-col">
            <div class="live-pill">
              <div class="ldot"></div>
              <span class="live-txt">LIVE</span>
            </div>
            <div class="model-tag">AI BOT</div>
          </div>
        </div>

        <div class="stats">
          <div class="stat"><div class="sn">500+</div><div class="sl">Properties</div></div>
          <div class="stat"><div class="sn">15+</div><div class="sl">Areas</div></div>
          <div class="stat"><div class="sn">24/7</div><div class="sl">Support</div></div>
          <div class="stat"><div class="sn">&#x20B9;25L</div><div class="sl">Starting</div></div>
        </div>
      </div>

      <div class="divider"></div>

      <!-- ── MESSAGES ── -->
      <div class="messages" id="msgs">
        <div class="mrow bot">
          <div class="mav mav-bot">🏛️</div>
          <div class="mbody">
            <div class="welcome">
              <div class="w-title">✨ Welcome to Dream Home Realty</div>
              <div class="w-items">
                <div class="w-item"><div class="w-icon">🏠</div>Buy, sell or rent residential &amp; commercial property</div>
                <div class="w-item"><div class="w-icon">📍</div>Premium locations across Ahmedabad</div>
                <div class="w-item"><div class="w-icon">🏦</div>Free home loan assistance — SBI, HDFC, ICICI</div>
                <div class="w-item"><div class="w-icon">📅</div>Free site visits arranged within 24 hours</div>
              </div>
            </div>
            <div class="mtime" id="wtime"></div>
          </div>
        </div>
      </div>

      <!-- Typing -->
      <div class="typing-row" id="typing">
        <div class="mav mav-bot">🏛️</div>
        <div class="typing-bub">
          <div class="td"></div><div class="td"></div><div class="td"></div>
        </div>
      </div>

      <!-- Quick chips -->
      <div class="qstrip" id="qstrip">
        <button class="qchip" onclick="qs('I want to buy a property')">🏠 Buy</button>
        <button class="qchip" onclick="qs('Show me rental options')">🔑 Rent</button>
        <button class="qchip" onclick="qs('What are your price ranges?')">💰 Prices</button>
        <button class="qchip" onclick="qs('Help with home loan')">🏦 Loan</button>
        <button class="qchip" onclick="qs('Book a free site visit')">📅 Visit</button>
      </div>

      <!-- Input -->
      <div class="input-zone">
        <div class="input-shell">
          <input class="ifield" id="inp" type="text"
            placeholder="Ask about properties in Ahmedabad…"
            autocomplete="off"
            onkeypress="if(event.key==='Enter')doSend()"/>
          <button class="send-btn" onclick="doSend()">
            <svg viewBox="0 0 24 24"><path d="M2 21L23 12 2 3v7l15 2-15 2v7z"/></svg>
          </button>
        </div>
        <div class="input-foot">
          <span class="ifoot-item">🔒 Private</span>
          <span class="ifoot-sep"></span>
          <span class="ifoot-item">⚡ Instant</span>
          <span class="ifoot-sep"></span>
          <span class="ifoot-item">🤖 AI Powered</span>
        </div>
      </div>
    </div><!-- /chat-card -->
  </div><!-- /card-wrapper -->
</div><!-- /scene -->

<!-- Toast -->
<div class="toast" id="toast"></div>

<script>
/* ═══════════════════════════════════════════
   CUSTOM CURSOR
═══════════════════════════════════════════ */
const dot  = document.getElementById('cursor-dot');
const ring = document.getElementById('cursor-ring');
let mx=0, my=0, rx=0, ry=0;
document.addEventListener('mousemove', e => { mx=e.clientX; my=e.clientY; });
function animCursor(){
  rx += (mx - rx) * 0.14;
  ry += (my - ry) * 0.14;
  dot.style.left  = mx + 'px'; dot.style.top  = my + 'px';
  ring.style.left = rx + 'px'; ring.style.top = ry + 'px';
  requestAnimationFrame(animCursor);
}
animCursor();

/* ═══════════════════════════════════════════
   CITY BACKGROUND
═══════════════════════════════════════════ */
const cityCanvas = document.getElementById('city-canvas');
const cc = cityCanvas.getContext('2d');
let CW, CH, stars=[], buildings=[];
let cityFrame = 0;

function resizeCity(){
  CW = cityCanvas.width  = window.innerWidth;
  CH = cityCanvas.height = window.innerHeight;
  buildCity();
}
function buildCity(){
  stars = Array.from({length:180},()=>({
    x: Math.random()*CW, y: Math.random()*CH*0.72,
    r: Math.random()*1.6+0.3,
    phase: Math.random()*Math.PI*2,
    speed: Math.random()*0.007+0.003,
    warm: Math.random()>0.35
  }));
  buildings=[]; let bx=0;
  while(bx < CW+100){
    const bw=25+Math.random()*75;
    const bh=60+Math.random()*260;
    const accented = Math.random()>0.72;
    const b={x:bx, w:bw, h:bh, accented, wins:[]};
    for(let wy=14; wy<bh-14; wy+=22)
      for(let wx=8; wx<bw-8; wx+=17)
        b.wins.push({
          x:wx, y:wy,
          lit: Math.random()>0.35,
          flicker: Math.random()>0.78,
          warm: Math.random()>0.4,
          size: 8+Math.random()*4
        });
    buildings.push(b);
    bx += bw + 3 + Math.random()*15;
  }
}

function drawCity(){
  cc.clearRect(0,0,CW,CH); cityFrame++;

  // Sky
  const sky = cc.createLinearGradient(0,0,0,CH);
  sky.addColorStop(0,'#020408');
  sky.addColorStop(0.55,'#030610');
  sky.addColorStop(1,'#07091a');
  cc.fillStyle=sky; cc.fillRect(0,0,CW,CH);

  // Nebula blobs
  [[CW*0.2,CH*0.25,180,'212,168,67',0.04],[CW*0.8,CH*0.1,220,'61,214,245',0.03],[CW*0.55,CH*0.4,150,'180,120,40',0.03]].forEach(([x,y,r,c,a])=>{
    const g=cc.createRadialGradient(x,y,0,x,y,r);
    g.addColorStop(0,`rgba(${c},${a})`);
    g.addColorStop(1,'transparent');
    cc.fillStyle=g; cc.fillRect(0,0,CW,CH);
  });

  // Moon
  const mx=CW*0.78, my=CH*0.14;
  // Glow corona
  for(let i=3;i>0;i--){
    const mg=cc.createRadialGradient(mx,my,22,mx,my,22+i*50);
    mg.addColorStop(0,`rgba(245,200,66,${0.04*i})`);
    mg.addColorStop(1,'transparent');
    cc.fillStyle=mg; cc.fillRect(0,0,CW,CH);
  }
  cc.beginPath(); cc.arc(mx,my,26,0,Math.PI*2);
  const moonG=cc.createRadialGradient(mx-6,my-6,0,mx,my,26);
  moonG.addColorStop(0,'rgba(255,250,200,0.95)');
  moonG.addColorStop(0.55,'rgba(220,175,60,0.85)');
  moonG.addColorStop(1,'rgba(180,125,30,0.25)');
  cc.fillStyle=moonG; cc.fill();
  // Moon craters
  [[mx-8,my+6,4,'rgba(180,140,40,0.25)'],[mx+7,my-8,3,'rgba(200,160,50,0.2)'],[mx-2,my-12,2,'rgba(160,120,30,0.22)']].forEach(([cx,cy,cr,col])=>{
    cc.beginPath(); cc.arc(cx,cy,cr,0,Math.PI*2); cc.fillStyle=col; cc.fill();
  });

  // Stars
  stars.forEach(s=>{
    s.phase += s.speed;
    const a=0.15+Math.abs(Math.sin(s.phase))*0.8;
    const c=s.warm?'255,240,195':'200,220,255';
    cc.beginPath(); cc.arc(s.x,s.y,s.r,0,Math.PI*2);
    cc.fillStyle=`rgba(${c},${a})`; cc.fill();
    if(s.r>1.3 && Math.sin(s.phase*0.4)>0.7){
      cc.strokeStyle=`rgba(${c},${a*0.4})`;
      cc.lineWidth=0.4;
      cc.beginPath(); cc.moveTo(s.x-5,s.y); cc.lineTo(s.x+5,s.y); cc.stroke();
      cc.beginPath(); cc.moveTo(s.x,s.y-5); cc.lineTo(s.x,s.y+5); cc.stroke();
    }
  });

  const gY = CH*0.73;
  // Fog layer
  const fog=cc.createLinearGradient(0,gY-100,0,gY);
  fog.addColorStop(0,'transparent');
  fog.addColorStop(1,'rgba(245,200,66,0.05)');
  cc.fillStyle=fog; cc.fillRect(0,gY-100,CW,100);

  // Buildings
  buildings.forEach(b=>{
    const bx2=b.x, by2=gY-b.h;

    // Shadow
    const sh=cc.createLinearGradient(bx2,by2,bx2,gY);
    sh.addColorStop(0,'rgba(0,0,0,0)');
    sh.addColorStop(1,'rgba(0,0,0,0.6)');
    cc.fillStyle='rgba(0,0,0,0.3)';
    cc.fillRect(bx2-3,by2+4,b.w+3,b.h);

    // Main face
    const bf=cc.createLinearGradient(bx2,by2,bx2+b.w,by2+b.h);
    bf.addColorStop(0,'rgba(16,20,34,0.97)');
    bf.addColorStop(0.6,'rgba(10,13,22,0.99)');
    bf.addColorStop(1,'rgba(7,9,16,0.99)');
    cc.fillStyle=bf; cc.fillRect(bx2,by2,b.w,b.h);

    // Left face 3D
    cc.beginPath();
    cc.moveTo(bx2,by2); cc.lineTo(bx2-8,by2+12); cc.lineTo(bx2-8,gY+12); cc.lineTo(bx2,gY);
    cc.fillStyle='rgba(4,5,10,0.85)'; cc.fill();

    // Edge highlight
    if(b.accented){
      cc.strokeStyle=`rgba(245,200,66,${0.08+0.04*Math.sin(cityFrame*0.02+b.x)})`;
    } else {
      cc.strokeStyle='rgba(245,200,66,0.05)';
    }
    cc.lineWidth=0.8; cc.strokeRect(bx2,by2,b.w,b.h);

    // Roof accent line for some buildings
    if(b.accented){
      const rl=cc.createLinearGradient(bx2,by2,bx2+b.w,by2);
      rl.addColorStop(0,'transparent');
      rl.addColorStop(0.5,`rgba(245,200,66,${0.3+0.2*Math.sin(cityFrame*0.03)})`);
      rl.addColorStop(1,'transparent');
      cc.strokeStyle=rl; cc.lineWidth=1.5;
      cc.beginPath(); cc.moveTo(bx2,by2); cc.lineTo(bx2+b.w,by2); cc.stroke();
    }

    // Windows
    b.wins.forEach(win=>{
      if(win.flicker && cityFrame%(180+Math.floor(b.x)%80)===0) win.lit=!win.lit;
      if(!win.lit) return;
      const wx=bx2+win.x, wy=by2+win.y;
      const wg=cc.createRadialGradient(wx+win.size/2,wy+win.size/2*0.8,0,wx+win.size/2,wy+win.size/2*0.8,win.size);
      if(win.warm){
        wg.addColorStop(0,'rgba(255,215,90,0.95)');
        wg.addColorStop(0.5,'rgba(212,165,50,0.5)');
      } else {
        wg.addColorStop(0,'rgba(160,220,255,0.9)');
        wg.addColorStop(0.5,'rgba(80,180,240,0.3)');
      }
      wg.addColorStop(1,'transparent');
      cc.fillStyle=wg; cc.fillRect(wx,wy,win.size,win.size*1.2);
    });

    // Rooftop blinker
    const blink=0.35+0.55*Math.sin(cityFrame*0.035+b.x*0.018);
    cc.beginPath(); cc.arc(bx2+b.w/2, by2+3, 2.5, 0, Math.PI*2);
    cc.fillStyle=`rgba(255,70,70,${blink})`;
    cc.shadowBlur=10; cc.shadowColor=`rgba(255,70,70,0.6)`;
    cc.fill(); cc.shadowBlur=0;
  });

  // Ground
  cc.fillStyle='#040610'; cc.fillRect(0,gY,CW,CH-gY);
  // Ground glow
  const gg=cc.createLinearGradient(0,gY,0,gY+60);
  gg.addColorStop(0,'rgba(245,200,66,0.09)');
  gg.addColorStop(0.5,'rgba(245,200,66,0.03)');
  gg.addColorStop(1,'transparent');
  cc.fillStyle=gg; cc.fillRect(0,gY,CW,60);
  // Horizon line
  const hl=cc.createLinearGradient(0,gY,CW,gY);
  hl.addColorStop(0,'transparent');
  hl.addColorStop(0.3,'rgba(245,200,66,0.12)');
  hl.addColorStop(0.5,'rgba(61,214,245,0.06)');
  hl.addColorStop(0.7,'rgba(245,200,66,0.12)');
  hl.addColorStop(1,'transparent');
  cc.fillStyle=hl; cc.fillRect(0,gY-1,CW,2);
  // Road lines
  for(let i=0;i<CW;i+=90){
    const rl=cc.createLinearGradient(i,gY,i,CH);
    rl.addColorStop(0,'rgba(245,200,66,0.06)');
    rl.addColorStop(1,'transparent');
    cc.fillStyle=rl; cc.fillRect(i,gY,1,CH-gY);
  }

  requestAnimationFrame(drawCity);
}
window.addEventListener('resize', resizeCity);
resizeCity(); drawCity();

/* ═══════════════════════════════════════════
   PARTICLE CANVAS
═══════════════════════════════════════════ */
const pCanvas = document.getElementById('particle-canvas');
const pc = pCanvas.getContext('2d');
let PW, PH;
const particles = [];

function resizePCanvas(){
  PW = pCanvas.width  = window.innerWidth;
  PH = pCanvas.height = window.innerHeight;
}
window.addEventListener('resize', resizePCanvas);
resizePCanvas();

for(let i=0;i<60;i++){
  particles.push({
    x: Math.random()*window.innerWidth,
    y: Math.random()*window.innerHeight,
    vx: (Math.random()-0.5)*0.35,
    vy: -(Math.random()*0.8+0.3),
    r: Math.random()*2+0.5,
    alpha: Math.random(),
    life: Math.random(),
    maxLife: 0.6+Math.random()*0.4,
    color: Math.random()>0.25?'245,200,66':'61,214,245',
    flare: Math.random()>0.8
  });
}

function drawParticles(){
  pc.clearRect(0,0,PW,PH);
  particles.forEach(p=>{
    p.life += 0.004;
    if(p.life > p.maxLife){
      p.life=0; p.x=Math.random()*PW;
      p.y=PH+10; p.alpha=0;
    }
    p.x += p.vx + Math.sin(p.life*4)*0.3;
    p.y += p.vy;
    const t=p.life/p.maxLife;
    p.alpha = t<0.2 ? t/0.2 : t>0.8 ? (1-t)/0.2 : 1;

    if(p.flare){
      const pg=pc.createRadialGradient(p.x,p.y,0,p.x,p.y,p.r*4);
      pg.addColorStop(0,`rgba(${p.color},${p.alpha*0.9})`);
      pg.addColorStop(1,`rgba(${p.color},0)`);
      pc.fillStyle=pg;
      pc.beginPath(); pc.arc(p.x,p.y,p.r*4,0,Math.PI*2); pc.fill();
    }
    pc.beginPath(); pc.arc(p.x,p.y,p.r,0,Math.PI*2);
    pc.fillStyle=`rgba(${p.color},${p.alpha})`;
    pc.shadowBlur=6; pc.shadowColor=`rgba(${p.color},0.5)`;
    pc.fill(); pc.shadowBlur=0;
  });
  requestAnimationFrame(drawParticles);
}
drawParticles();

/* ═══════════════════════════════════════════
   3D TILT with smooth lerp
═══════════════════════════════════════════ */
const wrap = document.getElementById('cardWrapper');
let tX=0,tY=0,cX=0,cY=0;
document.addEventListener('mousemove', e=>{
  tX = (e.clientX - window.innerWidth/2)  / (window.innerWidth/2)  * 6;
  tY = (e.clientY - window.innerHeight/2) / (window.innerHeight/2) * -4;
});
document.addEventListener('mouseleave', ()=>{ tX=0; tY=0; });
function tiltLoop(){
  cX += (tX-cX)*0.06;
  cY += (tY-cY)*0.06;
  wrap.style.transform = `perspective(1400px) rotateY(${cX}deg) rotateX(${cY}deg)`;
  requestAnimationFrame(tiltLoop);
}
tiltLoop();

/* ═══════════════════════════════════════════
   CHAT
═══════════════════════════════════════════ */
let history = [];
document.getElementById('wtime').textContent = getTime();

function getTime(){
  return new Date().toLocaleTimeString('en-IN',{hour:'2-digit',minute:'2-digit'});
}

async function doSend(){
  const inp = document.getElementById('inp');
  const msg = inp.value.trim();
  if(!msg) return;
  document.getElementById('qstrip').style.display='none';
  addMsg(msg,'usr'); inp.value=''; setTyping(true);
  try{
    const res = await fetch('/chat',{
      method:'POST',
      headers:{'Content-Type':'application/json'},
      body:JSON.stringify({message:msg, history})
    });
    const data = await res.json();
    setTyping(false);
    addMsg(data.reply,'bot');
    history.push({role:'user',content:msg},{role:'assistant',content:data.reply});
  } catch(e){
    setTyping(false);
    addMsg('Connection issue — please try again in a moment.','bot');
  }
}

function qs(m){ document.getElementById('inp').value=m; doSend(); }

function addMsg(text, type){
  const msgs = document.getElementById('msgs');
  const row  = document.createElement('div');
  row.className = `mrow ${type}`;

  const av = document.createElement('div');
  av.className = `mav ${type==='bot'?'mav-bot':'mav-usr'}`;
  av.textContent = type==='bot'?'🏛️':'👤';

  const body = document.createElement('div'); body.className='mbody';
  if(type==='usr') body.style.alignItems='flex-end';

  const bub = document.createElement('div');
  bub.className = type==='bot'?'bbot':'busr';
  bub.textContent = text;

  const t = document.createElement('div'); t.className='mtime'; t.textContent=getTime();

  body.appendChild(bub); body.appendChild(t);
  if(type==='bot'){ row.appendChild(av); row.appendChild(body); }
  else            { row.appendChild(body); row.appendChild(av); }
  msgs.appendChild(row);
  row.scrollIntoView({behavior:'smooth',block:'end'});
}

function setTyping(on){
  const t=document.getElementById('typing');
  t.classList.toggle('on',on);
  if(on) t.scrollIntoView({behavior:'smooth',block:'end'});
}

/* ═══════════════════════════════════════════
   TOAST HELPER
═══════════════════════════════════════════ */
function showToast(msg){
  const t=document.getElementById('toast');
  t.textContent=msg; t.classList.add('show');
  setTimeout(()=>t.classList.remove('show'),3000);
}

// Greeting toast
setTimeout(()=>showToast('👋 Hello! Ask me anything about Ahmedabad properties.'),1600);
</script>
</body>
</html>
