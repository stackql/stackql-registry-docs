---
title: releases_latest
hide_title: false
hide_table_of_contents: false
keywords:
  - releases_latest
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
<tr><td><b>Name</b></td><td><code>releases_latest</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.releases_latest</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `upload_url` | `string` |  |
| `node_id` | `string` |  |
| `mentions_count` | `integer` |  |
| `tag_name` | `string` | The name of the tag. |
| `published_at` | `string` |  |
| `url` | `string` |  |
| `assets_url` | `string` |  |
| `body_html` | `string` |  |
| `tarball_url` | `string` |  |
| `target_commitish` | `string` | Specifies the commitish value that determines where the Git tag is created from. |
| `author` | `object` | A GitHub user. |
| `reactions` | `object` |  |
| `draft` | `boolean` | true to create a draft (unpublished) release, false to create a published one. |
| `prerelease` | `boolean` | Whether to identify the release as a prerelease or a full release. |
| `body` | `string` |  |
| `discussion_url` | `string` | The URL of the release discussion. |
| `zipball_url` | `string` |  |
| `assets` | `array` |  |
| `created_at` | `string` |  |
| `body_text` | `string` |  |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_latest_release` | `SELECT` | `owner, repo` |
