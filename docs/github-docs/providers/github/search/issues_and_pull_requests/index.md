---
title: issues_and_pull_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - issues_and_pull_requests
  - search
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
<tr><td><b>Name</b></td><td><code>issues_and_pull_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.search.issues_and_pull_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="active_lock_reason" /> | `string` |  |
| <CopyableCode code="assignee" /> | `object` | A GitHub user. |
| <CopyableCode code="assignees" /> | `array` |  |
| <CopyableCode code="author_association" /> | `string` | How the author is associated with the repository. |
| <CopyableCode code="body" /> | `string` |  |
| <CopyableCode code="body_html" /> | `string` |  |
| <CopyableCode code="body_text" /> | `string` |  |
| <CopyableCode code="closed_at" /> | `string` |  |
| <CopyableCode code="comments" /> | `integer` |  |
| <CopyableCode code="comments_url" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="draft" /> | `boolean` |  |
| <CopyableCode code="events_url" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="labels" /> | `array` |  |
| <CopyableCode code="labels_url" /> | `string` |  |
| <CopyableCode code="locked" /> | `boolean` |  |
| <CopyableCode code="milestone" /> | `object` | A collection of related issues and pull requests. |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="number" /> | `integer` |  |
| <CopyableCode code="performed_via_github_app" /> | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| <CopyableCode code="pull_request" /> | `object` |  |
| <CopyableCode code="reactions" /> | `object` |  |
| <CopyableCode code="repository" /> | `object` | A repository on GitHub. |
| <CopyableCode code="repository_url" /> | `string` |  |
| <CopyableCode code="score" /> | `number` |  |
| <CopyableCode code="state" /> | `string` |  |
| <CopyableCode code="state_reason" /> | `string` |  |
| <CopyableCode code="text_matches" /> | `array` |  |
| <CopyableCode code="timeline_url" /> | `string` |  |
| <CopyableCode code="title" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="user" /> | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="issues_and_pull_requests" /> | `SELECT` | <CopyableCode code="q" /> |
