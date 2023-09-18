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
| `user` | `object` | A GitHub user. |
| `events_url` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `reactions` | `object` |  |
| `created_at` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `locked` | `boolean` |  |
| `labels_url` | `string` |  |
| `body_html` | `string` |  |
| `assignee` | `object` | A GitHub user. |
| `repository` | `object` | A repository on GitHub. |
| `assignees` | `array` |  |
| `updated_at` | `string` |  |
| `active_lock_reason` | `string` |  |
| `labels` | `array` | Labels to associate with this issue; pass one or more label names to replace the set of labels on this issue; send an empty array to clear all labels from the issue; note that the labels are silently dropped for users without push access to the repository |
| `body` | `string` | Contents of the issue |
| `url` | `string` | URL for the issue |
| `state` | `string` | State of the issue; either 'open' or 'closed' |
| `body_text` | `string` |  |
| `state_reason` | `string` | The reason for the current state |
| `closed_by` | `object` | A GitHub user. |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `html_url` | `string` |  |
| `closed_at` | `string` |  |
| `comments_url` | `string` |  |
| `pull_request` | `object` |  |
| `node_id` | `string` |  |
| `repository_url` | `string` |  |
| `comments` | `integer` |  |
| `draft` | `boolean` |  |
| `number` | `integer` | Number uniquely identifying the issue within its repository |
| `title` | `string` | Title of the issue |
| `timeline_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_for_authenticated_user` | `SELECT` |  |
