---
title: sites_assets
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_assets
  - asset
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
<tr><td><b>Name</b></td><td><code>sites_assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>netlify.asset.sites_assets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `string` |
| `name` | `string` |
| `created_at` | `string` |
| `creator_id` | `string` |
| `updated_at` | `string` |
| `url` | `string` |
| `visibility` | `string` |
| `size` | `integer` |
| `state` | `string` |
| `content_type` | `string` |
| `site_id` | `string` |
| `key` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getSiteAssetInfo` | `SELECT` | `asset_id, site_id` |
| `listSiteAssets` | `SELECT` | `site_id` |
| `createSiteAsset` | `INSERT` | `site_id` |
| `deleteSiteAsset` | `DELETE` | `asset_id, site_id` |
| `updateSiteAsset` | `EXEC` | `asset_id, site_id` |
