---
title: firewall_policy_rule_collection_group_drafts
hide_title: false
hide_table_of_contents: false
keywords:
  - firewall_policy_rule_collection_group_drafts
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

Creates, updates, deletes, gets or lists a <code>firewall_policy_rule_collection_group_drafts</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>firewall_policy_rule_collection_group_drafts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.firewall_policy_rule_collection_group_drafts" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_firewall_policy_rule_collection_group_drafts', value: 'view', },
        { label: 'firewall_policy_rule_collection_group_drafts', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="firewallPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="priority" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="ruleCollectionGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rule_collections" /> | `text` | field from the `properties` object |
| <CopyableCode code="size" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Rule Group type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| <CopyableCode code="properties" /> | `object` | Properties of the rule collection group draft. |
| <CopyableCode code="type" /> | `string` | Rule Group type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="firewallPolicyName, resourceGroupName, ruleCollectionGroupName, subscriptionId" /> | Get Rule Collection Group Draft. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="firewallPolicyName, resourceGroupName, ruleCollectionGroupName, subscriptionId" /> | Create or Update Rule Collection Group Draft. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="firewallPolicyName, resourceGroupName, ruleCollectionGroupName, subscriptionId" /> | Delete Rule Collection Group Draft. |

## `SELECT` examples

Get Rule Collection Group Draft.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_firewall_policy_rule_collection_group_drafts', value: 'view', },
        { label: 'firewall_policy_rule_collection_group_drafts', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
firewallPolicyName,
priority,
resourceGroupName,
ruleCollectionGroupName,
rule_collections,
size,
subscriptionId,
type
FROM azure.network.vw_firewall_policy_rule_collection_group_drafts
WHERE firewallPolicyName = '{{ firewallPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleCollectionGroupName = '{{ ruleCollectionGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.network.firewall_policy_rule_collection_group_drafts
WHERE firewallPolicyName = '{{ firewallPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleCollectionGroupName = '{{ ruleCollectionGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>firewall_policy_rule_collection_group_drafts</code> resource.

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
INSERT INTO azure.network.firewall_policy_rule_collection_group_drafts (
firewallPolicyName,
resourceGroupName,
ruleCollectionGroupName,
subscriptionId,
properties,
name,
id
)
SELECT 
'{{ firewallPolicyName }}',
'{{ resourceGroupName }}',
'{{ ruleCollectionGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ name }}',
'{{ id }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: size
          value: string
        - name: priority
          value: integer
        - name: ruleCollections
          value:
            - - name: ruleCollectionType
                value: string
              - name: name
                value: string
              - name: priority
                value: integer
    - name: name
      value: string
    - name: type
      value: string
    - name: id
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>firewall_policy_rule_collection_group_drafts</code> resource.

```sql
/*+ delete */
DELETE FROM azure.network.firewall_policy_rule_collection_group_drafts
WHERE firewallPolicyName = '{{ firewallPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND ruleCollectionGroupName = '{{ ruleCollectionGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
