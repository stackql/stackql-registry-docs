---
title: email_services
hide_title: false
hide_table_of_contents: false
keywords:
  - email_services
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
<tr><td><b>Name</b></td><td><code>email_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.communication.email_services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | A class that describes the properties of the EmailService. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `EmailServices_Get` | `SELECT` | `emailServiceName, resourceGroupName, subscriptionId` | Get the EmailService and its properties. |
| `EmailServices_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Handles requests to list all resources in a resource group. |
| `EmailServices_ListBySubscription` | `SELECT` | `subscriptionId` | Handles requests to list all resources in a subscription. |
| `EmailServices_CreateOrUpdate` | `INSERT` | `emailServiceName, resourceGroupName, subscriptionId` | Create a new EmailService or update an existing EmailService. |
| `EmailServices_Delete` | `DELETE` | `emailServiceName, resourceGroupName, subscriptionId` | Operation to delete a EmailService. |
| `EmailServices_ListVerifiedExchangeOnlineDomains` | `EXEC` | `subscriptionId` | Get a list of domains that are fully verified in Exchange Online. |
| `EmailServices_Update` | `EXEC` | `emailServiceName, resourceGroupName, subscriptionId` | Operation to update an existing EmailService. |
