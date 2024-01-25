---
title: data_collection_rule_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - data_collection_rule_associations
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
<tr><td><b>Name</b></td><td><code>data_collection_rule_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.data_collection_rule_associations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified ID of the resource. |
| `name` | `string` | The name of the resource. |
| `etag` | `string` | Resource entity tag (ETag). |
| `properties` | `object` | Resource properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `associationName, resourceUri` |
| `list_by_data_collection_endpoint` | `SELECT` | `dataCollectionEndpointName, resourceGroupName, subscriptionId` |
| `list_by_resource` | `SELECT` | `resourceUri` |
| `list_by_rule` | `SELECT` | `dataCollectionRuleName, resourceGroupName, subscriptionId` |
| `create` | `INSERT` | `associationName, resourceUri` |
| `delete` | `DELETE` | `associationName, resourceUri` |
| `_list_by_data_collection_endpoint` | `EXEC` | `dataCollectionEndpointName, resourceGroupName, subscriptionId` |
| `_list_by_resource` | `EXEC` | `resourceUri` |
| `_list_by_rule` | `EXEC` | `dataCollectionRuleName, resourceGroupName, subscriptionId` |
