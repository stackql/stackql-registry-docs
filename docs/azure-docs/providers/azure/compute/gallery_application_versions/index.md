---
title: gallery_application_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_application_versions
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
<tr><td><b>Name</b></td><td><code>gallery_application_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.compute.gallery_application_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="location" /> | `string` | Resource location |
| <CopyableCode code="properties" /> | `object` | Describes the properties of a gallery image version. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId" /> | Retrieves information about a gallery Application Version. |
| <CopyableCode code="list_by_gallery_application" /> | `SELECT` | <CopyableCode code="galleryApplicationName, galleryName, resourceGroupName, subscriptionId" /> | List gallery Application Versions in a gallery Application Definition. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId" /> | Create or update a gallery Application Version. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId" /> | Delete a gallery Application Version. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId" /> | Update a gallery Application Version. |
