---
title: elastic_san
hide_title: false
hide_table_of_contents: false
keywords:
  - elastic_san
  - elastic_san
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>elastic_san</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.elastic_san.elastic_san</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives. |
| `properties` | `object` | Elastic San response properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ElasticSans_Get` | `SELECT` | `elasticSanName, resourceGroupName, subscriptionId` | Get a ElasticSan. |
| `ElasticSans_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets a list of ElasticSan in a resource group. |
| `ElasticSans_ListBySubscription` | `SELECT` | `subscriptionId` | Gets a list of ElasticSans in a subscription |
| `ElasticSans_Create` | `INSERT` | `elasticSanName, resourceGroupName, subscriptionId, data__properties` | Create ElasticSan. |
| `ElasticSans_Delete` | `DELETE` | `elasticSanName, resourceGroupName, subscriptionId` | Delete a Elastic San. |
| `ElasticSans_Update` | `EXEC` | `elasticSanName, resourceGroupName, subscriptionId` | Update a Elastic San. |
