export interface CardData {
  id: string;
  term: string;
  definition: string;
  synonyms: string[] | null;
  antonyms: string[] | null;
  example: string | null;
  partOfSpeech: string | null;
  audioUrl: string | null;
  pictogramUrl: string | null;
}
