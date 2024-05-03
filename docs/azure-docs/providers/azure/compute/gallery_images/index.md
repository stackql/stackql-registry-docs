---
title: gallery_images
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_images
  - compute
  - azure    
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
<tr><td><b>Name</b></td><td><code>gallery_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.gallery_images" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a gallery image definition. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryImageName, galleryName, resourceGroupName, subscriptionId" /> | Retrieves information about a gallery image definition. |
| <CopyableCode code="list_by_gallery" /> | `SELECT` | <CopyableCode code="galleryName, resourceGroupName, subscriptionId" /> | List gallery image definitions in a gallery. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="galleryImageName, galleryName, resourceGroupName, subscriptionId" /> | Create or update a gallery image definition. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="galleryImageName, galleryName, resourceGroupName, subscriptionId" /> | Delete a gallery image. |
| <CopyableCode code="_list_by_gallery" /> | `EXEC` | <CopyableCode code="galleryName, resourceGroupName, subscriptionId" /> | List gallery image definitions in a gallery. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="galleryImageName, galleryName, resourceGroupName, subscriptionId" /> | Update a gallery image definition. |
