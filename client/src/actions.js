async function login() {
  const response = await fetch('https://api.github.com');
  const data = await response.json();
  return data;
}

export default login;
