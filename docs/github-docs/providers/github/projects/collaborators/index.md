---
title: collaborators
hide_title: false
hide_table_of_contents: false
keywords:
  - collaborators
  - projects
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
<tr><td><b>Name</b></td><td><code>collaborators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.projects.collaborators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `organizations_url` | `string` |
| `events_url` | `string` |
| `followers_url` | `string` |
| `site_admin` | `boolean` |
| `starred_at` | `string` |
| `avatar_url` | `string` |
| `gravatar_id` | `string` |
| `type` | `string` |
| `repos_url` | `string` |
| `following_url` | `string` |
| `email` | `string` |
| `login` | `string` |
| `gists_url` | `string` |
| `url` | `string` |
| `node_id` | `string` |
| `received_events_url` | `string` |
| `html_url` | `string` |
| `starred_url` | `string` |
| `subscriptions_url` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_collaborators` | `SELECT` | `project_id` | Lists the collaborators for an organization project. For a project, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners. You must be an organization owner or a project `admin` to list collaborators. |
| `add_collaborator` | `INSERT` | `project_id, username` | Adds a collaborator to an organization project and sets their permission level. You must be an organization owner or a project `admin` to add a collaborator. |
| `remove_collaborator` | `DELETE` | `project_id, username` | Removes a collaborator from an organization project. You must be an organization owner or a project `admin` to remove a collaborator. |
