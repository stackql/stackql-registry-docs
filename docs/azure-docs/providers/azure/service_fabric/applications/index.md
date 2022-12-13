---
title: applications
hide_title: false
hide_table_of_contents: false
keywords:
  - applications
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
<tr><td><b>Name</b></td><td><code>applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric.applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `identity` | `object` | Describes the managed identities for an Azure resource. |
| `properties` | `object` | The application resource properties. |
| `etag` | `string` | Azure resource etag. |
| `type` | `string` | Azure resource type. |
| `location` | `string` | It will be deprecated in New API, resource location depends on the parent resource. |
| `tags` | `object` | Azure resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Applications_Get` | `SELECT` | `api-version, applicationName, clusterName, resourceGroupName, subscriptionId` | Get a Service Fabric application resource created or in the process of being created in the Service Fabric cluster resource. |
| `Applications_List` | `SELECT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Gets all application resources created or in the process of being created in the Service Fabric cluster resource. |
| `Applications_CreateOrUpdate` | `INSERT` | `api-version, applicationName, clusterName, resourceGroupName, subscriptionId` | Create or update a Service Fabric application resource with the specified name. |
| `Applications_Delete` | `DELETE` | `api-version, applicationName, clusterName, resourceGroupName, subscriptionId` | Delete a Service Fabric application resource with the specified name. |
| `Applications_Update` | `EXEC` | `api-version, applicationName, clusterName, resourceGroupName, subscriptionId` | Update a Service Fabric application resource with the specified name. |
