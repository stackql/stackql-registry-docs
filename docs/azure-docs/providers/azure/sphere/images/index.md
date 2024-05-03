---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - sphere
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
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sphere.images" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="catalogName, imageName, resourceGroupName, subscriptionId" /> | Get a Image |
| <CopyableCode code="list_by_catalog" /> | `SELECT` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | List Image resources by Catalog |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="catalogName, imageName, resourceGroupName, subscriptionId" /> | Create a Image |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="catalogName, imageName, resourceGroupName, subscriptionId" /> | Delete a Image |
| <CopyableCode code="_list_by_catalog" /> | `EXEC` | <CopyableCode code="catalogName, resourceGroupName, subscriptionId" /> | List Image resources by Catalog |
