---
title: releases_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - releases_tags
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
<tr><td><b>Name</b></td><td><code>releases_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.releases_tags</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `name` | `string` |  |
| `zipball_url` | `string` |  |
| `draft` | `boolean` | true to create a draft (unpublished) release, false to create a published one. |
| `url` | `string` |  |
| `body` | `string` |  |
| `mentions_count` | `integer` |  |
| `target_commitish` | `string` | Specifies the commitish value that determines where the Git tag is created from. |
| `reactions` | `object` |  |
| `body_text` | `string` |  |
| `tarball_url` | `string` |  |
| `published_at` | `string` |  |
| `author` | `object` | A GitHub user. |
| `html_url` | `string` |  |
| `prerelease` | `boolean` | Whether to identify the release as a prerelease or a full release. |
| `assets` | `array` |  |
| `discussion_url` | `string` | The URL of the release discussion. |
| `tag_name` | `string` | The name of the tag. |
| `upload_url` | `string` |  |
| `body_html` | `string` |  |
| `assets_url` | `string` |  |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_release_by_tag` | `SELECT` | `owner, repo, tag` |
