---
title: repos_events
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_events
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
<tr><td><b>Name</b></td><td><code>repos_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.repos_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `issue` | `object` | Issues are a great way to keep track of tasks, enhancements, and bugs for your projects. |
| `commit_url` | `string` |  |
| `requested_reviewer` | `object` | A GitHub user. |
| `review_requester` | `object` | A GitHub user. |
| `dismissed_review` | `object` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `lock_reason` | `string` |  |
| `label` | `object` | Issue Event Label |
| `actor` | `object` | A GitHub user. |
| `assignee` | `object` | A GitHub user. |
| `requested_team` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `url` | `string` |  |
| `rename` | `object` | Issue Event Rename |
| `commit_id` | `string` |  |
| `project_card` | `object` | Issue Event Project Card |
| `created_at` | `string` |  |
| `assigner` | `object` | A GitHub user. |
| `author_association` | `string` | How the author is associated with the repository. |
| `milestone` | `object` | Issue Event Milestone |
| `node_id` | `string` |  |
| `event` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_event` | `SELECT` | `event_id, owner, repo` | Gets a single event by the event id. |
| `list_events` | `SELECT` | `issue_number, owner, repo` | Lists all events for an issue. |
| `list_events_for_repo` | `SELECT` | `owner, repo` | Lists events for a repository. |
