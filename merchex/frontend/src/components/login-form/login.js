import ImgLogin from "../../assets/img-login.jpeg"

import CSRFToken from 'csrftoken';

export default function Login() {
  return <div>
    <div className="container">
      <div className="header">Entrez dans l'aventure</div>

      <form method='post'>
      <div className="content">
        <div className="image">
          <img alt="img-rpg" src={ImgLogin} />
        </div>

        <div className="form">
            <CSRFToken />
            <label htmlFor="username">Username</label>
            <input type="text" 
                  required="required" 
                  name="username" 
                  placeholder="Enter a username" />

            <label htmlFor="password">Password</label>
            <input type="password" required="required" name="password" placeholder="Enter a password"/>
        </div>
      </div>
      <div className="footer">
      <button type="submit">Send</button> <br /> <br />
        <button type="submit" className="btn"> 
            <a href="http://127.0.0.1:8000/page_carte_monde/">Login</a> 
        </button>
      </div>
      </form>
    </div>
  </div>
}