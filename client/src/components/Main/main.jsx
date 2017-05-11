import React from 'react';
import { observer } from 'mobx-react';
import './main.scss';

function Main({ store }) {
  return (
    <section className="redBackground" id="main">
      <h1 onClick={store.login}>Hello world</h1>
    </section>
  );
}

export default observer(Main);
