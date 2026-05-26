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
  strip_punctuation: boolean;
  lowercase: boolean;
  base_form: boolean;
}

export interface FileOptions {
  type: string;
  delimiter: string;
  word_column: number;
  has_header: boolean;
  strip_punctuation: boolean;
  lowercase: boolean;
  base_form: boolean;
}

export interface DeckOptions {
  include_pronunciation: boolean;
  include_pictogram: boolean;
  use_dictionary_audio: boolean;
  source: string;
  provider: string;
  mode: string;
  source_language: string;
  target_language: string;
  deck_name: string;
}

export interface StyleOptions {
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
