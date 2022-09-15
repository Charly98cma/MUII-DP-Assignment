# MUII-DP-Assignment
## Students

+ Miguel Alonso, Carlos - z170243
+ Fernández Molleda, Lucía - z170312
+ Leira García-Baamonde, Manuel - z170136

We couldn't find a 4th member, not even through Moodle forum, so we decided to
develop this project without that 4th student.

## Makefile
- **$ make install**: installs required dependencies

## Documents
### Reports

- **docs/Project_Plan.pdf**: document in which this project, its goals/objectives and
  any relevant information about its planning is specified.

- **docs/Technical_Report.pdf**: post-mortem of the project, in which the results of
  the analysis and the conclusions obtained from said analysis are explained
  with relevant plots, images and/or data.

### Data

- **csv/COVID19_data.csv**: Original dataset given to carry-on this project.

- **csv/covid_preprocessed.csv**: File with the dataset already pre-processed and
  ready to be used on a ML model to make predictions.

### Code

- **covid.ipynb**: Jupyter Notebook code used to clean the dataset and perform
  the analysis of its data, which generates plots that show any relevant
  information to understand the problem and give a final answer to the business
  and the data mining goals.

- **data_processes.knwf**: ML model that predicts the number of exitus and ICU
  patients using the `covid_preprocessed.csv` file.

### Additional files

- **README.md**: this file, which explains the contents of this directory.

- **Makefile**: file to install dependencies easily using `pip`.

- **.requirements.txt**: file with the dependencies of this project, all of them
  related to Python. This file is used by the `Makefile`, or it can be used
  manually with the command `pip install -r .requirements.txt` to install said
  dependencies.
  
# DICLAIMER

The authors are not responsible for the bad use, copy, or possible consequences related to plagiarism of this code or the contents of this repository.
Do the assignment, it is very easy, please.
