---
title: latest_releases
hide_title: false
hide_table_of_contents: false
keywords:
  - latest_releases
  - repos
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
<tr><td><b>Name</b></td><td><code>latest_releases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.latest_releases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `mentions_count` | `integer` |  |
| `node_id` | `string` |  |
| `body` | `string` |  |
| `draft` | `boolean` | true to create a draft (unpublished) release, false to create a published one. |
| `target_commitish` | `string` | Specifies the commitish value that determines where the Git tag is created from. |
| `assets_url` | `string` |  |
| `prerelease` | `boolean` | Whether to identify the release as a prerelease or a full release. |
| `published_at` | `string` |  |
| `tag_name` | `string` | The name of the tag. |
| `tarball_url` | `string` |  |
| `assets` | `array` |  |
| `upload_url` | `string` |  |
| `created_at` | `string` |  |
| `body_text` | `string` |  |
| `body_html` | `string` |  |
| `author` | `object` | Simple User |
| `url` | `string` |  |
| `discussion_url` | `string` | The URL of the release discussion. |
| `reactions` | `object` |  |
| `html_url` | `string` |  |
| `zipball_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_latest_release` | `SELECT` | `owner, repo` |
