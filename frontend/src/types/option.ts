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
