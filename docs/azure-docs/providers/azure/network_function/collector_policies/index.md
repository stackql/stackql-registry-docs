---
title: collector_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - collector_policies
  - network_function
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
<tr><td><b>Name</b></td><td><code>collector_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network_function.collector_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Collection policy properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `azureTrafficCollectorName, collectorPolicyName, resourceGroupName, subscriptionId` | Gets the collector policy in a specified Traffic Collector |
| `list` | `SELECT` | `azureTrafficCollectorName, resourceGroupName, subscriptionId` | Return list of Collector policies in a Azure Traffic Collector |
| `create_or_update` | `INSERT` | `azureTrafficCollectorName, collectorPolicyName, resourceGroupName, subscriptionId` | Creates or updates a Collector Policy resource |
| `delete` | `DELETE` | `azureTrafficCollectorName, collectorPolicyName, resourceGroupName, subscriptionId` | Deletes a specified Collector Policy resource. |
| `_list` | `EXEC` | `azureTrafficCollectorName, resourceGroupName, subscriptionId` | Return list of Collector policies in a Azure Traffic Collector |
