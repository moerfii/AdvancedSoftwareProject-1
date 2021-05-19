var chai = require("chai")
    ,chaiHttp = require("chai-http") ;
const { get } = require("superagent");
chai.use(chaiHttp);
var {app} = require("../src/server.js");

const expect = chai.expect;


describe("Checking all requests/responses", () => {


    describe("/listings_location", () => {
        it("returns status 200 for all", (done) => {
           chai.request(app)
           .get("/listing_location")
           .end(function (err, res) {
               expect(res).to.have.status(200);
               done();
           })
        }).timeout(5000)
        it("returns status 200 for id 2539",(done) => {
            chai.request(app)
            .get("/listing_location/2539")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(5000)
        it("returns status 200 for search params",(done) => {
            chai.request(app)
            .get("/listing_location?latitude.ge=0&longitude.le=80&Borough.eq='Harlem'")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(5000)
    })


    describe("/listing_detail", () => {
        it("returns status 200", (done) => {
            chai.request(app)
            .get("/listing_detail")
            .end((err,res) => {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(20000)

        it("returns status 200 for id 2539",(done) => {
            chai.request(app)
            .get("/listing_detail/2539")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(5000)
        it("returns status 200 for search params",(done) => {
            chai.request(app)
            .get("/listing_detail?price.le=100&guests_included.eq=2")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(5000)
    })


    describe("/listing_other", () => {
        it("returns status 200", (done) => {
            chai.request(app)
            .get("/listing_other")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(20000)
        it("returns status 200 for id 2539", (done) => {
            chai.request(app)
            .get("/listing_other/2539")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(5000)
        it("returns status 200 for search params", (done) => {
            chai.request(app)
            .get("/listing_other?square_feet.ge=100")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(5000)
    })


    describe("/listing_reviews", () => {
        it("returns status 200", (done) => {
            chai.request(app)
            .get("/listing_reviews")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(20000)
        it("returns status 200 for id 2539", (done) => {
            chai.request(app)
            .get("/listing_reviews/2539")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(5000)
        it("returns status 200 for search params", (done) => {
            chai.request(app)
            .get("/listing_reviews?review_scores_cleanliness.ge=5")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(5000)
    })


    describe("/host", () => {
        it("returns status 200", (done) => {
            chai.request(app)
            .get("/host")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(20000)
        it("returns status 200 for id 2787", (done) => {
            chai.request(app)
            .get("/host/2787")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(5000)
        it("returns status 200 for search params", (done) => {
            chai.request(app)
            .get("/host?host_is_superhost.eq='t'&host_total_listings_count.eq=6")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(5000)
    })


    describe("/reviews", () => {
        it("returns status 200 for id 17857", (done) => {
            chai.request(app)
            .get("/reviews/17857")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(5000)

        it("returns status 200 for search params", (done) => {
            chai.request(app)
            .get("/reviews?listing_id.eq=2595")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(5000)
    })


    describe("/village_category", () => {
        it("returns status 200", (done) => {
            chai.request(app)
            .get("/village_category")
            .end(function (err,res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(5000)

        it("returns status 200 for search params", (done) => {
            chai.request(app)
            .get("/village_category?category.eq='Food'")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(5000)

        it("returns status 200 for IN operator", (done) => {
            chai.request(app)
            .get("/village_category?category.in[]=Food&category.in[]=Nightlife")
            .end(function(err,res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(5000)
    })


    describe("/search_address", () => {
        
        it("returns status 200", (done) => {
            chai.request(app)
            .get("/search_address?location=300%20Jay%20St,%20Brooklyn,%20NY%2011201,%20United%20States")
            .end(function (err, res) {
                expect(res).to.have.status(200);
                done();
            })
        }).timeout(20000)
    })


    describe("/village_category as input for /listing_location", ()=>{
        it("returns status 200", (done) => {
            chai.request(app)
            .get("/village_category?category.eq='Food'")
            .end(function (err,res) {
                var param = res.body[0][0];
                chai.request(app)
                .get(`/listing_location?village.eq='${param}'`)
                .end(function(err,res) {
                    expect(res).to.have.status(200);
                    done();
                })
            })
        })
    })
})