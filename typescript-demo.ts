export type User = {
  id: number;
  name: string;
  score: number;
  active: boolean;
};

export const normalizeName = (name: string) => name.trim().toLowerCase();
export const greet = (name: string) => `Hello ${name}!`;
export const formatUser = (user: User) => `${user.name}: ${user.score}`;
export const isValidUser = (user: User) => user.active && user.name.trim().length > 0 && user.score >= 0;
export const bonusPoints = (score: number) => score + 10;
export const averageScore = (scores: number[]) => scores.length === 0 ? 0 : scores.reduce((sum, value) => sum + value, 0) / scores.length;
export const summary = (users: User[]) => users.map((user) => `${user.name} => ${user.score}`).join("\n");
export const totalScore = (users: User[]) => users.reduce((sum, user) => sum + user.score, 0);
export const scoreGrade = (score: number) => score >= 90 ? "A" : score >= 70 ? "B" : "C";
export const showResult = (label: string, value: string) => `${label}: ${value}`;
export const demoUsers: User[] = [
  { id: 1, name: 'Amina', score: 92, active: true },
  { id: 2, name: 'Bilal', score: 78, active: true },
  { id: 3, name: 'Sara', score: 88, active: true }
];
export const getTopUser = (users: User[]) => [...users].sort((a, b) => b.score - a.score)[0];
export const topThreeUsers = (users: User[]) => [...users].sort((a, b) => b.score - a.score).slice(0, 3);
export const printSummary = (users: User[]) => console.log(summary(users));
export const runDemo = () => {
  const top = getTopUser(demoUsers);
  const leaderboard = topThreeUsers(demoUsers).map((user) => `${user.name} (${scoreGrade(user.score)})`).join(', ');
  console.log(greet(top.name));
  console.log(showResult('Top score', String(top.score)));
  console.log(showResult('Average', String(averageScore(demoUsers.map((user) => user.score)))));
  console.log(showResult('Leaderboard', leaderboard));
};

runDemo();

// Additional demo operations
const testUser: User = { id: 4, name: 'Alex', score: 85, active: true };
console.log(showResult('Test User', formatUser(testUser)));
console.log(showResult('Valid', String(isValidUser(testUser))));
