---
title: policies
hide_title: false
hide_table_of_contents: false
keywords:
  - policies
  - data_replication
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

Creates, updates, deletes, gets or lists a <code>policies</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_replication.policies" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policies', value: 'view', },
        { label: 'policies', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name of the resource. |
| <CopyableCode code="custom_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="policyName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets or sets the type of the resource. |
| <CopyableCode code="vaultName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name of the resource. |
| <CopyableCode code="properties" /> | `object` | Policy model properties. |
| <CopyableCode code="systemData" /> | `object` | System data required to be defined for Azure resources. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="policyName, resourceGroupName, subscriptionId, vaultName" /> | Gets the details of the policy. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Gets the list of policies in the given vault. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="policyName, resourceGroupName, subscriptionId, vaultName, data__properties" /> | Creates the policy. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="policyName, resourceGroupName, subscriptionId, vaultName" /> | Removes the policy. |

## `SELECT` examples

Gets the list of policies in the given vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_policies', value: 'view', },
        { label: 'policies', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
custom_properties,
policyName,
provisioning_state,
resourceGroupName,
subscriptionId,
system_data,
type,
vaultName
FROM azure.data_replication.vw_policies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
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
FROM azure.data_replication.policies
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policies</code> resource.

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
INSERT INTO azure.data_replication.policies (
policyName,
resourceGroupName,
subscriptionId,
vaultName,
data__properties,
properties
)
SELECT 
'{{ policyName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ vaultName }}',
'{{ data__properties }}',
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
        - name: provisioningState
          value: string
        - name: customProperties
          value:
            - name: instanceType
              value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: systemData
      value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>policies</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_replication.policies
WHERE policyName = '{{ policyName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
