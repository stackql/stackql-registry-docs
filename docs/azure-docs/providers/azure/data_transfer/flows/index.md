---
title: flows
hide_title: false
hide_table_of_contents: false
keywords:
  - flows
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

Creates, updates, deletes, gets or lists a <code>flows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_transfer.flows" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_flows', value: 'view', },
        { label: 'flows', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="connection" /> | `text` | field from the `properties` object |
| <CopyableCode code="connectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="flowName" /> | `text` | field from the `properties` object |
| <CopyableCode code="flow_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="flow_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="identity" /> | `text` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="key_vault_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="link_status" /> | `text` | field from the `properties` object |
| <CopyableCode code="linked_flow_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="messaging_options" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan" /> | `text` | Plan for the resource. |
| <CopyableCode code="policies" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="schema" /> | `text` | field from the `properties` object |
| <CopyableCode code="service_bus_queue_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_account_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="storage_container_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="plan" /> | `object` | Plan for the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of flow |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="connectionName, flowName, resourceGroupName, subscriptionId" /> | Gets flow resource. |
| <CopyableCode code="list_by_connection" /> | `SELECT` | <CopyableCode code="connectionName, resourceGroupName, subscriptionId" /> | Gets flows in a connection. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="connectionName, flowName, resourceGroupName, subscriptionId, data__location" /> | Creates or updates the flow resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="connectionName, flowName, resourceGroupName, subscriptionId" /> | Deletes the flow resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="connectionName, flowName, resourceGroupName, subscriptionId" /> | Updates the flow resource. |
| <CopyableCode code="disable" /> | `EXEC` | <CopyableCode code="connectionName, flowName, resourceGroupName, subscriptionId" /> | Disables the specified flow |
| <CopyableCode code="enable" /> | `EXEC` | <CopyableCode code="connectionName, flowName, resourceGroupName, subscriptionId" /> | Enables the specified flow. |
| <CopyableCode code="link" /> | `EXEC` | <CopyableCode code="connectionName, flowName, resourceGroupName, subscriptionId, data__id" /> | Links the specified flow. |

## `SELECT` examples

Gets flows in a connection.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_flows', value: 'view', },
        { label: 'flows', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
connection,
connectionName,
data_type,
flowName,
flow_id,
flow_type,
identity,
key_vault_uri,
link_status,
linked_flow_id,
location,
messaging_options,
plan,
policies,
provisioning_state,
resourceGroupName,
schema,
service_bus_queue_id,
status,
storage_account_id,
storage_account_name,
storage_container_name,
subscriptionId,
tags
FROM azure.data_transfer.vw_flows
WHERE connectionName = '{{ connectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
identity,
location,
plan,
properties,
tags
FROM azure.data_transfer.flows
WHERE connectionName = '{{ connectionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>flows</code> resource.

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
INSERT INTO azure.data_transfer.flows (
connectionName,
flowName,
resourceGroupName,
subscriptionId,
data__location,
properties,
plan,
identity,
tags,
location
)
SELECT 
'{{ connectionName }}',
'{{ flowName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__location }}',
'{{ properties }}',
'{{ plan }}',
'{{ identity }}',
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
        - name: connection
          value:
            - name: name
              value: string
            - name: id
              value: string
            - name: location
              value: string
            - name: subscriptionName
              value: string
        - name: flowId
          value: string
        - name: keyVaultUri
          value: string
        - name: linkStatus
          value: string
        - name: linkedFlowId
          value: string
        - name: status
          value: string
        - name: storageAccountName
          value: string
        - name: storageAccountId
          value: string
        - name: storageContainerName
          value: string
        - name: serviceBusQueueId
          value: string
        - name: flowType
          value: []
        - name: dataType
          value: string
        - name: provisioningState
          value: string
        - name: policies
          value:
            - string
        - name: schema
          value:
            - name: id
              value: string
            - name: connectionId
              value: string
            - name: status
              value: string
            - name: name
              value: string
            - name: content
              value: string
            - name: direction
              value: string
        - name: messagingOptions
          value:
            - name: billingTier
              value: string
    - name: plan
      value:
        - name: name
          value: string
        - name: publisher
          value: string
        - name: product
          value: string
        - name: promotionCode
          value: string
        - name: version
          value: string
    - name: identity
      value:
        - name: principalId
          value: string
        - name: tenantId
          value: string
        - name: type
          value: []
        - name: userAssignedIdentities
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>flows</code> resource.

```sql
/*+ update */
UPDATE azure.data_transfer.flows
SET 
identity = '{{ identity }}',
tags = '{{ tags }}'
WHERE 
connectionName = '{{ connectionName }}'
AND flowName = '{{ flowName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>flows</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_transfer.flows
WHERE connectionName = '{{ connectionName }}'
AND flowName = '{{ flowName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
