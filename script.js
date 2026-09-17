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
