<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Dream Home Realty</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=Outfit:wght@300;400;500;600&display=swap" rel="stylesheet">
<style>
:root {
  --gold: #d4a843;
  --gold2: #f0c96a;
  --gold3: rgba(212,168,67,0.12);
  --dark: #080a0f;
  --dark2: #0d0f18;
  --dark3: #12151f;
  --dark4: #181b27;
  --glow: rgba(212,168,67,0.4);
  --text: #e8e4dc;
  --muted: #5a5848;
}
* { margin:0; padding:0; box-sizing:border-box; }
body {
  font-family: 'Outfit', sans-serif;
  background: var(--dark);
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  perspective: 1000px;
}
#bg-canvas { position: fixed; inset: 0; z-index: 0; }
.particles { position: fixed; inset: 0; pointer-events: none; z-index: 1; overflow: hidden; }
.particle {
  position: absolute;
  border-radius: 50%;
  background: radial-gradient(circle, var(--gold2), transparent);
  animation: floatParticle linear infinite;
  opacity: 0;
}
@keyframes floatParticle {
  0% { transform: translateY(100vh) translateX(0) scale(0); opacity:0; }
  10% { opacity: 0.6; }
  90% { opacity: 0.3; }
  100% { transform: translateY(-100px) translateX(var(--drift)) scale(1.5); opacity:0; }
}
.wrapper {
  position: relative; z-index: 10; width: 100%; max-width: 500px;
  padding: 16px; height: 100vh; display: flex;
  flex-direction: column; justify-content: center; align-items: center;
}
.card-3d {
  width: 100%; transform-style: preserve-3d;
  animation: cardEntrance 1s cubic-bezier(0.16,1,0.3,1) forwards;
  transition: transform 0.15s ease;
}
@keyframes cardEntrance {
  from { opacity:0; transform: perspective(800px) rotateX(20deg) translateY(60px) scale(0.9); }
  to { opacity:1; transform: perspective(800px) rotateX(0deg) translateY(0) scale(1); }
}
.chat {
  background: linear-gradient(160deg, #0f1220 0%, #0a0c14 50%, #0d0f1a 100%);
  border-radius: 30px; overflow: hidden; display: flex; flex-direction: column;
  height: min(720px, 88vh); position: relative;
  box-shadow: 0 0 0 1px rgba(212,168,67,0.15), 0 0 60px rgba(212,168,67,0.08),
    0 60px 120px rgba(0,0,0,0.8), inset 0 1px 0 rgba(255,255,255,0.05),
    inset 0 -1px 0 rgba(212,168,67,0.08);
}
.chat::before {
  content: ''; position: absolute; top: 0; left: -100%; right: 0; height: 2px;
  background: linear-gradient(90deg, transparent 0%, var(--gold2) 40%, var(--gold) 60%, transparent 100%);
  animation: scanLine 3s ease-in-out infinite; z-index: 10;
}
@keyframes scanLine { 0% { left: -100%; } 100% { left: 100%; } }
.chat::after {
  content: ''; position: absolute; inset: 0; border-radius: 30px;
  background: radial-gradient(ellipse 100% 40% at 50% 0%, rgba(212,168,67,0.06) 0%, transparent 60%),
    radial-gradient(ellipse 60% 30% at 50% 100%, rgba(212,168,67,0.03) 0%, transparent 60%);
  pointer-events: none; z-index: 1;
}
.corner { position: absolute; width: 20px; height: 20px; z-index: 5; }
.corner-tl { top: 12px; left: 12px; border-top: 2px solid var(--gold); border-left: 2px solid var(--gold); border-radius: 4px 0 0 0; }
.corner-tr { top: 12px; right: 12px; border-top: 2px solid var(--gold); border-right: 2px solid var(--gold); border-radius: 0 4px 0 0; }
.corner-bl { bottom: 12px; left: 12px; border-bottom: 2px solid var(--gold); border-left: 2px solid var(--gold); border-radius: 0 0 0 4px; }
.corner-br { bottom: 12px; right: 12px; border-bottom: 2px solid var(--gold); border-right: 2px solid var(--gold); border-radius: 0 0 4px 0; }
.header { padding: 22px 24px 18px; position: relative; z-index: 2; flex-shrink: 0; }
.header-main { display: flex; align-items: center; gap: 14px; }
.logo-3d { position: relative; width: 54px; height: 54px; flex-shrink: 0; }
.logo-face {
  width: 54px; height: 54px; border-radius: 16px;
  background: linear-gradient(135deg, #2a2010 0%, #1a1508 100%);
  border: 1px solid rgba(212,168,67,0.4);
  display: flex; align-items: center; justify-content: center; font-size: 24px;
  box-shadow: 0 8px 32px rgba(212,168,67,0.2), 0 2px 8px rgba(0,0,0,0.6),
    inset 0 1px 0 rgba(255,255,255,0.1), inset 0 -1px 0 rgba(0,0,0,0.3);
  animation: logoFloat 3s ease-in-out infinite; transform-style: preserve-3d;
}
@keyframes logoFloat {
  0%,100% { transform: translateY(0) rotateY(0deg); }
  25% { transform: translateY(-3px) rotateY(5deg); }
  75% { transform: translateY(-2px) rotateY(-3deg); }
}
.logo-ring {
  position: absolute; inset: -5px; border-radius: 20px;
  border: 1px solid rgba(212,168,67,0.25);
  animation: ringRotate 4s linear infinite;
}
@keyframes ringRotate { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
.agency-name {
  font-family: 'Cormorant Garamond', serif; font-size: 1.2rem; font-weight: 700;
  color: #fff; letter-spacing: 0.04em; text-shadow: 0 0 20px rgba(212,168,67,0.3);
}
.agency-name span { color: var(--gold2); }
.agency-tagline { font-size: 0.67rem; color: var(--muted); letter-spacing: 0.14em; text-transform: uppercase; margin-top: 2px; }
.live-badge { margin-left: auto; display: flex; flex-direction: column; align-items: flex-end; gap: 4px; }
.live-pill { display: flex; align-items: center; gap: 6px; background: rgba(0,230,100,0.08); border: 1px solid rgba(0,230,100,0.25); border-radius: 100px; padding: 4px 10px; }
.live-dot { width: 6px; height: 6px; border-radius: 50%; background: #00e664; box-shadow: 0 0 10px #00e664; animation: livePulse 1.5s ease-in-out infinite; }
@keyframes livePulse { 0%,100%{transform:scale(1);opacity:1} 50%{transform:scale(1.4);opacity:0.6} }
.live-text { font-size: 0.68rem; color: #00e664; font-weight: 600; letter-spacing: 0.08em; }
.stats-3d { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-top: 16px; }
.stat-card {
  background: linear-gradient(135deg, rgba(212,168,67,0.08) 0%, rgba(212,168,67,0.03) 100%);
  border: 1px solid rgba(212,168,67,0.12); border-radius: 12px; padding: 9px 6px;
  text-align: center; position: relative; overflow: hidden; transition: all 0.3s; cursor: default;
}
.stat-card::before {
  content: ''; position: absolute; top: 0; left: -100%; width: 100%; height: 100%;
  background: linear-gradient(90deg, transparent, rgba(212,168,67,0.08), transparent); transition: left 0.4s;
}
.stat-card:hover::before { left: 100%; }
.stat-card:hover { border-color: rgba(212,168,67,0.3); transform: translateY(-2px); box-shadow: 0 8px 20px rgba(212,168,67,0.1); }
.stat-num { font-family: 'Cormorant Garamond', serif; font-size: 1rem; font-weight: 700; color: var(--gold2); }
.stat-lbl { font-size: 0.58rem; color: var(--muted); text-transform: uppercase; letter-spacing: 0.06em; margin-top: 1px; }
.divider { height: 1px; background: linear-gradient(90deg, transparent, rgba(212,168,67,0.15), transparent); margin: 0 20px; flex-shrink: 0; }
.messages { flex: 1; overflow-y: auto; padding: 18px 18px 10px; display: flex; flex-direction: column; gap: 16px; position: relative; z-index: 2; }
.messages::-webkit-scrollbar { width: 2px; }
.messages::-webkit-scrollbar-thumb { background: rgba(212,168,67,0.2); border-radius: 2px; }
.msg-row { display: flex; gap: 10px; animation: msgPop 0.4s cubic-bezier(0.16,1,0.3,1); }
.msg-row.user { flex-direction: row-reverse; }
@keyframes msgPop { from { opacity:0; transform: scale(0.92) translateY(10px); } to { opacity:1; transform: scale(1) translateY(0); } }
.msg-av { width: 34px; height: 34px; border-radius: 11px; flex-shrink: 0; align-self: flex-end; display: flex; align-items: center; justify-content: center; font-size: 16px; }
.bot-av { background: linear-gradient(135deg, #2a2010, #1a1508); border: 1px solid rgba(212,168,67,0.3); box-shadow: 0 4px 12px rgba(212,168,67,0.15), inset 0 1px 0 rgba(255,255,255,0.08); }
.user-av { background: linear-gradient(135deg, #0f2010, #081208); border: 1px solid rgba(80,200,100,0.2); }
.msg-body { max-width: 80%; display: flex; flex-direction: column; gap: 4px; }
.msg-row.user .msg-body { align-items: flex-end; }
.bubble { padding: 12px 16px; border-radius: 18px; font-size: 0.875rem; line-height: 1.65; position: relative; }
.bot-bubble {
  background: linear-gradient(135deg, #181b27 0%, #12151e 100%);
  border: 1px solid rgba(212,168,67,0.14); color: var(--text);
  border-bottom-left-radius: 4px;
  box-shadow: 0 4px 20px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.04), 0 0 0 1px rgba(212,168,67,0.04);
}
.user-bubble {
  background: linear-gradient(135deg, #d4a843 0%, #b8882a 50%, #c9982e 100%);
  color: #1a0f00; border-bottom-right-radius: 4px; font-weight: 500;
  box-shadow: 0 4px 20px rgba(212,168,67,0.3), 0 1px 0 rgba(255,255,255,0.2) inset, 0 -1px 0 rgba(0,0,0,0.2) inset;
}
.msg-time { font-size: 0.6rem; color: var(--muted); padding: 0 4px; letter-spacing: 0.04em; }
.welcome-msg {
  background: linear-gradient(135deg, rgba(212,168,67,0.07), rgba(212,168,67,0.02));
  border: 1px solid rgba(212,168,67,0.18); border-radius: 18px; border-bottom-left-radius: 4px;
  padding: 18px; box-shadow: 0 8px 32px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.04);
}
.welcome-heading { font-family: 'Cormorant Garamond', serif; font-size: 1.05rem; font-weight: 700; color: var(--gold2); margin-bottom: 12px; }
.welcome-items { display: flex; flex-direction: column; gap: 7px; }
.welcome-item { display: flex; align-items: center; gap: 10px; font-size: 0.8rem; color: #9a9278; }
.wi-icon { width: 26px; height: 26px; border-radius: 8px; background: rgba(212,168,67,0.1); border: 1px solid rgba(212,168,67,0.18); display: flex; align-items: center; justify-content: center; font-size: 12px; flex-shrink: 0; }
.typing-row { display: none; gap: 10px; animation: msgPop 0.3s ease; }
.typing-row.show { display: flex; }
.typing-bub {
  background: linear-gradient(135deg, #181b27, #12151e); border: 1px solid rgba(212,168,67,0.14);
  border-radius: 18px; border-bottom-left-radius: 4px; padding: 14px 18px; display: flex; gap: 5px; align-items: center;
}
.td { width: 7px; height: 7px; border-radius: 50%; background: var(--gold); animation: tdBounce 1.2s ease-in-out infinite; opacity: 0.5; }
.td:nth-child(2){animation-delay:0.2s} .td:nth-child(3){animation-delay:0.4s}
@keyframes tdBounce { 0%,100%{transform:translateY(0) scale(1);opacity:0.4} 50%{transform:translateY(-6px) scale(1.1);opacity:1} }
.quick-area { padding: 8px 18px 12px; display: flex; gap: 7px; flex-wrap: wrap; flex-shrink: 0; position: relative; z-index: 2; }
.qbtn {
  background: linear-gradient(135deg, rgba(212,168,67,0.08), rgba(212,168,67,0.03));
  border: 1px solid rgba(212,168,67,0.2); color: var(--gold2); padding: 7px 13px;
  border-radius: 100px; font-size: 0.74rem; font-family: 'Outfit', sans-serif;
  cursor: pointer; transition: all 0.25s; white-space: nowrap; font-weight: 500; letter-spacing: 0.02em; position: relative; overflow: hidden;
}
.qbtn:hover { border-color: var(--gold); color: var(--gold2); transform: translateY(-2px) scale(1.02); box-shadow: 0 6px 20px rgba(212,168,67,0.18), 0 0 0 1px rgba(212,168,67,0.1); background: rgba(212,168,67,0.12); }
.qbtn:active { transform: scale(0.97); }
.input-zone { padding: 12px 16px 20px; flex-shrink: 0; position: relative; z-index: 2; }
.input-3d {
  display: flex; align-items: center; gap: 10px;
  background: linear-gradient(135deg, #141720, #0f121a);
  border: 1px solid rgba(212,168,67,0.18); border-radius: 18px; padding: 8px 8px 8px 18px;
  transition: all 0.3s;
  box-shadow: 0 4px 20px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.03);
}
.input-3d:focus-within {
  border-color: rgba(212,168,67,0.45);
  box-shadow: 0 4px 20px rgba(0,0,0,0.4), 0 0 0 3px rgba(212,168,67,0.07), 0 0 30px rgba(212,168,67,0.06), inset 0 1px 0 rgba(255,255,255,0.04);
}
.cinput { flex: 1; background: transparent; border: none; outline: none; font-size: 0.88rem; font-family: 'Outfit', sans-serif; color: var(--text); padding: 8px 0; letter-spacing: 0.01em; }
.cinput::placeholder { color: #3a3828; }
.send-3d {
  width: 44px; height: 44px; border-radius: 14px;
  background: linear-gradient(135deg, #d4a843 0%, #c09030 40%, #a87820 100%);
  border: none; cursor: pointer; display: flex; align-items: center; justify-content: center;
  transition: all 0.2s; flex-shrink: 0; position: relative;
  box-shadow: 0 6px 20px rgba(212,168,67,0.35), 0 1px 0 rgba(255,255,255,0.25) inset, 0 -2px 0 rgba(0,0,0,0.3) inset;
}
.send-3d::before {
  content: ''; position: absolute; top: 1px; left: 4px; right: 4px; height: 40%;
  background: linear-gradient(rgba(255,255,255,0.2), transparent); border-radius: 12px 12px 0 0; pointer-events: none;
}
.send-3d:hover { transform: translateY(-2px) scale(1.05); box-shadow: 0 10px 28px rgba(212,168,67,0.45), 0 1px 0 rgba(255,255,255,0.25) inset, 0 -2px 0 rgba(0,0,0,0.3) inset; }
.send-3d:active { transform: translateY(1px) scale(0.97); }
.send-3d svg { width:18px; height:18px; fill:#1a0e00; }
.input-foot { display: flex; justify-content: center; margin-top: 8px; gap: 16px; }
.foot-item { font-size: 0.62rem; color: #2a2820; display: flex; align-items: center; gap: 4px; letter-spacing: 0.04em; }
.foot-dot { width:3px;height:3px;border-radius:50%;background:#2a2820; }
</style>
</head>
<body>
<canvas id="bg-canvas"></canvas>
<div class="particles" id="particles"></div>

<div class="wrapper">
  <div class="card-3d" id="card3d">
    <div class="chat">
      <div class="corner corner-tl"></div>
      <div class="corner corner-tr"></div>
      <div class="corner corner-bl"></div>
      <div class="corner corner-br"></div>

      <div class="header">
        <div class="header-main">
          <div class="logo-3d">
            <div class="logo-face">🏛️</div>
            <div class="logo-ring"></div>
          </div>
          <div>
            <div class="agency-name">Dream Home <span>Realty</span></div>
            <div class="agency-tagline">Premium Properties · Ahmedabad</div>
          </div>
          <div class="live-badge">
            <div class="live-pill">
              <div class="live-dot"></div>
              <span class="live-text">LIVE AI</span>
            </div>
          </div>
        </div>
        <div class="stats-3d">
          <div class="stat-card"><div class="stat-num">500+</div><div class="stat-lbl">Properties</div></div>
          <div class="stat-card"><div class="stat-num">15+</div><div class="stat-lbl">Areas</div></div>
          <div class="stat-card"><div class="stat-num">24/7</div><div class="stat-lbl">Support</div></div>
          <div class="stat-card"><div class="stat-num">₹25L</div><div class="stat-lbl">Starting</div></div>
        </div>
      </div>

      <div class="divider"></div>

      <div class="messages" id="messages">
        <div class="msg-row bot">
          <div class="msg-av bot-av">🏛️</div>
          <div class="msg-body">
            <div class="welcome-msg">
              <div class="welcome-heading">✨ Welcome to Dream Home Realty</div>
              <div class="welcome-items">
                <div class="welcome-item"><div class="wi-icon">🏠</div>Buy, sell or rent residential & commercial property</div>
                <div class="welcome-item"><div class="wi-icon">📍</div>Premium locations across Ahmedabad</div>
                <div class="welcome-item"><div class="wi-icon">🏦</div>Free home loan assistance — SBI, HDFC, ICICI</div>
                <div class="welcome-item"><div class="wi-icon">📅</div>Free site visits arranged within 24 hours</div>
              </div>
            </div>
            <div class="msg-time" id="wt"></div>
          </div>
        </div>
      </div>

      <div class="typing-row" id="typing">
        <div class="msg-av bot-av">🏛️</div>
        <div class="typing-bub">
          <div class="td"></div><div class="td"></div><div class="td"></div>
        </div>
      </div>

      <div class="quick-area" id="qa">
        <button class="qbtn" onclick="q('I want to buy a property')">🏠 Buy</button>
        <button class="qbtn" onclick="q('Show me rental options')">🔑 Rent</button>
        <button class="qbtn" onclick="q('What are your price ranges?')">💰 Prices</button>
        <button class="qbtn" onclick="q('Help with home loan')">🏦 Loan</button>
        <button class="qbtn" onclick="q('Book a free site visit')">📅 Visit</button>
      </div>

      <div class="input-zone">
        <div class="input-3d">
          <input class="cinput" id="inp" type="text" placeholder="Ask about properties in Ahmedabad…" autocomplete="off" onkeypress="if(event.key==='Enter')send()"/>
          <button class="send-3d" onclick="send()">
            <svg viewBox="0 0 24 24"><path d="M2 21L23 12 2 3v7l15 2-15 2v7z"/></svg>
          </button>
        </div>
        <div class="input-foot">
          <span class="foot-item">🔒 Private</span>
          <span class="foot-dot"></span>
          <span class="foot-item">⚡ Instant</span>
          <span class="foot-dot"></span>
          <span class="foot-item">🤖 AI Powered</span>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
// 3D City Background
const canvas = document.getElementById('bg-canvas');
const ctx = canvas.getContext('2d');
let W, H, stars = [], buildings = [];

function resize() {
  W = canvas.width = window.innerWidth;
  H = canvas.height = window.innerHeight;
  initScene();
}

function initScene() {
  stars = Array.from({length: 120}, () => ({
    x: Math.random() * W, y: Math.random() * H * 0.7,
    r: Math.random() * 1.2, a: Math.random(), speed: Math.random() * 0.005 + 0.002
  }));
  buildings = [];
  let x = 0;
  while (x < W + 60) {
    const w = 30 + Math.random() * 60;
    const h = 60 + Math.random() * 200;
    const b = {x, w, h, windows: []};
    for (let wy = 10; wy < h - 10; wy += 18)
      for (let wx = 6; wx < w - 6; wx += 14)
        b.windows.push({x: wx, y: wy, lit: Math.random() > 0.35, flicker: Math.random() > 0.8});
    buildings.push(b);
    x += w + 2 + Math.random() * 8;
  }
}

let frame = 0;
function drawScene() {
  ctx.clearRect(0, 0, W, H); frame++;
  const sky = ctx.createLinearGradient(0, 0, 0, H);
  sky.addColorStop(0, '#03050a'); sky.addColorStop(0.6, '#060810'); sky.addColorStop(1, '#0a0c14');
  ctx.fillStyle = sky; ctx.fillRect(0, 0, W, H);

  const moonX = W * 0.75, moonY = H * 0.15;
  const moonGlow = ctx.createRadialGradient(moonX, moonY, 0, moonX, moonY, 120);
  moonGlow.addColorStop(0, 'rgba(212,168,67,0.08)'); moonGlow.addColorStop(1, 'transparent');
  ctx.fillStyle = moonGlow; ctx.fillRect(0, 0, W, H);

  ctx.beginPath(); ctx.arc(moonX, moonY, 22, 0, Math.PI * 2);
  const mg = ctx.createRadialGradient(moonX-4, moonY-4, 0, moonX, moonY, 22);
  mg.addColorStop(0, 'rgba(255,240,180,0.9)'); mg.addColorStop(0.6, 'rgba(212,168,67,0.7)'); mg.addColorStop(1, 'rgba(180,130,40,0.3)');
  ctx.fillStyle = mg; ctx.fill();

  stars.forEach(s => {
    s.a += s.speed;
    ctx.beginPath(); ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(255,240,200,${0.3 + Math.abs(Math.sin(s.a)) * 0.6})`; ctx.fill();
  });

  const groundY = H * 0.72;
  buildings.forEach(b => {
    const bx = b.x, by = groundY - b.h;
    const bg = ctx.createLinearGradient(bx, by, bx + b.w, by + b.h);
    bg.addColorStop(0, 'rgba(18,20,30,0.95)'); bg.addColorStop(1, 'rgba(10,12,18,0.98)');
    ctx.fillStyle = bg; ctx.fillRect(bx, by, b.w, b.h);
    ctx.strokeStyle = 'rgba(212,168,67,0.06)'; ctx.lineWidth = 0.5; ctx.strokeRect(bx, by, b.w, b.h);

    b.windows.forEach(win => {
      if (win.flicker && frame % 180 === 0) win.lit = !win.lit;
      if (!win.lit) return;
      const wx = bx + win.x, wy = by + win.y;
      const wg = ctx.createRadialGradient(wx+4, wy+5, 0, wx+4, wy+5, 8);
      wg.addColorStop(0, 'rgba(255,220,120,0.9)'); wg.addColorStop(1, 'rgba(212,168,67,0.1)');
      ctx.fillStyle = wg; ctx.fillRect(wx, wy, 8, 10);
    });

    ctx.beginPath(); ctx.arc(bx + b.w/2, by + 2, 2, 0, Math.PI * 2);
    ctx.fillStyle = `rgba(255,100,100,${0.5 + 0.4 * Math.sin(frame * 0.03)})`; ctx.fill();
  });

  ctx.fillStyle = '#070810'; ctx.fillRect(0, groundY, W, H - groundY);
  const sg = ctx.createLinearGradient(0, groundY, 0, groundY + 30);
  sg.addColorStop(0, 'rgba(212,168,67,0.06)'); sg.addColorStop(1, 'transparent');
  ctx.fillStyle = sg; ctx.fillRect(0, groundY, W, 30);
  requestAnimationFrame(drawScene);
}

window.addEventListener('resize', resize);
resize(); drawScene();

// Particles
const pc = document.getElementById('particles');
for (let i = 0; i < 20; i++) {
  const p = document.createElement('div');
  p.className = 'particle';
  const size = 2 + Math.random() * 4;
  p.style.cssText = `width:${size}px;height:${size}px;left:${Math.random()*100}%;animation-duration:${8+Math.random()*12}s;animation-delay:${Math.random()*10}s;--drift:${(Math.random()-0.5)*100}px;`;
  pc.appendChild(p);
}

// 3D tilt
const card = document.getElementById('card3d');
document.addEventListener('mousemove', e => {
  const dx = (e.clientX - window.innerWidth/2) / (window.innerWidth/2);
  const dy = (e.clientY - window.innerHeight/2) / (window.innerHeight/2);
  card.style.transform = `perspective(1200px) rotateY(${dx*4}deg) rotateX(${-dy*3}deg)`;
});
document.addEventListener('mouseleave', () => {
  card.style.transform = 'perspective(1200px) rotateY(0deg) rotateX(0deg)';
});

// Chat
let history = [];
document.getElementById('wt').textContent = getTime();
function getTime() { return new Date().toLocaleTimeString('en-IN', {hour:'2-digit',minute:'2-digit'}); }

async function send() {
  const inp = document.getElementById('inp');
  const msg = inp.value.trim();
  if (!msg) return;
  document.getElementById('qa').style.display = 'none';
  addMsg(msg, 'user'); inp.value = ''; showTyping(true);
  try {
    const res = await fetch('/chat', {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({message:msg,history})});
    const data = await res.json();
    showTyping(false); addMsg(data.reply, 'bot');
    history.push({role:'user',content:msg},{role:'assistant',content:data.reply});
  } catch(e) {
    showTyping(false);
    addMsg('Apologies, having trouble connecting. Please try again shortly.', 'bot');
  }
}

function q(msg) { document.getElementById('inp').value = msg; send(); }

function addMsg(text, type) {
  const msgs = document.getElementById('messages');
  const row = document.createElement('div'); row.className = `msg-row ${type}`;
  const av = document.createElement('div'); av.className = `msg-av ${type==='bot'?'bot-av':'user-av'}`; av.textContent = type==='bot'?'🏛️':'👤';
  const body = document.createElement('div'); body.className = 'msg-body';
  if (type==='user') body.style.alignItems='flex-end';
  const bub = document.createElement('div'); bub.className = `bubble ${type==='bot'?'bot-bubble':'user-bubble'}`; bub.textContent = text;
  const t = document.createElement('div'); t.className = 'msg-time'; t.textContent = getTime();
  body.appendChild(bub); body.appendChild(t);
  if (type==='bot'){row.appendChild(av);row.appendChild(body);}else{row.appendChild(body);row.appendChild(av);}
  msgs.appendChild(row); row.scrollIntoView({behavior:'smooth',block:'end'});
}

function showTyping(show) {
  const t = document.getElementById('typing'); t.classList.toggle('show', show);
  if (show) t.scrollIntoView({behavior:'smooth',block:'end'});
}
</script>
</body>
</html>
