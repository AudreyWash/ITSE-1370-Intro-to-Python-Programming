**Scenario**
AppInvest is a mobile application that helps people save money and safely invest in a varied portfolio of investment vehicles. The app has helped thousands of people to accomplish their financial goals. To invest money in the app is simple: you open an account with at least $1,000 and you’re ready to go.

There are a number of investment apps currently available on the market, but AppInvest excels in some areas and offers a better service than its competitors. Some advantages of the app include setting a short-term financial goal to be achieved, as well as immediate access to the user’s funds. The company is planning on releasing a new feature that will enable investors to increase gains depending on the amount invested. In other words, the more money you put in the app, the greater your rate of return. You have been tasked with adding this functionality.

Initially, the investment engine has to be extended to allow for investors to increase their gain margin if they invest more money on the app.

The company has agreed internally that 1 million is a good starting point to trigger the increase of the gain margin. If the invested amount surpasses $1 million, then the gain margin will be increased by 1%. Similarly, if the invested amount is 5 million dollars, then the gain margin will be increased by 5% and so on, limited by a maximum of 100%.

The standard gain margin is 0.1% per month, plus 1% each time the amount surpasses increments of 1 million dollars. For example:

If the amount invested is $5,000,000 ($5 million), then the gain margin would be: 0.1% + 5% = 5.1%.

For this assessment, you will write a function that for a given invested amount will return that amount plus the calculated investment gains. If the given amount is greater than the $1 million threshold, the app will need to increase the rate of return 1% for every million dollars invested plus the original rate of 0.1%. Finally, you will implement the functionality to estimate (forecast) the return on investment over a time period.

In order for you to start this project, we will provide a function template that can be followed to solve this challenge. The code block below is a sample way that this project could be structured.

