---
title: scope_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_assignments
  - managed_network
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

Creates, updates, deletes, gets or lists a <code>scope_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>scope_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network.scope_assignments" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scope_assignments', value: 'view', },
        { label: 'scope_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="assigned_managed_network" /> | `text` | field from the `properties` object |
| <CopyableCode code="etag" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="scopeAssignmentName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Properties of Managed Network |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="scope, scopeAssignmentName" /> | Get the specified scope assignment. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="scope" /> | Get the specified scope assignment. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="scope, scopeAssignmentName" /> | Creates a scope assignment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="scope, scopeAssignmentName" /> | Deletes a scope assignment. |

## `SELECT` examples

Get the specified scope assignment.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_scope_assignments', value: 'view', },
        { label: 'scope_assignments', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
assigned_managed_network,
etag,
provisioning_state,
scope,
scopeAssignmentName
FROM azure.managed_network.vw_scope_assignments
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.managed_network.scope_assignments
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>scope_assignments</code> resource.

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
INSERT INTO azure.managed_network.scope_assignments (
scope,
scopeAssignmentName,
properties
)
SELECT 
'{{ scope }}',
'{{ scopeAssignmentName }}',
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
        - name: assignedManagedNetwork
          value: string
        - name: provisioningState
          value: string
        - name: etag
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>scope_assignments</code> resource.

```sql
/*+ delete */
DELETE FROM azure.managed_network.scope_assignments
WHERE scope = '{{ scope }}'
AND scopeAssignmentName = '{{ scopeAssignmentName }}';
```
