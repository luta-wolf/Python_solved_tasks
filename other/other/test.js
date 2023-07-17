class FoodTracker {
	constructor(calorieGoal, dailyCalories) {
	  this.calorieGoal = calorieGoal;
	  this.dailyCalories = dailyCalories;
	  this.history = [];
	}

	addFood(name, calories) {
	  this.history.push({ name, calories });
	  this.dailyCalories += calories;
	}

	getRemainingCalories() {
	  return this.calorieGoal - this.dailyCalories;
	}

	getWeeklyCalories() {
	  const now = new Date();
	  const oneWeekAgo = new Date(now.getTime() - 7 * 24 * 60 * 60 * 1000);
	  const weeklyCalories = this.history
		.filter((entry) => new Date(entry.date) >= oneWeekAgo)
		.reduce((total, entry) => total + entry.calories, 0);
	  return weeklyCalories;
	}
  }

  const myTracker = new FoodTracker(2000, 0);

  myTracker.addFood("banana", 100);
  myTracker.addFood("chicken", 400);
  myTracker.addFood("salad", 200);

  console.log(myTracker.getRemainingCalories()); // Output: 1300
  console.log(myTracker.getWeeklyCalories()); // Output: 700

