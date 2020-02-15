import React from 'react';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Title from './Title';
import TrendingDownIcon from '@material-ui/icons/TrendingDown';
import TrendingUpIcon from '@material-ui/icons/TrendingUp';

// Generate Order Data
function createData(id, date, name, shipTo, paymentMethod, res, amount) {
  return { id, date, name, shipTo, paymentMethod, res, amount };
}

const rows = [
  createData(0, '15 Feb, 2019', 'SENSEX', 41257.74, -202.05, false, 0.483),
  createData(1, '15 Feb, 2019', 'NIFTY 50', 12113.45, -61.20, false, 0.504),
  createData(2, '15 Feb, 2019', 'BSE SMALLCAP', 14682.65, -59.07, false, 0.405),
  createData(3, '15 Feb, 2019', 'BSE MIDCAP', 15662.10, -124.66, false, 0.792),
  createData(4, '14 Feb, 2019', 'Dow Jones', 29398.08, -25.23, false, 0.084),
  createData(5, '14 Feb, 2019', 'Nasdaq', 9731.18, +19.21, true, 0.197),
  createData(6, '14 Feb, 2019', 'FTSE', 7409.13, -42.90, false, 0.576),
];

function preventDefault(event) {
  event.preventDefault();
}

const useStyles = makeStyles(theme => ({
  seeMore: {
    marginTop: theme.spacing(3),
  },
}));

export default function Orders() {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Title>Key Market Info</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Date</TableCell>
            <TableCell>Indices</TableCell>
            <TableCell>Price</TableCell>
            <TableCell>Change</TableCell>
            <TableCell align="right">% Change</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map(row => (
            <TableRow key={row.id}>
              <TableCell>{row.date}</TableCell>
              <TableCell>{row.name}</TableCell>
              <TableCell>{row.shipTo}</TableCell>
          <TableCell>{row.paymentMethod}{" "}{(row.res)?(<TrendingUpIcon style={{color: "#2dc937"}} />):(<TrendingDownIcon style={{color:"#cc3232"}}/>)}</TableCell>
              <TableCell align="right">{row.amount}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <div className={classes.seeMore}>
        <Link color="primary" href="#" onClick={preventDefault}>
          See more entries
        </Link>
      </div>
    </React.Fragment>
  );
}
