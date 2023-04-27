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
| `label` | `object` | Issue Event Label |
| `requested_reviewer` | `object` | Simple User |
| `dismissed_review` | `object` |  |
| `node_id` | `string` |  |
| `project_card` | `object` | Issue Event Project Card |
| `commit_id` | `string` |  |
| `lock_reason` | `string` |  |
| `created_at` | `string` |  |
| `commit_url` | `string` |  |
| `milestone` | `object` | Issue Event Milestone |
| `event` | `string` |  |
| `review_requester` | `object` | Simple User |
| `rename` | `object` | Issue Event Rename |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `issue` | `object` | Issues are a great way to keep track of tasks, enhancements, and bugs for your projects. |
| `author_association` | `string` | How the author is associated with the repository. |
| `actor` | `object` | Simple User |
| `assignee` | `object` | Simple User |
| `assigner` | `object` | Simple User |
| `url` | `string` |  |
| `requested_team` | `object` | Groups of organization members that gives permissions on specified repositories. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_event` | `SELECT` | `event_id, owner, repo` |
| `list_events_for_repo` | `SELECT` | `owner, repo` |
