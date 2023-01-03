---
title: sites_build_hooks
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
<tr><td><b>Name</b></td><td><code>sites_build_hooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.build_hook.sites_build_hooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `url` | `string` |
| `branch` | `string` |
| `created_at` | `string` |
| `site_id` | `string` |
| `title` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getSiteBuildHook` | `SELECT` | `id, site_id` |
| `listSiteBuildHooks` | `SELECT` | `site_id` |
| `createSiteBuildHook` | `INSERT` | `site_id` |
| `deleteSiteBuildHook` | `DELETE` | `id, site_id` |
| `updateSiteBuildHook` | `EXEC` | `id, site_id` |
