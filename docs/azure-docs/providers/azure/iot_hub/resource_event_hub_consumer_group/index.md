---
title: resource_event_hub_consumer_group
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_event_hub_consumer_group
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
<tr><td><b>Name</b></td><td><code>resource_event_hub_consumer_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub.resource_event_hub_consumer_group</code></td></tr>
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, eventHubEndpointName, name, resourceGroupName, resourceName, subscriptionId` | Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub. |
| `create` | `INSERT` | `api-version, eventHubEndpointName, name, resourceGroupName, resourceName, subscriptionId, data__properties` | Add a consumer group to an Event Hub-compatible endpoint in an IoT hub. |
| `delete` | `DELETE` | `api-version, eventHubEndpointName, name, resourceGroupName, resourceName, subscriptionId` | Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub. |
