import React from 'react';
import { render } from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css';

import store from './app/store';
import App from './app/app';

const el = document.createElement('div');
el.style.height = '100%';
document.body.appendChild(el);

render(
  <App store={store} />,
  el,
);
