---
title: platform_images
hide_title: false
hide_table_of_contents: false
keywords:
  - platform_images
  - compute_admin
  - azure_stack    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>platform_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_stack.compute_admin.platform_images" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | ID of the resource. |
| <CopyableCode code="name" /> | `string` | Name of the resource. |
| <CopyableCode code="location" /> | `string` | Location of the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of platform image. |
| <CopyableCode code="type" /> | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="location, offer, publisher, sku, subscriptionId, version" /> | Returns the specific platform image matching publisher, offer, skus and version. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Returns a list of all platform images. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="location, offer, publisher, sku, subscriptionId, version" /> | Creates a new platform image with given publisher, offer, skus and version. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="location, offer, publisher, sku, subscriptionId, version" /> | Delete a platform image |
