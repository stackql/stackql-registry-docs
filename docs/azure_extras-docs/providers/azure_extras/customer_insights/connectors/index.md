---
title: connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - connectors
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
<tr><td><b>Name</b></td><td><code>connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.customer_insights.connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `type` | `string` | Resource type. |
| `properties` | `object` | Properties of connector. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Connectors_Get` | `SELECT` | `connectorName, hubName, resourceGroupName, subscriptionId` | Gets a connector in the hub. |
| `Connectors_ListByHub` | `SELECT` | `hubName, resourceGroupName, subscriptionId` | Gets all the connectors in the specified hub. |
| `Connectors_CreateOrUpdate` | `INSERT` | `connectorName, hubName, resourceGroupName, subscriptionId` | Creates a connector or updates an existing connector in the hub. |
| `Connectors_Delete` | `DELETE` | `connectorName, hubName, resourceGroupName, subscriptionId` | Deletes a connector in the hub. |
