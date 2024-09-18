---
title: customer_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - customer_nodes
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

Creates, updates, deletes, gets or lists a <code>customer_nodes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customer_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.prod_tt_sasportal.customer_nodes" /></td></tr>
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
| <CopyableCode code="customers_nodes_list" /> | `SELECT` | <CopyableCode code="customersId" /> | Lists nodes. |
| <CopyableCode code="customers_nodes_nodes_list" /> | `SELECT` | <CopyableCode code="customersId, nodesId" /> | Lists nodes. |
| <CopyableCode code="customers_nodes_create" /> | `INSERT` | <CopyableCode code="customersId" /> | Creates a new node. |
| <CopyableCode code="customers_nodes_nodes_create" /> | `INSERT` | <CopyableCode code="customersId, nodesId" /> | Creates a new node. |
| <CopyableCode code="customers_nodes_delete" /> | `DELETE` | <CopyableCode code="customersId, nodesId" /> | Deletes a node. |

## `SELECT` examples

Lists nodes.

```sql
SELECT
name,
displayName,
sasUserIds
FROM google.prod_tt_sasportal.customer_nodes
WHERE customersId = '{{ customersId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>customer_nodes</code> resource.

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
INSERT INTO google.prod_tt_sasportal.customer_nodes (
customersId,
name,
sasUserIds,
displayName
)
SELECT 
'{{ customersId }}',
'{{ name }}',
'{{ sasUserIds }}',
'{{ displayName }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
sasUserIds:
  - type: string
displayName: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>customer_nodes</code> resource.

```sql
/*+ delete */
DELETE FROM google.prod_tt_sasportal.customer_nodes
WHERE customersId = '{{ customersId }}'
AND nodesId = '{{ nodesId }}';
```
