---
title: linked_services
hide_title: false
hide_table_of_contents: false
keywords:
  - linked_services
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

Creates, updates, deletes, gets or lists a <code>linked_services</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>linked_services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_factory.linked_services" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_linked_services', value: 'view', },
        { label: 'linked_services', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The resource identifier. |
| <CopyableCode code="name" /> | `text` | The resource name. |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="annotations" /> | `text` | field from the `properties` object |
| <CopyableCode code="connect_via" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | Etag identifies change in the resource. |
| <CopyableCode code="factoryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="linkedServiceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The resource type. |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | Etag identifies change in the resource. |
| <CopyableCode code="properties" /> | `object` | The nested object which contains the information and credential which can be used to connect with related store or compute resource. |
| <CopyableCode code="type" /> | `string` | The resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="factoryName, linkedServiceName, resourceGroupName, subscriptionId" /> | Gets a linked service. |
| <CopyableCode code="list_by_factory" /> | `SELECT` | <CopyableCode code="factoryName, resourceGroupName, subscriptionId" /> | Lists linked services. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="factoryName, linkedServiceName, resourceGroupName, subscriptionId, data__properties" /> | Creates or updates a linked service. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="factoryName, linkedServiceName, resourceGroupName, subscriptionId" /> | Deletes a linked service. |

## `SELECT` examples

Lists linked services.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_linked_services', value: 'view', },
        { label: 'linked_services', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
description,
annotations,
connect_via,
etag,
factoryName,
linkedServiceName,
parameters,
resourceGroupName,
subscriptionId,
type,
version
FROM azure.data_factory.vw_linked_services
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
FROM azure.data_factory.linked_services
WHERE factoryName = '{{ factoryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>linked_services</code> resource.

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
INSERT INTO azure.data_factory.linked_services (
factoryName,
linkedServiceName,
resourceGroupName,
subscriptionId,
data__properties,
properties
)
SELECT 
'{{ factoryName }}',
'{{ linkedServiceName }}',
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
        - name: version
          value: string
        - name: connectVia
          value:
            - name: type
              value: string
            - name: referenceName
              value: string
            - name: parameters
              value: []
        - name: description
          value: string
        - name: parameters
          value: []
        - name: annotations
          value:
            - object

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>linked_services</code> resource.

```sql
/*+ delete */
DELETE FROM azure.data_factory.linked_services
WHERE factoryName = '{{ factoryName }}'
AND linkedServiceName = '{{ linkedServiceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
