### Work Breakdown Structure (WBS)

#### PDF Chess Puzzle Extraction

Below is the WBS I am using to develop, test, and debug.

| *WBS ID* | *Description*                                   | *Status*      |
|-------|----------------------------------------------------|-------------|
| **1** | **PDF Import**                                     | *In progress*  |
| 1.1 | Create PDF of Chess puzzle book                      | In progress |
| 1.2 | Bash script to create PNG files from PDF pages       | [Complete](https://github.com/sean-gits-py/chess/blob/main/import_pdf_extract_pages/pdf_pages_to_png.sh) |
| **2** | **Preprocessing Steps**                            | *In progress* |
| 2.1 | Run Bash script, save pages PNG                      | Not Started |
| 2.2 | Create csv with book chapter, page, and puzzle info  | Complete |
| 2.3 | Load book chapter/section info from csv              | Not Started |
| 2.5 | Split each page into 6 puzzle images                 | Not Started |
| **3** | **OCR Processing**                                 | *Not Started* |
| 3.1 | Read puzzle num, page num and assign to chapter      | Not Started |
| 3.2 | Read which side plays next for each puzzle           | Not Started |
| **4** | **Board Extraction**                               | *Not Started* |
| 4.1 | Define 8 x 8 matrix and/or 64 cells                  | Not Started |
| 4.2 | Codify and save cells and pieces (piece images?)       | Not Started |
| 4.3 | Save information to puzzle DB                          | Not Started |
| **5** | **Convolutional Neural Network (CNN)**             | *Not Started* |
| 5.1 | Prepare Training Dataset (images)                      | Not Started |
| 5.2 | OpenCV - Run image classification                      | Not Started |
| **6** | **Puzzle Image Processing via CNN**                | *Not Started* |
| 6.1 | Find chess board in puzzle image                       | Not Started |
| 6.2 | Preprocess image for CNN                               | Not Started |
| 6.3 | Load CNN with labels                                   | Not Started |
| 6.4 | Extract cell info from image                           | Not Started |
| 6.5 | Predict accuracy of extracted info based on CNN        | Not Started |
| **7** | **FEN Conversion**                                 | *Not Started* |
| 7.1 | Convert FEN to Image                                   | Not Started |
