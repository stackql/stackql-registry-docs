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
| `milestone` | `object` | A collection of related issues and pull requests. |
| `text_matches` | `array` |  |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `comments` | `integer` |  |
| `body_text` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `repository_url` | `string` |  |
| `assignee` | `object` | Simple User |
| `body_html` | `string` |  |
| `number` | `integer` |  |
| `active_lock_reason` | `string` |  |
| `updated_at` | `string` |  |
| `title` | `string` |  |
| `draft` | `boolean` |  |
| `assignees` | `array` |  |
| `locked` | `boolean` |  |
| `reactions` | `object` |  |
| `labels` | `array` |  |
| `node_id` | `string` |  |
| `closed_at` | `string` |  |
| `score` | `number` |  |
| `user` | `object` | Simple User |
| `repository` | `object` | A git repository |
| `body` | `string` |  |
| `url` | `string` |  |
| `state` | `string` |  |
| `comments_url` | `string` |  |
| `timeline_url` | `string` |  |
| `labels_url` | `string` |  |
| `events_url` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `pull_request` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `issues_and_pull_requests` | `SELECT` | `q` |
