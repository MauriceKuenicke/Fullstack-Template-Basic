<template>
  <svg style="scale: 0.8"
       width="64" height="64"
       xmlns="http://www.w3.org/2000/svg">
    <defs>
      <linearGradient x1="0%" y1="100%" x2="50%" y2="0%" id="feature-1-a">
        <stop stop-color="#F9425F" stop-opacity=".8" offset="0%"/>
        <stop stop-color="#47A1F9" stop-opacity=".16" offset="100%"/>
      </linearGradient>
      <linearGradient x1="50%" y1="100%" x2="50%" y2="0%" id="feature-1-b">
        <stop stop-color="#FDFFDA" offset="0%"/>
        <stop stop-color="#F97059" stop-opacity=".798" offset="49.935%"/>
        <stop stop-color="#F9425F" stop-opacity="0" offset="100%"/>
      </linearGradient>
    </defs>
    <g fill="none" fill-rule="evenodd">
      <path d="M24 48H0V24C0 10.745 10.745 0 24 0h24v24c0 13.255-10.745 24-24 24" fill="url(#feature-1-a)"/>
      <path d="M40 64H16V40c0-13.255 10.745-24 24-24h24v24c0 13.255-10.745 24-24 24" fill="url(#feature-1-b)"/>
    </g>
  </svg>
</template>
