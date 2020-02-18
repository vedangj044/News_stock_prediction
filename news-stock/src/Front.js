import React, { useState , useEffect} from "react";
import Avatar from "@material-ui/core/Avatar";
import CssBaseline from "@material-ui/core/CssBaseline";
import Link from "@material-ui/core/Link";
import Paper from "@material-ui/core/Paper";
import Box from "@material-ui/core/Box";
import Grid from "@material-ui/core/Grid";
import Typography from "@material-ui/core/Typography";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import Chip from "@material-ui/core/Chip";
import frontimg1 from "./img/front1.jpg";
import Zoom from "react-reveal/Zoom";
import InputBase from "@material-ui/core/InputBase";
import IconButton from "@material-ui/core/IconButton";
import SearchIcon from "@material-ui/icons/Search";
import Skeleton from "@material-ui/lab/Skeleton";
import TrendingDownIcon from "@material-ui/icons/TrendingDown";
import TrendingUpIcon from "@material-ui/icons/TrendingUp";
import Cookies from 'universal-cookie';
import axios from 'axios';

function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {"Copyright © "}
      <Link color="inherit" href="https://material-ui.com/">
        Your Website
      </Link>{" "}
      {new Date().getFullYear()}
      {"."}
    </Typography>
  );
}

const useStyles = makeStyles(theme => ({
  root: {
    height: "100vh"
  },
  image: {
    backgroundImage: `url(${frontimg1})`,
    backgroundRepeat: "no-repeat",
    backgroundColor:
      theme.palette.type === "dark"
        ? theme.palette.grey[900]
        : theme.palette.grey[50],
    backgroundSize: "cover",
    backgroundPosition: "center",
    height: "100vh"
  },
  paper: {
    margin: theme.spacing(8, 4),
    display: "flex",
    flexDirection: "column",
    alignItems: "center"
  },
  avatar: {
    margin: theme.spacing(1),
    backgroundColor: theme.palette.secondary.main
  },
  form: {
    width: "100%", // Fix IE 11 issue.
    marginTop: theme.spacing(1)
  },
  submit: {
    margin: theme.spacing(3, 0, 2)
  },
  tfield: {
    padding: "2px 4px",
    display: "flex",
    alignItems: "center",
    width: 500
  },
  input: {
    marginLeft: theme.spacing(1),
    flex: 1
  },
  iconButton: {
    padding: 10
  },
  divider: {
    height: 28,
    margin: 4
  }
}));

