// Types for the options schema structure

import type { OptionItem } from './option';

export interface SchemaField {
  label: string;
  type: 'boolean' | 'select' | 'choice' | 'color' | 'range';
  items?: OptionItem[];
  props?: Record<string, unknown>;
  shouldShow?: boolean;
}
