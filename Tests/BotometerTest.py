# Library imports
import requests
import tweepy
import botometer
import os
from dotenv import load_dotenv


#Load keys to access API
load_dotenv()


# Test 1 - Testing if the correct data structure returns after API call

url = "https://botometer-pro.p.rapidapi.com/4/check_account"

payload = {
	"mentions": [
		{
			"contributors": None,
			"coordinates": None,
			"created_at": "Fri Aug 07 11:26:56 +0000 2020",
			"entities": {
				"hashtags": [],
				"symbols": [],
				"urls": [],
				"user_mentions": [
					{
						"id": 11330,
						"id_str": "11330",
						"indices": [3, 11],
						"name": "test user 1",
						"screen_name": "screen_name"
					}
				]
			},
			"favorite_count": 0,
			"favorited": False,
			"geo": None,
			"id": 1291697,
			"id_str": "1291697",
			"in_reply_to_screen_name": None,
			"in_reply_to_status_id": None,
			"in_reply_to_status_id_str": None,
			"in_reply_to_user_id": None,
			"in_reply_to_user_id_str": None,
			"is_quote_status": False,
			"lang": "en",
			"metadata": {
				"iso_language_code": "en",
				"result_type": "recent"
			},
			"place": None,
			"retweet_count": 14,
			"retweeted": False,
			"retweeted_status": {
				"contributors": None,
				"coordinates": None,
				"created_at": "Mon Jul 20 16:03:30 +0000 2020",
				"entities": {
					"hashtags": [],
					"symbols": [],
					"urls": [],
					"user_mentions": []
				},
				"favorite_count": 35,
				"favorited": False,
				"geo": None,
				"id": 128524,
				"id_str": "128524",
				"in_reply_to_screen_name": None,
				"in_reply_to_status_id": None,
				"in_reply_to_status_id_str": None,
				"in_reply_to_user_id": None,
				"in_reply_to_user_id_str": None,
				"is_quote_status": False,
				"lang": "en",
				"metadata": {
					"iso_language_code": "en",
					"result_type": "recent"
				},
				"place": None,
				"possibly_sensitive": False,
				"retweet_count": 14,
				"retweeted": False,
				"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
				"text": "orignial tweet",
				"truncated": True,
				"user": {
					"contributors_enabled": False,
					"created_at": "Mon May 27 17:57:42 +0000 2019",
					"default_profile": True,
					"default_profile_image": False,
					"description": "description",
					"entities": {},
					"favourites_count": 754,
					"follow_request_sent": False,
					"followers_count": 130,
					"following": False,
					"friends_count": 295,
					"geo_enabled": False,
					"has_extended_profile": True,
					"id": 11330,
					"id_str": "11330",
					"is_translation_enabled": False,
					"is_translator": False,
					"lang": None,
					"listed_count": 3,
					"location": "location",
					"name": "test user 1",
					"notifications": False,
					"profile_background_color": "F5F8FA",
					"profile_background_image_url": None,
					"profile_background_image_url_https": None,
					"profile_background_tile": False,
					"profile_banner_url": None,
					"profile_image_url": None,
					"profile_image_url_https": None,
					"profile_link_color": "1DA1F2",
					"profile_sidebar_border_color": "C0DEED",
					"profile_sidebar_fill_color": "DDEEF6",
					"profile_text_color": "333333",
					"profile_use_background_image": True,
					"protected": False,
					"screen_name": "screen_name",
					"statuses_count": 283,
					"time_zone": None,
					"translator_type": "none",
					"url": None,
					"utc_offset": None,
					"verified": False
				}
			},
			"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
			"text": "RT @test_screen_name: test tweet",
			"truncated": False,
			"user": {
				"contributors_enabled": False,
				"created_at": "Fri Jan 28 02:42:39 +0000 2011",
				"default_profile": True,
				"default_profile_image": False,
				"description": "",
				"entities": {"description": {"urls": []}},
				"favourites_count": 5756,
				"follow_request_sent": False,
				"followers_count": 31,
				"following": False,
				"friends_count": 260,
				"geo_enabled": True,
				"has_extended_profile": False,
				"id": 24391,
				"id_str": "24391",
				"is_translation_enabled": False,
				"is_translator": False,
				"lang": None,
				"listed_count": 0,
				"location": "location",
				"name": "test user 2",
				"notifications": False,
				"profile_background_color": "C0DEED",
				"profile_background_image_url": None,
				"profile_background_image_url_https": None,
				"profile_background_tile": False,
				"profile_image_url": None,
				"profile_image_url_https": None,
				"profile_link_color": "1DA1F2",
				"profile_sidebar_border_color": "C0DEED",
				"profile_sidebar_fill_color": "DDEEF6",
				"profile_text_color": "333333",
				"profile_use_background_image": True,
				"protected": False,
				"screen_name": "test_screen_name_2",
				"statuses_count": 351,
				"time_zone": None,
				"translator_type": "none",
				"url": None,
				"utc_offset": None,
				"verified": False
			}
		}
	],
	"timeline": [
		{
			"contributors": None,
			"coordinates": None,
			"created_at": "Fri Aug 07 14:26:36 +0000 2020",
			"entities": {
				"hashtags": [],
				"symbols": [],
				"urls": [],
				"user_mentions": [
					{
						"id": 2584,
						"id_str": "2584",
						"indices": [0, 12],
						"name": "mentined user",
						"screen_name": "mentioned_user"
					}
				]
			},
			"favorite_count": 0,
			"favorited": False,
			"geo": None,
			"id": 12917,
			"id_str": "12917",
			"in_reply_to_screen_name": "mentioned_user",
			"in_reply_to_status_id": 1291741,
			"in_reply_to_status_id_str": "1291741",
			"in_reply_to_user_id": 2584,
			"in_reply_to_user_id_str": "2584",
			"is_quote_status": False,
			"lang": "und",
			"place": None,
			"retweet_count": 0,
			"retweeted": False,
			"source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
			"text": "@mentioned_user Yes",
			"truncated": False,
			"user": {
				"contributors_enabled": False,
				"created_at": "Mon May 27 17:57:42 +0000 2019",
				"default_profile": True,
				"default_profile_image": False,
				"description": "description",
				"entities": {
					"description": {"urls": []},
					"url": {"urls": []}
				},
				"favourites_count": 754,
				"follow_request_sent": False,
				"followers_count": 130,
				"following": False,
				"friends_count": 295,
				"geo_enabled": False,
				"has_extended_profile": True,
				"id": 11330,
				"id_str": "11330",
				"is_translation_enabled": False,
				"is_translator": False,
				"lang": None,
				"listed_count": 3,
				"location": "location",
				"name": "test user 1",
				"notifications": False,
				"profile_background_color": "F5F8FA",
				"profile_background_image_url": None,
				"profile_background_image_url_https": None,
				"profile_background_tile": False,
				"profile_banner_url": None,
				"profile_image_url": None,
				"profile_image_url_https": None,
				"profile_link_color": "1DA1F2",
				"profile_sidebar_border_color": "C0DEED",
				"profile_sidebar_fill_color": "DDEEF6",
				"profile_text_color": "333333",
				"profile_use_background_image": True,
				"protected": False,
				"screen_name": "screen_name_2",
				"statuses_count": 283,
				"time_zone": None,
				"translator_type": "none",
				"url": None,
				"utc_offset": None,
				"verified": False
			}
		}
	],
	"user": {
		"id_str": "11330",
		"screen_name": "screen_name"
	}
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": os.getenv('rapidapi_key'),
	"X-RapidAPI-Host": "botometer-pro.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)





