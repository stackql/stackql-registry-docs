---
title: application_type_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - application_type_versions
  - service_fabric_managed_clusters
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
<tr><td><b>Name</b></td><td><code>application_type_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_fabric_managed_clusters.application_type_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Azure resource identifier. |
| `name` | `string` | Azure resource name. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Azure resource tags. |
| `type` | `string` | Azure resource type. |
| `location` | `string` | Resource location depends on the parent resource. |
| `properties` | `object` | The properties of the application type version resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApplicationTypeVersions_Get` | `SELECT` | `api-version, applicationTypeName, clusterName, resourceGroupName, subscriptionId, version` | Get a Service Fabric managed application type version resource created or in the process of being created in the Service Fabric managed application type name resource. |
| `ApplicationTypeVersions_ListByApplicationTypes` | `SELECT` | `api-version, applicationTypeName, clusterName, resourceGroupName, subscriptionId` | Gets all application type version resources created or in the process of being created in the Service Fabric managed application type name resource. |
| `ApplicationTypeVersions_CreateOrUpdate` | `INSERT` | `api-version, applicationTypeName, clusterName, resourceGroupName, subscriptionId, version` | Create or update a Service Fabric managed application type version resource with the specified name. |
| `ApplicationTypeVersions_Delete` | `DELETE` | `api-version, applicationTypeName, clusterName, resourceGroupName, subscriptionId, version` | Delete a Service Fabric managed application type version resource with the specified name. |
| `ApplicationTypeVersions_Update` | `EXEC` | `api-version, applicationTypeName, clusterName, resourceGroupName, subscriptionId, version` | Updates the tags of an application type version resource of a given managed cluster. |
