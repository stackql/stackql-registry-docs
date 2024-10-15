---
title: projects
hide_title: false
hide_table_of_contents: false
keywords:
  - projects
  - storage_mover
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

Creates, updates, deletes, gets or lists a <code>projects</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>projects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_mover.projects" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_projects', value: 'view', },
        { label: 'projects', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `text` | field from the `properties` object |
| <CopyableCode code="projectName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="storageMoverName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Project properties. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Gets a Project resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, storageMoverName, subscriptionId" /> | Lists all Projects in a Storage Mover. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Creates or updates a Project resource, which is a logical grouping of related jobs. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Deletes a Project resource. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="projectName, resourceGroupName, storageMoverName, subscriptionId" /> | Updates properties for a Project resource. Properties not specified in the request body will be unchanged. |

## `SELECT` examples

Lists all Projects in a Storage Mover.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_projects', value: 'view', },
        { label: 'projects', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
description,
projectName,
provisioning_state,
resourceGroupName,
storageMoverName,
subscriptionId,
system_data
FROM azure.storage_mover.vw_projects
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties,
systemData
FROM azure.storage_mover.projects
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>projects</code> resource.

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
INSERT INTO azure.storage_mover.projects (
projectName,
resourceGroupName,
storageMoverName,
subscriptionId,
properties,
systemData
)
SELECT 
'{{ projectName }}',
'{{ resourceGroupName }}',
'{{ storageMoverName }}',
'{{ subscriptionId }}',
'{{ properties }}',
'{{ systemData }}'
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
        - name: provisioningState
          value: []
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>projects</code> resource.

```sql
/*+ update */
UPDATE azure.storage_mover.projects
SET 
properties = '{{ properties }}'
WHERE 
projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```

## `DELETE` example

Deletes the specified <code>projects</code> resource.

```sql
/*+ delete */
DELETE FROM azure.storage_mover.projects
WHERE projectName = '{{ projectName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND storageMoverName = '{{ storageMoverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
