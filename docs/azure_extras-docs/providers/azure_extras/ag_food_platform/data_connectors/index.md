---
title: data_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - data_connectors
  - ag_food_platform
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
<tr><td><b>Name</b></td><td><code>data_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.ag_food_platform.data_connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `eTag` | `string` | The ETag value to implement optimistic concurrency. |
| `properties` | `object` | DataConnector Properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataConnectorName, dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId` | Get specific Data Connector resource by DataConnectorName. |
| `list` | `SELECT` | `dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId` | Lists the Data Connector Credentials for MADMA instance. |
| `create_or_update` | `INSERT` | `dataConnectorName, dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId, data__properties` | Create or update Data Connector For MADMA resource. |
| `delete` | `DELETE` | `dataConnectorName, dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId` | Delete a Data Connectors with given dataConnector name. |
| `_list` | `EXEC` | `dataManagerForAgricultureResourceName, resourceGroupName, subscriptionId` | Lists the Data Connector Credentials for MADMA instance. |
