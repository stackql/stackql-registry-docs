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
| `number` | `integer` |  |
| `draft` | `boolean` |  |
| `updated_at` | `string` |  |
| `repository` | `object` | A git repository |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `user` | `object` | Simple User |
| `reactions` | `object` |  |
| `state` | `string` |  |
| `assignees` | `array` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `body_text` | `string` |  |
| `active_lock_reason` | `string` |  |
| `url` | `string` |  |
| `comments_url` | `string` |  |
| `created_at` | `string` |  |
| `closed_at` | `string` |  |
| `node_id` | `string` |  |
| `locked` | `boolean` |  |
| `events_url` | `string` |  |
| `pull_request` | `object` |  |
| `repository_url` | `string` |  |
| `labels_url` | `string` |  |
| `labels` | `array` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `title` | `string` |  |
| `score` | `number` |  |
| `comments` | `integer` |  |
| `body_html` | `string` |  |
| `text_matches` | `array` |  |
| `body` | `string` |  |
| `html_url` | `string` |  |
| `assignee` | `object` | Simple User |
| `timeline_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `issues_and_pull_requests` | `SELECT` | `q` |
