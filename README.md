# SmartApply

### "Work smarter, not harder"

SmartApply takes job hunting to the next level. Say goodbye to all the 50+ tabs you'd open just for every job application.

SmartApply aggregates jobs from major job sites all at once (Indeed, Glassdoor, Monster, etc.), and presents them in a user-friendly manner. You can save these jobs to your to-do list, including the link to their applications for easy access.

You can mark certain jobs as completed (or you're not interested in) so that they won't appear in your search results anymore.

In addition, SmartApply has a Google Chrome extension that links to your SmartApply account settings. The extension allows you to SUPERCHARGE (autofill) through an active job application using your preferences, saving you all the manual work.

## Tentative Architecture

- React front-end
- Flask back-end to handle API and routes
    - Selenium web scraper script via Python
- MySQL database to hold user data and saved jobs
    - referential integrity is important so relational database preferred
- Google Chrome Extension
- AWS Web Hosting

## Features

- User login via Flask authentication to MySQL database
- Storage of user settings and preferences on MySQL
- Keyword search that web scrapes all major job sites and returns relevant listings
- To-do list to organize saved jobs
- Chrome Web Extension as mentioned above
- Export to-do list to Excel spreadsheet

## Current Goals

Set up architecture and ensure it plays nicely with Selenium web scraper.