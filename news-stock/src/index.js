import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import { createBrowserHistory } from "history";
import { Router, Route, Switch } from "react-router";
import Front from "./Front.js";
import SearchRes from "./SearchRes.js";

var hist = createBrowserHistory();

ReactDOM.render(<Router history={hist}>
    <Switch>
      <Route path="/Search" component={SearchRes} />
      <Route path="/" component={Front} />
    </Switch>
  </Router>,
  document.getElementById("root"));
