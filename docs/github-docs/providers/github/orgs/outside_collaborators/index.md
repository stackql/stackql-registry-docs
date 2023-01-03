---
title: outside_collaborators
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
<tr><td><b>Name</b></td><td><code>outside_collaborators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.outside_collaborators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `starred_url` | `string` |
| `organizations_url` | `string` |
| `login` | `string` |
| `email` | `string` |
| `type` | `string` |
| `node_id` | `string` |
| `site_admin` | `boolean` |
| `gravatar_id` | `string` |
| `html_url` | `string` |
| `following_url` | `string` |
| `repos_url` | `string` |
| `events_url` | `string` |
| `received_events_url` | `string` |
| `starred_at` | `string` |
| `gists_url` | `string` |
| `avatar_url` | `string` |
| `followers_url` | `string` |
| `subscriptions_url` | `string` |
| `url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_outside_collaborators` | `SELECT` | `org` | List all users who are outside collaborators of an organization. |
| `remove_outside_collaborator` | `DELETE` | `org, username` | Removing a user from this list will remove them from all the organization's repositories. |
| `convert_member_to_outside_collaborator` | `EXEC` | `org, username` | When an organization member is converted to an outside collaborator, they'll only have access to the repositories that their current team membership allows. The user will no longer be a member of the organization. For more information, see "[Converting an organization member to an outside collaborator](https://docs.github.com/articles/converting-an-organization-member-to-an-outside-collaborator/)". |
