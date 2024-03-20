using Maxyph.Logic;

namespace Maxyph.Data
{
    public class WordService
    {
        private WordService() { }

        private void LoadWords()
        {

        }

        public Word GetWord(string word)
        {
            if (word.Count() != 5)
            {
                throw new ArgumentException("Word must be 5 characters long");
            }
            return new Word(word);
        }
    }
}
