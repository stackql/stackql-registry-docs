---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
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
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `timeline_url` | `string` |  |
| `state_reason` | `string` | The reason for the current state |
| `state` | `string` | State of the issue; either 'open' or 'closed' |
| `reactions` | `object` |  |
| `labels_url` | `string` |  |
| `closed_by` | `object` | A GitHub user. |
| `body` | `string` | Contents of the issue |
| `html_url` | `string` |  |
| `closed_at` | `string` |  |
| `url` | `string` | URL for the issue |
| `number` | `integer` | Number uniquely identifying the issue within its repository |
| `locked` | `boolean` |  |
| `draft` | `boolean` |  |
| `node_id` | `string` |  |
| `body_html` | `string` |  |
| `body_text` | `string` |  |
| `updated_at` | `string` |  |
| `events_url` | `string` |  |
| `assignee` | `object` | A GitHub user. |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `repository` | `object` | A repository on GitHub. |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `title` | `string` | Title of the issue |
| `assignees` | `array` |  |
| `comments_url` | `string` |  |
| `comments` | `integer` |  |
| `user` | `object` | A GitHub user. |
| `labels` | `array` | Labels to associate with this issue; pass one or more label names to replace the set of labels on this issue; send an empty array to clear all labels from the issue; note that the labels are silently dropped for users without push access to the repository |
| `created_at` | `string` |  |
| `active_lock_reason` | `string` |  |
| `pull_request` | `object` |  |
| `repository_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_for_authenticated_user` | `SELECT` |  |
