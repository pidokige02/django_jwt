<template>
  <div class="post-create-container">
    <h1>Create a New Post</h1>
    <form @submit.prevent="createPost" novalidate>
      <div class="form-group">
        <label for="title">Title</label>
        <input
          type="text"
          id="title"
          v-model="title"
          class="form-control"
          required
        />
      </div>
      <div class="form-group">
        <label for="content">Content</label>
        <textarea
          id="content"
          v-model="content"
          class="form-control"
          rows="5"
          required
        ></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Create Post</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      title: "",
      content: "",
    };
  },
  methods: {
    async createPost() {
      try {
        const response = await axios.post("//localhost:8000/blog/api/create/", {
          title: this.title,
          content: this.content,
        });
        alert("Post created successfully!");
        this.$router.push(`/post/${response.data.id}`);
      } catch (error) {
        console.error("Error creating post:", error.response.data);
        alert("Failed to create the post. Please try again.");
      }
    },
  },
};
</script>

<style>
.post-create-container {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 5px;
  background-color: #f9f9f9;
}
.form-group {
  margin-bottom: 15px;
}
.form-group label {
  display: block;
  margin-bottom: 5px;
}
.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.btn {
  display: inline-block;
  padding: 10px 20px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
.btn:hover {
  background-color: #0056b3;
}
</style>
