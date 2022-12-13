---
title: configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - configurations
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
<tr><td><b>Name</b></td><td><code>configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hdinsight.configurations</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Configurations_List` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets all configuration information for an HDI cluster. |
| `Configurations_Get` | `EXEC` | `clusterName, configurationName, resourceGroupName, subscriptionId` | The configuration object for the specified cluster. This API is not recommended and might be removed in the future. Please consider using List configurations API instead. |
| `Configurations_Update` | `EXEC` | `clusterName, configurationName, resourceGroupName, subscriptionId` | Configures the HTTP settings on the specified cluster. This API is deprecated, please use UpdateGatewaySettings in cluster endpoint instead. |
