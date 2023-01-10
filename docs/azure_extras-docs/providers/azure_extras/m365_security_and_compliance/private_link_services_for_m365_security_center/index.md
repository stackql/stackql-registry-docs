---
title: private_link_services_for_m365_security_center
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services_for_m365_security_center
  - m365_security_and_compliance
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
<tr><td><b>Name</b></td><td><code>private_link_services_for_m365_security_center</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.m365_security_and_compliance.private_link_services_for_m365_security_center</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `kind` | `string` | The kind of the service. |
| `type` | `string` | The resource type. |
| `tags` | `object` | The resource tags. |
| `etag` | `string` | An etag associated with the resource, used for optimistic concurrency when editing it. |
| `identity` | `object` | Setting indicating whether the service has a managed identity associated with it. |
| `location` | `string` | The resource location. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `properties` | `object` | The properties of a service instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `privateLinkServicesForM365SecurityCenter_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Get the metadata of a privateLinkServicesForM365SecurityCenter resource. |
| `privateLinkServicesForM365SecurityCenter_List` | `SELECT` | `subscriptionId` | Get all the privateLinkServicesForM365SecurityCenter instances in a subscription. |
| `privateLinkServicesForM365SecurityCenter_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the service instances in a resource group. |
| `privateLinkServicesForM365SecurityCenter_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create or update the metadata of a privateLinkServicesForM365SecurityCenter instance. |
| `privateLinkServicesForM365SecurityCenter_Delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Delete a service instance. |
| `privateLinkServicesForM365SecurityCenter_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Update the metadata of a privateLinkServicesForM365SecurityCenter instance. |
