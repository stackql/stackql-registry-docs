---
title: issues
hide_title: false
hide_table_of_contents: false
keywords:
  - issues
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
<tr><td><b>Name</b></td><td><code>issues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.issues</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `labels` | `array` | Labels to associate with this issue; pass one or more label names to replace the set of labels on this issue; send an empty array to clear all labels from the issue; note that the labels are silently dropped for users without push access to the repository |
| `user` | `object` | A GitHub user. |
| `body` | `string` | Contents of the issue |
| `assignees` | `array` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `title` | `string` | Title of the issue |
| `assignee` | `object` | A GitHub user. |
| `body_html` | `string` |  |
| `created_at` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `number` | `integer` | Number uniquely identifying the issue within its repository |
| `timeline_url` | `string` |  |
| `draft` | `boolean` |  |
| `html_url` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `labels_url` | `string` |  |
| `node_id` | `string` |  |
| `closed_by` | `object` | A GitHub user. |
| `active_lock_reason` | `string` |  |
| `body_text` | `string` |  |
| `reactions` | `object` |  |
| `repository_url` | `string` |  |
| `updated_at` | `string` |  |
| `events_url` | `string` |  |
| `closed_at` | `string` |  |
| `comments` | `integer` |  |
| `comments_url` | `string` |  |
| `repository` | `object` | A repository on GitHub. |
| `locked` | `boolean` |  |
| `state` | `string` | State of the issue; either 'open' or 'closed' |
| `url` | `string` | URL for the issue |
| `state_reason` | `string` | The reason for the current state |
| `pull_request` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` |  |
