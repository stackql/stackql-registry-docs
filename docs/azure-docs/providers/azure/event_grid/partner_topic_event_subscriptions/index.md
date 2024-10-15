---
title: partner_topic_event_subscriptions
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_topic_event_subscriptions
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

Creates, updates, deletes, gets or lists a <code>partner_topic_event_subscriptions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partner_topic_event_subscriptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.partner_topic_event_subscriptions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_partner_topic_event_subscriptions', value: 'view', },
        { label: 'partner_topic_event_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="dead_letter_destination" /> | `text` | field from the `properties` object |
| <CopyableCode code="dead_letter_with_resource_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="delivery_with_resource_identity" /> | `text` | field from the `properties` object |
| <CopyableCode code="destination" /> | `text` | field from the `properties` object |
| <CopyableCode code="eventSubscriptionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_delivery_schema" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_time_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="filter" /> | `text` | field from the `properties` object |
| <CopyableCode code="labels" /> | `text` | field from the `properties` object |
| <CopyableCode code="partnerTopicName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="retry_policy" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="topic" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the Event Subscription. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId" /> | Get properties of an event subscription of a partner topic. |
| <CopyableCode code="list_by_partner_topic" /> | `SELECT` | <CopyableCode code="partnerTopicName, resourceGroupName, subscriptionId" /> | List event subscriptions that belong to a specific partner topic. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId" /> | Asynchronously creates or updates an event subscription of a partner topic with the specified parameters. Existing event subscriptions will be updated with this API. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId" /> | Delete an existing event subscription of a partner topic. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="eventSubscriptionName, partnerTopicName, resourceGroupName, subscriptionId" /> | Update an existing event subscription of a partner topic. |

## `SELECT` examples

List event subscriptions that belong to a specific partner topic.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_partner_topic_event_subscriptions', value: 'view', },
        { label: 'partner_topic_event_subscriptions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
dead_letter_destination,
dead_letter_with_resource_identity,
delivery_with_resource_identity,
destination,
eventSubscriptionName,
event_delivery_schema,
expiration_time_utc,
filter,
labels,
partnerTopicName,
provisioning_state,
resourceGroupName,
retry_policy,
subscriptionId,
system_data,
topic,
type
FROM azure.event_grid.vw_partner_topic_event_subscriptions
WHERE partnerTopicName = '{{ partnerTopicName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
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
FROM azure.event_grid.partner_topic_event_subscriptions
WHERE partnerTopicName = '{{ partnerTopicName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>partner_topic_event_subscriptions</code> resource.

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
INSERT INTO azure.event_grid.partner_topic_event_subscriptions (
eventSubscriptionName,
partnerTopicName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ eventSubscriptionName }}',
'{{ partnerTopicName }}',
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
        - name: topic
          value: string
        - name: provisioningState
          value: string
        - name: destination
          value:
            - name: endpointType
              value: string
        - name: deliveryWithResourceIdentity
          value:
            - name: identity
              value:
                - name: type
                  value: string
                - name: userAssignedIdentity
                  value: string
        - name: filter
          value:
            - name: subjectBeginsWith
              value: string
            - name: subjectEndsWith
              value: string
            - name: includedEventTypes
              value:
                - string
            - name: isSubjectCaseSensitive
              value: boolean
            - name: enableAdvancedFilteringOnArrays
              value: boolean
            - name: advancedFilters
              value:
                - - name: operatorType
                    value: string
                  - name: key
                    value: string
        - name: labels
          value:
            - string
        - name: expirationTimeUtc
          value: string
        - name: eventDeliverySchema
          value: string
        - name: retryPolicy
          value:
            - name: maxDeliveryAttempts
              value: integer
            - name: eventTimeToLiveInMinutes
              value: integer
        - name: deadLetterDestination
          value:
            - name: endpointType
              value: string
        - name: deadLetterWithResourceIdentity
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>partner_topic_event_subscriptions</code> resource.

```sql
/*+ update */
UPDATE azure.event_grid.partner_topic_event_subscriptions
SET 
destination = '{{ destination }}',
deliveryWithResourceIdentity = '{{ deliveryWithResourceIdentity }}',
filter = '{{ filter }}',
labels = '{{ labels }}',
expirationTimeUtc = '{{ expirationTimeUtc }}',
eventDeliverySchema = '{{ eventDeliverySchema }}',
retryPolicy = '{{ retryPolicy }}',
deadLetterDestination = '{{ deadLetterDestination }}',
deadLetterWithResourceIdentity = '{{ deadLetterWithResourceIdentity }}'
WHERE 
eventSubscriptionName = '{{ eventSubscriptionName }}'
AND partnerTopicName = '{{ partnerTopicName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>partner_topic_event_subscriptions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.event_grid.partner_topic_event_subscriptions
WHERE eventSubscriptionName = '{{ eventSubscriptionName }}'
AND partnerTopicName = '{{ partnerTopicName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
