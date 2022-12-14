---
title: private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - private_link_resources
  - purview
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
<tr><td><b>Name</b></td><td><code>private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.purview.private_link_resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The private link resource identifier. |
| `name` | `string` | The private link resource name. |
| `properties` | `object` | A privately linkable resource properties. |
| `type` | `string` | The private link resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PrivateLinkResources_ListByAccount` | `SELECT` | `accountName, api-version, resourceGroupName, subscriptionId` | Gets a list of privately linkable resources for an account |
| `PrivateLinkResources_GetByGroupId` | `EXEC` | `accountName, api-version, groupId, resourceGroupName, subscriptionId` | Gets a privately linkable resources for an account with given group identifier |
