namespace Maxyph
{
    public class PuzzleData
    {
        public Puzzle puzzle { get; set; }
    }

    public class Puzzle
    {
        public string date { get; set; }
        public string id { get; set; }
        public Datum[] data { get; set; }
    }

    public class Datum
    {
        public string letter { get; set; }
        public int lockIndex { get; set; }
    }
}