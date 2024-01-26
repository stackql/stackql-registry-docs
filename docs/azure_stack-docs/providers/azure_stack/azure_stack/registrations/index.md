---
title: registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - registrations
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
<tr><td><b>Name</b></td><td><code>registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_stack.azure_stack.registrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `etag` | `string` | The entity tag used for optimistic concurrency when modifying the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties portion of the registration resource. |
| `tags` | `object` | Custom tags for the resource. |
| `type` | `string` | Type of Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `registrationName, resourceGroup, subscriptionId` | Returns the properties of an Azure Stack registration. |
| `list` | `SELECT` | `resourceGroup, subscriptionId` | Returns a list of all registrations. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Returns a list of all registrations under current subscription. |
| `create_or_update` | `INSERT` | `registrationName, resourceGroup, subscriptionId, data__location, data__properties` | Create or update an Azure Stack registration. |
| `delete` | `DELETE` | `registrationName, resourceGroup, subscriptionId` | Delete the requested Azure Stack registration. |
| `_list` | `EXEC` | `resourceGroup, subscriptionId` | Returns a list of all registrations. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Returns a list of all registrations under current subscription. |
| `enable_remote_management` | `EXEC` | `registrationName, resourceGroup, subscriptionId` | Enables remote management for device under the Azure Stack registration. |
| `update` | `EXEC` | `registrationName, resourceGroup, subscriptionId, data__location, data__properties` | Patch an Azure Stack registration. |
