Modern Desktop Password Generator

A modern desktop application for generating secure passwords and PIN codes, featuring multi-language support, theme switching, entropy analysis, and a unique memorable mode. Developed in Python using Tkinter and CustomTkinter GUI libraries.

Key Features

 Two Generation Modes:
  1. Standard Mode: Custom length adjustment (4 to 64 characters), character set selection (digits, lowercase/uppercase letters, special characters), and filtering of ambiguous characters (0, O, o, l, L, 1, i, I).
  2. Memorable Mode: Creation of easily memorable yet secure dictionary-based combinations (with custom word support).

 Mask Generator: Support for custom templates (e.g., LLL-DD-S, where L stands for Letter, D for Digit, and S for Special character).

 PIN Code Generator: Rapid creation and copying of structured PIN codes ranging from 4 to 12 characters.

 Real-time Security Analysis:
  1. Entropy calculation (in bits).
  2. Brute-force time estimation.
  3. Breach check against a database of compromised passwords.
  4. Password strength indicator.

 UI & UX:
  1. Light and dark theme support.
  2. Bilingual interface (Russian / English).
  3. Session history with hover-highlighting elements and input protection.
  4. Color-coded syntax highlighting for different character types in the result field.
  5. Option to mask passwords (``).

Tech Stack

1. Python 3.x
2. Tkinter / CustomTkinter (for modern GUI design)
3. Threading (for animations and background processes)
4. Math / Random / String (core generation logic)
