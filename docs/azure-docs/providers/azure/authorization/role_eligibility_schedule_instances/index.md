---
title: role_eligibility_schedule_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - role_eligibility_schedule_instances
  - authorization
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

Creates, updates, deletes, gets or lists a <code>role_eligibility_schedule_instances</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_eligibility_schedule_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.role_eligibility_schedule_instances" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_eligibility_schedule_instances', value: 'view', },
        { label: 'role_eligibility_schedule_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | The role eligibility schedule instance ID. |
| <CopyableCode code="name" /> | `text` | The role eligibility schedule instance name. |
| <CopyableCode code="condition" /> | `text` | field from the `properties` object |
| <CopyableCode code="condition_version" /> | `text` | field from the `properties` object |
| <CopyableCode code="created_on" /> | `text` | field from the `properties` object |
| <CopyableCode code="end_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="expanded_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="member_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="principal_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="roleEligibilityScheduleInstanceName" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_definition_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="role_eligibility_schedule_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="scope" /> | `text` | field from the `properties` object |
| <CopyableCode code="start_date_time" /> | `text` | field from the `properties` object |
| <CopyableCode code="status" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | The role eligibility schedule instance type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The role eligibility schedule instance ID. |
| <CopyableCode code="name" /> | `string` | The role eligibility schedule instance name. |
| <CopyableCode code="properties" /> | `object` | Role eligibility schedule properties with scope. |
| <CopyableCode code="type" /> | `string` | The role eligibility schedule instance type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="roleEligibilityScheduleInstanceName, scope" /> | Gets the specified role eligibility schedule instance. |
| <CopyableCode code="list_for_scope" /> | `SELECT` | <CopyableCode code="scope" /> | Gets role eligibility schedule instances of a role eligibility schedule. |

## `SELECT` examples

Gets role eligibility schedule instances of a role eligibility schedule.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_role_eligibility_schedule_instances', value: 'view', },
        { label: 'role_eligibility_schedule_instances', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
condition,
condition_version,
created_on,
end_date_time,
expanded_properties,
member_type,
principal_id,
principal_type,
roleEligibilityScheduleInstanceName,
role_definition_id,
role_eligibility_schedule_id,
scope,
start_date_time,
status,
type
FROM azure.authorization.vw_role_eligibility_schedule_instances
WHERE scope = '{{ scope }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
type
FROM azure.authorization.role_eligibility_schedule_instances
WHERE scope = '{{ scope }}';
```
</TabItem></Tabs>

