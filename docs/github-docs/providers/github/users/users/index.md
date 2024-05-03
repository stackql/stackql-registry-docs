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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.users.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `integer` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="avatar_url" /> | `string` |
| <CopyableCode code="bio" /> | `string` |
| <CopyableCode code="blog" /> | `string` |
| <CopyableCode code="business_plus" /> | `boolean` |
| <CopyableCode code="collaborators" /> | `integer` |
| <CopyableCode code="company" /> | `string` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="disk_usage" /> | `integer` |
| <CopyableCode code="email" /> | `string` |
| <CopyableCode code="events_url" /> | `string` |
| <CopyableCode code="followers" /> | `integer` |
| <CopyableCode code="followers_url" /> | `string` |
| <CopyableCode code="following" /> | `integer` |
| <CopyableCode code="following_url" /> | `string` |
| <CopyableCode code="gists_url" /> | `string` |
| <CopyableCode code="gravatar_id" /> | `string` |
| <CopyableCode code="hireable" /> | `boolean` |
| <CopyableCode code="html_url" /> | `string` |
| <CopyableCode code="ldap_dn" /> | `string` |
| <CopyableCode code="location" /> | `string` |
| <CopyableCode code="login" /> | `string` |
| <CopyableCode code="node_id" /> | `string` |
| <CopyableCode code="organizations_url" /> | `string` |
| <CopyableCode code="owned_private_repos" /> | `integer` |
| <CopyableCode code="plan" /> | `object` |
| <CopyableCode code="private_gists" /> | `integer` |
| <CopyableCode code="public-user_avatar_url" /> | `string` |
| <CopyableCode code="public-user_bio" /> | `string` |
| <CopyableCode code="public-user_blog" /> | `string` |
| <CopyableCode code="public-user_collaborators" /> | `integer` |
| <CopyableCode code="public-user_company" /> | `string` |
| <CopyableCode code="public-user_created_at" /> | `string` |
| <CopyableCode code="public-user_disk_usage" /> | `integer` |
| <CopyableCode code="public-user_email" /> | `string` |
| <CopyableCode code="public-user_events_url" /> | `string` |
| <CopyableCode code="public-user_followers" /> | `integer` |
| <CopyableCode code="public-user_followers_url" /> | `string` |
| <CopyableCode code="public-user_following" /> | `integer` |
| <CopyableCode code="public-user_following_url" /> | `string` |
| <CopyableCode code="public-user_gists_url" /> | `string` |
| <CopyableCode code="public-user_gravatar_id" /> | `string` |
| <CopyableCode code="public-user_hireable" /> | `boolean` |
| <CopyableCode code="public-user_html_url" /> | `string` |
| <CopyableCode code="public-user_id" /> | `integer` |
| <CopyableCode code="public-user_location" /> | `string` |
| <CopyableCode code="public-user_login" /> | `string` |
| <CopyableCode code="public-user_name" /> | `string` |
| <CopyableCode code="public-user_node_id" /> | `string` |
| <CopyableCode code="public-user_organizations_url" /> | `string` |
| <CopyableCode code="public-user_owned_private_repos" /> | `integer` |
| <CopyableCode code="public-user_plan" /> | `object` |
| <CopyableCode code="public-user_private_gists" /> | `integer` |
| <CopyableCode code="public-user_public_gists" /> | `integer` |
| <CopyableCode code="public-user_public_repos" /> | `integer` |
| <CopyableCode code="public-user_received_events_url" /> | `string` |
| <CopyableCode code="public-user_repos_url" /> | `string` |
| <CopyableCode code="public-user_site_admin" /> | `boolean` |
| <CopyableCode code="public-user_starred_url" /> | `string` |
| <CopyableCode code="public-user_subscriptions_url" /> | `string` |
| <CopyableCode code="public-user_suspended_at" /> | `string` |
| <CopyableCode code="public-user_total_private_repos" /> | `integer` |
| <CopyableCode code="public-user_twitter_username" /> | `string` |
| <CopyableCode code="public-user_type" /> | `string` |
| <CopyableCode code="public-user_updated_at" /> | `string` |
| <CopyableCode code="public-user_url" /> | `string` |
| <CopyableCode code="public_gists" /> | `integer` |
| <CopyableCode code="public_repos" /> | `integer` |
| <CopyableCode code="received_events_url" /> | `string` |
| <CopyableCode code="repos_url" /> | `string` |
| <CopyableCode code="site_admin" /> | `boolean` |
| <CopyableCode code="starred_url" /> | `string` |
| <CopyableCode code="subscriptions_url" /> | `string` |
| <CopyableCode code="suspended_at" /> | `string` |
| <CopyableCode code="total_private_repos" /> | `integer` |
| <CopyableCode code="twitter_username" /> | `string` |
| <CopyableCode code="two_factor_authentication" /> | `boolean` |
| <CopyableCode code="type" /> | `string` |
| <CopyableCode code="updated_at" /> | `string` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_authenticated" /> | `SELECT` |  | If the authenticated user is authenticated with an OAuth token with the `user` scope, then the response lists public and private profile information.<br /><br />If the authenticated user is authenticated through OAuth without the `user` scope, then the response lists only public profile information. |
| <CopyableCode code="get_by_username" /> | `SELECT` | <CopyableCode code="username" /> | Provides publicly available information about someone with a GitHub account.<br /><br />GitHub Apps with the `Plan` user permission can use this endpoint to retrieve information about a user's GitHub plan. The GitHub App must be authenticated as a user. See "[Identifying and authorizing users for GitHub Apps](https://docs.github.com/apps/building-github-apps/identifying-and-authorizing-users-for-github-apps/)" for details about authentication. For an example response, see 'Response with GitHub plan information' below"<br /><br />The `email` key in the following response is the publicly visible email address from your GitHub [profile page](https://github.com/settings/profile). When setting up your profile, you can select a primary email address to be “public” which provides an email entry for this endpoint. If you do not set a public email address for `email`, then it will have a value of `null`. You only see publicly visible email addresses when authenticated with GitHub. For more information, see [Authentication](https://docs.github.com/rest/overview/resources-in-the-rest-api#authentication).<br /><br />The Emails API enables you to list all of your email addresses, and toggle a primary email to be visible publicly. For more information, see "[Emails API](https://docs.github.com/rest/users/emails)". |
| <CopyableCode code="update_authenticated" /> | `EXEC` |  | **Note:** If your email is set to private and you send an `email` parameter as part of this request to update your profile, your privacy settings are still enforced: the email address will not be displayed on your public profile or via the API. |
