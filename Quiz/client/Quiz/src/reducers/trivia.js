import * as types from '../actions/types';

const initialState = {
  numberOfQuestions: 1,
  difficulty: 'easy',
  difficultyLevels: ['easy', 'medium', 'hard', 'mix'],
  loadingQuestions: false,
  triviaQuestions: [],
  triviaState: false, // when this state is active trivia view is used
  playerScore: 0
}

export default function triviaReducer(state = initialState, action){
  switch (action.type) {
    case types.FETCH_REQUESTED:
      return {
        ...state,
        loadingQuestions: true
      }
    case types.FETCH_SUCCEEDED:
      return {
        ...state,
        triviaQuestions: action.data,
        loadingQuestions: false,
        triviaState: true,
      }
    case types.FETCH_FAILED:
      return {
        ...state,
        loadingQuestions: false,
      }
    case types.ADD_TO_SCORE:
      return {
        ...state,
        playerScore: state.playerScore + 1
      }
    case types.RESTART_TRIVIA:
      return {
        ...state,
        triviaState: false,
        playerScore: 0
      }
    case types.SELECT_NUMBER_OF_QUESTIONS:
      return {
        ...state,
        numberOfQuestions: action.numberOfQuestions
      }
    case types.SELECT_DIFFICULTY:
      return {
        ...state,
        difficulty: action.difficulty
      }
    default:
      return state;
  }
}