---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.users.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `company` | `string` |
| `public_gists` | `integer` |
| `public-user_total_private_repos` | `integer` |
| `public-user_created_at` | `string` |
| `public-user_disk_usage` | `integer` |
| `location` | `string` |
| `suspended_at` | `string` |
| `organizations_url` | `string` |
| `email` | `string` |
| `public-user_collaborators` | `integer` |
| `gists_url` | `string` |
| `events_url` | `string` |
| `two_factor_authentication` | `boolean` |
| `public-user_html_url` | `string` |
| `subscriptions_url` | `string` |
| `avatar_url` | `string` |
| `html_url` | `string` |
| `public-user_blog` | `string` |
| `public-user_node_id` | `string` |
| `node_id` | `string` |
| `public-user_avatar_url` | `string` |
| `public-user_id` | `integer` |
| `public-user_followers` | `integer` |
| `twitter_username` | `string` |
| `starred_url` | `string` |
| `public-user_private_gists` | `integer` |
| `created_at` | `string` |
| `bio` | `string` |
| `public-user_following` | `integer` |
| `site_admin` | `boolean` |
| `updated_at` | `string` |
| `owned_private_repos` | `integer` |
| `public-user_organizations_url` | `string` |
| `ldap_dn` | `string` |
| `disk_usage` | `integer` |
| `public-user_public_repos` | `integer` |
| `public-user_public_gists` | `integer` |
| `public_repos` | `integer` |
| `public-user_hireable` | `boolean` |
| `public-user_following_url` | `string` |
| `public-user_received_events_url` | `string` |
| `public-user_location` | `string` |
| `type` | `string` |
| `business_plus` | `boolean` |
| `public-user_bio` | `string` |
| `url` | `string` |
| `gravatar_id` | `string` |
| `public-user_suspended_at` | `string` |
| `public-user_company` | `string` |
| `public-user_updated_at` | `string` |
| `following_url` | `string` |
| `received_events_url` | `string` |
| `public-user_login` | `string` |
| `followers` | `integer` |
| `public-user_site_admin` | `boolean` |
| `public-user_events_url` | `string` |
| `repos_url` | `string` |
| `plan` | `object` |
| `total_private_repos` | `integer` |
| `blog` | `string` |
| `collaborators` | `integer` |
| `public-user_twitter_username` | `string` |
| `public-user_gravatar_id` | `string` |
| `public-user_owned_private_repos` | `integer` |
| `public-user_gists_url` | `string` |
| `public-user_repos_url` | `string` |
| `followers_url` | `string` |
| `hireable` | `boolean` |
| `public-user_starred_url` | `string` |
| `private_gists` | `integer` |
| `following` | `integer` |
| `login` | `string` |
| `public-user_plan` | `object` |
| `public-user_followers_url` | `string` |
| `public-user_name` | `string` |
| `public-user_email` | `string` |
| `public-user_type` | `string` |
| `public-user_subscriptions_url` | `string` |
| `public-user_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_by_username` | `SELECT` | `username` | Provides publicly available information about someone with a GitHub account.<br /><br />GitHub Apps with the `Plan` user permission can use this endpoint to retrieve information about a user's GitHub plan. The GitHub App must be authenticated as a user. See "[Identifying and authorizing users for GitHub Apps](https://docs.github.com/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/)" for details about authentication. For an example response, see 'Response with GitHub plan information' below"<br /><br />The `email` key in the following response is the publicly visible email address from your GitHub [profile page](https://github.com/settings/profile). When setting up your profile, you can select a primary email address to be “public” which provides an email entry for this endpoint. If you do not set a public email address for `email`, then it will have a value of `null`. You only see publicly visible email addresses when authenticated with GitHub. For more information, see [Authentication](https://docs.github.com/rest/overview/resources-in-the-rest-api#authentication).<br /><br />The Emails API enables you to list all of your email addresses, and toggle a primary email to be visible publicly. For more information, see "[Emails API](https://docs.github.com/rest/reference/users#emails)". |
| `list` | `SELECT` |  | Lists all users, in the order that they signed up on GitHub. This list includes personal user accounts and organization accounts.<br /><br />Note: Pagination is powered exclusively by the `since` parameter. Use the [Link header](https://docs.github.com/rest/overview/resources-in-the-rest-api#link-header) to get the URL for the next page of users. |
| `get_authenticated` | `EXEC` |  | If the authenticated user is authenticated through basic authentication or OAuth with the `user` scope, then the response lists public and private profile information.<br /><br />If the authenticated user is authenticated through OAuth without the `user` scope, then the response lists only public profile information. |
| `update_authenticated` | `EXEC` |  | **Note:** If your email is set to private and you send an `email` parameter as part of this request to update your profile, your privacy settings are still enforced: the email address will not be displayed on your public profile or via the API. |
