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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sites_assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.asset.sites_assets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `string` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="content_type" /> | `string` |
| <CopyableCode code="created_at" /> | `string` |
| <CopyableCode code="creator_id" /> | `string` |
| <CopyableCode code="key" /> | `string` |
| <CopyableCode code="site_id" /> | `string` |
| <CopyableCode code="size" /> | `integer` |
| <CopyableCode code="state" /> | `string` |
| <CopyableCode code="updated_at" /> | `string` |
| <CopyableCode code="url" /> | `string` |
| <CopyableCode code="visibility" /> | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getSiteAssetInfo" /> | `SELECT` | <CopyableCode code="asset_id, site_id" /> |
| <CopyableCode code="listSiteAssets" /> | `SELECT` | <CopyableCode code="site_id" /> |
| <CopyableCode code="createSiteAsset" /> | `INSERT` | <CopyableCode code="site_id" /> |
| <CopyableCode code="deleteSiteAsset" /> | `DELETE` | <CopyableCode code="asset_id, site_id" /> |
| <CopyableCode code="updateSiteAsset" /> | `EXEC` | <CopyableCode code="asset_id, site_id" /> |
