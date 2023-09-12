---
title: orgs
hide_title: false
hide_table_of_contents: false
keywords:
  - orgs
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
<tr><td><b>Name</b></td><td><code>orgs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.orgs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `pull_request` | `object` |  |
| `closed_at` | `string` |  |
| `user` | `object` | A GitHub user. |
| `assignees` | `array` |  |
| `state` | `string` | State of the issue; either 'open' or 'closed' |
| `timeline_url` | `string` |  |
| `updated_at` | `string` |  |
| `events_url` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `draft` | `boolean` |  |
| `closed_by` | `object` | A GitHub user. |
| `body` | `string` | Contents of the issue |
| `reactions` | `object` |  |
| `body_text` | `string` |  |
| `comments` | `integer` |  |
| `labels_url` | `string` |  |
| `created_at` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `repository_url` | `string` |  |
| `state_reason` | `string` | The reason for the current state |
| `body_html` | `string` |  |
| `comments_url` | `string` |  |
| `repository` | `object` | A repository on GitHub. |
| `locked` | `boolean` |  |
| `html_url` | `string` |  |
| `active_lock_reason` | `string` |  |
| `number` | `integer` | Number uniquely identifying the issue within its repository |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `url` | `string` | URL for the issue |
| `node_id` | `string` |  |
| `title` | `string` | Title of the issue |
| `labels` | `array` | Labels to associate with this issue; pass one or more label names to replace the set of labels on this issue; send an empty array to clear all labels from the issue; note that the labels are silently dropped for users without push access to the repository |
| `assignee` | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_for_org` | `SELECT` | `org` |
