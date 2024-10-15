---
title: consumer_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_groups
  - event_hubs
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

Creates, updates, deletes, gets or lists a <code>consumer_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumer_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_hubs.consumer_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `` | Single item in List or Get Consumer group operation |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="consumerGroupName, eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Gets a description for the specified consumer group. |
| <CopyableCode code="list_by_event_hub" /> | `SELECT` | <CopyableCode code="eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Gets all the consumer groups in a Namespace. An empty feed is returned if no consumer group exists in the Namespace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="consumerGroupName, eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Creates or updates an Event Hubs consumer group as a nested resource within a Namespace. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="consumerGroupName, eventHubName, namespaceName, resourceGroupName, subscriptionId" /> | Deletes a consumer group from the specified Event Hub and resource group. |

## `SELECT` examples

Gets all the consumer groups in a Namespace. An empty feed is returned if no consumer group exists in the Namespace.


```sql
SELECT
id,
name,
location,
properties,
systemData,
type
FROM azure.event_hubs.consumer_groups
WHERE eventHubName = '{{ eventHubName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>consumer_groups</code> resource.

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
INSERT INTO azure.event_hubs.consumer_groups (
consumerGroupName,
eventHubName,
namespaceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ consumerGroupName }}',
'{{ eventHubName }}',
'{{ namespaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>consumer_groups</code> resource.

```sql
/*+ delete */
DELETE FROM azure.event_hubs.consumer_groups
WHERE consumerGroupName = '{{ consumerGroupName }}'
AND eventHubName = '{{ eventHubName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
