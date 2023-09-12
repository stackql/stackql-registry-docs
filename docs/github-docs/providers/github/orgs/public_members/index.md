---
title: public_members
hide_title: false
hide_table_of_contents: false
keywords:
  - public_members
  - orgs
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
<tr><td><b>Name</b></td><td><code>public_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.public_members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `subscriptions_url` | `string` |
| `url` | `string` |
| `html_url` | `string` |
| `starred_at` | `string` |
| `type` | `string` |
| `login` | `string` |
| `received_events_url` | `string` |
| `avatar_url` | `string` |
| `repos_url` | `string` |
| `gravatar_id` | `string` |
| `node_id` | `string` |
| `gists_url` | `string` |
| `email` | `string` |
| `organizations_url` | `string` |
| `followers_url` | `string` |
| `following_url` | `string` |
| `events_url` | `string` |
| `starred_url` | `string` |
| `site_admin` | `boolean` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_public_members` | `SELECT` | `org` | Members of an organization can choose to have their membership publicized or not. |
| `remove_public_membership_for_authenticated_user` | `DELETE` | `org, username` | Removes the public membership for the authenticated user from the specified organization, unless public visibility is enforced by default. |
| `check_public_membership_for_user` | `EXEC` | `org, username` | Check if the provided user is a public member of the organization. |
| `set_public_membership_for_authenticated_user` | `EXEC` | `org, username` | The user can publicize their own membership. (A user cannot publicize the membership for another user.)<br /><br />Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
