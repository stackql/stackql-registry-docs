---
title: route_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - route_tables
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

Creates, updates, deletes, gets or lists a <code>route_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>route_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.networkconnectivity.route_tables" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The name of the route table. Route table names must be unique. They use the following form: `projects/{project_number}/locations/global/hubs/{hub}/routeTables/{route_table_id}` |
| <CopyableCode code="description" /> | `string` | An optional description of the route table. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time the route table was created. |
| <CopyableCode code="labels" /> | `object` | Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements). |
| <CopyableCode code="state" /> | `string` | Output only. The current lifecycle state of this route table. |
| <CopyableCode code="uid" /> | `string` | Output only. The Google-generated UUID for the route table. This value is unique across all route table resources. If a route table is deleted and another with the same name is created, the new route table is assigned a different `uid`. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The time the route table was last updated. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="hubsId, projectsId, routeTablesId" /> | Gets details about a Network Connectivity Center route table. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="hubsId, projectsId" /> | Lists route tables in a given hub. |

## `SELECT` examples

Lists route tables in a given hub.

```sql
SELECT
name,
description,
createTime,
labels,
state,
uid,
updateTime
FROM google.networkconnectivity.route_tables
WHERE hubsId = '{{ hubsId }}'
AND projectsId = '{{ projectsId }}';
```
