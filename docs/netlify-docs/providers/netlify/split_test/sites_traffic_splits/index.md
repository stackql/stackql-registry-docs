---
title: sites_traffic_splits
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_traffic_splits
  - split_test
  - netlify    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Netlify resources using SQL
custom_edit_url: null
image: /img/providers/netlify/stackql-netlify-provider-featured-image.png
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
| `path` | `string` |
| `branches` | `array` |
| `updated_at` | `string` |
| `site_id` | `string` |
| `active` | `boolean` |
| `created_at` | `string` |
| `unpublished_at` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getSplitTest` | `SELECT` | `site_id, split_test_id` |
| `getSplitTests` | `SELECT` | `site_id` |
| `createSplitTest` | `INSERT` | `site_id` |
| `updateSplitTest` | `EXEC` | `site_id, split_test_id` |
