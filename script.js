const API = 'http://localhost:5000/api';

async function classify() {
  const text = document.getElementById("email").value;
  const res = await fetch(API + "/classify", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({text})
  });
  const data = await res.json();
  document.getElementById("result").innerText =
    data.is_spam ? "🚫 Spam" : "✅ Not Spam";
}
