import React from "react";
import { useNavigate, Navigate } from "react-router-dom";

const Home = () => {
    const navigate = useNavigate();

    function submitApp() {
        const search = document.getElementById("search").value;
    
        if (search === "") {
            alert("Please enter a job title in the search box.");
        }
        else {
            // open the results page with search query
            console.log("Opening results...");
            navigate("/search", {state: "Software Engineer"});
        }
    }

    return (
        <div className="background">
            <header className="App-header">
                {/* <img src={logo} className="App-logo" alt="logo" /> */}
                <div class="logo-placeholder">
                    <h1>SmartApply ✅</h1>
                    <h2>Apply smarter, not harder</h2>
                </div>
                Search for a job to begin
                <div class="search-container">
                    <input id="search" type="text" placeholder="Enter job title here..."></input>
                    <button type="submit" onClick={submitApp}>Search</button>
                </div>
            </header>
            SmartApply v1.0 Alpha. Last updated on 6/26/2022.
        </div>
    );
};

export default Home;