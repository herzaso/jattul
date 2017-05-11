import React from 'react';
import { observer } from 'mobx-react';
import Login from '../components/Login/login';
import Main from '../components/Main/main';
import './app.scss';

function App({ store }) {
  return (
    <div id="app">
      <Login store={store} />
      <Main store={store} />
    </div>
  );
}

export default observer(App);
