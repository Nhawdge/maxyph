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
   
  },
});

var appRunning = app.mount("#app");
