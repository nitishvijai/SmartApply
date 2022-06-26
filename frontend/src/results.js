import React from "react";

const Results = () => {
    return (
        <div className="background">
            <header className="search-header">
                <div class="logo-placeholder results">
                    <h1 class="logo left-align">SmartApply ✅</h1>
                    <div class="search-container left-align">
                        <input type="text" placeholder="Enter job title here..."></input>
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