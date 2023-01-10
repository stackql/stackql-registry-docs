---
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
  - issues
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
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `dismissed_review` | `object` |  |
| `review_requester` | `object` | Simple User |
| `requested_team` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `event` | `string` |  |
| `requested_reviewer` | `object` | Simple User |
| `assigner` | `object` | Simple User |
| `milestone` | `object` | Issue Event Milestone |
| `project_card` | `object` | Issue Event Project Card |
| `issue` | `object` | Issues are a great way to keep track of tasks, enhancements, and bugs for your projects. |
| `commit_id` | `string` |  |
| `node_id` | `string` |  |
| `lock_reason` | `string` |  |
| `actor` | `object` | Simple User |
| `assignee` | `object` | Simple User |
| `author_association` | `string` | How the author is associated with the repository. |
| `commit_url` | `string` |  |
| `url` | `string` |  |
| `rename` | `object` | Issue Event Rename |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `created_at` | `string` |  |
| `label` | `object` | Issue Event Label |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_event` | `SELECT` | `event_id, owner, repo` |
| `list_events_for_repo` | `SELECT` | `owner, repo` |
