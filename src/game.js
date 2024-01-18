const { createApp } = Vue;

var app = createApp({
  data() {
    return {
      words: ["", "", "", "", "", ""],
      required: [
        ["", "i", "", "", ""],
        ["", "", ".", "", ""],
        ["", "", "", "", "."],
        [".", "", "", "", ""],
        ["", "", "", ".", ""],
        ["", ".", "", "", ""],
      ],
      typeIndex: 0,
      validWords: [],
      error: "",
    };
  },
  methods: {
    getLetterAtPos(wordi, i) {
      var letter = this.required[wordi][i] || this.words[wordi][i];
      if (letter == ".") {
        return this.words[wordi - 1][i];
      }
      return letter;
    },
    getStyleAtPos(wordi, i) {
      return this.required[wordi][i] ? "locked" : "";
    },
    wordIsValid(word) {
      var isvalid = this.validWords.includes(word);
      if (isvalid) {
        this.error = "";
      } else {
        this.error = `'${word}' is not in the wordlist `;
      }
      return isvalid;
    },
    quit() {},
  },
  computed: {
    score() {
      var total = new Set(this.words.join(""));
      return total.size;
    },
  },
  created() {
    fetch("words.txt")
      .then((response) => response.text())
      .then((text) => {
        this.validWords = text.split("\n").map((x) => x.toLowerCase().trim());
        console.log(this.validWords);
      });
    document.addEventListener("keydown", (e) => {
      if (e.key == "Backspace") {
        if (this.words[this.typeIndex].length == 0) {
          this.typeIndex = Math.max(0, Math.min(5, this.typeIndex - 1));
        }
        this.words[this.typeIndex] = this.words[this.typeIndex].substring(0, this.words[this.typeIndex].length - 1);
      } else if (e.key == "Enter") {
        console.log(this.words[this.typeIndex].length, this.words[this.typeIndex], this.wordIsValid(this.words[this.typeIndex]));
        if (this.words[this.typeIndex].length == 5 && this.wordIsValid(this.words[this.typeIndex])) {
          this.typeIndex = Math.max(0, Math.min(5, this.typeIndex + 1));
        }
      }

      if (e.key.length == 1 && this.words[this.typeIndex].length < 5) {
        this.words[this.typeIndex] += e.key;
        var required = this.getLetterAtPos(this.typeIndex, this.words[this.typeIndex].length);
        console.log(required, e.key);
        if (required) {
          this.words[this.typeIndex] += required;
        }
      }
    });
  },
});

var appRunning = app.mount("#app");
