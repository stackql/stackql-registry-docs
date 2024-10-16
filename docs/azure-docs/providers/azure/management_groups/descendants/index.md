---
title: descendants
hide_title: false
hide_table_of_contents: false
keywords:
  - descendants
  - management_groups
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

Creates, updates, deletes, gets or lists a <code>descendants</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>descendants</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.management_groups.descendants" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The fully qualified ID for the descendant.  For example, /providers/Microsoft.Management/managementGroups/0000000-0000-0000-0000-000000000000 or /subscriptions/0000000-0000-0000-0000-000000000000 |
| <CopyableCode code="name" /> | `string` | The name of the descendant. For example, 00000000-0000-0000-0000-000000000000 |
| <CopyableCode code="properties" /> | `object` | The generic properties of an descendant. |
| <CopyableCode code="type" /> | `string` | The type of the resource. For example, Microsoft.Management/managementGroups or /subscriptions |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupId" /> | List all entities that descend from a management group. |

## `SELECT` examples

List all entities that descend from a management group.


```sql
SELECT
id,
name,
properties,
type
FROM azure.management_groups.descendants
WHERE groupId = '{{ groupId }}';
```