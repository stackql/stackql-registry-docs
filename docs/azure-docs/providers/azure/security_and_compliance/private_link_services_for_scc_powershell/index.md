---
title: private_link_services_for_scc_powershell
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services_for_scc_powershell
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
<tr><td><b>Name</b></td><td><code>private_link_services_for_scc_powershell</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_and_compliance.private_link_services_for_scc_powershell</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `etag` | `string` | An etag associated with the resource, used for optimistic concurrency when editing it. |
| `identity` | `object` | Setting indicating whether the service has a managed identity associated with it. |
| `kind` | `string` | The kind of the service. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The properties of a service instance. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Get the metadata of a privateLinkServicesForSCCPowershell resource. |
| `list` | `SELECT` | `subscriptionId` | Get all the privateLinkServicesForSCCPowershell instances in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the service instances in a resource group. |
| `create_or_update` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create or update the metadata of a privateLinkServicesForSCCPowershell instance. |
| `delete` | `DELETE` | `resourceGroupName, resourceName, subscriptionId` | Delete a service instance. |
| `_list` | `EXEC` | `subscriptionId` | Get all the privateLinkServicesForSCCPowershell instances in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get all the service instances in a resource group. |
| `update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Update the metadata of a privateLinkServicesForSCCPowershell instance. |
