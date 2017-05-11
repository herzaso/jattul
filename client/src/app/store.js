import { observable, action } from 'mobx';
import { login } from '../actions';

class Store {
  @observable timer = 0;

  @action login = (event) => {
    event.preventDefault();
    alert(event);
    login('1', '1').then(() => {
      document.querySelector('#app').scrollTop += document.querySelector('#login').offsetHeight;
    });
  };
  @action forgot = () => { alert('It would be a nice feature, but it\'s not implemented yet'); };
}

export default new Store();
