public class article {
    private string title;
    private string summary;
    private double interestWeight;

    public article(final String source, int sourceType) {
        switch(sourceType)
        case 0: //raw text
            parseRawText(source);
            break;
        case 1: //URL

            break;
        case 2: //document path
            break;
        case 3: //
            break;
        case 4:
            break;
    }

    private void parseRawText(final String text) {

    }

    private void parseWebSite(final String url) {

    }

    private void parseDocument(final String documentPath) {

    }
}