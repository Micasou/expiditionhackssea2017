public class preferences {
    private Map<String, double> interests;

    public preferences(final int size) {
        interests = new Map<String, boolean>(size + 1); // set init size to list size
    }

    public void addInterest(final String interest) {
        if (interests.get(interest).isEmpty()) {
            interests.add(interest, true);
        }
    }
    public static preferences createPreference(List<String> interest) {
        preferences =  new preferences(interest.size());
        interest.foreach(inter -> preferences.addInterest(inter));
        return createPreference();
    }
}