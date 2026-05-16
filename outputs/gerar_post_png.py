import cairosvg

svg = '''<svg width="1080" height="1080" viewBox="0 0 1080 1080" xmlns="http://www.w3.org/2000/svg">
<defs>
  <!-- Fundo hero -->
  <radialGradient id="heroBg" cx="50%" cy="0%" r="80%">
    <stop offset="0%"   stop-color="#1e1a14"/>
    <stop offset="45%"  stop-color="#111008"/>
    <stop offset="100%" stop-color="#0A0A0A"/>
  </radialGradient>

  <!-- Luz de produto vinda do topo -->
  <radialGradient id="heroLight" cx="50%" cy="0%" r="55%">
    <stop offset="0%"   stop-color="rgba(220,200,160,0.11)"/>
    <stop offset="100%" stop-color="rgba(0,0,0,0)"/>
  </radialGradient>

  <!-- Handle body -->
  <linearGradient id="handleBody" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#E8E8E8"/>
    <stop offset="8%"   stop-color="#F5F5F5"/>
    <stop offset="18%"  stop-color="#CDCDCD"/>
    <stop offset="32%"  stop-color="#B8B8B8"/>
    <stop offset="50%"  stop-color="#D2D2D2"/>
    <stop offset="65%"  stop-color="#A8A8A8"/>
    <stop offset="80%"  stop-color="#C5C5C5"/>
    <stop offset="92%"  stop-color="#8A8A8A"/>
    <stop offset="100%" stop-color="#707070"/>
  </linearGradient>

  <linearGradient id="handleHighlight" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="rgba(255,255,255,0.9)"/>
    <stop offset="40%"  stop-color="rgba(255,255,255,0.3)"/>
    <stop offset="100%" stop-color="rgba(255,255,255,0)"/>
  </linearGradient>

  <linearGradient id="baseGrad" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%"   stop-color="#C0C0C0"/>
    <stop offset="30%"  stop-color="#9A9A9A"/>
    <stop offset="70%"  stop-color="#7A7A7A"/>
    <stop offset="100%" stop-color="#5A5A5A"/>
  </linearGradient>

  <linearGradient id="baseTop" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#DCDCDC"/>
    <stop offset="100%" stop-color="#B0B0B0"/>
  </linearGradient>

  <linearGradient id="innerShadow" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="rgba(0,0,0,0.4)"/>
    <stop offset="20%"  stop-color="rgba(0,0,0,0)"/>
    <stop offset="80%"  stop-color="rgba(0,0,0,0)"/>
    <stop offset="100%" stop-color="rgba(0,0,0,0.5)"/>
  </linearGradient>

  <radialGradient id="castShadow" cx="50%" cy="20%" r="60%">
    <stop offset="0%"   stop-color="rgba(0,0,0,0.55)"/>
    <stop offset="100%" stop-color="rgba(0,0,0,0)"/>
  </radialGradient>

  <linearGradient id="divider" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%"   stop-color="rgba(255,140,0,0)"/>
    <stop offset="20%"  stop-color="#FF8C00"/>
    <stop offset="80%"  stop-color="#FF8C00"/>
    <stop offset="100%" stop-color="rgba(255,140,0,0)"/>
  </linearGradient>

  <!-- Icon gradients -->
  <radialGradient id="circleInner" cx="38%" cy="38%" r="55%">
    <stop offset="0%"   stop-color="#FFA020"/>
    <stop offset="50%"  stop-color="#FF8C00"/>
    <stop offset="100%" stop-color="#CC5500"/>
  </radialGradient>

  <radialGradient id="spiralRed" cx="50%" cy="50%" r="50%">
    <stop offset="0%"   stop-color="#DD3300"/>
    <stop offset="100%" stop-color="#AA1500"/>
  </radialGradient>

  <clipPath id="bodyClip">
    <rect x="200" y="390" width="680" height="96" rx="48" ry="48"/>
  </clipPath>

  <filter id="softShadow">
    <feDropShadow dx="0" dy="12" stdDeviation="18" flood-color="rgba(0,0,0,0.8)"/>
  </filter>

  <!-- Textura escovada para o puxador -->
  <pattern id="brushed" x="0" y="0" width="1" height="4" patternUnits="userSpaceOnUse">
    <rect width="1080" height="4" fill="none"/>
    <line x1="0" y1="1" x2="1080" y2="1" stroke="rgba(255,255,255,0.07)" stroke-width="0.8"/>
    <line x1="0" y1="3" x2="1080" y2="3" stroke="rgba(0,0,0,0.05)" stroke-width="0.6"/>
  </pattern>
</defs>

<!-- ==============================
     FUNDO HERO (0 - 810)
     ============================== -->
<rect x="0" y="0" width="1080" height="810" fill="url(#heroBg)"/>
<rect x="0" y="0" width="1080" height="810" fill="url(#heroLight)"/>

<!-- Grid sutil -->
<g opacity="0.04">
  <!-- linhas horizontais a cada 38px -->
  <line x1="0" y1="38"  x2="1080" y2="38"  stroke="white" stroke-width="1"/>
  <line x1="0" y1="76"  x2="1080" y2="76"  stroke="white" stroke-width="1"/>
  <line x1="0" y1="114" x2="1080" y2="114" stroke="white" stroke-width="1"/>
  <line x1="0" y1="152" x2="1080" y2="152" stroke="white" stroke-width="1"/>
  <line x1="0" y1="190" x2="1080" y2="190" stroke="white" stroke-width="1"/>
  <line x1="0" y1="228" x2="1080" y2="228" stroke="white" stroke-width="1"/>
  <line x1="0" y1="266" x2="1080" y2="266" stroke="white" stroke-width="1"/>
  <line x1="0" y1="304" x2="1080" y2="304" stroke="white" stroke-width="1"/>
  <line x1="0" y1="342" x2="1080" y2="342" stroke="white" stroke-width="1"/>
  <line x1="0" y1="380" x2="1080" y2="380" stroke="white" stroke-width="1"/>
  <line x1="0" y1="418" x2="1080" y2="418" stroke="white" stroke-width="1"/>
  <line x1="0" y1="456" x2="1080" y2="456" stroke="white" stroke-width="1"/>
  <line x1="0" y1="494" x2="1080" y2="494" stroke="white" stroke-width="1"/>
  <line x1="0" y1="532" x2="1080" y2="532" stroke="white" stroke-width="1"/>
  <line x1="0" y1="570" x2="1080" y2="570" stroke="white" stroke-width="1"/>
  <line x1="0" y1="608" x2="1080" y2="608" stroke="white" stroke-width="1"/>
  <line x1="0" y1="646" x2="1080" y2="646" stroke="white" stroke-width="1"/>
  <line x1="0" y1="684" x2="1080" y2="684" stroke="white" stroke-width="1"/>
  <line x1="0" y1="722" x2="1080" y2="722" stroke="white" stroke-width="1"/>
  <line x1="0" y1="760" x2="1080" y2="760" stroke="white" stroke-width="1"/>
  <line x1="0" y1="798" x2="1080" y2="798" stroke="white" stroke-width="1"/>
  <!-- linhas verticais -->
  <line x1="38"  y1="0" x2="38"  y2="810" stroke="white" stroke-width="1"/>
  <line x1="76"  y1="0" x2="76"  y2="810" stroke="white" stroke-width="1"/>
  <line x1="114" y1="0" x2="114" y2="810" stroke="white" stroke-width="1"/>
  <line x1="152" y1="0" x2="152" y2="810" stroke="white" stroke-width="1"/>
  <line x1="190" y1="0" x2="190" y2="810" stroke="white" stroke-width="1"/>
  <line x1="228" y1="0" x2="228" y2="810" stroke="white" stroke-width="1"/>
  <line x1="266" y1="0" x2="266" y2="810" stroke="white" stroke-width="1"/>
  <line x1="304" y1="0" x2="304" y2="810" stroke="white" stroke-width="1"/>
  <line x1="342" y1="0" x2="342" y2="810" stroke="white" stroke-width="1"/>
  <line x1="380" y1="0" x2="380" y2="810" stroke="white" stroke-width="1"/>
  <line x1="418" y1="0" x2="418" y2="810" stroke="white" stroke-width="1"/>
  <line x1="456" y1="0" x2="456" y2="810" stroke="white" stroke-width="1"/>
  <line x1="494" y1="0" x2="494" y2="810" stroke="white" stroke-width="1"/>
  <line x1="532" y1="0" x2="532" y2="810" stroke="white" stroke-width="1"/>
  <line x1="570" y1="0" x2="570" y2="810" stroke="white" stroke-width="1"/>
  <line x1="608" y1="0" x2="608" y2="810" stroke="white" stroke-width="1"/>
  <line x1="646" y1="0" x2="646" y2="810" stroke="white" stroke-width="1"/>
  <line x1="684" y1="0" x2="684" y2="810" stroke="white" stroke-width="1"/>
  <line x1="722" y1="0" x2="722" y2="810" stroke="white" stroke-width="1"/>
  <line x1="760" y1="0" x2="760" y2="810" stroke="white" stroke-width="1"/>
  <line x1="798" y1="0" x2="798" y2="810" stroke="white" stroke-width="1"/>
  <line x1="836" y1="0" x2="836" y2="810" stroke="white" stroke-width="1"/>
  <line x1="874" y1="0" x2="874" y2="810" stroke="white" stroke-width="1"/>
  <line x1="912" y1="0" x2="912" y2="810" stroke="white" stroke-width="1"/>
  <line x1="950" y1="0" x2="950" y2="810" stroke="white" stroke-width="1"/>
  <line x1="988" y1="0" x2="988" y2="810" stroke="white" stroke-width="1"/>
  <line x1="1026" y1="0" x2="1026" y2="810" stroke="white" stroke-width="1"/>
</g>

<!-- Arcos decorativos dourados sutis -->
<circle cx="540" cy="490" r="360" fill="none" stroke="rgba(180,140,60,0.10)" stroke-width="1"/>
<circle cx="540" cy="490" r="280" fill="none" stroke="rgba(180,140,60,0.07)" stroke-width="1"/>

<!-- ==============================
     TAGLINE
     ============================== -->
<!-- Eyebrow -->
<text x="540" y="130" text-anchor="middle"
      font-family="Georgia, serif" font-size="19" fill="rgba(255,140,0,0.75)"
      letter-spacing="8">HARDWARE PARA MARCENARIA</text>

<!-- Main tagline -->
<text x="540" y="195" text-anchor="middle"
      font-family="Georgia, serif" font-size="58" font-style="italic"
      fill="rgba(255,255,255,0.82)" letter-spacing="1">Elegância em cada detalhe</text>

<!-- Linha laranja decorativa tagline -->
<rect x="516" y="215" width="48" height="1.5" fill="rgba(255,140,0,0.6)"/>

<!-- ==============================
     PUXADOR (centralizado em 540, região 280-680)
     ============================== -->
<g transform="translate(200, 290)">
  <!-- sombra projetada -->
  <ellipse cx="340" cy="295" rx="310" ry="22" fill="url(#castShadow)" opacity="0.7"/>

  <!-- BASE ESQUERDA -->
  <g filter="url(#softShadow)">
    <rect x="72" y="148" width="64" height="52" rx="6" fill="url(#baseGrad)"/>
    <path d="M72,148 L136,148 L130,128 L78,128 Z" fill="url(#baseTop)"/>
    <path d="M136,148 L136,200 L130,192 L130,128 Z" fill="rgba(0,0,0,0.35)"/>
    <circle cx="104" cy="174" r="7" fill="#1A1A1A"/>
    <circle cx="104" cy="174" r="5" fill="#111"/>
    <circle cx="104" cy="174" r="3.5" fill="url(#baseGrad)"/>
    <circle cx="104" cy="174" r="1.5" fill="#333"/>
    <line x1="101.5" y1="174" x2="106.5" y2="174" stroke="#555" stroke-width="1"/>
  </g>

  <!-- BASE DIREITA -->
  <g filter="url(#softShadow)">
    <rect x="544" y="148" width="64" height="52" rx="6" fill="url(#baseGrad)"/>
    <path d="M544,148 L608,148 L602,128 L550,128 Z" fill="url(#baseTop)"/>
    <path d="M608,148 L608,200 L602,192 L602,128 Z" fill="rgba(0,0,0,0.35)"/>
    <circle cx="576" cy="174" r="7" fill="#1A1A1A"/>
    <circle cx="576" cy="174" r="5" fill="#111"/>
    <circle cx="576" cy="174" r="3.5" fill="url(#baseGrad)"/>
    <circle cx="576" cy="174" r="1.5" fill="#333"/>
    <line x1="573.5" y1="174" x2="578.5" y2="174" stroke="#555" stroke-width="1"/>
  </g>

  <!-- BARRA PRINCIPAL -->
  <rect x="58" y="99" width="564" height="82" rx="41" fill="rgba(0,0,0,0.5)" filter="url(#softShadow)"/>
  <rect x="60" y="100" width="560" height="80" rx="40" fill="url(#handleBody)"/>
  <rect x="60" y="100" width="560" height="80" rx="40" fill="url(#brushed)" clip-path="url(#bodyClip)" opacity="0.5"/>
  <rect x="60" y="100" width="560" height="80" rx="40" fill="url(#innerShadow)" clip-path="url(#bodyClip)"/>
  <!-- Highlight especular -->
  <rect x="90" y="104" width="500" height="24" rx="12" fill="url(#handleHighlight)" clip-path="url(#bodyClip)" opacity="0.85"/>
  <!-- Segundo highlight deslocado -->
  <rect x="160" y="108" width="240" height="8" rx="4" fill="rgba(255,255,255,0.55)" clip-path="url(#bodyClip)"/>
  <!-- Reflexo inferior -->
  <ellipse cx="340" cy="172" rx="220" ry="6" fill="rgba(255,255,255,0.08)" clip-path="url(#bodyClip)"/>
  <!-- Reflexo laranja sutil (assinatura de marca) -->
  <rect x="60" y="100" width="560" height="80" rx="40" fill="rgba(255,140,0,0.05)" clip-path="url(#bodyClip)"/>
  <!-- Tampas laterais -->
  <ellipse cx="62" cy="140" rx="8" ry="40" fill="url(#baseGrad)" opacity="0.7"/>
  <ellipse cx="62" cy="140" rx="5" ry="36" fill="rgba(80,80,80,0.6)"/>
  <ellipse cx="618" cy="140" rx="8" ry="40" fill="url(#baseGrad)" opacity="0.5"/>
  <!-- Linha central fina (detalhe de torneamento) -->
  <line x1="100" y1="140" x2="580" y2="140" stroke="rgba(255,255,255,0.12)" stroke-width="1" clip-path="url(#bodyClip)"/>

  <!-- Reflexo especular no chão -->
  <g opacity="0.15">
    <rect x="60" y="100" width="560" height="80" rx="40" fill="url(#handleBody)"
          transform="translate(0,322) scale(1,-0.18) translate(0,-322)"/>
  </g>
</g>

<!-- Texto de apoio -->
<text x="540" y="764" text-anchor="middle"
      font-family="Georgia, serif" font-size="20" fill="rgba(255,255,255,0.42)"
      letter-spacing="5">PUXADORES PREMIUM PARA MÓVEIS PLANEJADOS</text>

<!-- ==============================
     DIVISOR LARANJA
     ============================== -->
<rect x="0" y="810" width="1080" height="3" fill="url(#divider)"/>

<!-- ==============================
     LOGO BAR (810 - 1080)
     ============================== -->
<rect x="0" y="813" width="1080" height="267" fill="#000000"/>
<!-- Borda inferior bronze -->
<rect x="0" y="1078" width="1080" height="1" fill="rgba(180,140,60,0.2)"/>

<!-- Logo centralizada: bloco texto + ícone -->
<!-- Centrado horizontalmente em 540, verticalmente em ~946 -->
<g transform="translate(258, 866)">

  <!-- TEXTO -->
  <text x="0" y="72"
        font-family="Impact, Arial Black, sans-serif"
        font-size="80" font-weight="900"
        fill="#FFFFFF" letter-spacing="-1">CASA</text>

  <text x="6" y="101"
        font-family="Impact, Arial Black, sans-serif"
        font-size="29" font-weight="400"
        fill="#CCCCCC" letter-spacing="7">do</text>

  <text x="0" y="148"
        font-family="Impact, Arial Black, sans-serif"
        font-size="59" font-weight="900"
        fill="#FFFFFF" letter-spacing="-0.5">MARCENEIRO</text>

  <text x="400" y="162"
        font-family="Georgia, Times New Roman, serif"
        font-size="15" font-style="italic"
        fill="rgba(255,255,255,0.65)">Desde 1986</text>

  <!-- ÍCONE C/CHAMA — à direita do texto -->
  <g transform="translate(502, 82)">
    <!-- Espiral vermelha externa -->
    <path d="M -46 12 A 48 48 0 1 1 18 52 L 12 40 A 36 36 0 1 0 -34 10 Z"
          fill="url(#spiralRed)" opacity="0.92"/>
    <!-- Prolongamento chama inferior -->
    <path d="M 18 52 C 30 64, 38 70, 30 80 C 20 90, -10 82, -28 60 L -18 50 C -4 66, 14 72, 20 65 C 26 58, 20 50, 14 43 Z"
          fill="#CC2200" opacity="0.85"/>
    <!-- Ponta superior orgânica -->
    <path d="M -34 10 C -42 -8, -28 -28, -10 -36 C -18 -20, -22 -8, -16 4 Z"
          fill="#BB1A00" opacity="0.8"/>
    <!-- Círculo laranja central -->
    <circle cx="0" cy="0" r="34" fill="url(#circleInner)"/>
    <!-- C vermelho interno -->
    <path d="M 18 -16 A 22 22 0 1 0 18 16 L 10 10 A 14 14 0 1 1 10 -10 Z"
          fill="#CC2200"/>
    <!-- Reflexo volume -->
    <circle cx="-8" cy="-8" r="12" fill="rgba(255,200,100,0.18)"/>
  </g>
</g>

<!-- ==============================
     BORDA INTERNA DOURADA
     ============================== -->
<rect x="14" y="14" width="1052" height="1052"
      fill="none" stroke="rgba(180,140,60,0.35)" stroke-width="1"/>

</svg>'''

cairosvg.svg2png(bytestring=svg.encode('utf-8'),
                 write_to='/home/user/dev1/outputs/post-casa-marceneiro-puxador.png',
                 output_width=1080,
                 output_height=1080)

print("PNG gerado com sucesso!")
