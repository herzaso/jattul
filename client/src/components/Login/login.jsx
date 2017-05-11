import React from 'react';
import { observer } from 'mobx-react';
import './login.scss';

function Login({ store }) {
  return (
    <section className="blueBackground" id="login">
      <div className="logo container centered">
        <h1 className="text-center">Login</h1>
        <p className="text-center">Go ahead and track your time...</p>
        <form onSubmit={store.login}>
          <div className="form-group has-feedback">
            <input type="text" id="username" className="form-control input-lg shadow" placeholder="Username" />
            <span className="glyphicon glyphicon-user form-control-feedback" aria-hidden="true" />
          </div>
          <div className="form-group has-feedback">
            <input type="password" id="password" className="form-control input-lg shadow" placeholder="Password" />
            <span className="glyphicon glyphicon-lock form-control-feedback" aria-hidden="true" />
          </div>
          <div className="form-group">
            <input type="checkbox" id="remember" /> Keep me logged in
          </div>
          <div className="form-group">
            <button type="submit" className="btn btn-success btn-block shadow">Login</button>
          </div>
          <div className="form-group text-center">
            <a onClick={store.forgot}>Forgot Password?</a>
          </div>
        </form>
      </div>
    </section>
  );
}

export default observer(Login);
