---
title: private_link_services_for_o365_management_activity_api
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services_for_o365_management_activity_api
  - security_and_compliance
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
<tr><td><b>Name</b></td><td><code>private_link_services_for_o365_management_activity_api</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_and_compliance.private_link_services_for_o365_management_activity_api</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `properties` | `object` | The properties of a service instance. |
| `location` | `string` | The resource location. |
| `tags` | `object` | The resource tags. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `kind` | `string` | The kind of the service. |
| `identity` | `object` | Setting indicating whether the service has a managed identity associated with it. |
| `type` | `string` | The resource type. |
| `etag` | `string` | An etag associated with the resource, used for optimistic concurrency when editing it. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `privateLinkServicesForO365ManagementActivityAPI_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Get the metadata of a privateLinkServicesForO365ManagementActivityAPI resource. |
| `privateLinkServicesForO365ManagementActivityAPI_List` | `SELECT` | `subscriptionId` | Get all the privateLinkServicesForO365ManagementActivityAPI instances in a subscription. |
| `privateLinkServicesForO365ManagementActivityAPI_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the service instances in a resource group. |
| `privateLinkServicesForO365ManagementActivityAPI_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create or update the metadata of a privateLinkServicesForO365ManagementActivityAPI instance. |
| `privateLinkServicesForO365ManagementActivityAPI_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Delete a service instance. |
| `privateLinkServicesForO365ManagementActivityAPI_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Update the metadata of a privateLinkServicesForO365ManagementActivityAPI instance. |
