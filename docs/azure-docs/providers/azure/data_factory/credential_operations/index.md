---
title: credential_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - credential_operations
  - data_factory
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

Creates, updates, deletes, gets or lists a <code>credential_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>credential_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.credential_operations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_credential_operations', value: 'view', },
        { label: 'credential_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotations" /> | `text` | field from the `properties` object |
| <CopyableCode code="credentialName" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag identifies change in the resource. |
| <CopyableCode code="factoryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | Etag identifies change in the resource. |
| <CopyableCode code="properties" /> | `object` | The Azure Data Factory nested object which contains the information and credential which can be used to connect with related store or compute resource. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="credentialName, factoryName, resourceGroupName, subscriptionId" /> | Gets a credential. |
| <CopyableCode code="list_by_factory" /> | `SELECT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | List credentials. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="credentialName, factoryName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a credential. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="credentialName, factoryName, resourceGroupName, subscriptionId" /> | Deletes a credential. |

## `SELECT` examples

List credentials.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_credential_operations', value: 'view', },
        { label: 'credential_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
annotations,
credentialName,
etag,
factoryName,
resourceGroupName,
subscriptionId,
type
FROM azure.data_factory.vw_credential_operations
WHERE factoryName = '{{ factoryName }}'
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
type
FROM azure.data_factory.credential_operations
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>credential_operations</code> resource.

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
INSERT INTO azure.data_factory.credential_operations (
credentialName,
factoryName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ credentialName }}',
'{{ factoryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ data__properties }}',
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
    - name: etag
      value: string
    - name: properties
      value:
        - name: type
          value: string
        - name: description
          value: string
        - name: annotations
          value:
            - object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>credential_operations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_factory.credential_operations
WHERE credentialName = '{{ credentialName }}'
AND factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
