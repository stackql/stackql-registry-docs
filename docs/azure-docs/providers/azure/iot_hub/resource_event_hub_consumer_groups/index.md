---
title: resource_event_hub_consumer_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_event_hub_consumer_groups
  - iot_hub
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>resource_event_hub_consumer_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_event_hub_consumer_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.resource_event_hub_consumer_groups" /></td></tr>
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
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="eventHubEndpointName, name, resourceGroupName, resourceName, subscriptionId" /> | Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="eventHubEndpointName, resourceGroupName, resourceName, subscriptionId" /> | Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="eventHubEndpointName, name, resourceGroupName, resourceName, subscriptionId, data__properties" /> | Add a consumer group to an Event Hub-compatible endpoint in an IoT hub. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="eventHubEndpointName, name, resourceGroupName, resourceName, subscriptionId" /> | Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub. |

## `SELECT` examples

Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub.


```sql
SELECT
id,
name,
etag,
properties,
type
FROM azure.iot_hub.resource_event_hub_consumer_groups
WHERE eventHubEndpointName = '{{ eventHubEndpointName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_event_hub_consumer_groups</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.iot_hub.resource_event_hub_consumer_groups (
eventHubEndpointName,
name,
resourceGroupName,
resourceName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ eventHubEndpointName }}',
'{{ name }}',
'{{ resourceGroupName }}',
'{{ resourceName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: name
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>resource_event_hub_consumer_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_hub.resource_event_hub_consumer_groups
WHERE eventHubEndpointName = '{{ eventHubEndpointName }}'
AND name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND resourceName = '{{ resourceName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
