---
title: private_link_services_for_edm_upload
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services_for_edm_upload
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
<tr><td><b>Name</b></td><td><code>private_link_services_for_edm_upload</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.security_and_compliance.private_link_services_for_edm_upload</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `kind` | `string` | The kind of the service. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `etag` | `string` | An etag associated with the resource, used for optimistic concurrency when editing it. |
| `tags` | `object` | The resource tags. |
| `location` | `string` | The resource location. |
| `properties` | `object` | The properties of a service instance. |
| `identity` | `object` | Setting indicating whether the service has a managed identity associated with it. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `privateLinkServicesForEDMUpload_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Get the metadata of a privateLinkServicesForEDMUpload resource. |
| `privateLinkServicesForEDMUpload_List` | `SELECT` | `subscriptionId` | Get all the privateLinkServicesForEDMUpload instances in a subscription. |
| `privateLinkServicesForEDMUpload_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the service instances in a resource group. |
| `privateLinkServicesForEDMUpload_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create or update the metadata of a privateLinkServicesForEDMUpload instance. |
| `privateLinkServicesForEDMUpload_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Update the metadata of a privateLinkServicesForEDMUpload instance. |
