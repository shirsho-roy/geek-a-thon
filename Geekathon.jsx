import firebase from "firebase/compat/app"
import "firebase/compat/auth"
import "firebase/compat/database"
import "firebase/compat/firestore"


const firebaseConfig = {
  apiKey: "AIzaSyApdtnHdclIVF9lteKwtMhGwllUG39JfLA",
  authDomain: "geekathon-eb2eb.firebaseapp.com",
  projectId: "geekathon-eb2eb",
  storageBucket: "geekathon-eb2eb.appspot.com",
  messagingSenderId: "324616733070",
  appId: "1:324616733070:web:380568d1a0920586e3e4df",
  measurementId: "G-Z2T04VV5TH"
};

const db = firebaseApp.firestore();

const auth = firebase.auth();

export {db, auth};

