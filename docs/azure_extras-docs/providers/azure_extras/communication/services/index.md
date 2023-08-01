---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - communication
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.communication.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | A class that describes the properties of the CommunicationService. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `CommunicationServices_Get` | `SELECT` | `communicationServiceName, resourceGroupName, subscriptionId` | Get the CommunicationService and its properties. |
| `CommunicationServices_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Handles requests to list all resources in a resource group. |
| `CommunicationServices_ListBySubscription` | `SELECT` | `subscriptionId` | Handles requests to list all resources in a subscription. |
| `CommunicationServices_CreateOrUpdate` | `INSERT` | `communicationServiceName, resourceGroupName, subscriptionId` | Create a new CommunicationService or update an existing CommunicationService. |
| `CommunicationServices_Delete` | `DELETE` | `communicationServiceName, resourceGroupName, subscriptionId` | Operation to delete a CommunicationService. |
| `CommunicationServices_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks that the CommunicationService name is valid and is not already in use. |
| `CommunicationServices_LinkNotificationHub` | `EXEC` | `communicationServiceName, resourceGroupName, subscriptionId, data__connectionString, data__resourceId` | Links an Azure Notification Hub to this communication service. |
| `CommunicationServices_ListKeys` | `EXEC` | `communicationServiceName, resourceGroupName, subscriptionId` | Get the access keys of the CommunicationService resource. |
| `CommunicationServices_RegenerateKey` | `EXEC` | `communicationServiceName, resourceGroupName, subscriptionId` | Regenerate CommunicationService access key. PrimaryKey and SecondaryKey cannot be regenerated at the same time. |
| `CommunicationServices_Update` | `EXEC` | `communicationServiceName, resourceGroupName, subscriptionId` | Operation to update an existing CommunicationService. |
