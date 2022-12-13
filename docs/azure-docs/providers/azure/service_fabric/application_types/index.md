---
title: application_types
hide_title: false
hide_table_of_contents: false
keywords:
  - application_types
  - service_fabric
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
<tr><td><b>Name</b></td><td><code>application_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric.application_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `properties` | `object` | The application type name properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Azure resource tags. |
| `type` | `string` | Azure resource type. |
| `etag` | `string` | Azure resource etag. |
| `location` | `string` | It will be deprecated in New API, resource location depends on the parent resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApplicationTypes_Get` | `SELECT` | `api-version, applicationTypeName, clusterName, resourceGroupName, subscriptionId` | Get a Service Fabric application type name resource created or in the process of being created in the Service Fabric cluster resource. |
| `ApplicationTypes_List` | `SELECT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Gets all application type name resources created or in the process of being created in the Service Fabric cluster resource. |
| `ApplicationTypes_CreateOrUpdate` | `INSERT` | `api-version, applicationTypeName, clusterName, resourceGroupName, subscriptionId` | Create or update a Service Fabric application type name resource with the specified name. |
| `ApplicationTypes_Delete` | `DELETE` | `api-version, applicationTypeName, clusterName, resourceGroupName, subscriptionId` | Delete a Service Fabric application type name resource with the specified name. |
