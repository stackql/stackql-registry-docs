---
title: access_connectors
hide_title: false
hide_table_of_contents: false
keywords:
  - access_connectors
  - databricks
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
<tr><td><b>Name</b></td><td><code>access_connectors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_isv.databricks.access_connectors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectorName, resourceGroupName, subscriptionId` | Gets an azure databricks accessConnector. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the azure databricks accessConnectors within a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets all the azure databricks accessConnectors within a subscription. |
| `create_or_update` | `INSERT` | `connectorName, resourceGroupName, subscriptionId` | Creates or updates azure databricks accessConnector. |
| `delete` | `DELETE` | `connectorName, resourceGroupName, subscriptionId` | Deletes the azure databricks accessConnector. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all the azure databricks accessConnectors within a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets all the azure databricks accessConnectors within a subscription. |
| `update` | `EXEC` | `connectorName, resourceGroupName, subscriptionId` | Updates an azure databricks accessConnector. |
