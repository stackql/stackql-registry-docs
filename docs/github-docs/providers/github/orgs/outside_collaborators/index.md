---
title: outside_collaborators
hide_title: false
hide_table_of_contents: false
keywords:
  - outside_collaborators
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
<tr><td><b>Name</b></td><td><code>outside_collaborators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.orgs.outside_collaborators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `url` | `string` |
| `login` | `string` |
| `starred_at` | `string` |
| `type` | `string` |
| `html_url` | `string` |
| `starred_url` | `string` |
| `organizations_url` | `string` |
| `site_admin` | `boolean` |
| `followers_url` | `string` |
| `email` | `string` |
| `gravatar_id` | `string` |
| `node_id` | `string` |
| `events_url` | `string` |
| `gists_url` | `string` |
| `following_url` | `string` |
| `subscriptions_url` | `string` |
| `avatar_url` | `string` |
| `repos_url` | `string` |
| `received_events_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_outside_collaborators` | `SELECT` | `org` | List all users who are outside collaborators of an organization. |
| `remove_outside_collaborator` | `DELETE` | `org, username` | Removing a user from this list will remove them from all the organization's repositories. |
| `convert_member_to_outside_collaborator` | `EXEC` | `org, username` | When an organization member is converted to an outside collaborator, they'll only have access to the repositories that their current team membership allows. The user will no longer be a member of the organization. For more information, see "[Converting an organization member to an outside collaborator](https://docs.github.com/articles/converting-an-organization-member-to-an-outside-collaborator/)". |
