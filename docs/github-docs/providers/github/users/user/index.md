---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
  - users
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.users.user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `public-user_type` | `string` |
| `public-user_starred_url` | `string` |
| `public-user_collaborators` | `integer` |
| `ldap_dn` | `string` |
| `avatar_url` | `string` |
| `public-user_private_gists` | `integer` |
| `public_gists` | `integer` |
| `public-user_received_events_url` | `string` |
| `public-user_gravatar_id` | `string` |
| `disk_usage` | `integer` |
| `public-user_hireable` | `boolean` |
| `public-user_plan` | `object` |
| `login` | `string` |
| `following_url` | `string` |
| `public-user_location` | `string` |
| `suspended_at` | `string` |
| `gists_url` | `string` |
| `created_at` | `string` |
| `received_events_url` | `string` |
| `public-user_total_private_repos` | `integer` |
| `public-user_public_gists` | `integer` |
| `type` | `string` |
| `public-user_subscriptions_url` | `string` |
| `plan` | `object` |
| `public-user_updated_at` | `string` |
| `repos_url` | `string` |
| `public-user_name` | `string` |
| `private_gists` | `integer` |
| `owned_private_repos` | `integer` |
| `hireable` | `boolean` |
| `total_private_repos` | `integer` |
| `html_url` | `string` |
| `organizations_url` | `string` |
| `public-user_id` | `integer` |
| `public-user_created_at` | `string` |
| `subscriptions_url` | `string` |
| `location` | `string` |
| `starred_url` | `string` |
| `bio` | `string` |
| `public-user_avatar_url` | `string` |
| `two_factor_authentication` | `boolean` |
| `business_plus` | `boolean` |
| `public-user_followers_url` | `string` |
| `collaborators` | `integer` |
| `public-user_disk_usage` | `integer` |
| `email` | `string` |
| `public-user_html_url` | `string` |
| `public-user_company` | `string` |
| `public-user_repos_url` | `string` |
| `public-user_bio` | `string` |
| `public_repos` | `integer` |
| `url` | `string` |
| `public-user_organizations_url` | `string` |
| `public-user_suspended_at` | `string` |
| `company` | `string` |
| `public-user_following` | `integer` |
| `following` | `integer` |
| `site_admin` | `boolean` |
| `events_url` | `string` |
| `public-user_owned_private_repos` | `integer` |
| `public-user_public_repos` | `integer` |
| `gravatar_id` | `string` |
| `public-user_followers` | `integer` |
| `public-user_blog` | `string` |
| `public-user_login` | `string` |
| `public-user_events_url` | `string` |
| `public-user_following_url` | `string` |
| `twitter_username` | `string` |
| `public-user_node_id` | `string` |
| `public-user_email` | `string` |
| `public-user_gists_url` | `string` |
| `public-user_site_admin` | `boolean` |
| `public-user_twitter_username` | `string` |
| `public-user_url` | `string` |
| `followers_url` | `string` |
| `blog` | `string` |
| `updated_at` | `string` |
| `followers` | `integer` |
| `node_id` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_authenticated` | `SELECT` |  | If the authenticated user is authenticated with an OAuth token with the `user` scope, then the response lists public and private profile information.<br /><br />If the authenticated user is authenticated through OAuth without the `user` scope, then the response lists only public profile information. |
| `update_authenticated` | `EXEC` |  | **Note:** If your email is set to private and you send an `email` parameter as part of this request to update your profile, your privacy settings are still enforced: the email address will not be displayed on your public profile or via the API. |
