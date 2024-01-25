---
title: web_pub_sub
hide_title: false
hide_table_of_contents: false
keywords:
  - web_pub_sub
  - web_pubsub
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
<tr><td><b>Name</b></td><td><code>web_pub_sub</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_pubsub.web_pub_sub</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | A class represent managed identities used for request and response |
| `kind` | `string` | The kind of the service |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | A class that describes the properties of the resource |
| `sku` | `object` | The billing information of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Get the resource and its properties. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Handles requests to list all resources in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Handles requests to list all resources in a subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create or update a resource. |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Operation to delete a resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Handles requests to list all resources in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Handles requests to list all resources in a subscription. |
| `check_name_availability` | `EXEC` | `location, subscriptionId, data__name, data__type` | Checks that the resource name is valid and is not already in use. |
| `regenerate_key` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Regenerate the access key for the resource. PrimaryKey and SecondaryKey cannot be regenerated at the same time. |
| `restart` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Operation to restart a resource. |
| `update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Operation to update an exiting resource. |
