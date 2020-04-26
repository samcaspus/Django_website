const mongoose = require("mongoose");

const blogsScheme = new mongoose.Schema({
    content:{
        type: String,
        required: true,
    }
});


const Blogs = mongoose.model("Blogs",blogsScheme);

module.exports = Blogs