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
| `published_at` | `string` |  |
| `reactions` | `object` |  |
| `body` | `string` |  |
| `draft` | `boolean` | true to create a draft (unpublished) release, false to create a published one. |
| `url` | `string` |  |
| `node_id` | `string` |  |
| `author` | `object` | Simple User |
| `created_at` | `string` |  |
| `mentions_count` | `integer` |  |
| `prerelease` | `boolean` | Whether to identify the release as a prerelease or a full release. |
| `upload_url` | `string` |  |
| `assets` | `array` |  |
| `tarball_url` | `string` |  |
| `body_html` | `string` |  |
| `tag_name` | `string` | The name of the tag. |
| `body_text` | `string` |  |
| `assets_url` | `string` |  |
| `discussion_url` | `string` | The URL of the release discussion. |
| `zipball_url` | `string` |  |
| `target_commitish` | `string` | Specifies the commitish value that determines where the Git tag is created from. |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_latest_release` | `SELECT` | `owner, repo` |
