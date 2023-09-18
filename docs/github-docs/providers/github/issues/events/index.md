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
| `project_card` | `object` | Issue Event Project Card |
| `url` | `string` |  |
| `assignee` | `object` | A GitHub user. |
| `requested_team` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `rename` | `object` | Issue Event Rename |
| `node_id` | `string` |  |
| `dismissed_review` | `object` |  |
| `label` | `object` | Issue Event Label |
| `assigner` | `object` | A GitHub user. |
| `commit_id` | `string` |  |
| `event` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `requested_reviewer` | `object` | A GitHub user. |
| `milestone` | `object` | Issue Event Milestone |
| `commit_url` | `string` |  |
| `review_requester` | `object` | A GitHub user. |
| `created_at` | `string` |  |
| `issue` | `object` | Issues are a great way to keep track of tasks, enhancements, and bugs for your projects. |
| `actor` | `object` | A GitHub user. |
| `lock_reason` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_event` | `SELECT` | `event_id, owner, repo` | Gets a single event by the event id. |
| `list_events` | `SELECT` | `issue_number, owner, repo` | Lists all events for an issue. |
| `list_events_for_repo` | `SELECT` | `owner, repo` | Lists events for a repository. |
