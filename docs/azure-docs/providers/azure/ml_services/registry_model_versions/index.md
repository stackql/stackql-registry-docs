---
title: registry_model_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - registry_model_versions
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

Creates, updates, deletes, gets or lists a <code>registry_model_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>registry_model_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.ml_services.registry_model_versions" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registry_model_versions', value: 'view', },
        { label: 'registry_model_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="flavors" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_anonymous" /> | `text` | field from the `properties` object |
| <CopyableCode code="is_archived" /> | `text` | field from the `properties` object |
| <CopyableCode code="job_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="modelName" /> | `text` | field from the `properties` object |
| <CopyableCode code="model_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="model_uri" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="registryName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="stage" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="version" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Model asset version details. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="modelName, registryName, resourceGroupName, subscriptionId, version" /> |  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="modelName, registryName, resourceGroupName, subscriptionId" /> |  |
| <CopyableCode code="create_or_get_start_pending_upload" /> | `INSERT` | <CopyableCode code="modelName, registryName, resourceGroupName, subscriptionId, version" /> |  |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="modelName, registryName, resourceGroupName, subscriptionId, version, data__properties" /> |  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="modelName, registryName, resourceGroupName, subscriptionId, version" /> |  |

## `SELECT` examples



<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_registry_model_versions', value: 'view', },
        { label: 'registry_model_versions', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
flavors,
is_anonymous,
is_archived,
job_name,
modelName,
model_type,
model_uri,
provisioning_state,
registryName,
resourceGroupName,
stage,
subscriptionId,
version
FROM azure.ml_services.vw_registry_model_versions
WHERE modelName = '{{ modelName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.ml_services.registry_model_versions
WHERE modelName = '{{ modelName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>registry_model_versions</code> resource.

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
INSERT INTO azure.ml_services.registry_model_versions (
modelName,
registryName,
resourceGroupName,
subscriptionId,
version,
pendingUploadId,
pendingUploadType
)
SELECT 
'{{ modelName }}',
'{{ registryName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ version }}',
'{{ pendingUploadId }}',
'{{ pendingUploadType }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: pendingUploadId
      value: string
    - name: pendingUploadType
      value: []

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>registry_model_versions</code> resource.

```sql
/*+ delete */
DELETE FROM azure.ml_services.registry_model_versions
WHERE modelName = '{{ modelName }}'
AND registryName = '{{ registryName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND version = '{{ version }}';
```
