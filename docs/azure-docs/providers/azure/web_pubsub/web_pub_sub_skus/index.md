---
title: web_pub_sub_skus
hide_title: false
hide_table_of_contents: false
keywords:
  - web_pub_sub_skus
  - web_pubsub
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
<tr><td><b>Name</b></td><td><code>web_pub_sub_skus</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.web_pubsub.web_pub_sub_skus</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `capacity` | `object` | Describes scaling information of a sku. |
| `resourceType` | `string` | The resource type that this object applies to |
| `sku` | `object` | The billing information of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |
| `_list` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` |
