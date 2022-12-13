---
title: private_end_point_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - private_end_point_connections
  - data_factory
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
<tr><td><b>Name</b></td><td><code>private_end_point_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_factory.private_end_point_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `properties` | `object` | A remote private endpoint connection |
| `type` | `string` | The resource type. |
| `etag` | `string` | Etag identifies change in the resource. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `privateEndPointConnections_ListByFactory` | `SELECT` | `api-version, factoryName, resourceGroupName, subscriptionId` |
