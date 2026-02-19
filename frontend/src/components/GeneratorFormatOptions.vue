<script setup lang="ts"></script>

<template>
    <h3 class="text-2xl font-medium">Options</h3>
    <div class="p-2">
      <div class="general-options">
        <ul class="flex-col accent-neutral">
          <li class="flex gap-2">
            <input type="checkbox" id="include-Pronunciation" class="cursor-pointer" />
            <label for="include-Pronunciation">Include Pronunciation</label>
          </li>
          <li class="flex gap-2">
            <input type="checkbox" id="include-photos" class="cursor-pointer" />
            <label for="include-photos">Include Photos</label>
          </li>
        </ul>
      </div>
      <div class="mt-2 flex justify-between">
        <h4 class="font-medium">Definition Source</h4>
        <div>
          <select name="" id="">
            <option value="a">AI</option>
          </select>
          <select name="AI_Options" id="">
            <option value="a">Groq</option>
          </select>
        </div>
      </div>
    </div>
</template>

<!-- <style scoped>
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
</style> -->
