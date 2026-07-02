#!/usr/bin/env python3
"""
YouTube API Music - Telegram Music Bot Usage Examples

This file demonstrates how to use the YouTube Music API
with a Telegram bot.

Author: Your Name
License: MIT
"""

import requests
from typing import Dict, List, Optional


class YouTubeMusicAPI:
    """Client for the YouTube Music API."""

    def __init__(
        self,
        api_key: str,
        base_url: str = "http://localhost:8000"
    ):
        """
        Initialize the API client.

        Args:
            api_key: Your API key for authentication
            base_url: Base URL of the API service
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {"X-API-Key": api_key}

    def _make_request(
        self,
        endpoint: str,
        params: Optional[Dict] = None
    ) -> Dict:
        """
        Make a request to the API.

        Args:
            endpoint: API endpoint to call
            params: Query parameters

        Returns:
            JSON response from the API
        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = requests.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()

    def health_check(self) -> Dict:
        """Check API health status."""
        return self._make_request("/health")

    def search(
        self,
        query: str,
        max_results: int = 10,
        platform: str = "youtube"
    ) -> List[Dict]:
        """
        Search for videos.

        Args:
            query: Search query
            max_results: Maximum number of results
            platform: Platform to search (youtube, soundcloud)

        Returns:
            List of video results
        """
        result = self._make_request(
            "/search",
            params={
                "q": query,
                "max_results": max_results,
                "platform": platform
            }
        )
        return result.get("results", [])

    def get_video_info(self, video_id: str, platform: str = "youtube") -> Optional[Dict]:
        """
        Get detailed video information.

        Args:
            video_id: YouTube video ID or URL
            platform: Platform (youtube, soundcloud)

        Returns:
            Video information or None
        """
        result = self._make_request(
            "/video",
            params={"id": video_id, "platform": platform}
        )
        return result.get("video")

    def get_audio_stream(self, video_id: str, platform: str = "youtube") -> Optional[Dict]:
        """
        Get audio stream URL.

        Args:
            video_id: YouTube video ID or URL
            platform: Platform (youtube, soundcloud)

        Returns:
            Audio stream information or None
        """
        result = self._make_request(
            "/audio",
            params={"id": video_id, "platform": platform}
        )
        return result.get("audio")

    def get_stream_url(
        self,
        video_id: str,
        format: Optional[str] = None,
        platform: str = "youtube"
    ) -> Optional[Dict]:
        """
        Get playable stream URL.

        Args:
            video_id: YouTube video ID or URL
            format: Custom format string
            platform: Platform (youtube, soundcloud)

        Returns:
            Stream information or None
        """
        params = {"id": video_id, "platform": platform}
        if format:
            params["format"] = format
        result = self._make_request("/stream", params=params)
        return result.get("stream")

    def get_related_videos(self, video_id: str) -> List[Dict]:
        """
        Get related videos.

        Args:
            video_id: YouTube video ID

        Returns:
            List of related videos
        """
        result = self._make_request("/related", params={"id": video_id})
        return result.get("related", [])

    def search_lyrics(self, query: str) -> Optional[str]:
        """
        Search for lyrics.

        Args:
            query: Song name or artist + song name

        Returns:
            Lyrics or None
        """
        result = self._make_request("/lyrics", params={"q": query})
        return result.get("lyrics")

    def get_download_info(
        self,
        video_id: str,
        format: Optional[str] = None,
        type: Optional[str] = None,
        platform: str = "youtube"
    ) -> Optional[Dict]:
        """
        Get download information.

        Args:
            video_id: YouTube video ID or URL
            format: Custom format string
            type: Type (audio or video)
            platform: Platform (youtube, soundcloud)

        Returns:
            Download information or None
        """
        params = {"id": video_id, "platform": platform}
        if format:
            params["format"] = format
        if type:
            params["type"] = type
        result = self._make_request("/download", params=params)
        return result.get("download")


def main():
    """Example usage of the YouTubeMusicAPI."""
    # Initialize the API client
    API_KEY = os.getenv("YT_API_KEY")
    API_URL = os.getenv("YTPROXY_URL")

    api = YouTubeMusicAPI(api_key=API_KEY, base_url=API_URL)

    print("=== YouTube API Music - Example Usage ===\n")

    # Example 1: Health Check
    print("1. Health Check:")
    try:
        health = api.health_check()
        print(f"   Status: {health.get('status')}")
        print(f"   Version: {health.get('version')}")
        print(f"   yt-dlp: {health.get('ytdlp_version')}\n")
    except Exception as e:
        print(f"   Error: {e}\n")

    # Example 2: Search for a song
    print("2. Search for a song:")
    try:
        results = api.search("never gonna give you up", max_results=3)
        for idx, video in enumerate(results, 1):
            print(f"   {idx}. {video.get('title')} ({video.get('id')})")
        print()
    except Exception as e:
        print(f"   Error: {e}\n")

    # Example 3: Get audio stream for first result
    if results:
        print("3. Get audio stream:")
        try:
            first_video_id = results[0].get('id')
            audio = api.get_audio_stream(first_video_id)
            if audio:
                print(f"   Title: {audio.get('title')}")
                print(f"   URL: {audio.get('url')}")
                print(f"   Format: {audio.get('format')}")
                print(f"   Size: {audio.get('filesize', 'N/A')} bytes\n")
        except Exception as e:
            print(f"   Error: {e}\n")


if __name__ == "__main__":
    main()

