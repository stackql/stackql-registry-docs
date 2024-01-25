---
title: resource_event_hub_consumer_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_event_hub_consumer_groups
  - iot_hub
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
<tr><td><b>Name</b></td><td><code>resource_event_hub_consumer_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub.resource_event_hub_consumer_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The Event Hub-compatible consumer group identifier. |
| `name` | `string` | The Event Hub-compatible consumer group name. |
| `etag` | `string` | The etag. |
| `properties` | `object` | The tags. |
| `type` | `string` | the resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `api-version, eventHubEndpointName, resourceGroupName, resourceName, subscriptionId` |
| `_list` | `EXEC` | `api-version, eventHubEndpointName, resourceGroupName, resourceName, subscriptionId` |
