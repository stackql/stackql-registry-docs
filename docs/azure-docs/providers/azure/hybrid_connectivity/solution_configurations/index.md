---
title: solution_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - solution_configurations
  - hybrid_connectivity
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

Creates, updates, deletes, gets or lists a <code>solution_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>solution_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_connectivity.solution_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_solution_configurations', value: 'view', },
        { label: 'solution_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="last_sync_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceUri" /> | `text` | field from the `properties` object |
| <CopyableCode code="solutionConfiguration" /> | `text` | field from the `properties` object |
| <CopyableCode code="solution_settings" /> | `text` | field from the `properties` object |
| <CopyableCode code="solution_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="status_details" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Solution configuration resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceUri, solutionConfiguration" /> | Get a SolutionConfiguration |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceUri" /> | List SolutionConfiguration resources by parent |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="resourceUri, solutionConfiguration" /> | Create a SolutionConfiguration |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="resourceUri, solutionConfiguration" /> | Delete a SolutionConfiguration |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="resourceUri, solutionConfiguration" /> | Update a SolutionConfiguration |
| <CopyableCode code="sync_now" /> | `EXEC` | <CopyableCode code="resourceUri, solutionConfiguration" /> | Trigger immediate sync with source cloud |

## `SELECT` examples

List SolutionConfiguration resources by parent

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_solution_configurations', value: 'view', },
        { label: 'solution_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
last_sync_time,
provisioning_state,
resourceUri,
solutionConfiguration,
solution_settings,
solution_type,
status,
status_details
FROM azure.hybrid_connectivity.vw_solution_configurations
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
properties
FROM azure.hybrid_connectivity.solution_configurations
WHERE resourceUri = '{{ resourceUri }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>solution_configurations</code> resource.

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
INSERT INTO azure.hybrid_connectivity.solution_configurations (
resourceUri,
solutionConfiguration,
properties
)
SELECT 
'{{ resourceUri }}',
'{{ solutionConfiguration }}',
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
        - name: provisioningState
          value: []
        - name: solutionType
          value: string
        - name: solutionSettings
          value: []
        - name: status
          value: []
        - name: statusDetails
          value: string
        - name: lastSyncTime
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>solution_configurations</code> resource.

```sql
/*+ update */
UPDATE azure.hybrid_connectivity.solution_configurations
SET 
properties = '{{ properties }}'
WHERE 
resourceUri = '{{ resourceUri }}'
AND solutionConfiguration = '{{ solutionConfiguration }}';
```

## `DELETE` example

Deletes the specified <code>solution_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.hybrid_connectivity.solution_configurations
WHERE resourceUri = '{{ resourceUri }}'
AND solutionConfiguration = '{{ solutionConfiguration }}';
```
