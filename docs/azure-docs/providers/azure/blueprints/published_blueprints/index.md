---
title: published_blueprints
hide_title: false
hide_table_of_contents: false
keywords:
  - published_blueprints
  - blueprints
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

Creates, updates, deletes, gets or lists a <code>published_blueprints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>published_blueprints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.blueprints.published_blueprints" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_published_blueprints', value: 'view', },
        { label: 'published_blueprints', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | String Id used to locate any resource on Azure. |
| <CopyableCode code="name" /> | `text` | Name of this resource. |
| <CopyableCode code="blueprintName" /> | `text` | field from the `properties` object |
| <CopyableCode code="blueprint_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="change_notes" /> | `text` | field from the `properties` object |
| <CopyableCode code="parameters" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceScope" /> | `text` | field from the `properties` object |
| <CopyableCode code="resource_groups" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="target_scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of this resource. |
| <CopyableCode code="versionId" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | String Id used to locate any resource on Azure. |
| <CopyableCode code="name" /> | `string` | Name of this resource. |
| <CopyableCode code="properties" /> | `object` | Schema for published blueprint definition properties. |
| <CopyableCode code="type" /> | `string` | Type of this resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="blueprintName, resourceScope, versionId" /> | Get a published version of a blueprint definition. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="blueprintName, resourceScope" /> | List published versions of given blueprint definition. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="blueprintName, resourceScope, versionId, data__properties" /> | Publish a new version of the blueprint definition with the latest artifacts. Published blueprint definitions are immutable. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="blueprintName, resourceScope, versionId" /> | Delete a published version of a blueprint definition. |

## `SELECT` examples

List published versions of given blueprint definition.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_published_blueprints', value: 'view', },
        { label: 'published_blueprints', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
blueprintName,
blueprint_name,
change_notes,
parameters,
resourceScope,
resource_groups,
status,
target_scope,
type,
versionId
FROM azure.blueprints.vw_published_blueprints
WHERE blueprintName = '{{ blueprintName }}'
AND resourceScope = '{{ resourceScope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.blueprints.published_blueprints
WHERE blueprintName = '{{ blueprintName }}'
AND resourceScope = '{{ resourceScope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>published_blueprints</code> resource.

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
INSERT INTO azure.blueprints.published_blueprints (
blueprintName,
resourceScope,
versionId,
data__properties,
properties
)
SELECT 
'{{ blueprintName }}',
'{{ resourceScope }}',
'{{ versionId }}',
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
    - name: type
      value: string
    - name: name
      value: string
    - name: properties
      value:
        - name: status
          value:
            - name: timeCreated
              value: string
            - name: lastModified
              value: string
        - name: targetScope
          value: string
        - name: parameters
          value: object
        - name: resourceGroups
          value: object
        - name: blueprintName
          value: string
        - name: changeNotes
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>published_blueprints</code> resource.

```sql
/*+ delete */
DELETE FROM azure.blueprints.published_blueprints
WHERE blueprintName = '{{ blueprintName }}'
AND resourceScope = '{{ resourceScope }}'
AND versionId = '{{ versionId }}';
```
