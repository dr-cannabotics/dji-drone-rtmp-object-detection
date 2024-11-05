 const NodeMediaServer = require('node-media-server');

const config = {
  logType: 3, // Log level: 3 is for errors only
  rtmp: {
    port: 1935,
    chunk_size: 4096,   // Smaller chunk size for lower latency
    gop_cache: false,   // Disable GOP cache to reduce latency
    ping: 10,           // Lower ping interval
    ping_timeout: 30    // Lower ping timeout
  }
};

const nms = new NodeMediaServer(config);
nms.run();
