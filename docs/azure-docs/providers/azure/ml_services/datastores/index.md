---
title: datastores
hide_title: false
hide_table_of_contents: false
keywords:
  - datastores
  - ml_services
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

Creates, updates, deletes, gets or lists a <code>datastores</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>datastores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.datastores" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_datastores', value: 'view', },
        { label: 'datastores', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="datastore_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_default" /> | `text` | field from the `properties` object |
| <CopyableCode code="properties" /> | `text` | Base definition for datastore contents configuration. |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Base definition for datastore contents configuration. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId, workspaceName, data__properties" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId, workspaceName" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_datastores', value: 'view', },
        { label: 'datastores', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
description,
credentials,
datastore_type,
is_default,
properties,
resourceGroupName,
subscriptionId,
tags,
workspaceName
FROM azure.ml_services.vw_datastores
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.ml_services.datastores
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>datastores</code> resource.

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
INSERT INTO azure.ml_services.datastores (
name,
resourceGroupName,
subscriptionId,
workspaceName,
data__properties,
properties
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
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
        - name: description
          value: string
        - name: properties
          value: object
        - name: tags
          value: object
        - name: credentials
          value:
            - name: credentialsType
              value: []
        - name: datastoreType
          value: []
        - name: isDefault
          value: boolean

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>datastores</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ml_services.datastores
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
