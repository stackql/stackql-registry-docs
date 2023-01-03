---
title: latest_releases
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
<tr><td><b>Name</b></td><td><code>latest_releases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.latest_releases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `body` | `string` |  |
| `draft` | `boolean` | true to create a draft (unpublished) release, false to create a published one. |
| `mentions_count` | `integer` |  |
| `discussion_url` | `string` | The URL of the release discussion. |
| `assets_url` | `string` |  |
| `node_id` | `string` |  |
| `author` | `object` | Simple User |
| `reactions` | `object` |  |
| `target_commitish` | `string` | Specifies the commitish value that determines where the Git tag is created from. |
| `prerelease` | `boolean` | Whether to identify the release as a prerelease or a full release. |
| `body_html` | `string` |  |
| `tag_name` | `string` | The name of the tag. |
| `created_at` | `string` |  |
| `published_at` | `string` |  |
| `upload_url` | `string` |  |
| `url` | `string` |  |
| `tarball_url` | `string` |  |
| `html_url` | `string` |  |
| `zipball_url` | `string` |  |
| `assets` | `array` |  |
| `body_text` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_latest_release` | `SELECT` | `owner, repo` |
