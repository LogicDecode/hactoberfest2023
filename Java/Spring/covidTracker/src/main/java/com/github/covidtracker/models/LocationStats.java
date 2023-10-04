package com.github.covidtracker.models;

public class LocationStats {

    private String state;
    private String country;
    private int latestTotalCases;
    private int newDailyCases;

    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }

    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }

    public int getLatestTotalCases() {
        return latestTotalCases;
    }

    public void setLatestTotalCases(int latestTotalCases) {
        this.latestTotalCases = latestTotalCases;
    }

    public int getNewDailyCases() {
        return newDailyCases;
    }

    public void setNewDailyCases(int newDailyCases) {
        this.newDailyCases = newDailyCases;
    }

    public int dailyNew() {
        return latestTotalCases - newDailyCases;
    }
    @Override
    public String toString() {
        return "LocationStats{" +
                "state='" + state + '\'' +
                ", country='" + country + '\'' +
                ", latestTotalCases=" + latestTotalCases +
                ", newDailyCases=" + dailyNew() +
                '}';
    }
}
