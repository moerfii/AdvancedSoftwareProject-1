var chai = require("chai")
    ,chaiHttp = require("chai-http") ;
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
            })
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