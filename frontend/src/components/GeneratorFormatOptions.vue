<script setup lang="ts"></script>

<template>
  <div class="deck-generator__format-options">
    <h3>Options</h3>
    <div class="format-options">
      <div class="general-options">
        <ul>
          <li><input type="checkbox" id="1" /> <label for="1">Include Photos</label></li>
          <li><input type="checkbox" id="1" /> <label for="1">Include Photos</label></li>
        </ul>
      </div>
      <div class="definition-options">
        <h4>Definition Source</h4>
        <div class="definition-options-choices">
          <select name="" id="">
            <option value="a">AI</option>
          </select>
          <select name="AI_Options" id="">
            <option value="a">Groq</option>
          </select>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
h3 {
  margin: 10px 0;
}

.general-options ul {
  list-style-type: none;
}

.format-options {
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.definition-options {
  display: flex;
  justify-content: space-between;
}

.definition-options-choices {
  display: flex;
  gap: 10px;
}
</style>
