---
title: data_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - data_versions
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

Creates, updates, deletes, gets or lists a <code>data_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.data_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_versions', value: 'view', },
        { label: 'data_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_anonymous" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_archived" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Data version base definition |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, version, workspaceName" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId, workspaceName" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId, version, workspaceName, data__properties" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId, version, workspaceName" /> |  |
| <CopyableCode code="publish" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, version, workspaceName" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_versions', value: 'view', },
        { label: 'data_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
name,
data_type,
data_uri,
is_anonymous,
is_archived,
resourceGroupName,
subscriptionId,
version,
workspaceName
FROM azure.ml_services.vw_data_versions
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.ml_services.data_versions
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_versions</code> resource.

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
INSERT INTO azure.ml_services.data_versions (
name,
resourceGroupName,
subscriptionId,
version,
workspaceName,
data__properties,
properties
)
SELECT 
'{{ name }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ version }}',
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
        - name: isAnonymous
          value: boolean
        - name: isArchived
          value: boolean
        - name: dataType
          value: []
        - name: dataUri
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>data_versions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ml_services.data_versions
WHERE name = '{{ name }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND version = '{{ version }}'
AND workspaceName = '{{ workspaceName }}';
```
