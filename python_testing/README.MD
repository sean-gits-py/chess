### PDF Chess Puzzle Extraction Work Breakdown Structure (WBS)

| WBS ID | Description                                   | Status      |
|-------|------------------------------------------------------|-------------|
| 1   | PDF Import                                             | Complete    |
| 1.1 | Import pages from PDF                                  | Not Started |
| 2   | PDF Preprocess Steps                                   | Not Started |
| 2.1 | Save pages/puzzles as PNG                              | Not Started |
| 2.2 | Load book chapter/section info (py)                    | Not Started |
| 2.3 | Read PNG puzzle & page #, assign to chapter            | Not Started |
| 2.4 | Split each page into 6 puzzle images                   | Not Started |
| 3   | OCR Processing                                         | Not Started |
| 3.1 | Read puzzle & page                                     | Not Started |
| 3.2 | Read which side plays next                             | Not Started |
| 4   | Board Extraction                                       | Not Started |
| 4.1 | Define 8 x 8 matrix and/or 64 cells                    | Not Started |
| 4.2 | Codify and save cells and pieces (piece images?)       | Not Started |
| 4.3 | Save information to puzzle DB                          | Not Started |
| 5   | Convolutional Neural Network (CNN)                     | Not Started |
| 5.1 | Prepare Training Dataset (images)                      | Not Started |
| 5.2 | OpenCV - Run image classification                      | Not Started |
| 6   | Puzzle Image Processing via CNN                        | Not Started |
| 6.1 | Find chess board in puzzle image                       | Not Started |
| 6.2 | Preprocess image for CNN                               | Not Started |
| 6.3 | Load CNN with labels                                   | Not Started |
| 6.4 | Extract cell info from image                           | Not Started |
| 6.5 | Predict accuracy of extracted info based on CNN        | Not Started |
| 7   | FEN Conversion                                         | Not Started |
| 7.1 | Convert FEN to Image                                   | Not Started |
