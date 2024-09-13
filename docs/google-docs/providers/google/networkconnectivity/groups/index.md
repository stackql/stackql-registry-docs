---
title: groups
hide_title: false
hide_table_of_contents: false
keywords:
  - groups
  - networkconnectivity
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

Creates, updates, deletes or gets an <code>group</code> resource or lists <code>groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkconnectivity.groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The name of the group. Group names must be unique. They use the following form: `projects/{project_number}/locations/global/hubs/{hub}/groups/{group_id}` |
| <CopyableCode code="description" /> | `string` | Optional. The description of the group. |
| <CopyableCode code="autoAccept" /> | `object` | The auto-accept setting for a group controls whether proposed spokes are automatically attached to the hub. If auto-accept is enabled, the spoke immediately is attached to the hub and becomes part of the group. In this case, the new spoke is in the ACTIVE state. If auto-accept is disabled, the spoke goes to the INACTIVE state, and it must be reviewed and accepted by a hub administrator. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the group was created. |
| <CopyableCode code="labels" /> | `object` | Optional. Labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |
| <CopyableCode code="routeTable" /> | `string` | Output only. The name of the route table that corresponds to this group. They use the following form: `projects/{project_number}/locations/global/hubs/{hub_id}/routeTables/{route_table_id}` |
| <CopyableCode code="state" /> | `string` | Output only. The current lifecycle state of this group. |
| <CopyableCode code="uid" /> | `string` | Output only. The Google-generated UUID for the group. This value is unique across all group resources. If a group is deleted and another with the same name is created, the new route table is assigned a different unique_id. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time the group was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="groupsId, hubsId, projectsId" /> | Gets details about a Network Connectivity Center group. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="hubsId, projectsId" /> | Lists groups in a given hub. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="groupsId, hubsId, projectsId" /> | Updates the parameters of a Network Connectivity Center group. |

## `SELECT` examples

Lists groups in a given hub.

```sql
SELECT
name,
description,
autoAccept,
createTime,
labels,
routeTable,
state,
uid,
updateTime
FROM google.networkconnectivity.groups
WHERE hubsId = '{{ hubsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `UPDATE` example

Updates a group only if the necessary resources are available.

```sql
UPDATE google.networkconnectivity.groups
SET 
name = '{{ name }}',
createTime = '{{ createTime }}',
updateTime = '{{ updateTime }}',
labels = '{{ labels }}',
description = '{{ description }}',
uid = '{{ uid }}',
state = '{{ state }}',
autoAccept = '{{ autoAccept }}',
routeTable = '{{ routeTable }}'
WHERE 
groupsId = '{{ groupsId }}'
AND hubsId = '{{ hubsId }}'
AND projectsId = '{{ projectsId }}';
```
