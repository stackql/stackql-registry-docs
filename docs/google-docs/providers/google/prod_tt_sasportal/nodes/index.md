---
title: nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - nodes
  - prod_tt_sasportal
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

Creates, updates, deletes, gets or lists a <code>nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.prod_tt_sasportal.nodes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Resource name. |
| <CopyableCode code="displayName" /> | `string` | The node's display name. |
| <CopyableCode code="sasUserIds" /> | `array` | User ids used by the devices belonging to this node. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="nodes_nodes_list" /> | `SELECT` | <CopyableCode code="nodesId" /> | Lists nodes. |
| <CopyableCode code="nodes_nodes_nodes_list" /> | `SELECT` | <CopyableCode code="nodesId, nodesId1" /> | Lists nodes. |
| <CopyableCode code="nodes_nodes_create" /> | `INSERT` | <CopyableCode code="nodesId" /> | Creates a new node. |
| <CopyableCode code="nodes_nodes_nodes_create" /> | `INSERT` | <CopyableCode code="nodesId, nodesId1" /> | Creates a new node. |
| <CopyableCode code="nodes_nodes_delete" /> | `DELETE` | <CopyableCode code="nodesId, nodesId1" /> | Deletes a node. |
| <CopyableCode code="customers_nodes_patch" /> | `UPDATE` | <CopyableCode code="customersId, nodesId" /> | Updates an existing node. |
| <CopyableCode code="nodes_nodes_patch" /> | `UPDATE` | <CopyableCode code="nodesId, nodesId1" /> | Updates an existing node. |
| <CopyableCode code="customers_nodes_move" /> | `EXEC` | <CopyableCode code="customersId, nodesId" /> | Moves a node under another node or customer. |
| <CopyableCode code="nodes_nodes_move" /> | `EXEC` | <CopyableCode code="nodesId, nodesId1" /> | Moves a node under another node or customer. |

## `SELECT` examples

Lists nodes.

```sql
SELECT
name,
displayName,
sasUserIds
FROM google.prod_tt_sasportal.nodes
WHERE nodesId = '{{ nodesId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>nodes</code> resource.

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
INSERT INTO google.prod_tt_sasportal.nodes (
nodesId,
name,
sasUserIds,
displayName
)
SELECT 
'{{ nodesId }}',
'{{ name }}',
'{{ sasUserIds }}',
'{{ displayName }}'
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

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>nodes</code> resource.

```sql
/*+ update */
UPDATE google.prod_tt_sasportal.nodes
SET 
name = '{{ name }}',
sasUserIds = '{{ sasUserIds }}',
displayName = '{{ displayName }}'
WHERE 
nodesId = '{{ nodesId }}'
AND nodesId1 = '{{ nodesId1 }}';
```

## `DELETE` example

Deletes the specified <code>nodes</code> resource.

```sql
/*+ delete */
DELETE FROM google.prod_tt_sasportal.nodes
WHERE nodesId = '{{ nodesId }}'
AND nodesId1 = '{{ nodesId1 }}';
```
