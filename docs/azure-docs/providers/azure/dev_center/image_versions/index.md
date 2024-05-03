---
title: image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - image_versions
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
<tr><td><b>Name</b></td><td><code>image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.dev_center.image_versions" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="devCenterName, galleryName, imageName, resourceGroupName, subscriptionId, versionName" /> | Gets an image version. |
| <CopyableCode code="list_by_image" /> | `SELECT` | <CopyableCode code="devCenterName, galleryName, imageName, resourceGroupName, subscriptionId" /> | Lists versions for an image. |
| <CopyableCode code="_list_by_image" /> | `EXEC` | <CopyableCode code="devCenterName, galleryName, imageName, resourceGroupName, subscriptionId" /> | Lists versions for an image. |
