---
title: virtual_machines
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_machines
  - hdinsight
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
<tr><td><b>Name</b></td><td><code>virtual_machines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hdinsight.virtual_machines</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualMachines_GetAsyncOperationStatus` | `EXEC` | `clusterName, operationId, resourceGroupName, subscriptionId` | Gets the async operation status. |
| `VirtualMachines_ListHosts` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Lists the HDInsight clusters hosts |
| `VirtualMachines_RestartHosts` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Restarts the specified HDInsight cluster hosts. |
