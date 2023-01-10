---
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
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
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.search.topics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `name` | `string` |
| `description` | `string` |
| `text_matches` | `array` |
| `short_description` | `string` |
| `repository_count` | `integer` |
| `display_name` | `string` |
| `score` | `number` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `curated` | `boolean` |
| `aliases` | `array` |
| `released` | `string` |
| `logo_url` | `string` |
| `created_by` | `string` |
| `related` | `array` |
| `featured` | `boolean` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `topics` | `SELECT` | `q` |
