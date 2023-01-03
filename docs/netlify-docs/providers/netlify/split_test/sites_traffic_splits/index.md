---
title: sites_traffic_splits
hide_title: false
hide_table_of_contents: false
keywords:
  - netlify
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sites_traffic_splits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.split_test.sites_traffic_splits</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `created_at` | `string` |
| `updated_at` | `string` |
| `site_id` | `string` |
| `unpublished_at` | `string` |
| `path` | `string` |
| `active` | `boolean` |
| `branches` | `array` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getSplitTest` | `SELECT` | `site_id, split_test_id` |
| `getSplitTests` | `SELECT` | `site_id` |
| `createSplitTest` | `INSERT` | `site_id` |
| `updateSplitTest` | `EXEC` | `site_id, split_test_id` |
