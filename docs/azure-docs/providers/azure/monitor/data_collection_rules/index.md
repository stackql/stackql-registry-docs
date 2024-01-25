---
title: data_collection_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - data_collection_rules
  - monitor
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
<tr><td><b>Name</b></td><td><code>data_collection_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.data_collection_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified ID of the resource. |
| `name` | `string` | The name of the resource. |
| `etag` | `string` | Resource entity tag (ETag). |
| `identity` | `object` | Managed service identity of the resource. |
| `kind` | `string` | The kind of the resource. |
| `location` | `string` | The geo-location where the resource lives. |
| `properties` | `object` | Resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `dataCollectionRuleName, resourceGroupName, subscriptionId` |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` |
| `list_by_subscription` | `SELECT` | `subscriptionId` |
| `create` | `INSERT` | `dataCollectionRuleName, resourceGroupName, subscriptionId, data__location` |
| `delete` | `DELETE` | `dataCollectionRuleName, resourceGroupName, subscriptionId` |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` |
| `_list_by_subscription` | `EXEC` | `subscriptionId` |
| `update` | `EXEC` | `dataCollectionRuleName, resourceGroupName, subscriptionId` |
