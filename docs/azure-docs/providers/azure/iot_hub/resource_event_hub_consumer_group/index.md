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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_event_hub_consumer_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.resource_event_hub_consumer_group" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Event Hub-compatible consumer group identifier. |
| <CopyableCode code="name" /> | `string` | The Event Hub-compatible consumer group name. |
| <CopyableCode code="etag" /> | `string` | The etag. |
| <CopyableCode code="properties" /> | `object` | The tags. |
| <CopyableCode code="type" /> | `string` | the resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, eventHubEndpointName, name, resourceGroupName, resourceName, subscriptionId" /> | Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="api-version, eventHubEndpointName, name, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Add a consumer group to an Event Hub-compatible endpoint in an IoT hub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, eventHubEndpointName, name, resourceGroupName, resourceName, subscriptionId" /> | Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub. |
