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
| `tag_name` | `string` | The name of the tag. |
| `node_id` | `string` |  |
| `body` | `string` |  |
| `assets` | `array` |  |
| `target_commitish` | `string` | Specifies the commitish value that determines where the Git tag is created from. |
| `created_at` | `string` |  |
| `published_at` | `string` |  |
| `mentions_count` | `integer` |  |
| `body_html` | `string` |  |
| `zipball_url` | `string` |  |
| `url` | `string` |  |
| `body_text` | `string` |  |
| `prerelease` | `boolean` | Whether to identify the release as a prerelease or a full release. |
| `author` | `object` | A GitHub user. |
| `tarball_url` | `string` |  |
| `upload_url` | `string` |  |
| `html_url` | `string` |  |
| `draft` | `boolean` | true to create a draft (unpublished) release, false to create a published one. |
| `reactions` | `object` |  |
| `discussion_url` | `string` | The URL of the release discussion. |
| `assets_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_latest_release` | `SELECT` | `owner, repo` |
