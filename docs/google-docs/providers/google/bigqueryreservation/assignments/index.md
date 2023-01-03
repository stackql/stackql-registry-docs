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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.bigqueryreservation.assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Name of the resource. E.g.: `projects/myproject/locations/US/reservations/team1-prod/assignments/123`. The assignment_id must only contain lower case alphanumeric characters or dashes and the max length is 64 characters. |
| `state` | `string` | Output only. State of the assignment. |
| `assignee` | `string` | The resource which will use the reservation. E.g. `projects/myproject`, `folders/123`, or `organizations/456`. |
| `jobType` | `string` | Which type of jobs will use the reservation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_reservations_assignments_list` | `SELECT` | `locationsId, projectsId, reservationsId` | Lists assignments. Only explicitly created assignments will be returned. Example: * Organization `organizationA` contains two projects, `project1` and `project2`. * Reservation `res1` exists and was created previously. * CreateAssignment was used previously to define the following associations between entities and reservations: `` and `` In this example, ListAssignments will just return the above two assignments for reservation `res1`, and no expansion/merge will happen. The wildcard "-" can be used for reservations in the request. In that case all assignments belongs to the specified project and location will be listed. **Note** "-" cannot be used for projects nor locations. |
| `projects_locations_reservations_assignments_create` | `INSERT` | `locationsId, projectsId, reservationsId` | Creates an assignment object which allows the given project to submit jobs of a certain type using slots from the specified reservation. Currently a resource (project, folder, organization) can only have one assignment per each (job_type, location) combination, and that reservation will be used for all jobs of the matching type. Different assignments can be created on different levels of the projects, folders or organization hierarchy. During query execution, the assignment is looked up at the project, folder and organization levels in that order. The first assignment found is applied to the query. When creating assignments, it does not matter if other assignments exist at higher levels. Example: * The organization `organizationA` contains two projects, `project1` and `project2`. * Assignments for all three entities (`organizationA`, `project1`, and `project2`) could all be created and mapped to the same or different reservations. "None" assignments represent an absence of the assignment. Projects assigned to None use on-demand pricing. To create a "None" assignment, use "none" as a reservation_id in the parent. Example parent: `projects/myproject/locations/US/reservations/none`. Returns `google.rpc.Code.PERMISSION_DENIED` if user does not have 'bigquery.admin' permissions on the project using the reservation and the project that owns this reservation. Returns `google.rpc.Code.INVALID_ARGUMENT` when location of the assignment does not match location of the reservation. |
| `projects_locations_reservations_assignments_delete` | `DELETE` | `assignmentsId, locationsId, projectsId, reservationsId` | Deletes a assignment. No expansion will happen. Example: * Organization `organizationA` contains two projects, `project1` and `project2`. * Reservation `res1` exists and was created previously. * CreateAssignment was used previously to define the following associations between entities and reservations: `` and `` In this example, deletion of the `` assignment won't affect the other assignment ``. After said deletion, queries from `project1` will still use `res1` while queries from `project2` will switch to use on-demand mode. |
| `projects_locations_reservations_assignments_move` | `EXEC` | `assignmentsId, locationsId, projectsId, reservationsId` | Moves an assignment under a new reservation. This differs from removing an existing assignment and recreating a new one by providing a transactional change that ensures an assignee always has an associated reservation. |
| `projects_locations_reservations_assignments_patch` | `EXEC` | `assignmentsId, locationsId, projectsId, reservationsId` | Updates an existing assignment. Only the `priority` field can be updated. |
