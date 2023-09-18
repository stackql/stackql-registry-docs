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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>issues_and_pull_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.search.issues_and_pull_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `body_html` | `string` |  |
| `labels` | `array` |  |
| `html_url` | `string` |  |
| `state_reason` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `assignees` | `array` |  |
| `assignee` | `object` | A GitHub user. |
| `pull_request` | `object` |  |
| `active_lock_reason` | `string` |  |
| `repository` | `object` | A repository on GitHub. |
| `comments` | `integer` |  |
| `events_url` | `string` |  |
| `updated_at` | `string` |  |
| `text_matches` | `array` |  |
| `score` | `number` |  |
| `locked` | `boolean` |  |
| `reactions` | `object` |  |
| `title` | `string` |  |
| `user` | `object` | A GitHub user. |
| `timeline_url` | `string` |  |
| `state` | `string` |  |
| `draft` | `boolean` |  |
| `closed_at` | `string` |  |
| `repository_url` | `string` |  |
| `labels_url` | `string` |  |
| `url` | `string` |  |
| `body_text` | `string` |  |
| `node_id` | `string` |  |
| `body` | `string` |  |
| `comments_url` | `string` |  |
| `number` | `integer` |  |
| `created_at` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `issues_and_pull_requests` | `SELECT` | `q` |
