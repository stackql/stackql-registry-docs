---
title: course_work_materials
hide_title: false
hide_table_of_contents: false
keywords:
  - course_work_materials
  - classroom
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>course_work_materials</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.classroom.course_work_materials</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Classroom-assigned identifier of this course work material, unique per course. Read-only. |
| `description` | `string` | Optional description of this course work material. The text must be a valid UTF-8 string containing no more than 30,000 characters. |
| `creatorUserId` | `string` | Identifier for the user that created the course work material. Read-only. |
| `individualStudentsOptions` | `object` | Assignee details about a coursework/announcement. This field is set if and only if `assigneeMode` is `INDIVIDUAL_STUDENTS`. |
| `topicId` | `string` | Identifier for the topic that this course work material is associated with. Must match an existing topic in the course. |
| `materials` | `array` | Additional materials. A course work material must have no more than 20 material items. |
| `updateTime` | `string` | Timestamp of the most recent change to this course work material. Read-only. |
| `assigneeMode` | `string` | Assignee mode of the course work material. If unspecified, the default value is `ALL_STUDENTS`. |
| `scheduledTime` | `string` | Optional timestamp when this course work material is scheduled to be published. |
| `title` | `string` | Title of this course work material. The title must be a valid UTF-8 string containing between 1 and 3000 characters. |
| `courseId` | `string` | Identifier of the course. Read-only. |
| `alternateLink` | `string` | Absolute link to this course work material in the Classroom web UI. This is only populated if `state` is `PUBLISHED`. Read-only. |
| `state` | `string` | Status of this course work material. If unspecified, the default state is `DRAFT`. |
| `creationTime` | `string` | Timestamp when this course work material was created. Read-only. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `courses_courseWorkMaterials_get` | `SELECT` | `courseId, id` | Returns a course work material. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course or course work material, or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course or course work material does not exist. |
| `courses_courseWorkMaterials_list` | `SELECT` | `courseId` | Returns a list of course work material that the requester is permitted to view. Course students may only view `PUBLISHED` course work material. Course teachers and domain administrators may view all course work material. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course does not exist. |
| `courses_courseWorkMaterials_create` | `INSERT` | `courseId` | Creates a course work material. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course, create course work material in the requested course, share a Drive attachment, or for access errors. * `INVALID_ARGUMENT` if the request is malformed or if more than 20 * materials are provided. * `NOT_FOUND` if the requested course does not exist. * `FAILED_PRECONDITION` for the following request error: * AttachmentNotVisible |
| `courses_courseWorkMaterials_delete` | `DELETE` | `courseId, id` | Deletes a course work material. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work material item. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting developer project did not create the corresponding course work material, if the requesting user is not permitted to delete the requested course or for access errors. * `FAILED_PRECONDITION` if the requested course work material has already been deleted. * `NOT_FOUND` if no course exists with the requested ID. |
| `courses_courseWorkMaterials_patch` | `EXEC` | `courseId, id` | Updates one or more fields of a course work material. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting developer project for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `FAILED_PRECONDITION` if the requested course work material has already been deleted. * `NOT_FOUND` if the requested course or course work material does not exist |
