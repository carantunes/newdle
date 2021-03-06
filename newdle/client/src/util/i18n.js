import es from '../locales/es/messages.js';
import en from '../locales/en/messages.js';

export function getInitialLanguage() {
  if (window.location.hash !== '#i18n' && !localStorage.getItem('userLanguage')) {
    // since we do not have any complete translations, we always default to english for now
    return 'en';
  }
  return localStorage.getItem('userLanguage') || navigator.language.substring(0, 2);
}

export function getTranslationCatalogs() {
  return {en, es};
}

export function getLanguageOptions() {
  return {en: 'English', es: 'Spanish'};
}
