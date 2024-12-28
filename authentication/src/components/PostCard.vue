<template>
  <div class="post-card">
    <div class="post-header">
      <p><strong>Author:</strong> {{ post.author }}</p>
    </div>
    <div class="post-content">
      <p>{{ post.content }}</p>
    </div>
    <div class="post-footer">
      <p><strong>Created At:</strong> {{ formatDate(post.created_at) }}</p>
      <p><strong>Updated At:</strong> {{ formatDate(post.updated_at) }}</p>
      <p v-if="post.published_at"><strong>Published At:</strong> {{ formatDate(post.published_at) }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "PostCard",
  props: {
    post: {
      type: Object,
      required: true,
    },
  },
  methods: {
    formatDate(date) {
      if (!date) return "";
      const options = { year: "numeric", month: "short", day: "numeric" };
      return new Date(date).toLocaleDateString(undefined, options);
    },
  },
};
</script>

<style scoped>
.post-card {
  padding: 1.5em;
  border: 1px solid #ddd;
  border-radius: 8px;
  margin-bottom: 1.5em;
  background-color: #fff;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.post-header {
  font-size: 1.2em;
  margin-bottom: 0.5em;
  color: #333;
}

.post-content {
  font-size: 1em;
  margin-bottom: 1em;
  color: #555;
  line-height: 1.6;
}

.post-footer {
  font-size: 0.9em;
  color: #777;
}

.post-footer p {
  margin: 0.3em 0;
}

.post-card:hover {
  transform: translateY(-2px);
  transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.15);
}
</style>
