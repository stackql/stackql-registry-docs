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
| `lock_reason` | `string` |  |
| `assigner` | `object` | Simple User |
| `node_id` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `commit_url` | `string` |  |
| `requested_reviewer` | `object` | Simple User |
| `requested_team` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `dismissed_review` | `object` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `event` | `string` |  |
| `url` | `string` |  |
| `milestone` | `object` | Issue Event Milestone |
| `review_requester` | `object` | Simple User |
| `actor` | `object` | Simple User |
| `project_card` | `object` | Issue Event Project Card |
| `created_at` | `string` |  |
| `label` | `object` | Issue Event Label |
| `assignee` | `object` | Simple User |
| `rename` | `object` | Issue Event Rename |
| `commit_id` | `string` |  |
| `issue` | `object` | Issues are a great way to keep track of tasks, enhancements, and bugs for your projects. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_event` | `SELECT` | `event_id, owner, repo` |
| `list_events_for_repo` | `SELECT` | `owner, repo` |
