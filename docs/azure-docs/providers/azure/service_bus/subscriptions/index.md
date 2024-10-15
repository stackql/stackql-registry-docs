---
title: subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - subscriptions
  - service_bus
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

Creates, updates, deletes, gets or lists a <code>subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.service_bus.subscriptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_subscriptions', value: 'view', },
        { label: 'subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="accessed_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="auto_delete_on_idle" /> | `text` | field from the `properties` object |
| <CopyableCode code="client_affine_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="count_details" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_at" /> | `text` | field from the `properties` object |
| <CopyableCode code="dead_lettering_on_filter_evaluation_exceptions" /> | `text` | field from the `properties` object |
| <CopyableCode code="dead_lettering_on_message_expiration" /> | `text` | field from the `properties` object |
| <CopyableCode code="default_message_time_to_live" /> | `text` | field from the `properties` object |
| <CopyableCode code="duplicate_detection_history_time_window" /> | `text` | field from the `properties` object |
| <CopyableCode code="enable_batched_operations" /> | `text` | field from the `properties` object |
| <CopyableCode code="forward_dead_lettered_messages_to" /> | `text` | field from the `properties` object |
| <CopyableCode code="forward_to" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_client_affine" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="lock_duration" /> | `text` | field from the `properties` object |
| <CopyableCode code="max_delivery_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="message_count" /> | `text` | field from the `properties` object |
| <CopyableCode code="namespaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="requires_session" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="topicName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
| <CopyableCode code="updated_at" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName} |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Description of Subscription Resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.EventHub/Namespaces" or "Microsoft.EventHub/Namespaces/EventHubs" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId, subscriptionName, topicName" /> | Returns a subscription description for the specified topic. |
| <CopyableCode code="list_by_topic" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId, topicName" /> | List all the subscriptions under a specified topic. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId, subscriptionName, topicName" /> | Creates a topic subscription. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId, subscriptionName, topicName" /> | Deletes a subscription from the specified topic. |

## `SELECT` examples

List all the subscriptions under a specified topic.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_subscriptions', value: 'view', },
        { label: 'subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accessed_at,
auto_delete_on_idle,
client_affine_properties,
count_details,
created_at,
dead_lettering_on_filter_evaluation_exceptions,
dead_lettering_on_message_expiration,
default_message_time_to_live,
duplicate_detection_history_time_window,
enable_batched_operations,
forward_dead_lettered_messages_to,
forward_to,
is_client_affine,
location,
lock_duration,
max_delivery_count,
message_count,
namespaceName,
requires_session,
resourceGroupName,
status,
subscriptionId,
subscriptionName,
system_data,
topicName,
type,
updated_at
FROM azure.service_bus.vw_subscriptions
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND topicName = '{{ topicName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
location,
properties,
systemData,
type
FROM azure.service_bus.subscriptions
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND topicName = '{{ topicName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>subscriptions</code> resource.

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
INSERT INTO azure.service_bus.subscriptions (
namespaceName,
resourceGroupName,
subscriptionId,
subscriptionName,
topicName,
properties
)
SELECT 
'{{ namespaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ subscriptionName }}',
'{{ topicName }}',
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
        - name: messageCount
          value: integer
        - name: createdAt
          value: string
        - name: accessedAt
          value: string
        - name: updatedAt
          value: string
        - name: countDetails
          value:
            - name: activeMessageCount
              value: integer
            - name: deadLetterMessageCount
              value: integer
            - name: scheduledMessageCount
              value: integer
            - name: transferMessageCount
              value: integer
            - name: transferDeadLetterMessageCount
              value: integer
        - name: lockDuration
          value: string
        - name: requiresSession
          value: boolean
        - name: defaultMessageTimeToLive
          value: string
        - name: deadLetteringOnFilterEvaluationExceptions
          value: boolean
        - name: deadLetteringOnMessageExpiration
          value: boolean
        - name: duplicateDetectionHistoryTimeWindow
          value: string
        - name: maxDeliveryCount
          value: integer
        - name: status
          value: []
        - name: enableBatchedOperations
          value: boolean
        - name: autoDeleteOnIdle
          value: string
        - name: forwardTo
          value: string
        - name: forwardDeadLetteredMessagesTo
          value: string
        - name: isClientAffine
          value: boolean
        - name: clientAffineProperties
          value:
            - name: clientId
              value: string
            - name: isDurable
              value: boolean
            - name: isShared
              value: boolean
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

Deletes the specified <code>subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.service_bus.subscriptions
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND subscriptionName = '{{ subscriptionName }}'
AND topicName = '{{ topicName }}';
```