export default function Front() {
  var port="192.168.43.48:5000/";
  const cookies = new Cookies();
  const classes = useStyles();

  // let history = useHistory();

  const routeChange = () => {
    let path = `/Dashboard`;
    cookies.set('userId', comp, { path: '/' });
    // history.push(path);
  }

 const [news, setNews] = useState([]);

  const handleDeleteChip = event => {
    var index = comp.indexOf(event.target.value);
    comp.splice(index, 1);
    setComp(comp);
    fetch(`${port}news`, {
      'methods' : 'Post',
      'query' : comp  
    })
    .then(res => res.json())
    .then(res => setNews(res))
    .catch(err => console.error(err));
  };

  const handleClick = () => {
    console.info("You clicked the Chip.");
  };



  const handleEnter = event => {
    if (event.key === "Enter") {
      var compadd = event.target.value;
      if (compadd!=="" && comp.indexOf(compadd)==-1)
      {
      setComp([...comp, compadd]);
      console.log("WIIOSFUI")
        var params = {
          query : 'tesla'
        }
        event.preventDefault();
         axios.post('http://192.168.43.48:5000/news', params)
         .then(res => res.json())
         .then(res => console.log(res))
         .catch(err => console.log(err))
      
      }
    }
  };

  const handleComp = event => {
    var compadd = event.target.value;
    setComp([...comp, compadd]);
  };

  const [loading, setLoad] = useState(false);

  const [comp, setComp] = useState(["Tesla", "Wipro"]);

  const [compgrow, setCompgrow] = useState(true);

  const [comparr, setComparr] = useState([
    { price: true, day:"tuesday"},
    { price: false, day:"mon  day"}
  ]);

  useEffect(() => {
    console.log(comp)
  });


  return (
    <Grid container component="main" className={classes.root}>
      <CssBaseline />
      <Container maxWidth="xl" className={classes.image}>
        <Zoom duration="4000">
          <Typography
            variant="h1"
            align="center"
            style={{
              fontFamily: "varela round",
              color: "#3c3428",
              marginTop: "20%"
            }}
          >
            Famulus
          </Typography>

          <Typography
            variant="h3"
            align="center"
            style={{ fontFamily: "source sans pro", color: "#3c3428" }}
          >
            Your Intelligent Stock Assistant
          </Typography>
        </Zoom>
      </Container>
      <Container maxWidth="sm" style={{ height: "100%" }}>
        <div className={classes.paper}>
          <form className={classes.form} noValidate>
           
            <Paper
              component="form"
              className={classes.tfield}
              style={{ borderRadius: "100px" }}
            >
              <IconButton
                type="submit"
                className={classes.iconButton}
                aria-label="search"
              >
                <SearchIcon />
              </IconButton>
              <InputBase
                className={classes.input}
                placeholder="Search Companies of interest"
                inputProps={{ "aria-label": "search companies" }}
                // onChange={handleComp}
                onKeyPress={handleEnter}
              />
            </Paper>
            {comp.map(comp1 => (
              <Chip
                variant="outlined"
                color="primary"
                avatar={<Avatar>{comp1.charAt(0)}</Avatar>}
                label={comp1}
                onClick={handleClick}
                onDelete={event => handleDeleteChip(event, comp1)}
                style={{ margin: "20px" }}
                value={comp1}
                key={comp1}
              />
            ))}
          </form>
        </div>
        {(loading)?
        (
        <Grid container>
          <Box width={500}>
            <Skeleton variant="rect" width={600} height={400} />
            <Box pt={0.5}>
              <Skeleton />
            </Box>
          </Box>
        </Grid>
        ):
        (<Paper style={{ padding: "30px", width: "600px" }}>
          <Grid container spacing="8">
            <Grid item>
              <Typography variant="h3" style={{ color: "grey" }}>
                Stock Analysis
              </Typography>
            </Grid>
            <Grid item>
              {compgrow ? (
                <TrendingUpIcon
                  style={{ fontSize: "60px", color: "#2dc937" }}
                />
              ) : (
                <TrendingDownIcon
                  style={{ fontSize: "60px", color: "#cc3232" }}
                />
              )}
            </Grid>
          </Grid>

          <Typography variant="h6" color="textSecondary">
            The stock for Tesla is expected to {" "}
            {(compgrow)?
            (<span
              style={{
                fontSize: "35px",
                borderBottom: "7px solid #2dc937",
                fontFamily: "varela round",
                padding: "1px",
                color: "black",
                borderRadius: "3px"
              }}
            >
              Rise
            </span>)
            :(<span style={{fontSize: "35px",borderBottom:"7px solid #cc3232", fontFamily:"varela round", padding:"1px", color:"black",
            borderRadius:"3px"}}>Fall</span>)
}           about <b>0.08%</b> by tommorow, <b>0.41%</b> by next 7 days, <b>0.84%</b> in the next 15 days, <b>2.16%</b> in the next 30 days.
          </Typography>
          <Typography variant="h6" color="textSecondary">
            The stock for Wipro is expected to {" "}
            {(compgrow)?
            (<span
              style={{
                fontSize: "35px",
                borderBottom: "7px solid #2dc937",
                fontFamily: "varela round",
                padding: "1px",
                color: "black",
                borderRadius: "3px"
              }}
            >
              Rise
            </span>)
            :(<span style={{fontSize: "35px",borderBottom:"7px solid #cc3232", fontFamily:"varela round", padding:"1px", color:"black",
            borderRadius:"3px"}}>Fall</span>)
}
          </Typography>
        
        </Paper>)}
        
      </Container>
     
    </Grid>
  );
}
