---
title: routing_rule_collections
hide_title: false
hide_table_of_contents: false
keywords:
  - routing_rule_collections
  - network
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

Creates, updates, deletes, gets or lists a <code>routing_rule_collections</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>routing_rule_collections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.routing_rule_collections" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_routing_rule_collections', value: 'view', },
        { label: 'routing_rule_collections', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="applies_to" /> | `text` | field from the `properties` object |
| <CopyableCode code="configurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="disable_bgp_route_propagation" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="networkManagerName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_guid" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleCollectionName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="properties" /> | `object` | Defines the routing rule collection properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, ruleCollectionName, subscriptionId" /> | Gets a network manager routing configuration rule collection. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, subscriptionId" /> | Lists all the rule collections in a routing configuration, in a paginated format. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, ruleCollectionName, subscriptionId" /> | Creates or updates a routing rule collection. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configurationName, networkManagerName, resourceGroupName, ruleCollectionName, subscriptionId" /> | Deletes an routing rule collection. |

## `SELECT` examples

Lists all the rule collections in a routing configuration, in a paginated format.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_routing_rule_collections', value: 'view', },
        { label: 'routing_rule_collections', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
applies_to,
configurationName,
disable_bgp_route_propagation,
etag,
networkManagerName,
provisioning_state,
resourceGroupName,
resource_guid,
ruleCollectionName,
subscriptionId,
system_data,
type
FROM azure.network.vw_routing_rule_collections
WHERE configurationName = '{{ configurationName }}'
AND networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
etag,
properties,
systemData,
type
FROM azure.network.routing_rule_collections
WHERE configurationName = '{{ configurationName }}'
AND networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>routing_rule_collections</code> resource.

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
INSERT INTO azure.network.routing_rule_collections (
configurationName,
networkManagerName,
resourceGroupName,
ruleCollectionName,
subscriptionId,
properties
)
SELECT 
'{{ configurationName }}',
'{{ networkManagerName }}',
'{{ resourceGroupName }}',
'{{ ruleCollectionName }}',
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
      value:
        - name: description
          value: string
        - name: provisioningState
          value: []
        - name: resourceGuid
          value: string
        - name: appliesTo
          value:
            - - name: networkGroupId
                value: string
        - name: disableBgpRoutePropagation
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
    - name: etag
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>routing_rule_collections</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.routing_rule_collections
WHERE configurationName = '{{ configurationName }}'
AND networkManagerName = '{{ networkManagerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleCollectionName = '{{ ruleCollectionName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
