import React from 'react';
import ReactDOM from 'react-dom';
import { createBrowserHistory } from "history";
import { Router, Route, Switch } from "react-router";
import Front from "./Front.js";

var hist = createBrowserHistory();

ReactDOM.render(<Router history={hist}>
    <Switch>
      <Route path="/" component={Front} />
    </Switch>
  </Router>,
  document.getElementById("root"));
