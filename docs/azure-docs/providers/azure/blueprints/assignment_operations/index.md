---
title: assignment_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - assignment_operations
  - blueprints
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

Creates, updates, deletes, gets or lists a <code>assignment_operations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignment_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.blueprints.assignment_operations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assignment_operations', value: 'view', },
        { label: 'assignment_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | String Id used to locate any resource on Azure. |
| <CopyableCode code="name" /> | `text` | Name of this resource. |
| <CopyableCode code="assignmentName" /> | `text` | field from the `properties` object |
| <CopyableCode code="assignmentOperationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="assignment_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="blueprint_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="deployments" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceScope" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_created" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_finished" /> | `text` | field from the `properties` object |
| <CopyableCode code="time_started" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Type of this resource. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | String Id used to locate any resource on Azure. |
| <CopyableCode code="name" /> | `string` | Name of this resource. |
| <CopyableCode code="properties" /> | `object` | Properties of AssignmentOperation. |
| <CopyableCode code="type" /> | `string` | Type of this resource. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="assignmentName, assignmentOperationName, resourceScope" /> | Get a blueprint assignment operation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="assignmentName, resourceScope" /> | List operations for given blueprint assignment within a subscription or a management group. |

## `SELECT` examples

List operations for given blueprint assignment within a subscription or a management group.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_assignment_operations', value: 'view', },
        { label: 'assignment_operations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
assignmentName,
assignmentOperationName,
assignment_state,
blueprint_version,
deployments,
resourceScope,
time_created,
time_finished,
time_started,
type
FROM azure.blueprints.vw_assignment_operations
WHERE assignmentName = '{{ assignmentName }}'
AND resourceScope = '{{ resourceScope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.blueprints.assignment_operations
WHERE assignmentName = '{{ assignmentName }}'
AND resourceScope = '{{ resourceScope }}';
```
</TabItem></Tabs>

