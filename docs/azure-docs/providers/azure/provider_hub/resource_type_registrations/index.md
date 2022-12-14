---
title: resource_type_registrations
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_type_registrations
  - provider_hub
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
<tr><td><b>Name</b></td><td><code>resource_type_registrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.provider_hub.resource_type_registrations</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ResourceTypeRegistrations_Get` | `SELECT` | `providerNamespace, resourceType, subscriptionId` | Gets a resource type details in the given subscription and provider. |
| `ResourceTypeRegistrations_ListByProviderRegistration` | `SELECT` | `providerNamespace, subscriptionId` | Gets the list of the resource types for the given provider. |
| `ResourceTypeRegistrations_CreateOrUpdate` | `INSERT` | `providerNamespace, resourceType, subscriptionId` | Creates or updates a resource type. |
| `ResourceTypeRegistrations_Delete` | `DELETE` | `providerNamespace, resourceType, subscriptionId` | Deletes a resource type |
