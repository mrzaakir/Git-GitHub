export type User = {
  name: string;
  score: number;
};
export const greet = (name: string) => `Hello ${name}!`;
export const formatUser = (user: User) => `${user.name}: ${user.score}`;
export const isValidUser = (user: User) => user.name.trim().length > 0 && user.score >= 0;
