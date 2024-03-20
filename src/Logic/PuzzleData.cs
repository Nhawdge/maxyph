using System.Text.Json.Serialization;

namespace Maxyph
{
    public class PuzzleData
    {
        [JsonPropertyName("puzzle")]
        public List<List<PuzzleRow>> Puzzle { get; set; }

        [JsonPropertyName("date")]
        public DateTimeOffset Date { get; set; }
    }

    public class PuzzleRow
    {
        public long? LockedIndex;
        public string LockedValue;
    }
}