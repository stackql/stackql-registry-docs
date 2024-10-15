---
title: labels
hide_title: false
hide_table_of_contents: false
keywords:
  - labels
  - defender
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

Creates, updates, deletes, gets or lists a <code>labels</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>labels</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.defender.labels" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_labels', value: 'view', },
        { label: 'labels', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="color" /> | `text` | field from the `properties` object |
| <CopyableCode code="display_name" /> | `text` | field from the `properties` object |
| <CopyableCode code="labelName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="workspaceName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Label properties. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_by_workspace" /> | `SELECT` | <CopyableCode code="labelName, resourceGroupName, subscriptionId, workspaceName" /> | Returns a label in the given workspace. |
| <CopyableCode code="list_by_workspace" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, workspaceName" /> | Returns a list of labels in the given workspace. |
| <CopyableCode code="create_and_update" /> | `INSERT` | <CopyableCode code="labelName, resourceGroupName, subscriptionId, workspaceName" /> | Create or update a Label. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="labelName, resourceGroupName, subscriptionId, workspaceName" /> | Delete a Label. |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="labelName, resourceGroupName, subscriptionId, workspaceName" /> | Update a Label. |

## `SELECT` examples

Returns a list of labels in the given workspace.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_labels', value: 'view', },
        { label: 'labels', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
color,
display_name,
labelName,
provisioning_state,
resourceGroupName,
subscriptionId,
workspaceName
FROM azure.defender.vw_labels
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.defender.labels
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>labels</code> resource.

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
INSERT INTO azure.defender.labels (
labelName,
resourceGroupName,
subscriptionId,
workspaceName,
properties
)
SELECT 
'{{ labelName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ workspaceName }}',
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
        - name: displayName
          value: string
        - name: color
          value: string
        - name: provisioningState
          value: []

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>labels</code> resource.

```sql
/*+ update */
UPDATE azure.defender.labels
SET 
properties = '{{ properties }}'
WHERE 
labelName = '{{ labelName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```

## `DELETE` example

Deletes the specified <code>labels</code> resource.

```sql
/*+ delete */
DELETE FROM azure.defender.labels
WHERE labelName = '{{ labelName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND workspaceName = '{{ workspaceName }}';
```
