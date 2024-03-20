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

        public void LockLetter(int i)
        {
            try
            {
                Letters[i].Locked = true;
            }
            catch (Exception) { }
        }

        public List<Letter> Letters = new();
        public string GetLetterAtPosition(int i)
        {
            return Letters[i].Value.ToString();
        }

        public string GetStyleForPos(int i)
        {
            return Letters[i].Locked ? "locked" : string.Empty;
        }

        public override string ToString()
        {
            return string.Join("", Letters.Select(x => x.Value));
        }
    }

    public class Letter
    {
        public char Value;
        public bool Locked;
    }

}
