---
title: capacities
hide_title: false
hide_table_of_contents: false
keywords:
  - capacities
  - powerbi_dedicated
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
<tr><td><b>Name</b></td><td><code>capacities</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.powerbi_dedicated.capacities" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | An identifier that represents the PowerBI Dedicated resource. |
| <CopyableCode code="name" /> | `string` | The name of the PowerBI Dedicated resource. |
| <CopyableCode code="location" /> | `string` | Location of the PowerBI Dedicated resource. |
| <CopyableCode code="properties" /> | `object` | Properties of Dedicated Capacity resource. |
| <CopyableCode code="sku" /> | `object` | Represents the SKU name and Azure pricing tier for PowerBI Dedicated capacity resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Key-value pairs of additional resource provisioning properties. |
| <CopyableCode code="type" /> | `string` | The type of the PowerBI Dedicated resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Lists all the Dedicated capacities for the given subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the Dedicated capacities for the given resource group. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="dedicatedCapacityName, resourceGroupName, subscriptionId, data__sku" /> | Provisions the specified Dedicated capacity based on the configuration specified in the request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dedicatedCapacityName, resourceGroupName, subscriptionId" /> | Deletes the specified Dedicated capacity. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Lists all the Dedicated capacities for the given subscription. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets all the Dedicated capacities for the given resource group. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="location, subscriptionId" /> | Check the name availability in the target location. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="dedicatedCapacityName, resourceGroupName, subscriptionId" /> | Resumes operation of the specified Dedicated capacity instance. |
| <CopyableCode code="suspend" /> | `EXEC` | <CopyableCode code="dedicatedCapacityName, resourceGroupName, subscriptionId" /> | Suspends operation of the specified dedicated capacity instance. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="dedicatedCapacityName, resourceGroupName, subscriptionId" /> | Updates the current state of the specified Dedicated capacity. |
