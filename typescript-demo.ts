export type User = {
  name: string;
  score: number;
};
export const greet = (name: string) => `Hello ${name}!`;
export const formatUser = (user: User) => `${user.name}: ${user.score}`;
export const isValidUser = (user: User) => user.name.trim().length > 0 && user.score >= 0;
export const bonusPoints = (score: number) => score + 10;
export const averageScore = (scores: number[]) => scores.reduce((sum, value) => sum + value, 0) / scores.length;
export const summary = (users: User[]) => users.map((user) => `${user.name} => ${user.score}`).join("\n");
export const totalScore = (users: User[]) => users.reduce((sum, user) => sum + user.score, 0);
export const rankUser = (user: User) => user.score >= 90 ? "A" : user.score >= 70 ? "B" : "C";
export const showResult = (label: string, value: string) => `${label}: ${value}`;
export const demoUsers: User[] = [ { name: "Amina", score: 92 }, { name: "Bilal", score: 78 }, { name: "Sara", score: 88 } ];
export const getTopUser = (users: User[]) => users.sort((a, b) => b.score - a.score)[0];
export const printSummary = (users: User[]) => console.log(summary(users));
