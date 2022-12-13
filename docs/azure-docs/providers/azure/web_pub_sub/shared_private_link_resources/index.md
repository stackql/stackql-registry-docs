---
title: shared_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_private_link_resources
  - web_pub_sub
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
<tr><td><b>Name</b></td><td><code>shared_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_pub_sub.shared_private_link_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Describes the properties of an existing Shared Private Link Resource |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WebPubSubSharedPrivateLinkResources_Get` | `SELECT` | `resourceGroupName, resourceName, sharedPrivateLinkResourceName, subscriptionId` | Get the specified shared private link resource |
| `WebPubSubSharedPrivateLinkResources_List` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` | List shared private link resources |
| `WebPubSubSharedPrivateLinkResources_CreateOrUpdate` | `INSERT` | `resourceGroupName, resourceName, sharedPrivateLinkResourceName, subscriptionId` | Create or update a shared private link resource |
| `WebPubSubSharedPrivateLinkResources_Delete` | `DELETE` | `resourceGroupName, resourceName, sharedPrivateLinkResourceName, subscriptionId` | Delete the specified shared private link resource |
