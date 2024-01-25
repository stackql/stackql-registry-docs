---
title: elastic_sans
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_sans
  - elastic_san
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
<tr><td><b>Name</b></td><td><code>elastic_sans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.elastic_san.elastic_sans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Elastic San response properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `elasticSanName, resourceGroupName, subscriptionId` | Get a ElasticSan. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of ElasticSan in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets a list of ElasticSans in a subscription |
| `create` | `INSERT` | `elasticSanName, resourceGroupName, subscriptionId, data__location, data__properties` | Create ElasticSan. |
| `delete` | `DELETE` | `elasticSanName, resourceGroupName, subscriptionId` | Delete a Elastic San. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets a list of ElasticSan in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets a list of ElasticSans in a subscription |
| `update` | `EXEC` | `elasticSanName, resourceGroupName, subscriptionId` | Update a Elastic San. |
