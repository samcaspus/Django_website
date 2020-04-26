const express = require("express");
const path = require("path");
const app = express();
const port = 8000;
const db = require("./config/mongoose");
const Blogs = require("./models/blogs");


app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));
app.use(express.urlencoded());


app.get("/", (req, res) => {

    Blogs.find({}, (err, resp) => {
        if (err) {
            console.log("something is wrong");
            return;
        }

        res.render("index", { content: resp });

    });


});

app.get("/delete-blog/:objectid", (req, res) => {
    console.log(req.params.objectid);

    Blogs.findOneAndDelete({ _id: req.params.objectid }, (err) => {
        if (err) {
            console.log("didnt go well");
        }

        return res.redirect("back");
    })


})

app.post("/post-blog", (req, res) => {

    Blogs.create({
        content: req.body.blog,
    }, (err, newContent) => {
        if (err) {
            console.log("fault");
            return;
        }

        console.log(req.body);
        return res.redirect("back");

    });


});



app.listen(port, (err) => {


    if (err) {
        console.log("error");
        return;

    }

    console.log("running on port", 8000);
});