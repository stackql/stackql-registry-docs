---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - data_transfer
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

Creates, updates, deletes, gets or lists a <code>connections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_transfer.connections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connections', value: 'view', },
        { label: 'connections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="approver" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="date_submitted" /> | `text` | field from the `properties` object |
| <CopyableCode code="direction" /> | `text` | field from the `properties` object |
| <CopyableCode code="flow_types" /> | `text` | field from the `properties` object |
| <CopyableCode code="justification" /> | `text` | field from the `properties` object |
| <CopyableCode code="link_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="linked_connection_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="pin" /> | `text` | field from the `properties` object |
| <CopyableCode code="pipeline" /> | `text` | field from the `properties` object |
| <CopyableCode code="policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="primary_contact" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="remote_subscription_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="requirement_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schemas" /> | `text` | field from the `properties` object |
| <CopyableCode code="secondary_contacts" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_reason" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of connection |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId" /> | Gets connection resource. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets connections in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets connections in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId, data__location" /> | Creates or updates the connection resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId" /> | Deletes the connection resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId" /> | Updates the connection resource. |
| <CopyableCode code="link" /> | `EXEC` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId, data__id" /> | Links the connection to its pending connection. |

## `SELECT` examples

Gets connections in a subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_connections', value: 'view', },
        { label: 'connections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
approver,
connectionName,
date_submitted,
direction,
flow_types,
justification,
link_status,
linked_connection_id,
location,
pin,
pipeline,
policies,
primary_contact,
provisioning_state,
remote_subscription_id,
requirement_id,
resourceGroupName,
schemas,
secondary_contacts,
status,
status_reason,
subscriptionId,
tags
FROM azure.data_transfer.vw_connections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
location,
properties,
tags
FROM azure.data_transfer.connections
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>connections</code> resource.

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
INSERT INTO azure.data_transfer.connections (
connectionName,
resourceGroupName,
subscriptionId,
data__location,
properties,
tags,
location
)
SELECT 
'{{ connectionName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ properties }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: pipeline
          value: string
        - name: direction
          value: string
        - name: justification
          value: string
        - name: status
          value: string
        - name: statusReason
          value: string
        - name: linkStatus
          value: string
        - name: linkedConnectionId
          value: string
        - name: flowTypes
          value: []
        - name: requirementId
          value: string
        - name: remoteSubscriptionId
          value: string
        - name: approver
          value: string
        - name: pin
          value: string
        - name: dateSubmitted
          value: string
        - name: primaryContact
          value: string
        - name: secondaryContacts
          value:
            - string
        - name: provisioningState
          value: string
        - name: policies
          value:
            - string
        - name: schemas
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>connections</code> resource.

```sql
/*+ update */
UPDATE azure.data_transfer.connections
SET 
tags = '{{ tags }}'
WHERE 
connectionName = '{{ connectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>connections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_transfer.connections
WHERE connectionName = '{{ connectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
