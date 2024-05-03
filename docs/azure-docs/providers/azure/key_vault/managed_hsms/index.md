---
title: managed_hsms
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_hsms
  - key_vault
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
<tr><td><b>Name</b></td><td><code>managed_hsms</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.key_vault.managed_hsms" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Azure Resource Manager resource ID for the managed HSM Pool. |
| <CopyableCode code="name" /> | `string` | The name of the managed HSM Pool. |
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The supported Azure location where the managed HSM Pool should be created. |
| <CopyableCode code="properties" /> | `object` | Properties of the managed HSM Pool |
| <CopyableCode code="sku" /> | `object` | SKU details |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the key vault resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags |
| <CopyableCode code="type" /> | `string` | The resource type of the managed HSM Pool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Gets the specified managed HSM Pool. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List operation gets information about the managed HSM Pools associated with the subscription and within the specified resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | The List operation gets information about the managed HSM Pools associated with the subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Create or update a managed HSM Pool in the specified subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Deletes the specified managed HSM Pool. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | The List operation gets information about the managed HSM Pools associated with the subscription and within the specified resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | The List operation gets information about the managed HSM Pools associated with the subscription. |
| <CopyableCode code="check_mhsm_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name" /> | Checks that the managed hsm name is valid and is not already in use. |
| <CopyableCode code="purge_deleted" /> | `EXEC` | <CopyableCode code="location, name, subscriptionId" /> | Permanently deletes the specified managed HSM. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Update a managed HSM Pool in the specified subscription. |
