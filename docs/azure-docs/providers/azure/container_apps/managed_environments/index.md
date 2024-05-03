---
title: managed_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_environments
  - container_apps
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
<tr><td><b>Name</b></td><td><code>managed_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.managed_environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | Kind of the Environment. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Managed environment resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Get the properties of a Managed Environment used to host container apps. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the Managed Environments in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all Managed Environments for a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Creates or updates a Managed Environment used to host container apps. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Delete a Managed Environment if it does not have any container apps. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all the Managed Environments in a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Get all Managed Environments for a subscription. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="environmentName, resourceGroupName, subscriptionId" /> | Patches a Managed Environment using JSON Merge Patch |
