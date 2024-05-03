---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - dev_center
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
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.images" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="devCenterName, galleryName, imageName, resourceGroupName, subscriptionId" /> | Gets a gallery image. |
| <CopyableCode code="list_by_dev_center" /> | `SELECT` | <CopyableCode code="devCenterName, resourceGroupName, subscriptionId" /> | Lists images for a devcenter. |
| <CopyableCode code="list_by_gallery" /> | `SELECT` | <CopyableCode code="devCenterName, galleryName, resourceGroupName, subscriptionId" /> | Lists images for a gallery. |
| <CopyableCode code="_list_by_dev_center" /> | `EXEC` | <CopyableCode code="devCenterName, resourceGroupName, subscriptionId" /> | Lists images for a devcenter. |
| <CopyableCode code="_list_by_gallery" /> | `EXEC` | <CopyableCode code="devCenterName, galleryName, resourceGroupName, subscriptionId" /> | Lists images for a gallery. |
