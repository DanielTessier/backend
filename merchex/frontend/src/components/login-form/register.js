import ImgLogin from "../../assets/img-login.jpeg"

import CSRFToken from 'csrftoken';

export default function Register() {
  return <div>
    <div className="container">
      <div className="header">Entrez dans l'aventure</div>

      <form method='post'>
      <div className="content">
        <div className="image">
          <img alt="img-rpg" src={ImgLogin} />
        </div>
        <div className="form">
          <div className="form-group">
            <label htmlFor="username">Username</label>
            <input type="text" 
                  required="required" 
                  name="username" 
                  placeholder="Enter a username" />
          </div>

          <div className="form-group">
            <CSRFToken />
            <label htmlFor="email">Email</label>
            <input type="email" 
                  required="required" 
                  name="email" 
                  placeholder="Enter an email" />
            <label htmlFor="password">Password</label>
            <input type="text" 
                  required="required" 
                  name="password" 
                  placeholder="Enter a password" />
          </div>

        </div>
      </div>
      <div className="footer">
        <button type="submit">Send</button> <br /> <br />
        <button type="submit" className="btn"> 
              <a href="http://127.0.0.1:8000/page_daccueil/">Register</a> 
        </button>
      </div>
      </form>
    </div>
  </div>
}