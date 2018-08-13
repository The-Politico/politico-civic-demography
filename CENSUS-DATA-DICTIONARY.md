# Election Census Demographics
This README documents seven possible census demographics using 2016 ACS five-year data for POLITICO's race ratings project.

### The ACS API
Census table + variable lookup: https://api.census.gov/data/2016/acs/acs5/variables.html

#### Minority share or percent white
- Table: B03002
  - total: 001E
  - white: 003E
- Front-end calculation: d => ((d.total - d.white) / d.total) * 100

### Percent College Educated
- Table: B15003
  - total: 001E
  - someCollege: 020E-025E
  - Our range includes [Some college, 1 or more years, no degree] - [Doctorate Degree]
- Front-end calculation: d => (d.someCollege / d.total) * 100

### Percent Foreign Born
- Table: B05002
  - total: 001E
  - outsideUS: 013E
- Front-end calculation: d => (d.outsideUS / d.total) * 100

### Median Age
- Table: B01002
  - total: 001E

### Population
- Table: B00001
  - total: 001E

### Gini Index
- Table: B19083
  - total: 001E

### Median Income
- Table: B19013
  - total: 001E
