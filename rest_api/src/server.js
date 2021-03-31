const dotenv = require('dotenv'); //load .env variables
dotenv.config();

const express = require("express");
const { Pool } = require("pg");
const cors = require("cors");
const { query } = require("express");

PORT = 8888

const app = express();
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


/*
overview site
*/
app.get(
    "/",
    (req,res) => {
        res.sendFile("index.html",{root: __dirname})
    })
/*
Returns all listings
*/
app.get(
    "/listings",
    (req,res) => {
        pool.query(
            "SELECT * FROM listing;",
            (error,result) => {
                if(error) {
                    console.log(error)
                    res.status(500).send();
                } else {
                    console.log(result.rows)
                    res.status(200).send(result.rows);
                }
            }
        )
    }
)

/*
returns locations of all listings
*/
app.get(
    "/listings/location",
    (req,res) => {
        var lat1 = req.query.lat1 ? Number(req.query.lat1) : -180
        var lat2 = req.query.lat2 ? Number(req.query.lat2) :  180
        var lon1 = req.query.lon1 ? Number(req.query.lon1) : -180
        var lon2 = req.query.lon2 ? Number(req.query.lon2) :  180
        pool.query(
            `SELECT id, longitude, latitude
             FROM listing
             WHERE longitude >= $1 AND longitude <= $2
             AND latitude >= $3 AND latitude <= $4;`,
             [lon1, lon2, lat1, lat2],
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
Returns specific listing
*/
app.get(
    "/listing/:id",
    (req,res) => {
        pool.query(
            "SELECT * FROM listing WHERE id=$1",
            [req.params.id],
            (error,result) => {
                if(error) {
                    console.log(error)
                    res.status(500).send()
                } else {
                    res.status(200).send(result.rows);
                }
            }
        )
    })


/*
returns reviews for listing id
*/
app.get(
    "/listing/:id/reviews",
    (req,res) => {
        pool.query(
            "SELECT * FROM review WHERE listing_id=$1",
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


/*
returns specific review for specific listing
*/
app.get(
    "/listing/:id/review/:review_id",
    (req,res) => {
        pool.query(
            "SELECT * FROM review WHERE listing_id=$1 AND review_id=$2",
            [req.params.id, req.params.review_id],
            (error,result) => {
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
