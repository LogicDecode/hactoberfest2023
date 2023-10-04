package com.github.covidtracker.controllers;

import com.github.covidtracker.models.LocationStats;
import com.github.covidtracker.services.CovidDataService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

import java.util.List;

@Controller
public class HomeController {

    @Autowired
    CovidDataService covidDataService;

    @GetMapping("/")
    public String home(Model model) {
        List<LocationStats> allStats = covidDataService.getAllStats();
        int totalReportedCases = allStats.stream().mapToInt(LocationStats::getLatestTotalCases).sum();
        int dailyCases = allStats.stream().mapToInt(LocationStats::getNewDailyCases).sum();
        int newCases = totalReportedCases - dailyCases;
        model.addAttribute("locationStats", allStats);
        model.addAttribute("totalReportedCases", totalReportedCases);
        model.addAttribute("newCases", newCases);
        return "home";
    }

}
