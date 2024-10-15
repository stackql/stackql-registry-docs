---
title: key_values
hide_title: false
hide_table_of_contents: false
keywords:
  - key_values
  - app_configuration
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

Creates, updates, deletes, gets or lists a <code>key_values</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>key_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.app_configuration.key_values" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_key_values', value: 'view', },
        { label: 'key_values', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource ID. |
| <CopyableCode code="name" /> | `text` | The name of the resource. |
| <CopyableCode code="configStoreName" /> | `text` | field from the `properties` object |
| <CopyableCode code="content_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="e_tag" /> | `text` | field from the `properties` object |
| <CopyableCode code="key" /> | `text` | field from the `properties` object |
| <CopyableCode code="keyValueName" /> | `text` | field from the `properties` object |
| <CopyableCode code="label" /> | `text` | field from the `properties` object |
| <CopyableCode code="last_modified" /> | `text` | field from the `properties` object |
| <CopyableCode code="locked" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The type of the resource. |
| <CopyableCode code="value" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource ID. |
| <CopyableCode code="name" /> | `string` | The name of the resource. |
| <CopyableCode code="properties" /> | `object` | All key-value properties. |
| <CopyableCode code="type" /> | `string` | The type of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="configStoreName, keyValueName, resourceGroupName, subscriptionId" /> | Gets the properties of the specified key-value. NOTE: This operation is intended for use in ARM Template deployments. For all other scenarios involving App Configuration key-values the data plane API should be used instead. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="configStoreName, keyValueName, resourceGroupName, subscriptionId" /> | Creates a key-value. NOTE: This operation is intended for use in ARM Template deployments. For all other scenarios involving App Configuration key-values the data plane API should be used instead. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="configStoreName, keyValueName, resourceGroupName, subscriptionId" /> | Deletes a key-value. NOTE: This operation is intended for use in ARM Template deployments. For all other scenarios involving App Configuration key-values the data plane API should be used instead. |

## `SELECT` examples

Gets the properties of the specified key-value. NOTE: This operation is intended for use in ARM Template deployments. For all other scenarios involving App Configuration key-values the data plane API should be used instead.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_key_values', value: 'view', },
        { label: 'key_values', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
configStoreName,
content_type,
e_tag,
key,
keyValueName,
label,
last_modified,
locked,
resourceGroupName,
subscriptionId,
tags,
type,
value
FROM azure.app_configuration.vw_key_values
WHERE configStoreName = '{{ configStoreName }}'
AND keyValueName = '{{ keyValueName }}'
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
type
FROM azure.app_configuration.key_values
WHERE configStoreName = '{{ configStoreName }}'
AND keyValueName = '{{ keyValueName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>key_values</code> resource.

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
INSERT INTO azure.app_configuration.key_values (
configStoreName,
keyValueName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ configStoreName }}',
'{{ keyValueName }}',
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
    - name: properties
      value:
        - name: key
          value: string
        - name: label
          value: string
        - name: value
          value: string
        - name: contentType
          value: string
        - name: eTag
          value: string
        - name: lastModified
          value: string
        - name: locked
          value: boolean
        - name: tags
          value: object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>key_values</code> resource.

```sql
/*+ delete */
DELETE FROM azure.app_configuration.key_values
WHERE configStoreName = '{{ configStoreName }}'
AND keyValueName = '{{ keyValueName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
