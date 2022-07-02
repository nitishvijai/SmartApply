import React from "react";
import { useLocation } from "react-router-dom";

const Results = () => {
    const location = useLocation();
    let jobTitle = location.state;

    return (
        <div className="background">
            <header className="search-header">
                <div class="logo-placeholder results">
                    <h1 class="logo left-align">SmartApply ✅</h1>
                    <div class="search-container left-align">
                        <input type="text" placeholder="Enter job title here..." value={jobTitle}></input>
                        <button type="submit">Search</button>
                    </div>
                </div>
                <div class="results-placeholder">
                    Results Placeholder
                </div>
            </header>
            SmartApply v1.0 Alpha. Last updated on 6/26/2022.
        </div>
    );
};

export default Results;