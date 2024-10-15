---
title: workspace_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_settings
  - security
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

Creates, updates, deletes, gets or lists a <code>workspace_settings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.security.workspace_settings" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_settings', value: 'view', },
        { label: 'workspace_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource Id |
| <CopyableCode code="name" /> | `text` | Resource name |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type |
| <CopyableCode code="workspaceSettingName" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspace_id" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id |
| <CopyableCode code="name" /> | `string` | Resource name |
| <CopyableCode code="properties" /> | `object` | Workspace setting data |
| <CopyableCode code="type" /> | `string` | Resource type |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="subscriptionId, workspaceSettingName" /> | Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="subscriptionId, workspaceSettingName" /> | creating settings about where we should store your security data and logs |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="subscriptionId, workspaceSettingName" /> | Deletes the custom workspace settings for this subscription. new VMs will report to the default workspace |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="subscriptionId, workspaceSettingName" /> | Settings about where we should store your security data and logs |

## `SELECT` examples

Settings about where we should store your security data and logs. If the result is empty, it means that no custom-workspace configuration was set

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_workspace_settings', value: 'view', },
        { label: 'workspace_settings', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
scope,
subscriptionId,
type,
workspaceSettingName,
workspace_id
FROM azure.security.vw_workspace_settings
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.security.workspace_settings
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>workspace_settings</code> resource.

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
INSERT INTO azure.security.workspace_settings (
subscriptionId,
workspaceSettingName,
properties
)
SELECT 
'{{ subscriptionId }}',
'{{ workspaceSettingName }}',
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
        - name: workspaceId
          value: string
        - name: scope
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>workspace_settings</code> resource.

```sql
/*+ update */
UPDATE azure.security.workspace_settings
SET 
properties = '{{ properties }}'
WHERE 
subscriptionId = '{{ subscriptionId }}'
AND workspaceSettingName = '{{ workspaceSettingName }}';
```

## `DELETE` example

Deletes the specified <code>workspace_settings</code> resource.

```sql
/*+ delete */
DELETE FROM azure.security.workspace_settings
WHERE subscriptionId = '{{ subscriptionId }}'
AND workspaceSettingName = '{{ workspaceSettingName }}';
```
