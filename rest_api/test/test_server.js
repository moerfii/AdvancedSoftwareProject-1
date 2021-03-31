var chai = require("chai")
    ,chaiHttp = require("chai-http") ;
const { get } = require("superagent");
chai.use(chaiHttp);
var {app} = require("../src/server.js");

const expect = chai.expect;


describe("Checking all requests/responses", () => {
    describe("Get all listings (/listings)", () => {
        it("returns status 200", (done) => {

           chai.request(app)
           .get("/listings")
           .end(function (err, res) {
               expect(res).to.have.status(200);
               done();
           })
        })
    })
    describe("Get location data of all reviews", () => {
        it("returns status 200", (done) => {
            chai.request(app)
            .get("/listings/location")
            .end((err,res) => {
                expect(res).to.have.status(200);
                done();
            })
        })
    })
    describe("get listing #2539 (/listing/2539)", () => {
        it("returns status 200", (done) => {
            chai.request(app)
            .get("/listing/2539")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        })
    })
    describe("get all reviews of listing id #2539 (/listing/2539/reviews)", () => {
        it("returns status 200", (done) => {
            chai.request(app)
            .get("/listing/2539/reviews")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            }).timeout(5000)
        })
    })
    describe("get review #55688172 of listing  #2539 (/listing/2539/reviews/55688172)", () => {
        it("returns status 200", (done) => {
            chai.request(app)
            .get("/listing/2539/review/55688172")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        })
    })
})