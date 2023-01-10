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
| `node_id` | `string` |  |
| `assignee` | `object` | Simple User |
| `draft` | `boolean` |  |
| `labels_url` | `string` |  |
| `active_lock_reason` | `string` |  |
| `timeline_url` | `string` |  |
| `repository` | `object` | A git repository |
| `body_html` | `string` |  |
| `assignees` | `array` |  |
| `html_url` | `string` |  |
| `comments` | `integer` |  |
| `labels` | `array` |  |
| `user` | `object` | Simple User |
| `text_matches` | `array` |  |
| `title` | `string` |  |
| `comments_url` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `reactions` | `object` |  |
| `pull_request` | `object` |  |
| `events_url` | `string` |  |
| `url` | `string` |  |
| `state` | `string` |  |
| `score` | `number` |  |
| `body_text` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `locked` | `boolean` |  |
| `closed_at` | `string` |  |
| `body` | `string` |  |
| `number` | `integer` |  |
| `updated_at` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `repository_url` | `string` |  |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `issues_and_pull_requests` | `SELECT` | `q` |
