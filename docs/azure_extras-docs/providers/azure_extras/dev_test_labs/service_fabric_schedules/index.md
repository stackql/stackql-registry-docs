---
title: service_fabric_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - service_fabric_schedules
  - dev_test_labs
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>service_fabric_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_test_labs.service_fabric_schedules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Properties of a schedule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServiceFabricSchedules_Get` | `SELECT` | `api-version, labName, name, resourceGroupName, serviceFabricName, subscriptionId, userName` | Get schedule. |
| `ServiceFabricSchedules_List` | `SELECT` | `api-version, labName, resourceGroupName, serviceFabricName, subscriptionId, userName` | List schedules in a given service fabric. |
| `ServiceFabricSchedules_CreateOrUpdate` | `INSERT` | `api-version, labName, name, resourceGroupName, serviceFabricName, subscriptionId, userName, data__properties` | Create or replace an existing schedule. |
| `ServiceFabricSchedules_Delete` | `DELETE` | `api-version, labName, name, resourceGroupName, serviceFabricName, subscriptionId, userName` | Delete schedule. |
| `ServiceFabricSchedules_Execute` | `EXEC` | `api-version, labName, name, resourceGroupName, serviceFabricName, subscriptionId, userName` | Execute a schedule. This operation can take a while to complete. |
| `ServiceFabricSchedules_Update` | `EXEC` | `api-version, labName, name, resourceGroupName, serviceFabricName, subscriptionId, userName` | Allows modifying tags of schedules. All other properties will be ignored. |
