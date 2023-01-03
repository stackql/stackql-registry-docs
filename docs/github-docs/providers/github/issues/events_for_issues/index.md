---
title: events_for_issues
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
<tr><td><b>Name</b></td><td><code>events_for_issues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.events_for_issues</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `review-requested-issue-event_event` | `string` |  |
| `added-to-project-issue-event_event` | `string` |  |
| `review-request-removed-issue-event_event` | `string` |  |
| `renamed-issue-event_commit_id` | `string` |  |
| `dismissed_review` | `object` |  |
| `milestoned-issue-event_created_at` | `string` |  |
| `actor` | `object` | Simple User |
| `demilestoned-issue-event_commit_url` | `string` |  |
| `locked-issue-event_node_id` | `string` |  |
| `added-to-project-issue-event_id` | `integer` |  |
| `review-request-removed-issue-event_node_id` | `string` |  |
| `unassigned-issue-event_created_at` | `string` |  |
| `requested_reviewer` | `object` | Simple User |
| `milestoned-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `milestone` | `object` |  |
| `converted-note-to-issue-issue-event_commit_id` | `string` |  |
| `review-dismissed-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `removed-from-project-issue-event_commit_url` | `string` |  |
| `node_id` | `string` |  |
| `removed-from-project-issue-event_event` | `string` |  |
| `milestoned-issue-event_event` | `string` |  |
| `converted-note-to-issue-issue-event_event` | `string` |  |
| `removed-from-project-issue-event_url` | `string` |  |
| `moved-column-in-project-issue-event_url` | `string` |  |
| `unlabeled-issue-event_id` | `integer` |  |
| `assigned-issue-event_created_at` | `string` |  |
| `converted-note-to-issue-issue-event_project_card` | `object` |  |
| `unlabeled-issue-event_label` | `object` |  |
| `locked-issue-event_actor` | `object` | Simple User |
| `review-dismissed-issue-event_created_at` | `string` |  |
| `unlabeled-issue-event_created_at` | `string` |  |
| `removed-from-project-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `milestoned-issue-event_commit_id` | `string` |  |
| `review-request-removed-issue-event_commit_id` | `string` |  |
| `label` | `object` |  |
| `demilestoned-issue-event_milestone` | `object` |  |
| `renamed-issue-event_commit_url` | `string` |  |
| `unassigned-issue-event_url` | `string` |  |
| `moved-column-in-project-issue-event_project_card` | `object` |  |
| `added-to-project-issue-event_created_at` | `string` |  |
| `moved-column-in-project-issue-event_node_id` | `string` |  |
| `commit_url` | `string` |  |
| `removed-from-project-issue-event_id` | `integer` |  |
| `review-requested-issue-event_node_id` | `string` |  |
| `removed-from-project-issue-event_created_at` | `string` |  |
| `unassigned-issue-event_actor` | `object` | Simple User |
| `lock_reason` | `string` |  |
| `milestoned-issue-event_id` | `integer` |  |
| `milestoned-issue-event_node_id` | `string` |  |
| `review-requested-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `unlabeled-issue-event_commit_id` | `string` |  |
| `converted-note-to-issue-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `created_at` | `string` |  |
| `added-to-project-issue-event_actor` | `object` | Simple User |
| `review-request-removed-issue-event_id` | `integer` |  |
| `converted-note-to-issue-issue-event_actor` | `object` | Simple User |
| `review-requested-issue-event_actor` | `object` | Simple User |
| `locked-issue-event_event` | `string` |  |
| `review-request-removed-issue-event_url` | `string` |  |
| `review-request-removed-issue-event_requested_reviewer` | `object` | Simple User |
| `added-to-project-issue-event_node_id` | `string` |  |
| `unassigned-issue-event_assignee` | `object` | Simple User |
| `renamed-issue-event_created_at` | `string` |  |
| `removed-from-project-issue-event_project_card` | `object` |  |
| `review-dismissed-issue-event_id` | `integer` |  |
| `demilestoned-issue-event_id` | `integer` |  |
| `locked-issue-event_commit_url` | `string` |  |
| `review-requested-issue-event_commit_url` | `string` |  |
| `review-request-removed-issue-event_created_at` | `string` |  |
| `moved-column-in-project-issue-event_actor` | `object` | Simple User |
| `milestoned-issue-event_url` | `string` |  |
| `review-dismissed-issue-event_actor` | `object` | Simple User |
| `locked-issue-event_created_at` | `string` |  |
| `unassigned-issue-event_commit_id` | `string` |  |
| `demilestoned-issue-event_event` | `string` |  |
| `converted-note-to-issue-issue-event_id` | `integer` |  |
| `renamed-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `added-to-project-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `converted-note-to-issue-issue-event_created_at` | `string` |  |
| `unassigned-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `review-request-removed-issue-event_requested_team` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `moved-column-in-project-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `moved-column-in-project-issue-event_created_at` | `string` |  |
| `assigned-issue-event_actor` | `object` | Simple User |
| `converted-note-to-issue-issue-event_url` | `string` |  |
| `review-requested-issue-event_id` | `integer` |  |
| `unlabeled-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `assigned-issue-event_id` | `integer` |  |
| `assignee` | `object` | Simple User |
| `review-requested-issue-event_created_at` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `url` | `string` |  |
| `moved-column-in-project-issue-event_id` | `integer` |  |
| `review-dismissed-issue-event_commit_id` | `string` |  |
| `removed-from-project-issue-event_actor` | `object` | Simple User |
| `renamed-issue-event_url` | `string` |  |
| `milestoned-issue-event_commit_url` | `string` |  |
| `unassigned-issue-event_id` | `integer` |  |
| `event` | `string` |  |
| `review-request-removed-issue-event_commit_url` | `string` |  |
| `unassigned-issue-event_commit_url` | `string` |  |
| `review-dismissed-issue-event_commit_url` | `string` |  |
| `assigned-issue-event_commit_id` | `string` |  |
| `locked-issue-event_id` | `integer` |  |
| `review-request-removed-issue-event_actor` | `object` | Simple User |
| `demilestoned-issue-event_actor` | `object` | Simple User |
| `renamed-issue-event_event` | `string` |  |
| `renamed-issue-event_node_id` | `string` |  |
| `removed-from-project-issue-event_node_id` | `string` |  |
| `locked-issue-event_url` | `string` |  |
| `review-request-removed-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `added-to-project-issue-event_commit_url` | `string` |  |
| `added-to-project-issue-event_url` | `string` |  |
| `assigned-issue-event_commit_url` | `string` |  |
| `demilestoned-issue-event_node_id` | `string` |  |
| `rename` | `object` |  |
| `milestoned-issue-event_actor` | `object` | Simple User |
| `locked-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `unlabeled-issue-event_url` | `string` |  |
| `removed-from-project-issue-event_commit_id` | `string` |  |
| `unlabeled-issue-event_node_id` | `string` |  |
| `review-dismissed-issue-event_url` | `string` |  |
| `review-requested-issue-event_url` | `string` |  |
| `assigned-issue-event_node_id` | `string` |  |
| `demilestoned-issue-event_created_at` | `string` |  |
| `unassigned-issue-event_assigner` | `object` | Simple User |
| `unlabeled-issue-event_actor` | `object` | Simple User |
| `moved-column-in-project-issue-event_commit_id` | `string` |  |
| `unassigned-issue-event_node_id` | `string` |  |
| `review-request-removed-issue-event_review_requester` | `object` | Simple User |
| `moved-column-in-project-issue-event_event` | `string` |  |
| `project_card` | `object` |  |
| `review-dismissed-issue-event_node_id` | `string` |  |
| `review-requested-issue-event_commit_id` | `string` |  |
| `unlabeled-issue-event_event` | `string` |  |
| `assigned-issue-event_url` | `string` |  |
| `assigner` | `object` | Simple User |
| `demilestoned-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `review-dismissed-issue-event_event` | `string` |  |
| `commit_id` | `string` |  |
| `locked-issue-event_commit_id` | `string` |  |
| `moved-column-in-project-issue-event_commit_url` | `string` |  |
| `converted-note-to-issue-issue-event_commit_url` | `string` |  |
| `unassigned-issue-event_event` | `string` |  |
| `added-to-project-issue-event_commit_id` | `string` |  |
| `renamed-issue-event_id` | `integer` |  |
| `renamed-issue-event_actor` | `object` | Simple User |
| `assigned-issue-event_performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `demilestoned-issue-event_url` | `string` |  |
| `converted-note-to-issue-issue-event_node_id` | `string` |  |
| `review_requester` | `object` | Simple User |
| `unlabeled-issue-event_commit_url` | `string` |  |
| `requested_team` | `object` | Groups of organization members that gives permissions on specified repositories. |
| `assigned-issue-event_event` | `string` |  |
| `demilestoned-issue-event_commit_id` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_events` | `SELECT` | `issue_number, owner, repo` |
