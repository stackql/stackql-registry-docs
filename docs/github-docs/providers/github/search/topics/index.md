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
| `related` | `array` |
| `score` | `number` |
| `short_description` | `string` |
| `created_at` | `string` |
| `featured` | `boolean` |
| `curated` | `boolean` |
| `repository_count` | `integer` |
| `logo_url` | `string` |
| `text_matches` | `array` |
| `display_name` | `string` |
| `created_by` | `string` |
| `released` | `string` |
| `aliases` | `array` |
| `updated_at` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `topics` | `SELECT` | `q` |
