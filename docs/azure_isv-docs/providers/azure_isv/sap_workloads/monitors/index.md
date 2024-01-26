---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - sap_workloads
  - azure_isv    
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
<tr><td><b>Name</b></td><td><code>monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.sap_workloads.monitors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | A pre-created user assigned identity with appropriate roles assigned. To learn more on identity and roles required, visit the ACSS how-to-guide. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes the properties of a SAP monitor. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` | Gets properties of a SAP monitor for the specified subscription, resource group, and resource name. |
| `list` | `SELECT` | `subscriptionId` | Gets a list of SAP monitors in the specified subscription. The operations returns various properties of each SAP monitor. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of SAP monitors in the specified resource group. |
| `create` | `INSERT` | `monitorName, resourceGroupName, subscriptionId` | Creates a SAP monitor for the specified subscription, resource group, and resource name. |
| `delete` | `DELETE` | `monitorName, resourceGroupName, subscriptionId` | Deletes a SAP monitor with the specified subscription, resource group, and SAP monitor name. |
| `_list` | `EXEC` | `subscriptionId` | Gets a list of SAP monitors in the specified subscription. The operations returns various properties of each SAP monitor. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets a list of SAP monitors in the specified resource group. |
| `update` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` | Patches the Tags field of a SAP monitor for the specified subscription, resource group, and SAP monitor name. |
