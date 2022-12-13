---
title: access_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - access_connectors
  - databricks
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
<tr><td><b>Name</b></td><td><code>access_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.databricks.access_connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AccessConnectors_Get` | `SELECT` | `connectorName, resourceGroupName, subscriptionId` | Gets an azure databricks accessConnector. |
| `AccessConnectors_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the azure databricks accessConnectors within a resource group. |
| `AccessConnectors_ListBySubscription` | `SELECT` | `subscriptionId` | Gets all the azure databricks accessConnectors within a subscription. |
| `AccessConnectors_CreateOrUpdate` | `INSERT` | `connectorName, resourceGroupName, subscriptionId` | Creates or updates azure databricks accessConnector. |
| `AccessConnectors_Delete` | `DELETE` | `connectorName, resourceGroupName, subscriptionId` | Deletes the azure databricks accessConnector. |
| `AccessConnectors_Update` | `EXEC` | `connectorName, resourceGroupName, subscriptionId` | Updates an azure databricks accessConnector. |
