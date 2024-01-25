---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - communication
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.communication.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | A class that describes the properties of the CommunicationService. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `communicationServiceName, resourceGroupName, subscriptionId` | Get the CommunicationService and its properties. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Handles requests to list all resources in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Handles requests to list all resources in a subscription. |
| `create_or_update` | `INSERT` | `communicationServiceName, resourceGroupName, subscriptionId` | Create a new CommunicationService or update an existing CommunicationService. |
| `delete` | `DELETE` | `communicationServiceName, resourceGroupName, subscriptionId` | Operation to delete a CommunicationService. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Handles requests to list all resources in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Handles requests to list all resources in a subscription. |
| `check_name_availability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks that the CommunicationService name is valid and is not already in use. |
| `link_notification_hub` | `EXEC` | `communicationServiceName, resourceGroupName, subscriptionId, data__connectionString, data__resourceId` | Links an Azure Notification Hub to this communication service. |
| `regenerate_key` | `EXEC` | `communicationServiceName, resourceGroupName, subscriptionId` | Regenerate CommunicationService access key. PrimaryKey and SecondaryKey cannot be regenerated at the same time. |
| `update` | `EXEC` | `communicationServiceName, resourceGroupName, subscriptionId` | Operation to update an existing CommunicationService. |
