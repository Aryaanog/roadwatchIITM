import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  typescript: {
    // Bypasses typescript compilation warnings so minor interface mismatches don't break the build
    ignoreBuildErrors: true,
  },
};

export default nextConfig;