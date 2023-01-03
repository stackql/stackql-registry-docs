---
title: topics
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
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.search.topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `name` | `string` |
| `description` | `string` |
| `curated` | `boolean` |
| `short_description` | `string` |
| `created_by` | `string` |
| `featured` | `boolean` |
| `text_matches` | `array` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `repository_count` | `integer` |
| `logo_url` | `string` |
| `released` | `string` |
| `related` | `array` |
| `score` | `number` |
| `aliases` | `array` |
| `display_name` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `topics` | `SELECT` | `q` |
