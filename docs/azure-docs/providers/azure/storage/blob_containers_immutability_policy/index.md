---
title: blob_containers_immutability_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - blob_containers_immutability_policy
  - storage
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
<tr><td><b>Name</b></td><td><code>blob_containers_immutability_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.blob_containers_immutability_policy</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Resource Etag. |
| `properties` | `object` | The properties of an ImmutabilityPolicy of a blob container. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, containerName, immutabilityPolicyName, resourceGroupName, subscriptionId` | Gets the existing immutability policy along with the corresponding ETag in response headers and body. |
| `create_or_update` | `INSERT` | `accountName, containerName, immutabilityPolicyName, resourceGroupName, subscriptionId, data__properties` | Creates or updates an unlocked immutability policy. ETag in If-Match is honored if given but not required for this operation. |
| `delete` | `DELETE` | `If-Match, accountName, containerName, immutabilityPolicyName, resourceGroupName, subscriptionId` | Aborts an unlocked immutability policy. The response of delete has immutabilityPeriodSinceCreationInDays set to 0. ETag in If-Match is required for this operation. Deleting a locked immutability policy is not allowed, the only way is to delete the container after deleting all expired blobs inside the policy locked container. |
