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
| `author_association` | `string` | How the author is associated with the repository. |
| `pull_request` | `object` |  |
| `text_matches` | `array` |  |
| `events_url` | `string` |  |
| `title` | `string` |  |
| `comments_url` | `string` |  |
| `number` | `integer` |  |
| `active_lock_reason` | `string` |  |
| `score` | `number` |  |
| `node_id` | `string` |  |
| `body` | `string` |  |
| `updated_at` | `string` |  |
| `locked` | `boolean` |  |
| `repository_url` | `string` |  |
| `repository` | `object` | A git repository |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `created_at` | `string` |  |
| `assignee` | `object` | Simple User |
| `state` | `string` |  |
| `timeline_url` | `string` |  |
| `user` | `object` | Simple User |
| `body_text` | `string` |  |
| `reactions` | `object` |  |
| `labels_url` | `string` |  |
| `draft` | `boolean` |  |
| `html_url` | `string` |  |
| `url` | `string` |  |
| `labels` | `array` |  |
| `comments` | `integer` |  |
| `body_html` | `string` |  |
| `assignees` | `array` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `closed_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `issues_and_pull_requests` | `SELECT` | `q` |
