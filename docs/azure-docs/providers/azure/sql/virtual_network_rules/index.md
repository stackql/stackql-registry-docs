---
title: virtual_network_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_rules
  - sql
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

Creates, updates, deletes, gets or lists a <code>virtual_network_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_network_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.virtual_network_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_rules', value: 'view', },
        { label: 'virtual_network_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="ignore_missing_vnet_service_endpoint" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="serverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="state" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtualNetworkRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="virtual_network_subnet_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of a virtual network rule. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, virtualNetworkRuleName" /> | Gets a virtual network rule. |
| <CopyableCode code="list_by_server" /> | `SELECT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId" /> | Gets a list of virtual network rules in a server. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, virtualNetworkRuleName" /> | Creates or updates an existing virtual network rule. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceGroupName, serverName, subscriptionId, virtualNetworkRuleName" /> | Deletes the virtual network rule with the given name. |

## `SELECT` examples

Gets a list of virtual network rules in a server.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_virtual_network_rules', value: 'view', },
        { label: 'virtual_network_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
ignore_missing_vnet_service_endpoint,
resourceGroupName,
serverName,
state,
subscriptionId,
virtualNetworkRuleName,
virtual_network_subnet_id
FROM azure.sql.vw_virtual_network_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.sql.virtual_network_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>virtual_network_rules</code> resource.

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
INSERT INTO azure.sql.virtual_network_rules (
resourceGroupName,
serverName,
subscriptionId,
virtualNetworkRuleName,
properties
)
SELECT 
'{{ resourceGroupName }}',
'{{ serverName }}',
'{{ subscriptionId }}',
'{{ virtualNetworkRuleName }}',
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
        - name: virtualNetworkSubnetId
          value: string
        - name: ignoreMissingVnetServiceEndpoint
          value: boolean
        - name: state
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>virtual_network_rules</code> resource.

```sql
/*+ delete */
DELETE FROM azure.sql.virtual_network_rules
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkRuleName = '{{ virtualNetworkRuleName }}';
```
