---
title: configuration_group_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_group_schemas
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>configuration_group_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.configuration_group_schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Configuration group schema properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `configurationGroupSchemaName, publisherName, resourceGroupName, subscriptionId` | Gets information about the specified configuration group schema. |
| `list_by_publisher` | `SELECT` | `publisherName, resourceGroupName, subscriptionId` | Gets information of the configuration group schemas under a publisher. |
| `create_or_update` | `INSERT` | `configurationGroupSchemaName, publisherName, resourceGroupName, subscriptionId` | Creates or updates a configuration group schema. |
| `delete` | `DELETE` | `configurationGroupSchemaName, publisherName, resourceGroupName, subscriptionId` | Deletes a specified configuration group schema. |
| `_list_by_publisher` | `EXEC` | `publisherName, resourceGroupName, subscriptionId` | Gets information of the configuration group schemas under a publisher. |
| `update` | `EXEC` | `configurationGroupSchemaName, publisherName, resourceGroupName, subscriptionId` | Updates a configuration group schema resource. |
