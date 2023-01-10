---
title: private_link_services_for_edm_upload
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_services_for_edm_upload
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
<tr><td><b>Name</b></td><td><code>private_link_services_for_edm_upload</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.m365_security_and_compliance.private_link_services_for_edm_upload</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `properties` | `object` | The properties of a service instance. |
| `type` | `string` | The resource type. |
| `kind` | `string` | The kind of the service. |
| `location` | `string` | The resource location. |
| `tags` | `object` | The resource tags. |
| `identity` | `object` | Setting indicating whether the service has a managed identity associated with it. |
| `etag` | `string` | An etag associated with the resource, used for optimistic concurrency when editing it. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `privateLinkServicesForEDMUpload_Get` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | Get the metadata of a privateLinkServicesForEDMUpload resource. |
| `privateLinkServicesForEDMUpload_List` | `SELECT` | `subscriptionId` | Get all the privateLinkServicesForEDMUpload instances in a subscription. |
| `privateLinkServicesForEDMUpload_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the service instances in a resource group. |
| `privateLinkServicesForEDMUpload_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, subscriptionId` | Create or update the metadata of a privateLinkServicesForEDMUpload instance. |
| `privateLinkServicesForEDMUpload_Update` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | Update the metadata of a privateLinkServicesForEDMUpload instance. |
