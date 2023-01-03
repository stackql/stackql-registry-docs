---
title: events
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
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `commit_url` | `string` |  |
| `label` | `object` | Issue Event Label |
| `milestone` | `object` | Issue Event Milestone |
| `requested_team` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `actor` | `object` | Simple User |
| `author_association` | `string` | How the author is associated with the repository. |
| `project_card` | `object` | Issue Event Project Card |
| `review_requester` | `object` | Simple User |
| `dismissed_review` | `object` |  |
| `assignee` | `object` | Simple User |
| `node_id` | `string` |  |
| `url` | `string` |  |
| `rename` | `object` | Issue Event Rename |
| `event` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `assigner` | `object` | Simple User |
| `lock_reason` | `string` |  |
| `issue` | `object` | Issues are a great way to keep track of tasks, enhancements, and bugs for your projects. |
| `created_at` | `string` |  |
| `requested_reviewer` | `object` | Simple User |
| `commit_id` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_event` | `SELECT` | `event_id, owner, repo` |
| `list_events_for_repo` | `SELECT` | `owner, repo` |
