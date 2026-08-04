// Types for option values used in deck generation steps

export interface OptionItem {
  label: string;
  value: string;
}

export interface Option {
  label: string;
  type: 'boolean' | 'select' | 'choice' | 'color' | 'range';
  items?: OptionItem[];
  props?: {};
}

export interface TextOptions {
  type: string;
  delimiter: string;
  stripPunctuation: boolean;
  lowercase: boolean;
  baseForm: boolean;
}

export interface FileOptions {
  type: string;
  delimiter: string;
  wordColumn: number;
  hasHeader: boolean;
  stripPunctuation: boolean;
  lowercase: boolean;
  baseForm: boolean;
}

export interface UrlOptions {
  vocabularyLevel: string;
  maxCards: number;
  includeIdioms: boolean;
}

export interface ContentOptions {
  file: FileOptions;
  text: TextOptions;
  youtube: UrlOptions;
  article: UrlOptions;
}

interface CardFields {
  partOfSpeech: boolean;
  example: boolean;
  synonyms: boolean;
  antonyms: boolean;
  audio: boolean;
  image: boolean;
}

export interface DefinitionOptions {
  useDictionaryAudio: boolean;
  source: string;
  provider: string;
  mode: string;
  model: string;
  sourceLanguage: string;
  targetLanguage: string;
  cardFields: CardFields;
}

export interface AppearanceOptions {
  fontFamily: string;
  fontSize: number;
  lineHeight: number;
  padding: number;
  textAlign: string;
  accentColor: string;
  backgroundColor: string;
  color: string;
  nightMode: boolean;
}
