---
title: monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - monitors
  - workloads
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
<tr><td><b>Name</b></td><td><code>monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.workloads.monitors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes the properties of a SAP monitor. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Managed service identity (user assigned identities) |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Get` | `SELECT` | `monitorName, resourceGroupName, subscriptionId` | Gets properties of a SAP monitor for the specified subscription, resource group, and resource name. |
| `List` | `SELECT` | `subscriptionId` | Gets a list of SAP monitors in the specified subscription. The operations returns various properties of each SAP monitor. |
| `ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of SAP monitors in the specified resource group. |
| `Create` | `INSERT` | `monitorName, resourceGroupName, subscriptionId` | Creates a SAP monitor for the specified subscription, resource group, and resource name. |
| `Delete` | `DELETE` | `monitorName, resourceGroupName, subscriptionId` | Deletes a SAP monitor with the specified subscription, resource group, and SAP monitor name. |
| `Update` | `EXEC` | `monitorName, resourceGroupName, subscriptionId` | Patches the Tags field of a SAP monitor for the specified subscription, resource group, and SAP monitor name. |
