---
title: issues_and_pull_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `comments_url` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `updated_at` | `string` |  |
| `events_url` | `string` |  |
| `score` | `number` |  |
| `url` | `string` |  |
| `body_html` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `assignee` | `object` | Simple User |
| `body_text` | `string` |  |
| `pull_request` | `object` |  |
| `body` | `string` |  |
| `labels` | `array` |  |
| `labels_url` | `string` |  |
| `node_id` | `string` |  |
| `locked` | `boolean` |  |
| `repository_url` | `string` |  |
| `repository` | `object` | A git repository |
| `title` | `string` |  |
| `user` | `object` | Simple User |
| `author_association` | `string` | How the author is associated with the repository. |
| `comments` | `integer` |  |
| `assignees` | `array` |  |
| `timeline_url` | `string` |  |
| `active_lock_reason` | `string` |  |
| `text_matches` | `array` |  |
| `draft` | `boolean` |  |
| `number` | `integer` |  |
| `state` | `string` |  |
| `html_url` | `string` |  |
| `reactions` | `object` |  |
| `created_at` | `string` |  |
| `closed_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `issues_and_pull_requests` | `SELECT` | `q` |
