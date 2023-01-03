---
title: following
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>following</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.users.following</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `login` | `string` |
| `gists_url` | `string` |
| `received_events_url` | `string` |
| `html_url` | `string` |
| `starred_url` | `string` |
| `events_url` | `string` |
| `following_url` | `string` |
| `email` | `string` |
| `node_id` | `string` |
| `subscriptions_url` | `string` |
| `organizations_url` | `string` |
| `gravatar_id` | `string` |
| `url` | `string` |
| `followers_url` | `string` |
| `avatar_url` | `string` |
| `site_admin` | `boolean` |
| `repos_url` | `string` |
| `starred_at` | `string` |
| `type` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_followed_by_authenticated_user` | `SELECT` |  | Lists the people who the authenticated user follows. |
| `list_following_for_user` | `SELECT` | `username` | Lists the people who the specified user follows. |
| `check_following_for_user` | `EXEC` | `target_user, username` |  |
| `check_person_is_followed_by_authenticated` | `EXEC` | `username` |  |
| `follow` | `EXEC` | `username` | Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)."<br /><br />Following a user requires the user to be logged in and authenticated with basic auth or OAuth with the `user:follow` scope. |
| `unfollow` | `EXEC` | `username` | Unfollowing a user requires the user to be logged in and authenticated with basic auth or OAuth with the `user:follow` scope. |
