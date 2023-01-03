---
title: community
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
<tr><td><b>Name</b></td><td><code>community</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.community</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `description` | `string` |
| `updated_at` | `string` |
| `content_reports_enabled` | `boolean` |
| `documentation` | `string` |
| `files` | `object` |
| `health_percentage` | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_community_profile_metrics` | `SELECT` | `owner, repo` |
