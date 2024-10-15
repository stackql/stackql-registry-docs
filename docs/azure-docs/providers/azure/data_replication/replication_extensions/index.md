---
title: replication_extensions
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_extensions
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

Creates, updates, deletes, gets or lists a <code>replication_extensions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>replication_extensions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_replication.replication_extensions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_extensions', value: 'view', },
        { label: 'replication_extensions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the Id of the resource. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name of the resource. |
| <CopyableCode code="custom_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="replicationExtensionName" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | Replication extension model properties. |
| <CopyableCode code="systemData" /> | `object` | System data required to be defined for Azure resources. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="replicationExtensionName, resourceGroupName, subscriptionId, vaultName" /> | Gets the details of the replication extension. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Gets the list of replication extensions in the given vault. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="replicationExtensionName, resourceGroupName, subscriptionId, vaultName, data__properties" /> | Creates the replication extension in the given vault. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="replicationExtensionName, resourceGroupName, subscriptionId, vaultName" /> | Deletes the replication extension in the given vault. |

## `SELECT` examples

Gets the list of replication extensions in the given vault.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_replication_extensions', value: 'view', },
        { label: 'replication_extensions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
custom_properties,
provisioning_state,
replicationExtensionName,
resourceGroupName,
subscriptionId,
system_data,
type,
vaultName
FROM azure.data_replication.vw_replication_extensions
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
FROM azure.data_replication.replication_extensions
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>replication_extensions</code> resource.

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
INSERT INTO azure.data_replication.replication_extensions (
replicationExtensionName,
resourceGroupName,
subscriptionId,
vaultName,
data__properties,
properties
)
SELECT 
'{{ replicationExtensionName }}',
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

Deletes the specified <code>replication_extensions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_replication.replication_extensions
WHERE replicationExtensionName = '{{ replicationExtensionName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND vaultName = '{{ vaultName }}';
```
