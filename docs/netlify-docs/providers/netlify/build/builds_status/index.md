---
title: builds_status
hide_title: false
hide_table_of_contents: false
keywords:
  - builds_status
  - build
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
<tr><td><b>Name</b></td><td><code>builds_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.build.builds_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `active` | `integer` |
| `build_count` | `integer` |
| `enqueued` | `integer` |
| `minutes` | `object` |
| `pending_concurrency` | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getAccountBuildStatus` | `SELECT` | `account_id` |
