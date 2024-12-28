<template>
  <div>
    <h1>Dashboard</h1>
    <!-- Create Blog Post Button -->
    <router-link to="/create" class="create-post-button">
      Create Blog Post
    </router-link>

    <template v-if="!isLoading">
      <div v-for="post in posts" :key="post.id">
        <!-- Router link wrapping PostCard -->
        <router-link :to="`/post/${post.id}`" class="post-link">
          <PostCard :post="post" />
        </router-link>
      </div>
    </template>
    <p v-else>Loading posts</p>

    <!-- Pagination Controls -->
    <div class="pagination" v-if="!isLoading && totalPages > 1">
      <button
        class="pagination-button"
        :disabled="!previous"
        @click="fetchPosts(previous)"
      >
        Previous
      </button>
      <span>Page {{ currentPage }} of {{ totalPages }}</span>
      <button
        class="pagination-button"
        :disabled="!next"
        @click="fetchPosts(next)"
      >
        Next
      </button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import PostCard from "../components/PostCard";

export default {
  components: { PostCard },
  data() {
    return {
      isLoading: true,
      posts: [],
      next: null,
      previous: null,
      currentPage: 1,
      totalPages: 1,
    };
  },
  methods: {
    fetchPosts(page = 1) {
      const url = `//localhost:8000/blog/api?page=${page}`;
      this.isLoading = true;
      axios
        .get(url)
        .then(({ data }) => {
          this.posts = data.results || [];
          this.next = data.next || null; // 다음 페이지 번호
          this.previous = data.previous || null; // 이전 페이지 번호
          this.currentPage = data.current || 1; // 현재 페이지
          this.totalPages = data.total_pages || 1; // 전체 페이지 수
        })
        .catch((error) => {
          console.error("Error fetching posts:", error);
          this.posts = [];
          this.next = null;
          this.previous = null;
          this.currentPage = 1;
          this.totalPages = 1;
        })
        .finally(() => {
          this.isLoading = false;
        });
    },
  },
  created() {
    this.fetchPosts();
  },
};
</script>

<style>
/* Style for the Create Post Button */
.create-post-button {
  display: inline-block;
  margin-bottom: 20px;
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  text-align: center;
}
.create-post-button:hover {
  background-color: #0056b3;
}

/* Style for Post Link */
.post-link {
  text-decoration: none;
  color: inherit;
  display: block;
  margin-bottom: 15px;
}

/* Pagination Style */
.pagination {
  margin-top: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
}
.pagination-button {
  margin: 0 10px;
  padding: 5px 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}
.pagination-button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>
