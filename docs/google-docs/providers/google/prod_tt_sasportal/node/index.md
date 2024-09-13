---
title: node
hide_title: false
hide_table_of_contents: false
keywords:
  - node
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

Creates, updates, deletes or gets an <code>node</code> resource or lists <code>node</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>node</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.prod_tt_sasportal.node" /></td></tr>
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
| <CopyableCode code="nodes_get" /> | `SELECT` | <CopyableCode code="nodesId" /> | Returns a requested node. |
| <CopyableCode code="nodes_nodes_get" /> | `SELECT` | <CopyableCode code="nodesId, nodesId1" /> | Returns a requested node. |

## `SELECT` examples

Returns a requested node.

```sql
SELECT
name,
displayName,
sasUserIds
FROM google.prod_tt_sasportal.node
WHERE nodesId = '{{ nodesId }}'; 
```
