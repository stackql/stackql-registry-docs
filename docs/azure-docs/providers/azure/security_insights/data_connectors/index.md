---
title: data_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - data_connectors
  - security_insights
  - azure    
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
<tr><td><b>Name</b></td><td><code>data_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_insights.data_connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Etag of the azure resource |
| `kind` | `string` | The kind of the data connector |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DataConnectors_Get` | `SELECT` | `dataConnectorId, resourceGroupName, subscriptionId, workspaceName` | Gets a data connector. |
| `DataConnectors_List` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all data connectors. |
| `DataConnectors_CreateOrUpdate` | `INSERT` | `dataConnectorId, resourceGroupName, subscriptionId, workspaceName, data__kind` | Creates or updates the data connector. |
| `DataConnectors_Delete` | `DELETE` | `dataConnectorId, resourceGroupName, subscriptionId, workspaceName` | Delete the data connector. |
| `DataConnectors_Connect` | `EXEC` | `dataConnectorId, resourceGroupName, subscriptionId, workspaceName` | Connects a data connector. |
| `DataConnectors_Disconnect` | `EXEC` | `dataConnectorId, resourceGroupName, subscriptionId, workspaceName` | Disconnect a data connector. |
