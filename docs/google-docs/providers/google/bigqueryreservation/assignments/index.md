---
title: assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - assignments
  - bigqueryreservation
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

Creates, updates, deletes, gets or lists a <code>assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.bigqueryreservation.assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Output only. Name of the resource. E.g.: `projects/myproject/locations/US/reservations/team1-prod/assignments/123`. The assignment_id must only contain lower case alphanumeric characters or dashes and the max length is 64 characters. |
| <CopyableCode code="assignee" /> | `string` | The resource which will use the reservation. E.g. `projects/myproject`, `folders/123`, or `organizations/456`. |
| <CopyableCode code="jobType" /> | `string` | Which type of jobs will use the reservation. |
| <CopyableCode code="state" /> | `string` | Output only. State of the assignment. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId, reservationsId" /> | Lists assignments. Only explicitly created assignments will be returned. Example: * Organization `organizationA` contains two projects, `project1` and `project2`. * Reservation `res1` exists and was created previously. * CreateAssignment was used previously to define the following associations between entities and reservations: `` and `` In this example, ListAssignments will just return the above two assignments for reservation `res1`, and no expansion/merge will happen. The wildcard "-" can be used for reservations in the request. In that case all assignments belongs to the specified project and location will be listed. **Note** "-" cannot be used for projects nor locations. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId, reservationsId" /> | Creates an assignment object which allows the given project to submit jobs of a certain type using slots from the specified reservation. Currently a resource (project, folder, organization) can only have one assignment per each (job_type, location) combination, and that reservation will be used for all jobs of the matching type. Different assignments can be created on different levels of the projects, folders or organization hierarchy. During query execution, the assignment is looked up at the project, folder and organization levels in that order. The first assignment found is applied to the query. When creating assignments, it does not matter if other assignments exist at higher levels. Example: * The organization `organizationA` contains two projects, `project1` and `project2`. * Assignments for all three entities (`organizationA`, `project1`, and `project2`) could all be created and mapped to the same or different reservations. "None" assignments represent an absence of the assignment. Projects assigned to None use on-demand pricing. To create a "None" assignment, use "none" as a reservation_id in the parent. Example parent: `projects/myproject/locations/US/reservations/none`. Returns `google.rpc.Code.PERMISSION_DENIED` if user does not have 'bigquery.admin' permissions on the project using the reservation and the project that owns this reservation. Returns `google.rpc.Code.INVALID_ARGUMENT` when location of the assignment does not match location of the reservation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="assignmentsId, locationsId, projectsId, reservationsId" /> | Deletes a assignment. No expansion will happen. Example: * Organization `organizationA` contains two projects, `project1` and `project2`. * Reservation `res1` exists and was created previously. * CreateAssignment was used previously to define the following associations between entities and reservations: `` and `` In this example, deletion of the `` assignment won't affect the other assignment ``. After said deletion, queries from `project1` will still use `res1` while queries from `project2` will switch to use on-demand mode. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="assignmentsId, locationsId, projectsId, reservationsId" /> | Updates an existing assignment. Only the `priority` field can be updated. |
| <CopyableCode code="move" /> | `EXEC` | <CopyableCode code="assignmentsId, locationsId, projectsId, reservationsId" /> | Moves an assignment under a new reservation. This differs from removing an existing assignment and recreating a new one by providing a transactional change that ensures an assignee always has an associated reservation. |

## `SELECT` examples

Lists assignments. Only explicitly created assignments will be returned. Example: * Organization `organizationA` contains two projects, `project1` and `project2`. * Reservation `res1` exists and was created previously. * CreateAssignment was used previously to define the following associations between entities and reservations: `` and `` In this example, ListAssignments will just return the above two assignments for reservation `res1`, and no expansion/merge will happen. The wildcard "-" can be used for reservations in the request. In that case all assignments belongs to the specified project and location will be listed. **Note** "-" cannot be used for projects nor locations.

```sql
SELECT
name,
assignee,
jobType,
state
FROM google.bigqueryreservation.assignments
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND reservationsId = '{{ reservationsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>assignments</code> resource.

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
INSERT INTO google.bigqueryreservation.assignments (
locationsId,
projectsId,
reservationsId,
assignee,
jobType
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ reservationsId }}',
'{{ assignee }}',
'{{ jobType }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: assignee
      value: string
    - name: jobType
      value: string
    - name: state
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>assignments</code> resource.

```sql
/*+ update */
UPDATE google.bigqueryreservation.assignments
SET 
assignee = '{{ assignee }}',
jobType = '{{ jobType }}'
WHERE 
assignmentsId = '{{ assignmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND reservationsId = '{{ reservationsId }}';
```

## `DELETE` example

Deletes the specified <code>assignments</code> resource.

```sql
/*+ delete */
DELETE FROM google.bigqueryreservation.assignments
WHERE assignmentsId = '{{ assignmentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND reservationsId = '{{ reservationsId }}';
```
