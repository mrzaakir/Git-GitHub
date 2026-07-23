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
