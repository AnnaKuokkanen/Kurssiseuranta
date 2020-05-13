package domain;

public abstract class Course {
    private int id;
    private String content;
    
    public int getId() {
        return this.id;
    }
    
    public String getContent() {
        return this.content;
    }
}
