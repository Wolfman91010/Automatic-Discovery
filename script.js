const form = document.getElementById('oracle-form');
const questionInput = document.getElementById('question-input');
const readingSign = document.getElementById('reading-sign');
const readingTitle = document.getElementById('reading-title');
const readingText = document.getElementById('reading-text');

const readings = [
  {
    sign: 'The Aurora of Momentum',
    title: 'Action will open the door',
    text: 'Your next steps are not meant to be perfect. The cosmos favors courage, timing, and a willingness to move before certainty arrives.'
  },
  {
    sign: 'Moonlit Alignment',
    title: 'Trust the quiet signal',
    text: 'The answer is already present, but it speaks softly. Pause, listen, and follow the thread that brings calm instead of noise.'
  },
  {
    sign: 'The Crown of Renewal',
    title: 'A new chapter is forming',
    text: 'Release what has already finished its work. This cycle is ending so that a more luminous path can emerge with clarity.'
  },
  {
    sign: 'Solar Flame',
    title: 'Confidence will sharpen your direction',
    text: 'You do not need every answer before stepping forward. The next move becomes clear when your intention is sincere and steady.'
  },
  {
    sign: 'The Horizon Watcher',
    title: 'Patience is part of the magic',
    text: 'Some truths arrive only after the dust settles. Continue with integrity, and the right opportunity will reveal itself in its own season.'
  }
];

function pickReading() {
  const index = Math.floor(Math.random() * readings.length);
  return readings[index];
}

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const question = questionInput.value.trim();
  const reading = pickReading();

  if (!question) {
    questionInput.focus();
    questionInput.placeholder = 'Ask a question before the stars answer.';
    return;
  }

  const focusWord = question.split(' ').slice(0, 2).join(' ');
  readingTitle.textContent = `${reading.title} for ${focusWord}`;
  readingSign.textContent = reading.sign;
  readingText.textContent = `${reading.text} Your question, “${question}”, is being carried by a current of possibility and personal growth.`;
});
function speakCurrentOmen() {
    if (!('speechSynthesis' in window)) {
        console.warn("Speech synthesis is not supported in this browser.");
        return;
    }

    // Locate the paragraph containing the main omen text body
    // (Targeting the container element shown in your live view)
    const omenParagraph = document.querySelector('section[aria-live="polite"] p:last-of-type') || 
                           document.querySelector('.oracle-omen-body');

    if (!omenParagraph) return;

    let rawText = omenParagraph.innerText;

    // Strip out the metadata wrapper sentence: e.g., "Your question, "...", is being carried by..."
    // This leaves only the pure core message to be spoken out loud.
    let cleanOmenText = rawText.replace(/Your question,.*?, is being carried by.*?\./gs, "").trim();

    // Fallback if the regex pattern misses
    if (!cleanOmenText) {
        cleanOmenText = rawText;
    }

    const utterance = new SpeechSynthesisUtterance(cleanOmenText);
    
    // Set an oracle-like, deliberate cadence
    utterance.rate = 0.92;  // Slightly measured pace
    utterance.pitch = 1.0;  // Neutral, grounded pitch

    // Select a smooth natural system voice if available
    const voices = window.speechSynthesis.getVoices();
    const preferredVoice = voices.find(v => v.lang.includes('en') && (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha'))) || voices[0];
    
    if (preferredVoice) {
        utterance.voice = preferredVoice;
    }

    // Cancel any ongoing speech so they don't overlap, then speak
    window.speechSynthesis.cancel();
    window.speechSynthesis.speak(utterance);
}
