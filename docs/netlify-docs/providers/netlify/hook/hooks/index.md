---
title: hooks
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
<tr><td><b>Name</b></td><td><code>hooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.hook.hooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `event` | `string` |
| `site_id` | `string` |
| `type` | `string` |
| `updated_at` | `string` |
| `created_at` | `string` |
| `data` | `object` |
| `disabled` | `boolean` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getHook` | `SELECT` | `hook_id` |
| `listHooksBySiteId` | `SELECT` | `site_id` |
| `createHookBySiteId` | `INSERT` | `site_id` |
| `deleteHook` | `DELETE` | `hook_id` |
| `updateHook` | `EXEC` | `hook_id` |
