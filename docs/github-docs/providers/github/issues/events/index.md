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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.issues.events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="actor" /> | `object` | A GitHub user. |
| <CopyableCode code="assignee" /> | `object` | A GitHub user. |
| <CopyableCode code="assigner" /> | `object` | A GitHub user. |
| <CopyableCode code="author_association" /> | `string` | How the author is associated with the repository. |
| <CopyableCode code="commit_id" /> | `string` |  |
| <CopyableCode code="commit_url" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="dismissed_review" /> | `object` |  |
| <CopyableCode code="event" /> | `string` |  |
| <CopyableCode code="issue" /> | `object` | Issues are a great way to keep track of tasks, enhancements, and bugs for your projects. |
| <CopyableCode code="label" /> | `object` | Issue Event Label |
| <CopyableCode code="lock_reason" /> | `string` |  |
| <CopyableCode code="milestone" /> | `object` | Issue Event Milestone |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="performed_via_github_app" /> | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| <CopyableCode code="project_card" /> | `object` | Issue Event Project Card |
| <CopyableCode code="rename" /> | `object` | Issue Event Rename |
| <CopyableCode code="requested_reviewer" /> | `object` | A GitHub user. |
| <CopyableCode code="requested_team" /> | `object` | Groups of organization members that gives permissions on specified repositories. |
| <CopyableCode code="review_requester" /> | `object` | A GitHub user. |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_event" /> | `SELECT` | <CopyableCode code="event_id, owner, repo" /> | Gets a single event by the event id. |
| <CopyableCode code="list_events" /> | `SELECT` | <CopyableCode code="issue_number, owner, repo" /> | Lists all events for an issue. |
| <CopyableCode code="list_events_for_repo" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists events for a repository. |
