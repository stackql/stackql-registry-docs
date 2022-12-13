---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `properties` | `object` | The service resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Azure resource tags. |
| `type` | `string` | Azure resource type. |
| `etag` | `string` | Azure resource etag. |
| `location` | `string` | It will be deprecated in New API, resource location depends on the parent resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Services_Get` | `SELECT` | `api-version, applicationName, clusterName, resourceGroupName, serviceName, subscriptionId` | Get a Service Fabric service resource created or in the process of being created in the Service Fabric application resource. |
| `Services_List` | `SELECT` | `api-version, applicationName, clusterName, resourceGroupName, subscriptionId` | Gets all service resources created or in the process of being created in the Service Fabric application resource. |
| `Services_CreateOrUpdate` | `INSERT` | `api-version, applicationName, clusterName, resourceGroupName, serviceName, subscriptionId` | Create or update a Service Fabric service resource with the specified name. |
| `Services_Delete` | `DELETE` | `api-version, applicationName, clusterName, resourceGroupName, serviceName, subscriptionId` | Delete a Service Fabric service resource with the specified name. |
| `Services_Update` | `EXEC` | `api-version, applicationName, clusterName, resourceGroupName, serviceName, subscriptionId` | Update a Service Fabric service resource with the specified name. |
