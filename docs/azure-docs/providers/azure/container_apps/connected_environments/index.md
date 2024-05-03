---
title: connected_environments
hide_title: false
hide_table_of_contents: false
keywords:
  - connected_environments
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
<tr><td><b>Name</b></td><td><code>connected_environments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.container_apps.connected_environments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | The complex type of the extended location. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | ConnectedEnvironment resource specific properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Get the properties of an connectedEnvironment. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all connectedEnvironments in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Get all connectedEnvironments for a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Creates or updates an connectedEnvironment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Delete an connectedEnvironment. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Get all connectedEnvironments in a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="subscriptionId" /> | Get all connectedEnvironments for a subscription. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Checks if resource connectedEnvironmentName is available. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="connectedEnvironmentName, resourceGroupName, subscriptionId" /> | Patches a Managed Environment. Only patching of tags is supported currently |
