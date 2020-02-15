import React from 'react';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Title from './Title';
import TrendingDownIcon from '@material-ui/icons/TrendingDown';
import TrendingUpIcon from '@material-ui/icons/TrendingUp';
import Grid from "@material-ui/core/Grid";

function preventDefault(event) {
  event.preventDefault();
}

const useStyles = makeStyles({
  depositContext: {
    flex: 1,
  },
});

export default function Deposits() {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Title>Recent Price</Title>
      <Grid container>
        <Grid items>
      <Typography component="p" variant="h4">
        $3,024.00
      </Typography>
      </Grid>
      <Grid items>
        <TrendingUpIcon style={{fontSize:"50px", color:"#2dc937"}}/>
        {/* <TrendingDownIcon style={{fontSize:"50px", color:"#cc3232"}}/> */}
      </Grid>
      </Grid>
      <Typography color="textSecondary" className={classes.depositContext}>
        on 14 Feb, 2020
      </Typography>
      <div>
        <Link color="primary" href="#" onClick={preventDefault}>
          Explore
        </Link>
      </div>
    </React.Fragment>
  );
}
