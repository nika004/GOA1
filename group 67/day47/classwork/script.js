let num = Math.round(Math.random() *50)
console.log(num)



let a = 2
let b = 33
let c = 22
let d = 21
console.log(Math.min(a,b,c,d))



let num1 = Math.round(Math.random() *100)
console.log(num1)


// Math.round() ამრგვალებს რიცხვს მთელამდე
// math.ceil() ამრგვალებს ოღონდ ზემოთ
// Math.floor() მარგვალებს ოღონდ ქვემოთ

//vat არის ძველი მეთოდი ცვლადის შექმნისთვის
//let არის ჩვეულებრივი ცვლადი და შეგიძლია შეცვალო მნიშნელობა
//const არის მუდმივი და მნიშვნელობა არ ეცვლება

const word ="nika"
let ran1 = Math.floor(Math.random() *word.lenght)
console.log(word[ran1])