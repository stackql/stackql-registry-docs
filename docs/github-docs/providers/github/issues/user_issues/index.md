---
title: user_issues
hide_title: false
hide_table_of_contents: false
keywords:
  - user_issues
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
<tr><td><b>Name</b></td><td><code>user_issues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.user_issues</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `updated_at` | `string` |  |
| `state` | `string` | State of the issue; either 'open' or 'closed' |
| `title` | `string` | Title of the issue |
| `active_lock_reason` | `string` |  |
| `number` | `integer` | Number uniquely identifying the issue within its repository |
| `comments` | `integer` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `closed_by` | `object` | A GitHub user. |
| `html_url` | `string` |  |
| `created_at` | `string` |  |
| `events_url` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `closed_at` | `string` |  |
| `locked` | `boolean` |  |
| `repository` | `object` | A repository on GitHub. |
| `comments_url` | `string` |  |
| `node_id` | `string` |  |
| `pull_request` | `object` |  |
| `assignee` | `object` | A GitHub user. |
| `state_reason` | `string` | The reason for the current state |
| `timeline_url` | `string` |  |
| `draft` | `boolean` |  |
| `reactions` | `object` |  |
| `labels` | `array` | Labels to associate with this issue; pass one or more label names to replace the set of labels on this issue; send an empty array to clear all labels from the issue; note that the labels are silently dropped for users without push access to the repository |
| `repository_url` | `string` |  |
| `labels_url` | `string` |  |
| `body_html` | `string` |  |
| `body_text` | `string` |  |
| `body` | `string` | Contents of the issue |
| `url` | `string` | URL for the issue |
| `assignees` | `array` |  |
| `user` | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_for_authenticated_user` | `SELECT` |  |
