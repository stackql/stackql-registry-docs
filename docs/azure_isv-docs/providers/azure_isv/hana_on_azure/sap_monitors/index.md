---
title: sap_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - sap_monitors
  - hana_on_azure
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
<tr><td><b>Name</b></td><td><code>sap_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.hana_on_azure.sap_monitors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Describes the properties of a SAP monitor. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, sapMonitorName, subscriptionId` | Gets properties of a SAP monitor for the specified subscription, resource group, and resource name. |
| `list` | `SELECT` | `subscriptionId` | Gets a list of SAP monitors in the specified subscription. The operations returns various properties of each SAP monitor. |
| `create` | `INSERT` | `resourceGroupName, sapMonitorName, subscriptionId` | Creates a SAP monitor for the specified subscription, resource group, and resource name. |
| `delete` | `DELETE` | `resourceGroupName, sapMonitorName, subscriptionId` | Deletes a SAP monitor with the specified subscription, resource group, and monitor name. |
| `_list` | `EXEC` | `subscriptionId` | Gets a list of SAP monitors in the specified subscription. The operations returns various properties of each SAP monitor. |
| `update` | `EXEC` | `resourceGroupName, sapMonitorName, subscriptionId` | Patches the Tags field of a SAP monitor for the specified subscription, resource group, and monitor name. |
