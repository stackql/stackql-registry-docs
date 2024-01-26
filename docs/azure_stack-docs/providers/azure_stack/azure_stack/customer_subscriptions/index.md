---
title: customer_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_subscriptions
  - azure_stack
  - azure_stack    
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
<tr><td><b>Name</b></td><td><code>customer_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.azure_stack.customer_subscriptions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `etag` | `string` | The entity tag used for optimistic concurrency when modifying the resource. |
| `properties` | `object` | Customer subscription properties. |
| `type` | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `customerSubscriptionName, registrationName, resourceGroup, subscriptionId` | Returns the specified product. |
| `list` | `SELECT` | `registrationName, resourceGroup, subscriptionId` | Returns a list of products. |
| `create` | `INSERT` | `customerSubscriptionName, registrationName, resourceGroup, subscriptionId` | Creates a new customer subscription under a registration. |
| `delete` | `DELETE` | `customerSubscriptionName, registrationName, resourceGroup, subscriptionId` | Deletes a customer subscription under a registration. |
| `_list` | `EXEC` | `registrationName, resourceGroup, subscriptionId` | Returns a list of products. |
