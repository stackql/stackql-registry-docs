---
title: community_gallery_image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - community_gallery_image_versions
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
<tr><td><b>Name</b></td><td><code>community_gallery_image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.community_gallery_image_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="identifier" /> | `object` | The identifier information of community gallery. |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a gallery image version. |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryImageName, galleryImageVersionName, location, publicGalleryName, subscriptionId" /> | Get a community gallery image version. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="galleryImageName, location, publicGalleryName, subscriptionId" /> | List community gallery image versions inside an image. |
