const question = document.querySelector('#question');
const choices = Array.from(document.querySelectorAll('.choice-text'));
const progressText = document.querySelector('#progressText');
const scoreText = document.querySelector('#score');
const progressBarFull = document.querySelector('#progressBarFull');
// const loader = document.getElementById("loader")
// const game = document.getElementById("game")

let currentQuestion = {}
let acceptingAnswers = true 
let score = 0
let questionCounter = 0
let availableQuestions = []

let questions = [
 {
 	question:"What is 2 + 2?",
	choice1: "2",
	choice2: "4",
	choice3: "21",
	choice4: "17",
	answer:2
},
{
	question:"The Tallest building in the world is located in which city?",
	choice1:"Dubai",
	choice2:"New york",
	choice3:"Shanghai",
	choice4:"None of the above",
	answer:1
},
{
	question:"What percent of american adults believe that chocolate milk comes from brown cows?",
	choice1:"20%",
	choice2:"18%",
	choice3:"7%",
	choice4:"33%",
	answer:3
},
{
	question:"Approximately what percent of U.S power outages are caused by squirrels?",
	choice1:"10-20%",
	choice2:"5-10%",
	choice3:"15-20%",
	choice4:"30-40%",
	answer:1
}
 ]

// fetch("https://opentdb.com/api.php?amount=10&category=20&difficulty=easy&type=multiple")

//  .then(res => {
// 	return res.json()

//  })

//  .then(loadedQuestions => {
//  	console.log(loadedQuestions.results)
//  	questions = loadedQuestions.results.map(loadedQuestion => {
//  		const formattedQuestion = { 
//  			question: loadedQuestion.question
//  		}

//  		const answerChoices = [...loadedQuestion.incorrect_answers]
//  		formattedQuestion.answer = Math.floor(Math.random() * 3) + 1
//  		answerChoices.splice(formattedQuestion.answer -1, 0, loadedQuestion.correct_answer);

//      answerChoices.forEach((choice, index) => {
//      formattedQuestion["choice" + (index + 1)] = choice
//      })
 
//      return formattedQuestion
//  	})
// 	// questions = loadedQuestions
// 	startGame()
//  })
//  .catch(err =>{
//  	console.error(err)
//  })

// CONSTANTS

const SCORE_POINTS  = 10
const MAX_QUESTIONS = 4

startGame = () => {
    questionCounter = 0
	score = 0
	availableQuestions = [...questions]
	getNewQuestion()
	game.classList.remove("hidden")
	// loader.classList.add("hidden")
	
}

getNewQuestion = () => {
	if(availableQuestions.length === 0 || questionCounter > MAX_QUESTIONS) {
		localStorage.setItem('mostRecentScore',score)

		return window.location.assign('End.html')
	}

	questionCounter++
	progressText.innerText = `Question ${questionCounter} of ${MAX_QUESTIONS}`
	progressBarFull.style.width = `${(questionCounter/MAX_QUESTIONS) * 100}%`

	const questionsIndex = Math.floor(Math.random() * availableQuestions.length)
    currentQuestion = availableQuestions[questionsIndex]
    question.innerText = currentQuestion.question

    choices.forEach(choice => {
    	const number = choice.dataset['number']
    	choice.innerText = currentQuestion['choice' + number]
    })

    availableQuestions.splice(questionsIndex, 1)

    acceptingAnswers = true
}

choices.forEach(choice => {
	choice.addEventListener('click', e => {
		if(!acceptingAnswers) return
// (const) variable can't be changed,its lyk tuples in python
// u can changed d ppt of a const but u can't reassign it
		  acceptingAnswers = false
		  const selectedChoice = e.target
		  const selectedAnswer = selectedChoice.dataset['number']
// (let) is to reassign variables
		let classToApply = selectedAnswer == currentQuestion.answer ? 'correct' :
		  'incorrect'

		if(classToApply === 'correct'){
		  	incrementScore(SCORE_POINTS)
         }

		  selectedChoice.parentElement.classList.add(classToApply)

		  setTimeout (() => {
		  	selectedChoice.parentElement.classList.remove(classToApply)
		  	getNewQuestion()

		  },1000)
	})
})
	incrementScore = num => {
		score +=num
		scoreText.innerText = score
	
	}
	startGame()
