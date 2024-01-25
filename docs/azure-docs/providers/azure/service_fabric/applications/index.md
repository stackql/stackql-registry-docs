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
| `etag` | `string` | Azure resource etag. |
| `identity` | `object` | Describes the managed identities for an Azure resource. |
| `location` | `string` | It will be deprecated in New API, resource location depends on the parent resource. |
| `properties` | `object` | The application resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Azure resource tags. |
| `type` | `string` | Azure resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, applicationName, clusterName, resourceGroupName, subscriptionId` | Get a Service Fabric application resource created or in the process of being created in the Service Fabric cluster resource. |
| `list` | `SELECT` | `api-version, clusterName, resourceGroupName, subscriptionId` | Gets all application resources created or in the process of being created in the Service Fabric cluster resource. |
| `create_or_update` | `INSERT` | `api-version, applicationName, clusterName, resourceGroupName, subscriptionId` | Create or update a Service Fabric application resource with the specified name. |
| `delete` | `DELETE` | `api-version, applicationName, clusterName, resourceGroupName, subscriptionId` | Delete a Service Fabric application resource with the specified name. |
| `_list` | `EXEC` | `api-version, clusterName, resourceGroupName, subscriptionId` | Gets all application resources created or in the process of being created in the Service Fabric cluster resource. |
| `update` | `EXEC` | `api-version, applicationName, clusterName, resourceGroupName, subscriptionId` | Update a Service Fabric application resource with the specified name. |
