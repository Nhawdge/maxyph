namespace Maxyph.Logic
{
    public class Word
    {
        public Word()
        {
            Letters.Add(new Letter());
            Letters.Add(new Letter());
            Letters.Add(new Letter());
            Letters.Add(new Letter());
            Letters.Add(new Letter());
        }

        public Word(string word)
        {
            if (word.Count() != 5)
            {
                throw new ArgumentException("Word must be 5 characters long");
            }

            foreach (var letter in word)
            {
                Letters.Add(new Letter { Value = letter, Locked = false });
            }
        }

        public List<Letter> Letters = new();

        public void LockLetter(int i)
        {
            try
            {
                Letters[i].Locked = true;
            }
            catch (Exception) { }
        }

        public string GetLetterAtPosition(int i)
        {
            return Letters[i].Value.ToString();
        }
        public void SetLetterAtPosition(int i, char letter)
        {
            Letters[i].Value = letter;
        }

        public override string ToString()
        {
            return string.Join("", Letters.Select(x => x.Value));
        }

        public static PuzzleData ToPuzzleData(List<Word> words)
        {
            var puzzleData = new PuzzleData();
            puzzleData.puzzle = new Puzzle();
            puzzleData.puzzle.date = DateTime.Now.ToString("yyyy-MM-dd");
            puzzleData.puzzle.id = Guid.NewGuid().ToString();
            puzzleData.puzzle.data = new Datum[6];

            for (int i = 0; i < 6; i++)
            {
                puzzleData.puzzle.data[i] = new Datum
                {
                    letter = words[i].ToString(),
                    lockIndex = words[i].Letters.FindIndex(x => x.Locked)
                };
            }

            return puzzleData;

        }
    }

    public class Letter
    {
        public char Value;
        public bool Locked;
    }

}
