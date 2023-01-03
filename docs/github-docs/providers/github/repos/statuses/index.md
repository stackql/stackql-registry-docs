---
title: statuses
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
<tr><td><b>Name</b></td><td><code>statuses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.statuses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `description` | `string` |  |
| `updated_at` | `string` |  |
| `avatar_url` | `string` |  |
| `url` | `string` |  |
| `context` | `string` |  |
| `creator` | `object` | Simple User |
| `target_url` | `string` |  |
| `node_id` | `string` |  |
| `created_at` | `string` |  |
| `state` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_commit_statuses_for_ref` | `SELECT` | `owner, ref, repo` | Users with pull access in a repository can view commit statuses for a given ref. The ref can be a SHA, a branch name, or a tag name. Statuses are returned in reverse chronological order. The first status in the list will be the latest one.<br /><br />This resource is also available via a legacy route: `GET /repos/:owner/:repo/statuses/:ref`. |
| `create_commit_status` | `INSERT` | `owner, repo, sha, data__state` | Users with push access in a repository can create commit statuses for a given SHA.<br /><br />Note: there is a limit of 1000 statuses per `sha` and `context` within a repository. Attempts to create more than 1000 statuses will result in a validation error. |
