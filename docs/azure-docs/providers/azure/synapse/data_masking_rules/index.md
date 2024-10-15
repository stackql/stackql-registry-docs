---
title: data_masking_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - data_masking_rules
  - synapse
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

Creates, updates, deletes, gets or lists a <code>data_masking_rules</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_masking_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.synapse.data_masking_rules" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_masking_rules', value: 'view', },
        { label: 'data_masking_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | field from the `properties` object |
| <CopyableCode code="alias_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="column_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataMaskingPolicyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="dataMaskingRuleName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kind" /> | `text` | The kind of Data Masking Rule. Metadata, used for Azure portal. |
| <CopyableCode code="location" /> | `text` | The location of the data masking rule. |
| <CopyableCode code="masking_function" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_from" /> | `text` | field from the `properties` object |
| <CopyableCode code="number_to" /> | `text` | field from the `properties` object |
| <CopyableCode code="prefix_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="replacement_string" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="rule_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="schema_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="sqlPoolName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="suffix_size" /> | `text` | field from the `properties` object |
| <CopyableCode code="table_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` | The kind of Data Masking Rule. Metadata, used for Azure portal. |
| <CopyableCode code="location" /> | `string` | The location of the data masking rule. |
| <CopyableCode code="properties" /> | `object` | The properties of a Sql pool data masking rule. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataMaskingPolicyName, dataMaskingRuleName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Gets the specific Sql pool data masking rule. |
| <CopyableCode code="list_by_sql_pool" /> | `SELECT` | <CopyableCode code="dataMaskingPolicyName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Gets a list of Sql pool data masking rules. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataMaskingPolicyName, dataMaskingRuleName, resourceGroupName, sqlPoolName, subscriptionId, workspaceName" /> | Creates or updates a Sql pool data masking rule. |

## `SELECT` examples

Gets a list of Sql pool data masking rules.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_masking_rules', value: 'view', },
        { label: 'data_masking_rules', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
alias_name,
column_name,
dataMaskingPolicyName,
dataMaskingRuleName,
kind,
location,
masking_function,
number_from,
number_to,
prefix_size,
replacement_string,
resourceGroupName,
rule_state,
schema_name,
sqlPoolName,
subscriptionId,
suffix_size,
table_name,
workspaceName
FROM azure.synapse.vw_data_masking_rules
WHERE dataMaskingPolicyName = '{{ dataMaskingPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
kind,
location,
properties
FROM azure.synapse.data_masking_rules
WHERE dataMaskingPolicyName = '{{ dataMaskingPolicyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND sqlPoolName = '{{ sqlPoolName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_masking_rules</code> resource.

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
INSERT INTO azure.synapse.data_masking_rules (
dataMaskingPolicyName,
dataMaskingRuleName,
resourceGroupName,
sqlPoolName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ dataMaskingPolicyName }}',
'{{ dataMaskingRuleName }}',
'{{ resourceGroupName }}',
'{{ sqlPoolName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
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
        - name: id
          value: string
        - name: aliasName
          value: string
        - name: ruleState
          value: string
        - name: schemaName
          value: string
        - name: tableName
          value: string
        - name: columnName
          value: string
        - name: maskingFunction
          value: string
        - name: numberFrom
          value: string
        - name: numberTo
          value: string
        - name: prefixSize
          value: string
        - name: suffixSize
          value: string
        - name: replacementString
          value: string
    - name: location
      value: string
    - name: kind
      value: string

```
</TabItem>
</Tabs>
