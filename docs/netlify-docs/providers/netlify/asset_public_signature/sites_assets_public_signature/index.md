---
title: sites_assets_public_signature
hide_title: false
hide_table_of_contents: false
keywords:
  - sites_assets_public_signature
  - asset_public_signature
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
<tr><td><b>Name</b></td><td><code>sites_assets_public_signature</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="netlify.asset_public_signature.sites_assets_public_signature" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getSiteAssetPublicSignature" /> | `SELECT` | <CopyableCode code="asset_id, site_id" /> |
