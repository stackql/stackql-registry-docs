---
title: dedicated_hsm
hide_title: false
hide_table_of_contents: false
keywords:
  - dedicated_hsm
  - hardware_security_modules
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
<tr><td><b>Name</b></td><td><code>dedicated_hsm</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hardware_security_modules.dedicated_hsm" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Azure Resource Manager resource ID for the dedicated HSM. |
| <CopyableCode code="name" /> | `string` | The name of the dedicated HSM. |
| <CopyableCode code="location" /> | `string` | The supported Azure location where the dedicated HSM should be created. |
| <CopyableCode code="properties" /> | `object` | Properties of the dedicated hsm |
| <CopyableCode code="sku" /> | `object` | SKU of the dedicated HSM |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of dedicated hsm resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | The resource type of the dedicated HSM. |
| <CopyableCode code="zones" /> | `array` | The Dedicated Hsm zones. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Gets the specified Azure dedicated HSM. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List operation gets information about the dedicated hsms associated with the subscription and within the specified resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The List operation gets information about the dedicated HSMs associated with the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__location, data__properties, data__sku" /> | Create or Update a dedicated HSM in the specified subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Deletes the specified Azure Dedicated HSM. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Update a dedicated HSM in the specified subscription. |
