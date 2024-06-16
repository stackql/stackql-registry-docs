---
title: cassandra_clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - cassandra_clusters
  - cosmos_db
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cassandra_clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cosmos_db.cassandra_clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique resource identifier of the ARM resource. |
| <CopyableCode code="name" /> | `string` | The name of the ARM resource. |
| <CopyableCode code="identity" /> | `object` | Identity for the resource. |
| <CopyableCode code="location" /> | `string` | The location of the resource group to which the resource belongs. |
| <CopyableCode code="properties" /> | `object` | Properties of a managed Cassandra cluster. |
| <CopyableCode code="tags" /> | `object` | Tags are a list of key-value pairs that describe the resource. These tags can be used in viewing and grouping this resource (across resource groups). A maximum of 15 tags can be provided for a resource. Each tag must have a key no greater than 128 characters and value no greater than 256 characters. For example, the default experience for a template type is set with "defaultExperience": "Cassandra". Current "defaultExperience" values also include "Table", "Graph", "DocumentDB", and "MongoDB". |
| <CopyableCode code="type" /> | `string` | The type of Azure resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Get the properties of a managed Cassandra cluster. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all managed Cassandra clusters in this resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all managed Cassandra clusters in this subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Deletes a managed Cassandra cluster. |
| <CopyableCode code="create_update" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Create or update a managed Cassandra cluster. When updating, you must specify all writable properties. To update only some properties, use PATCH. |
| <CopyableCode code="deallocate" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Deallocate the Managed Cassandra Cluster and Associated Data Centers. Deallocation will deallocate the host virtual machine of this cluster, and reserved the data disk. This won't do anything on an already deallocated cluster. Use Start to restart the cluster. |
| <CopyableCode code="invoke_command" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__command, data__host" /> | Invoke a command like nodetool for cassandra maintenance  |
| <CopyableCode code="invoke_command_async" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId, data__command, data__host" /> | Invoke a command like nodetool for cassandra maintenance asynchronously |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Start the Managed Cassandra Cluster and Associated Data Centers. Start will start the host virtual machine of this cluster with reserved data disk. This won't do anything on an already running cluster. Use Deallocate to deallocate the cluster. |
| <CopyableCode code="status" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Gets the CPU, memory, and disk usage statistics for each Cassandra node in a cluster. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="clusterName, resourceGroupName, subscriptionId" /> | Updates some of the properties of a managed Cassandra cluster. |
