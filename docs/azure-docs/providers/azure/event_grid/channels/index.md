---
title: channels
hide_title: false
hide_table_of_contents: false
keywords:
  - channels
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

Creates, updates, deletes, gets or lists a <code>channels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>channels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.event_grid.channels" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_channels', value: 'view', },
        { label: 'channels', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `text` | The name of the resource |
| <CopyableCode code="channelName" /> | `text` | field from the `properties` object |
| <CopyableCode code="channel_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="expiration_time_if_not_activated_utc" /> | `text` | field from the `properties` object |
| <CopyableCode code="message_for_activation" /> | `text` | field from the `properties` object |
| <CopyableCode code="partnerNamespaceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_destination_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="partner_topic_info" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="readiness_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of the Channel. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="channelName, partnerNamespaceName, resourceGroupName, subscriptionId" /> | Get properties of a channel. |
| <CopyableCode code="list_by_partner_namespace" /> | `SELECT` | <CopyableCode code="partnerNamespaceName, resourceGroupName, subscriptionId" /> | List all the channels in a partner namespace. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="channelName, partnerNamespaceName, resourceGroupName, subscriptionId" /> | Synchronously creates or updates a new channel with the specified parameters. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="channelName, partnerNamespaceName, resourceGroupName, subscriptionId" /> | Delete an existing channel. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="channelName, partnerNamespaceName, resourceGroupName, subscriptionId" /> | Synchronously updates a channel with the specified parameters. |

## `SELECT` examples

List all the channels in a partner namespace.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_channels', value: 'view', },
        { label: 'channels', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
channelName,
channel_type,
expiration_time_if_not_activated_utc,
message_for_activation,
partnerNamespaceName,
partner_destination_info,
partner_topic_info,
provisioning_state,
readiness_state,
resourceGroupName,
subscriptionId,
system_data,
type
FROM azure.event_grid.vw_channels
WHERE partnerNamespaceName = '{{ partnerNamespaceName }}'
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
FROM azure.event_grid.channels
WHERE partnerNamespaceName = '{{ partnerNamespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>channels</code> resource.

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
INSERT INTO azure.event_grid.channels (
channelName,
partnerNamespaceName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ channelName }}',
'{{ partnerNamespaceName }}',
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
        - name: channelType
          value: string
        - name: partnerTopicInfo
          value:
            - name: azureSubscriptionId
              value: string
            - name: resourceGroupName
              value: string
            - name: name
              value: string
            - name: eventTypeInfo
              value:
                - name: kind
                  value: string
                - name: inlineEventTypes
                  value: object
            - name: source
              value: string
        - name: partnerDestinationInfo
          value:
            - name: azureSubscriptionId
              value: string
            - name: resourceGroupName
              value: string
            - name: name
              value: string
            - name: endpointType
              value: string
            - name: endpointServiceContext
              value: string
            - name: resourceMoveChangeHistory
              value:
                - - name: azureSubscriptionId
                    value: string
                  - name: resourceGroupName
                    value: string
                  - name: changedTimeUtc
                    value: string
        - name: messageForActivation
          value: string
        - name: provisioningState
          value: string
        - name: readinessState
          value: string
        - name: expirationTimeIfNotActivatedUtc
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>channels</code> resource.

```sql
/*+ update */
UPDATE azure.event_grid.channels
SET 
properties = '{{ properties }}'
WHERE 
channelName = '{{ channelName }}'
AND partnerNamespaceName = '{{ partnerNamespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>channels</code> resource.

```sql
/*+ delete */
DELETE FROM azure.event_grid.channels
WHERE channelName = '{{ channelName }}'
AND partnerNamespaceName = '{{ partnerNamespaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
