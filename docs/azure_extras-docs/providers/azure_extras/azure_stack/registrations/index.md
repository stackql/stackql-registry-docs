---
title: registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - registrations
  - azure_stack
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
<tr><td><b>Name</b></td><td><code>registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.azure_stack.registrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `location` | `string` | Location of the resource. |
| `properties` | `object` | Properties portion of the registration resource. |
| `tags` | `object` | Custom tags for the resource. |
| `type` | `string` | Type of Resource. |
| `etag` | `string` | The entity tag used for optimistic concurrency when modifying the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Registrations_Get` | `SELECT` | `registrationName, resourceGroup, subscriptionId` | Returns the properties of an Azure Stack registration. |
| `Registrations_List` | `SELECT` | `resourceGroup, subscriptionId` | Returns a list of all registrations. |
| `Registrations_ListBySubscription` | `SELECT` | `subscriptionId` | Returns a list of all registrations under current subscription. |
| `Registrations_CreateOrUpdate` | `INSERT` | `registrationName, resourceGroup, subscriptionId, data__location, data__properties` | Create or update an Azure Stack registration. |
| `Registrations_Delete` | `DELETE` | `registrationName, resourceGroup, subscriptionId` | Delete the requested Azure Stack registration. |
| `Registrations_EnableRemoteManagement` | `EXEC` | `registrationName, resourceGroup, subscriptionId` | Enables remote management for device under the Azure Stack registration. |
| `Registrations_GetActivationKey` | `EXEC` | `registrationName, resourceGroup, subscriptionId` | Returns Azure Stack Activation Key. |
| `Registrations_Update` | `EXEC` | `registrationName, resourceGroup, subscriptionId, data__location, data__properties` | Patch an Azure Stack registration. |
