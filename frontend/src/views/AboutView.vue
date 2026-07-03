<script setup lang="ts">
import FaqItem from '@/components/about/FaqItem.vue';
import HowItWorks from '@/components/about/HowItWorks.vue';

const faqs = [
  {
    question: 'What is AnkiBuilder?',
    answer:
      'AnkiBuilder is a web app that turns your content into ready-to-use Anki flashcard decks. Add a text, article, word list, or image — and it generates cards with definitions, examples, and pronunciations automatically.',
  },
  {
    question: 'How does it work?',
    answer:
      'Add your content, choose a source (AI or dictionary), review and edit the generated cards, then export a ready-to-use .apkg file directly into Anki.',
  },
  {
    question: 'Do I need an account?',
    answer:
      'No — AnkiBuilder requires no registration. Your API keys are stored locally in your browser.',
  },
  {
    question: 'Is it free?',
    answer:
      "The app itself is free. If you use the AI source, you'll need your own API key from Groq or Gemini — both have generous free tiers.",
  },
  {
    question: 'What is Anki?',
    answer:
      'Anki is a free flashcard app that uses spaced repetition to help you remember things long-term. Download it at ankiweb.net.',
  },
  {
    question: 'Why do I need my own API key?',
    answer:
      'To keep the app free and respect your privacy — your requests go directly from your browser to the AI provider using your own key, so nothing is stored on our servers.',
  },
];
</script>
<template>
  <section class="font-koho p-10 md:p-16 bg-surface text-neutral flex-col">
    <h2 class="text-4xl mb-10 font-medium">About</h2>
    <div class="border-l-2 border-primary pl-4">
      <h5 class="text-xs uppercase text-gray-600 font-bold tracking-widest mb-2">
        The Story Behind It
      </h5>
      <p class="text-gray-700">
        As someone learning English, I found myself spending more time creating flashcards than
        actually studying them. So I put my programming skills to use and built AnkiBuilder — a tool
        that automates the tedious process of making accurate, well-designed flashcards so you can
        focus on what actually matters: learning.
      </p>
    </div>
    <HowItWorks class="mt-5" />
    <div class="flex flex-col items-start">
      <FaqItem
        v-for="(faq, index) in faqs"
        :question="faq.question"
        :answer="faq.answer"
        :key="index"
      />
    </div>
  </section>
</template>
