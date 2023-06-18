# projects
# Harry Potter Character Network Analysis

This project aims to create a network of Harry Potter characters and derive insights from the information. The analysis includes determining the most important characters, tracking their importance over time, and identifying the strongest communities within the network.

## Table of Contents

- [Project Overview](#project-overview)
- [Data Scraping and Wrangling](#data-scraping-and-wrangling)
- [Natural Language Processing](#natural-language-processing)
- [Character Network Visualization](#character-network-visualization)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

In this project, we analyze the relationships between Harry Potter characters to create a network representation. By extracting data from a Harry Potter wiki website, performing data wrangling, and applying natural language processing techniques to the books, we can gain insights into the character network.

## Data Scraping and Wrangling

To build the character network, we start by scraping the character names from a Harry Potter wiki website. Using the `beautifulsoup` library, we extract the relevant information and create a dataframe. The scraped data is then cleaned and preprocessed to ensure it is suitable for analysis.

## Natural Language Processing

To identify relationships between characters, we employ natural language processing (NLP) techniques. We utilize the `spacy` library to read each of the Harry Potter books, which were downloaded in TXT format. By applying NLP, we can extract information about character interactions, affiliations, and mentions throughout the series.

## Character Network Visualization

To visualize the character network, we employ the `pyvis` and `networkx` libraries. Using the relationships derived from NLP, we construct a graph representation of the character network. By assigning importance scores to characters and analyzing the network structure, we can identify the most significant characters and observe how their importance evolves over time. Additionally, we identify strong communities within the network, which can provide insights into character relationships and story arcs.

## Dependencies

The following libraries were used in this project:

- `beautifulsoup`: For web scraping character names.
- `pandas`: For data manipulation and cleaning.
- `spacy`: For natural language processing and extracting relationships.
- `matplotlib`: For generating visualizations.
- `pyvis`: For creating interactive network visualizations.
- `networkx`: For constructing and analyzing the character network.

## Usage

To reproduce the analysis or visualize the character network, please follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Run the data scraping and wrangling scripts.
4. Run the natural language processing script to extract relationships from the Harry Potter books.
5. Execute the character network visualization script to generate interactive visualizations.

## Contributing

Contributions to this project are welcome. If you have any suggestions, bug fixes, or feature implementations, please submit a pull request. For major changes, please open an issue first to discuss the proposed changes.

## Conclusion

In this project, we have analyzed the Harry Potter character network by scraping character names, performing data wrangling, applying natural language processing techniques, and visualizing the network using graph representations. By exploring the relationships between characters, we can gain insights into their importance, evolution over time, and the presence of strong communities within the network.

We encourage you to explore the code in this repository, reproduce the analysis, and adapt it to your own projects. If you have any questions or feedback, feel free to contact us.

Happy exploring the magical world of Harry Potter characters!

