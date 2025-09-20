import { useState } from "react";
import { Link } from "react-router-dom";
function Login(){
    const [name,setName]=useState("");
    const [password,setPassword]=useState("");

    const [message, setMessage] = useState("");
    const handleSubmit = async (e) => {
        e.preventDefault();
        setMessage("");
        try {
            const res = await fetch("http://localhost:8000/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ email: name, password })
            });
            const data = await res.json();
            if (res.ok) {
                setMessage(data.msg);
            } else {
                setMessage(data.detail || "Login failed");
            }
        } catch (err) {
            setMessage("Network error");
        }
    }

 function NameChange(e){
        setName(e.target.value);
 }
    function PasswordChange(e) {
        setPassword(e.target.value);
    }



    return (
        <>
            <div>
                <form onSubmit={handleSubmit}>
                    <h1>LOGIN</h1>
                    <input value={name} type="email" placeholder="email" onChange={NameChange} />
                    <br />
                    <input value={password} type="password" placeholder="password" onChange={PasswordChange} />
                    <div>
                        <button type="submit">Login</button>
                    </div>
                    {message && <p>{message}</p>}
                    <p>
                        Don't have an account ? <Link to="/register">Register</Link>
                    </p>
                </form>
            </div>
        </>
    );
}
export default Login;