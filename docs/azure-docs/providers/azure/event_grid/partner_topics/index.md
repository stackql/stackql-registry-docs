---
title: partner_topics
hide_title: false
hide_table_of_contents: false
keywords:
  - partner_topics
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

Creates, updates, deletes, gets or lists a <code>partner_topics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>partner_topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.partner_topics" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_partner_topics', value: 'view', },
        { label: 'partner_topics', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="activation_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_type_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_time_if_not_activated_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | The identity information for the resource. |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="message_for_activation" /> | `text` | field from the `properties` object |
| <CopyableCode code="partnerTopicName" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_registration_immutable_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_topic_friendly_description" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="source" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | The identity information for the resource. |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the Partner Topic. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="partnerTopicName, resourceGroupName, subscriptionId" /> | Get properties of a partner topic. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | List all the partner topics under a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List all the partner topics under an Azure subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="partnerTopicName, resourceGroupName, subscriptionId" /> | Asynchronously creates a new partner topic with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="partnerTopicName, resourceGroupName, subscriptionId" /> | Delete existing partner topic. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="partnerTopicName, resourceGroupName, subscriptionId" /> | Asynchronously updates a partner topic with the specified parameters. |
| <CopyableCode code="activate" /> | `EXEC` | <CopyableCode code="partnerTopicName, resourceGroupName, subscriptionId" /> | Activate a newly created partner topic. |
| <CopyableCode code="deactivate" /> | `EXEC` | <CopyableCode code="partnerTopicName, resourceGroupName, subscriptionId" /> | Deactivate specific partner topic. |

## `SELECT` examples

List all the partner topics under an Azure subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_partner_topics', value: 'view', },
        { label: 'partner_topics', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
activation_state,
event_type_info,
expiration_time_if_not_activated_utc,
identity,
location,
message_for_activation,
partnerTopicName,
partner_registration_immutable_id,
partner_topic_friendly_description,
provisioning_state,
resourceGroupName,
source,
subscriptionId,
system_data,
tags
FROM azure.event_grid.vw_partner_topics
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
properties,
systemData,
tags
FROM azure.event_grid.partner_topics
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>partner_topics</code> resource.

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
INSERT INTO azure.event_grid.partner_topics (
partnerTopicName,
resourceGroupName,
subscriptionId,
tags,
location,
properties,
identity
)
SELECT 
'{{ partnerTopicName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ tags }}',
'{{ location }}',
'{{ properties }}',
'{{ identity }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: location
      value: string
    - name: properties
      value:
        - name: partnerRegistrationImmutableId
          value: string
        - name: source
          value: string
        - name: eventTypeInfo
          value:
            - name: kind
              value: string
            - name: inlineEventTypes
              value: object
        - name: expirationTimeIfNotActivatedUtc
          value: string
        - name: provisioningState
          value: string
        - name: activationState
          value: string
        - name: partnerTopicFriendlyDescription
          value: string
        - name: messageForActivation
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
    - name: identity
      value:
        - name: type
          value: string
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: userAssignedIdentities
          value: object

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>partner_topics</code> resource.

```sql
/*+ update */
UPDATE azure.event_grid.partner_topics
SET 
tags = '{{ tags }}',
identity = '{{ identity }}'
WHERE 
partnerTopicName = '{{ partnerTopicName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>partner_topics</code> resource.

```sql
/*+ delete */
DELETE FROM azure.event_grid.partner_topics
WHERE partnerTopicName = '{{ partnerTopicName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
