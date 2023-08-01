---
title: service_fabrics
hide_title: false
hide_table_of_contents: false
keywords:
  - service_fabrics
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
<tr><td><b>Name</b></td><td><code>service_fabrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_test_labs.service_fabrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Properties of a service fabric. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ServiceFabrics_Get` | `SELECT` | `api-version, labName, name, resourceGroupName, subscriptionId, userName` | Get service fabric. |
| `ServiceFabrics_List` | `SELECT` | `api-version, labName, resourceGroupName, subscriptionId, userName` | List service fabrics in a given user profile. |
| `ServiceFabrics_CreateOrUpdate` | `INSERT` | `api-version, labName, name, resourceGroupName, subscriptionId, userName, data__properties` | Create or replace an existing service fabric. This operation can take a while to complete. |
| `ServiceFabrics_Delete` | `DELETE` | `api-version, labName, name, resourceGroupName, subscriptionId, userName` | Delete service fabric. This operation can take a while to complete. |
| `ServiceFabrics_ListApplicableSchedules` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId, userName` | Lists the applicable start/stop schedules, if any. |
| `ServiceFabrics_Start` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId, userName` | Start a service fabric. This operation can take a while to complete. |
| `ServiceFabrics_Stop` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId, userName` | Stop a service fabric This operation can take a while to complete. |
| `ServiceFabrics_Update` | `EXEC` | `api-version, labName, name, resourceGroupName, subscriptionId, userName` | Allows modifying tags of service fabrics. All other properties will be ignored. |
