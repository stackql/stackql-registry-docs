---
title: connector_mappings
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_mappings
  - customer_insights
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
<tr><td><b>Name</b></td><td><code>connector_mappings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.connector_mappings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | The connector mapping definition. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectorName, hubName, mappingName, resourceGroupName, subscriptionId` | Gets a connector mapping in the connector. |
| `list_by_connector` | `SELECT` | `connectorName, hubName, resourceGroupName, subscriptionId` | Gets all the connector mappings in the specified connector. |
| `create_or_update` | `INSERT` | `connectorName, hubName, mappingName, resourceGroupName, subscriptionId` | Creates a connector mapping or updates an existing connector mapping in the connector. |
| `delete` | `DELETE` | `connectorName, hubName, mappingName, resourceGroupName, subscriptionId` | Deletes a connector mapping in the connector. |
| `_list_by_connector` | `EXEC` | `connectorName, hubName, resourceGroupName, subscriptionId` | Gets all the connector mappings in the specified connector. |
