class Program
{
    static void Main(string[] args)
    {
        string apiKey = Environment.GetEnvironmentVariable("OPENAI_API_KEY");
        string inputFilePath = "path/to/word/document.docx";
        string outputFilePath = "path/to/output/document.docx";

        DocumentProofreader proofreader = new DocumentProofreader(apiKey);
        proofreader.ProofreadDocument(inputFilePath, outputFilePath);
    }
}
