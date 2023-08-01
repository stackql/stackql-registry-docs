---
title: events_for_issues
hide_title: false
hide_table_of_contents: false
keywords:
  - events_for_issues
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
<tr><td><b>Name</b></td><td><code>events_for_issues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.events_for_issues</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `review-dismissed-issue-event_actor` | `object` | Simple User |
| `removed-from-project-issue-event_commit_id` | `string` |  |
| `renamed-issue-event_node_id` | `string` |  |
| `renamed-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `milestoned-issue-event_node_id` | `string` |  |
| `demilestoned-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `milestoned-issue-event_id` | `integer` |  |
| `added-to-project-issue-event_commit_id` | `string` |  |
| `review-dismissed-issue-event_node_id` | `string` |  |
| `assigned-issue-event_url` | `string` |  |
| `review-dismissed-issue-event_url` | `string` |  |
| `review-requested-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `review-request-removed-issue-event_created_at` | `string` |  |
| `renamed-issue-event_id` | `integer` |  |
| `unassigned-issue-event_node_id` | `string` |  |
| `renamed-issue-event_created_at` | `string` |  |
| `requested_team` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `added-to-project-issue-event_commit_url` | `string` |  |
| `added-to-project-issue-event_created_at` | `string` |  |
| `converted-note-to-issue-issue-event_event` | `string` |  |
| `added-to-project-issue-event_node_id` | `string` |  |
| `review_requester` | `object` | Simple User |
| `locked-issue-event_actor` | `object` | Simple User |
| `review-request-removed-issue-event_commit_url` | `string` |  |
| `converted-note-to-issue-issue-event_commit_url` | `string` |  |
| `unassigned-issue-event_assigner` | `object` | Simple User |
| `url` | `string` |  |
| `added-to-project-issue-event_actor` | `object` | Simple User |
| `assigner` | `object` | Simple User |
| `demilestoned-issue-event_actor` | `object` | Simple User |
| `review-requested-issue-event_commit_id` | `string` |  |
| `review-request-removed-issue-event_requested_reviewer` | `object` | Simple User |
| `converted-note-to-issue-issue-event_project_card` | `object` |  |
| `milestoned-issue-event_created_at` | `string` |  |
| `moved-column-in-project-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `assigned-issue-event_id` | `integer` |  |
| `converted-note-to-issue-issue-event_url` | `string` |  |
| `converted-note-to-issue-issue-event_created_at` | `string` |  |
| `moved-column-in-project-issue-event_actor` | `object` | Simple User |
| `review-requested-issue-event_id` | `integer` |  |
| `demilestoned-issue-event_created_at` | `string` |  |
| `converted-note-to-issue-issue-event_node_id` | `string` |  |
| `converted-note-to-issue-issue-event_id` | `integer` |  |
| `assigned-issue-event_commit_id` | `string` |  |
| `commit_id` | `string` |  |
| `review-request-removed-issue-event_requested_team` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `label` | `object` |  |
| `assigned-issue-event_actor` | `object` | Simple User |
| `demilestoned-issue-event_commit_id` | `string` |  |
| `removed-from-project-issue-event_url` | `string` |  |
| `moved-column-in-project-issue-event_event` | `string` |  |
| `added-to-project-issue-event_url` | `string` |  |
| `removed-from-project-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `removed-from-project-issue-event_actor` | `object` | Simple User |
| `event` | `string` |  |
| `review-requested-issue-event_actor` | `object` | Simple User |
| `locked-issue-event_url` | `string` |  |
| `unlabeled-issue-event_created_at` | `string` |  |
| `assigned-issue-event_commit_url` | `string` |  |
| `locked-issue-event_commit_id` | `string` |  |
| `locked-issue-event_event` | `string` |  |
| `locked-issue-event_commit_url` | `string` |  |
| `moved-column-in-project-issue-event_id` | `integer` |  |
| `milestoned-issue-event_commit_id` | `string` |  |
| `review-requested-issue-event_url` | `string` |  |
| `review-request-removed-issue-event_node_id` | `string` |  |
| `milestoned-issue-event_actor` | `object` | Simple User |
| `demilestoned-issue-event_node_id` | `string` |  |
| `review-request-removed-issue-event_actor` | `object` | Simple User |
| `review-request-removed-issue-event_event` | `string` |  |
| `removed-from-project-issue-event_project_card` | `object` |  |
| `review-dismissed-issue-event_event` | `string` |  |
| `review-requested-issue-event_node_id` | `string` |  |
| `moved-column-in-project-issue-event_project_card` | `object` |  |
| `unlabeled-issue-event_id` | `integer` |  |
| `demilestoned-issue-event_id` | `integer` |  |
| `added-to-project-issue-event_id` | `integer` |  |
| `converted-note-to-issue-issue-event_commit_id` | `string` |  |
| `demilestoned-issue-event_milestone` | `object` |  |
| `review-dismissed-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `review-requested-issue-event_created_at` | `string` |  |
| `review-dismissed-issue-event_commit_id` | `string` |  |
| `review-requested-issue-event_commit_url` | `string` |  |
| `renamed-issue-event_event` | `string` |  |
| `review-dismissed-issue-event_id` | `integer` |  |
| `unassigned-issue-event_actor` | `object` | Simple User |
| `lock_reason` | `string` |  |
| `renamed-issue-event_url` | `string` |  |
| `renamed-issue-event_actor` | `object` | Simple User |
| `commit_url` | `string` |  |
| `removed-from-project-issue-event_id` | `integer` |  |
| `milestoned-issue-event_url` | `string` |  |
| `assignee` | `object` | Simple User |
| `review-request-removed-issue-event_review_requester` | `object` | Simple User |
| `unlabeled-issue-event_label` | `object` |  |
| `unassigned-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `unlabeled-issue-event_url` | `string` |  |
| `locked-issue-event_id` | `integer` |  |
| `unassigned-issue-event_created_at` | `string` |  |
| `removed-from-project-issue-event_created_at` | `string` |  |
| `milestoned-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `removed-from-project-issue-event_commit_url` | `string` |  |
| `unlabeled-issue-event_actor` | `object` | Simple User |
| `review-request-removed-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `actor` | `object` | Simple User |
| `unassigned-issue-event_assignee` | `object` | Simple User |
| `node_id` | `string` |  |
| `unlabeled-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `demilestoned-issue-event_event` | `string` |  |
| `removed-from-project-issue-event_event` | `string` |  |
| `milestoned-issue-event_event` | `string` |  |
| `review-request-removed-issue-event_url` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `demilestoned-issue-event_url` | `string` |  |
| `assigned-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `added-to-project-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `assigned-issue-event_node_id` | `string` |  |
| `added-to-project-issue-event_event` | `string` |  |
| `moved-column-in-project-issue-event_node_id` | `string` |  |
| `review-dismissed-issue-event_commit_url` | `string` |  |
| `review-dismissed-issue-event_created_at` | `string` |  |
| `locked-issue-event_created_at` | `string` |  |
| `review-requested-issue-event_event` | `string` |  |
| `converted-note-to-issue-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `unassigned-issue-event_commit_url` | `string` |  |
| `review-request-removed-issue-event_commit_id` | `string` |  |
| `assigned-issue-event_event` | `string` |  |
| `moved-column-in-project-issue-event_commit_url` | `string` |  |
| `unassigned-issue-event_id` | `integer` |  |
| `renamed-issue-event_commit_id` | `string` |  |
| `moved-column-in-project-issue-event_created_at` | `string` |  |
| `unassigned-issue-event_event` | `string` |  |
| `created_at` | `string` |  |
| `moved-column-in-project-issue-event_commit_id` | `string` |  |
| `moved-column-in-project-issue-event_url` | `string` |  |
| `locked-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `project_card` | `object` |  |
| `unlabeled-issue-event_commit_url` | `string` |  |
| `unassigned-issue-event_url` | `string` |  |
| `removed-from-project-issue-event_node_id` | `string` |  |
| `demilestoned-issue-event_commit_url` | `string` |  |
| `review-request-removed-issue-event_id` | `integer` |  |
| `milestoned-issue-event_commit_url` | `string` |  |
| `unlabeled-issue-event_commit_id` | `string` |  |
| `rename` | `object` |  |
| `renamed-issue-event_commit_url` | `string` |  |
| `unlabeled-issue-event_node_id` | `string` |  |
| `converted-note-to-issue-issue-event_actor` | `object` | Simple User |
| `locked-issue-event_node_id` | `string` |  |
| `unassigned-issue-event_commit_id` | `string` |  |
| `dismissed_review` | `object` |  |
| `unlabeled-issue-event_event` | `string` |  |
| `requested_reviewer` | `object` | Simple User |
| `milestone` | `object` |  |
| `assigned-issue-event_created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_events` | `SELECT` | `issue_number, owner, repo` |
