<template>
  <div class="update-post">
    <h2>Edit Post</h2>
    <form @submit.prevent="updatePost">
      <div>
        <label for="title">Title:</label>
        <input id="title" v-model="post.title" type="text" required />
      </div>
      <div>
        <label for="content">Content:</label>
        <textarea id="content" v-model="post.content" required></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Save</button>
    </form>
  </div>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      post: {
        title: "",
        content: "",
      },
    };
  },
  created() {
    const postId = this.$route.params.id;
    axios
      .get(`http://localhost:8000/blog/api/${postId}/`)
      .then(({ data }) => {
        this.post = data;
      })
      .catch((error) => {
        console.error("Error fetching post:", error);
      });
  },
  methods: {
    updatePost() {
      axios
        .put(
          `http://localhost:8000/blog/api/update/${this.post.id}/`,
          this.post
        )
        .then(() => {
          alert("Post updated successfully!");
          this.$router.push(`/post/${this.post.id}`); // 상세 페이지로 리다이렉트
        })
        .catch((error) => {
          console.error("Error updating post:", error);
          alert("Failed to update post.");
        });
    },
  },
};
</script>
