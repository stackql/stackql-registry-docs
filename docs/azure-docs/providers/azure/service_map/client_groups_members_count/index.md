---
title: client_groups_members_count
hide_title: false
hide_table_of_contents: false
keywords:
  - client_groups_members_count
  - service_map
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
<tr><td><b>Name</b></td><td><code>client_groups_members_count</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_map.client_groups_members_count</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `accuracy` | `string` | Specifies the accuracy of a computation. |
| `count` | `integer` | Number of members in the client group. Use this value together with the value of ```accuracy```. If accuracy is `exact` then the value represents the actual number of members in the cloud. When accuracy is `estimated`, the actual number of members is larger than the value of ```count```. |
| `endTime` | `string` | Membership interval start time. |
| `groupId` | `string` | Client Group URI. |
| `startTime` | `string` | Membership interval start time. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `clientGroupName, resourceGroupName, subscriptionId, workspaceName` |
