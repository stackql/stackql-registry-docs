---
title: community_gallery_images
hide_title: false
hide_table_of_contents: false
keywords:
  - community_gallery_images
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
<tr><td><b>Name</b></td><td><code>community_gallery_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.community_gallery_images" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="identifier" /> | `object` | The identifier information of community gallery. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a gallery image definition. |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryImageName, location, publicGalleryName, subscriptionId" /> | Get a community gallery image. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, publicGalleryName, subscriptionId" /> | List community gallery images inside a gallery. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="location, publicGalleryName, subscriptionId" /> | List community gallery images inside a gallery. |
