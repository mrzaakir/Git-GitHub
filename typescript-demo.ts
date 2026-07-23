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
