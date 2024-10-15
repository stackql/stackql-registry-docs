---
title: namespace_topic_event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - namespace_topic_event_subscriptions
  - event_grid
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

Creates, updates, deletes, gets or lists a <code>namespace_topic_event_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>namespace_topic_event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.namespace_topic_event_subscriptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_namespace_topic_event_subscriptions', value: 'view', },
        { label: 'namespace_topic_event_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="delivery_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="eventSubscriptionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_delivery_schema" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="filters_configuration" /> | `text` | field from the `properties` object |
| <CopyableCode code="namespaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="topicName" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the event subscription. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="eventSubscriptionName, namespaceName, resourceGroupName, subscriptionId, topicName" /> | Get properties of an event subscription of a namespace topic. |
| <CopyableCode code="list_by_namespace_topic" /> | `SELECT` | <CopyableCode code="namespaceName, resourceGroupName, subscriptionId, topicName" /> | List event subscriptions that belong to a specific namespace topic. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="eventSubscriptionName, namespaceName, resourceGroupName, subscriptionId, topicName" /> | Asynchronously creates or updates an event subscription of a namespace topic with the specified parameters. Existing event subscriptions will be updated with this API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="eventSubscriptionName, namespaceName, resourceGroupName, subscriptionId, topicName" /> | Delete an existing event subscription of a namespace topic. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="eventSubscriptionName, namespaceName, resourceGroupName, subscriptionId, topicName" /> | Update an existing event subscription of a namespace topic. |

## `SELECT` examples

List event subscriptions that belong to a specific namespace topic.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_namespace_topic_event_subscriptions', value: 'view', },
        { label: 'namespace_topic_event_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
delivery_configuration,
eventSubscriptionName,
event_delivery_schema,
expiration_time_utc,
filters_configuration,
namespaceName,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
topicName,
type
FROM azure.event_grid.vw_namespace_topic_event_subscriptions
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
properties,
systemData,
type
FROM azure.event_grid.namespace_topic_event_subscriptions
WHERE namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND topicName = '{{ topicName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>namespace_topic_event_subscriptions</code> resource.

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
INSERT INTO azure.event_grid.namespace_topic_event_subscriptions (
eventSubscriptionName,
namespaceName,
resourceGroupName,
subscriptionId,
topicName,
properties
)
SELECT 
'{{ eventSubscriptionName }}',
'{{ namespaceName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ topicName }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
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
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: deliveryConfiguration
          value:
            - name: deliveryMode
              value: string
            - name: queue
              value:
                - name: receiveLockDurationInSeconds
                  value: integer
                - name: maxDeliveryCount
                  value: integer
                - name: deadLetterDestinationWithResourceIdentity
                  value:
                    - name: identity
                      value:
                        - name: type
                          value: string
                        - name: userAssignedIdentity
                          value: string
                    - name: deadLetterDestination
                      value:
                        - name: endpointType
                          value: string
                - name: eventTimeToLive
                  value: string
            - name: push
              value:
                - name: maxDeliveryCount
                  value: integer
                - name: eventTimeToLive
                  value: string
                - name: deliveryWithResourceIdentity
                  value:
                    - name: destination
                      value:
                        - name: endpointType
                          value: string
        - name: eventDeliverySchema
          value: string
        - name: filtersConfiguration
          value:
            - name: includedEventTypes
              value:
                - string
            - name: filters
              value:
                - - name: operatorType
                    value: string
                  - name: key
                    value: string
        - name: expirationTimeUtc
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>namespace_topic_event_subscriptions</code> resource.

```sql
/*+ update */
UPDATE azure.event_grid.namespace_topic_event_subscriptions
SET 
properties = '{{ properties }}'
WHERE 
eventSubscriptionName = '{{ eventSubscriptionName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND topicName = '{{ topicName }}';
```

## `DELETE` example

Deletes the specified <code>namespace_topic_event_subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.event_grid.namespace_topic_event_subscriptions
WHERE eventSubscriptionName = '{{ eventSubscriptionName }}'
AND namespaceName = '{{ namespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND topicName = '{{ topicName }}';
```
