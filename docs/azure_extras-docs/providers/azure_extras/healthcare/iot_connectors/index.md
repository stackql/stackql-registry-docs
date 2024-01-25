---
title: iot_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_connectors
  - healthcare
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
<tr><td><b>Name</b></td><td><code>iot_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.healthcare.iot_connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Setting indicating whether the service has a managed identity associated with it. |
| `properties` | `object` | IoT Connector properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `iotConnectorName, resourceGroupName, subscriptionId, workspaceName` | Gets the properties of the specified IoT Connector. |
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Lists all IoT Connectors for the given workspace |
| `create_or_update` | `INSERT` | `iotConnectorName, resourceGroupName, subscriptionId, workspaceName` | Creates or updates an IoT Connector resource with the specified parameters. |
| `delete` | `DELETE` | `iotConnectorName, resourceGroupName, subscriptionId, workspaceName` | Deletes an IoT Connector. |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Lists all IoT Connectors for the given workspace |
| `update` | `EXEC` | `iotConnectorName, resourceGroupName, subscriptionId, workspaceName` | Patch an IoT Connector. |
