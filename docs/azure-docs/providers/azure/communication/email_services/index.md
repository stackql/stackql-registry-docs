---
title: email_services
hide_title: false
hide_table_of_contents: false
keywords:
  - email_services
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
<tr><td><b>Name</b></td><td><code>email_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.communication.email_services</code></td></tr>
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
| `get` | `SELECT` | `emailServiceName, resourceGroupName, subscriptionId` | Get the EmailService and its properties. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Handles requests to list all resources in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Handles requests to list all resources in a subscription. |
| `create_or_update` | `INSERT` | `emailServiceName, resourceGroupName, subscriptionId` | Create a new EmailService or update an existing EmailService. |
| `delete` | `DELETE` | `emailServiceName, resourceGroupName, subscriptionId` | Operation to delete a EmailService. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Handles requests to list all resources in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Handles requests to list all resources in a subscription. |
| `update` | `EXEC` | `emailServiceName, resourceGroupName, subscriptionId` | Operation to update an existing EmailService. |
