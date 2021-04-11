const dotenv = require('dotenv'); //load .env variables
dotenv.config();

const express = require("express");
const { Pool } = require("pg");
const cors = require("cors");
const axios = require("axios")

const PORT = process.env.PORT

const app = express();
app.disable('x-powered-by');
app.use( express.json());   //only needed if we have POST requests
app.use(cors());            //needed to allow cors
//to check on travis

const pool = new Pool({
    host: process.env.DB_HOST,
    port: process.env.DB_PORT,
    database: process.env.DB_NAME,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD  
})

const operators = {
    "eq":"=",
    "ge":">=",
    "le":"<="
}


function buildQuery(queryString,query,setAND=false) {
    /*  Adds WHERE clauses to input queryString, cleans query params
        Inputs: - queryString: A string with a query
                - query: reqest query dict
                - count: Set to > 0 if there is already a WHERE constraint 
    */
    
    Object.entries(query).forEach(([key, value]) => {
        if(setAND) queryString += " AND ";
        else {
            queryString += " WHERE ";
            setAND=true;
        }
        key = key.split(".");
        if(key.length!=2) {
            return;
        }

        if(!(key[1] in operators)) {
            return;
        }
        const colName = key[0].replace(/[";]/g,"")
        const operator = operators[key[1]];
        const val = value.replace(/[";]/g,"")
        queryString += `${colName} ${operator} ${val}`
     });
     return queryString
}
/*
overview site
*/
app.get(
    "/",
    (req,res) => {
        res.sendFile("index.html",{root: __dirname})
    })


/*
returns locations of all listings
*/
app.get(
    "/listing_location",
    (req,res) => {
        var query = "SELECT * FROM listing_location"
        query = buildQuery(query,req.query)
        pool.query(
            query,
            (error, result) => {
                if(error) {
                    console.log(error);
                    res.status(500).send();
                } else {
                    res.status(200).send(result.rows);
                }
            }
        )
    }
)
app.get(
    "/listing_location/:id",
    (req,res) => {
        var query = "SELECT * FROM listing_location WHERE id=$1"
        pool.query(
            query,
            [req.params.id],
            (error, result) => {
                if(error) {
                    console.log(error);
                    res.status(500).send();
                } else {
                    res.status(200).send(result.rows);
                }
            }
        )
    }
)
app.get(
    "/listing_detail",
    (req,res) => {
        var query = "SELECT * FROM listing_detail"
        query = buildQuery(query,req.query)
        pool.query(
            query,
            (error, result) => {
                if(error) {
                    console.log(error);
                    res.status(500).send();
                } else {
                    res.status(200).send(result.rows);
                }
            }
        )
    }
)
app.get(
    "/listing_detail/:id",
    (req,res) => {
        var query = "SELECT * FROM listing_detail WHERE id=$1"
        query = buildQuery(query,req.query)
        pool.query(
            query,
            [req.params.id],
            (error, result) => {
                if(error) {
                    console.log(error);
                    res.status(500).send();
                } else {
                    res.status(200).send(result.rows);
                }
            }
        )
    }
)

app.get(
    "/listing_other",
    (req,res) => {
        var query = "SELECT * FROM listing_other"
        query = buildQuery(query,req.query)
        pool.query(
            query,
            (error, result) => {
                if(error) {
                    console.log(error);
                    res.status(500).send();
                } else {
                    res.status(200).send(result.rows);
                }
            }
        )
    }
)

app.get(
    "/listing_other/:id",
    (req,res) => {
        var query = "SELECT * FROM listing_other WHERE id=$1"
        pool.query(
            query,
            [req.params.id],
            (error, result) => {
                if(error) {
                    console.log(error);
                    res.status(500).send();
                } else {
                    res.status(200).send(result.rows);
                }
            }
        )
    }
)
app.get(
    "/listing_reviews",
    (req,res) => {
        var query = "SELECT * FROM listing_reviews"
        query = buildQuery(query,req.query)
        pool.query(
            query,
            (error, result) => {
                if(error) {
                    console.log(error);
                    res.status(500).send();
                } else {
                    res.status(200).send(result.rows);
                }
            }
        )
    }
)
app.get(
    "/listing_reviews/:id",
    (req,res) => {
        var query = "SELECT * FROM listing_reviews WHERE id=$1"
        query = buildQuery(query,req.query)
        pool.query(
            query,
            [req.params.id],
            (error, result) => {
                if(error) {
                    console.log(error);
                    res.status(500).send();
                } else {
                    res.status(200).send(result.rows);
                }
            }
        )
    }
)
app.get(
    "/host",
    (req,res) => {
        var query = "SELECT * FROM host"
        query = buildQuery(query,req.query)
        pool.query(
            query,
            (error, result) => {
                if(error) {
                    console.log(error);
                    res.status(500).send();
                } else {
                    res.status(200).send(result.rows);
                }
            }
        )
    }
)
app.get(
    "/host/:id",
    (req,res) => {
        var query = "SELECT * FROM host WHERE host_id=$1"
        query = buildQuery(query,req.query)
        pool.query(
            query,
            [req.params.id],
            (error, result) => {
                if(error) {
                    console.log(error);
                    res.status(500).send();
                } else {
                    res.status(200).send(result.rows);
                }
            }
        )
    }
)

/*
returns reviews for listing id
*/
app.get(
    "/reviews",
    (req,res) => {
        var query = buildQuery(`SELECT * FROM review`,req.query)
        
        pool.query(
            query,
            (error, result) => {
                if(error) {
                    console.log(error)
                    res.status(500).send()
                } else {
                    res.status(200).send(result.rows);
                }
            }
        )
    }
)

app.get(
    "/reviews/:id",
    (req,res) => {
        var query = `SELECT * FROM review WHERE id=$1`
        
        pool.query(
            query,
            [req.params.id],
            (error, result) => {
                if(error) {
                    console.log(error)
                    res.status(500).send()
                } else {
                    res.status(200).send(result.rows);
                }
            }
        )
    }
)


app.get(
    "/search_address",
    async (req,res) => {
        await axios({
            method:"GET",
            url:`http://mapquestapi.com/geocoding/v1/address?key=zleTvt8GJJlclq1BzheL9nXg05bpodk6&location=${req.query['location']}`,
        }).then((result) => {
                res.status(200).send(result.data['results'][0]['locations'][0]['latLng'])
            }
        )
    }
)

if(require.main === module) {
    app.listen(
        PORT,
        () => {
            console.log(`serving from port ${PORT}`);
        }
    )
} else {
    exports.app = app;
}
