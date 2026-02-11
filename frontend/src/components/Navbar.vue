<script setup lang="ts"></script>

<template>
  <nav class="navbar">
    <div class="navbar__left">AnkiBuilder</div>
    <div class="navbar__right">
      <ul>
        <li><button>Export</button></li>
        <li><button>Settings</button></li>
      </ul>
    </div>
  </nav>
</template>

<style scoped>
nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #062743;
  color: #e5e7eb;
  padding: 1rem;
  font-family: 'Inter', sans-serif;
  font-weight: bold;
}

.navbar__left {
    cursor: pointer;
    font-size: 1.2rem;
}

.navbar__right ul {
  display: flex;
  list-style-type: none;
  gap: 2rem;
}

.navbar__right ul li button {
  all: inherit;
  background-color: #113a5d;
  padding: 0.5rem;
  border: none;
  border-radius: 10px;
  cursor: pointer;
}

.navbar__right ul li button:hover {
  background-color: #c4ffdd;
  color: black;
  transition-property: background-color, color;
  transition-duration: 0.5s, 0.5s;
  transition-timing-function: ease-in, ease-out;
}
</style>
