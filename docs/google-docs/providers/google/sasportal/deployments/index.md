
---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - sasportal
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

Creates, updates, deletes or gets an <code>deployment</code> resource or lists <code>deployments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.sasportal.deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name. |
| <CopyableCode code="displayName" /> | `string` | The deployment's display name. |
| <CopyableCode code="frns" /> | `array` | Output only. The FCC Registration Numbers (FRNs) copied from its direct parent. |
| <CopyableCode code="sasUserIds" /> | `array` | User ID used by the devices belonging to this deployment. Each deployment should be associated with one unique user ID. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="customers_deployments_get" /> | `SELECT` | <CopyableCode code="customersId, deploymentsId" /> | Returns a requested deployment. |
| <CopyableCode code="customers_deployments_list" /> | `SELECT` | <CopyableCode code="customersId" /> | Lists deployments. |
| <CopyableCode code="customers_nodes_deployments_list" /> | `SELECT` | <CopyableCode code="customersId, nodesId" /> | Lists deployments. |
| <CopyableCode code="deployments_get" /> | `SELECT` | <CopyableCode code="deploymentsId" /> | Returns a requested deployment. |
| <CopyableCode code="nodes_deployments_get" /> | `SELECT` | <CopyableCode code="deploymentsId, nodesId" /> | Returns a requested deployment. |
| <CopyableCode code="nodes_deployments_list" /> | `SELECT` | <CopyableCode code="nodesId" /> | Lists deployments. |
| <CopyableCode code="nodes_nodes_deployments_list" /> | `SELECT` | <CopyableCode code="nodesId, nodesId1" /> | Lists deployments. |
| <CopyableCode code="customers_deployments_create" /> | `INSERT` | <CopyableCode code="customersId" /> | Creates a new deployment. |
| <CopyableCode code="customers_nodes_deployments_create" /> | `INSERT` | <CopyableCode code="customersId, nodesId" /> | Creates a new deployment. |
| <CopyableCode code="nodes_nodes_deployments_create" /> | `INSERT` | <CopyableCode code="nodesId, nodesId1" /> | Creates a new deployment. |
| <CopyableCode code="customers_deployments_delete" /> | `DELETE` | <CopyableCode code="customersId, deploymentsId" /> | Deletes a deployment. |
| <CopyableCode code="nodes_deployments_delete" /> | `DELETE` | <CopyableCode code="deploymentsId, nodesId" /> | Deletes a deployment. |
| <CopyableCode code="customers_deployments_patch" /> | `UPDATE` | <CopyableCode code="customersId, deploymentsId" /> | Updates an existing deployment. |
| <CopyableCode code="nodes_deployments_patch" /> | `UPDATE` | <CopyableCode code="deploymentsId, nodesId" /> | Updates an existing deployment. |
| <CopyableCode code="customers_deployments_move" /> | `EXEC` | <CopyableCode code="customersId, deploymentsId" /> | Moves a deployment under another node or customer. |
| <CopyableCode code="nodes_deployments_move" /> | `EXEC` | <CopyableCode code="deploymentsId, nodesId" /> | Moves a deployment under another node or customer. |

## `SELECT` examples

Lists deployments.

```sql
SELECT
name,
displayName,
frns,
sasUserIds
FROM google.sasportal.deployments
WHERE nodesId = '{{ nodesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployments</code> resource.

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
INSERT INTO google.sasportal.deployments (
customersId,
name,
sasUserIds,
displayName,
frns
)
SELECT 
'{{ customersId }}',
'{{ name }}',
'{{ sasUserIds }}',
'{{ displayName }}',
'{{ frns }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: sasUserIds
        value: '{{ sasUserIds }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: frns
        value: '{{ frns }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a deployment only if the necessary resources are available.

```sql
UPDATE google.sasportal.deployments
SET 
name = '{{ name }}',
sasUserIds = '{{ sasUserIds }}',
displayName = '{{ displayName }}',
frns = '{{ frns }}'
WHERE 
deploymentsId = '{{ deploymentsId }}'
AND nodesId = '{{ nodesId }}';
```

## `DELETE` example

Deletes the specified deployment resource.

```sql
DELETE FROM google.sasportal.deployments
WHERE deploymentsId = '{{ deploymentsId }}'
AND nodesId = '{{ nodesId }}';
```
