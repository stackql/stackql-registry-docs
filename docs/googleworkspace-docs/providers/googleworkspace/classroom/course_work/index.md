---
title: course_work
hide_title: false
hide_table_of_contents: false
keywords:
  - course_work
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
<tr><td><b>Name</b></td><td><code>course_work</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.classroom.course_work</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Classroom-assigned identifier of this course work, unique per course. Read-only. |
| `description` | `string` | Optional description of this course work. If set, the description must be a valid UTF-8 string containing no more than 30,000 characters. |
| `materials` | `array` | Additional materials. CourseWork must have no more than 20 material items. |
| `associatedWithDeveloper` | `boolean` | Whether this course work item is associated with the Developer Console project making the request. See CreateCourseWork for more details. Read-only. |
| `dueDate` | `object` | Represents a whole or partial calendar date, such as a birthday. The time of day and time zone are either specified elsewhere or are insignificant. The date is relative to the Gregorian Calendar. This can represent one of the following: * A full date, with non-zero year, month, and day values. * A month and day, with a zero year (for example, an anniversary). * A year on its own, with a zero month and a zero day. * A year and month, with a zero day (for example, a credit card expiration date). Related types: * google.type.TimeOfDay * google.type.DateTime * google.protobuf.Timestamp |
| `gradeCategory` | `object` | Details for a grade category in a course. Coursework may have zero or one grade category, and the category may be used in computing the overall grade. See the [help center article](https://support.google.com/edu/classroom/answer/9184995) for details. |
| `state` | `string` | Status of this course work. If unspecified, the default state is `DRAFT`. |
| `dueTime` | `object` | Represents a time of day. The date and time zone are either not significant or are specified elsewhere. An API may choose to allow leap seconds. Related types are google.type.Date and `google.protobuf.Timestamp`. |
| `title` | `string` | Title of this course work. The title must be a valid UTF-8 string containing between 1 and 3000 characters. |
| `multipleChoiceQuestion` | `object` | Additional details for multiple-choice questions. |
| `assigneeMode` | `string` | Assignee mode of the coursework. If unspecified, the default value is `ALL_STUDENTS`. |
| `creatorUserId` | `string` | Identifier for the user that created the coursework. Read-only. |
| `updateTime` | `string` | Timestamp of the most recent change to this course work. Read-only. |
| `courseId` | `string` | Identifier of the course. Read-only. |
| `assignment` | `object` | Additional details for assignments. |
| `individualStudentsOptions` | `object` | Assignee details about a coursework/announcement. This field is set if and only if `assigneeMode` is `INDIVIDUAL_STUDENTS`. |
| `creationTime` | `string` | Timestamp when this course work was created. Read-only. |
| `topicId` | `string` | Identifier for the topic that this coursework is associated with. Must match an existing topic in the course. |
| `submissionModificationMode` | `string` | Setting to determine when students are allowed to modify submissions. If unspecified, the default value is `MODIFIABLE_UNTIL_TURNED_IN`. |
| `maxPoints` | `number` | Maximum grade for this course work. If zero or unspecified, this assignment is considered ungraded. This must be a non-negative integer value. |
| `workType` | `string` | Type of this course work. The type is set when the course work is created and cannot be changed. |
| `alternateLink` | `string` | Absolute link to this course work in the Classroom web UI. This is only populated if `state` is `PUBLISHED`. Read-only. |
| `scheduledTime` | `string` | Optional timestamp when this course work is scheduled to be published. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `courses_courseWork_get` | `SELECT` | `courseId, id` | Returns course work. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course or course work, or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course or course work does not exist. |
| `courses_courseWork_list` | `SELECT` | `courseId` | Returns a list of course work that the requester is permitted to view. Course students may only view `PUBLISHED` course work. Course teachers and domain administrators may view all course work. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course does not exist. |
| `courses_courseWork_create` | `INSERT` | `courseId` | Creates course work. The resulting course work (and corresponding student submissions) are associated with the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to make the request. Classroom API requests to modify course work and student submissions must be made with an OAuth client ID from the associated Developer Console project. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course, create course work in the requested course, share a Drive attachment, or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course does not exist. * `FAILED_PRECONDITION` for the following request error: * AttachmentNotVisible |
| `courses_courseWork_delete` | `DELETE` | `courseId, id` | Deletes a course work. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work item. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting developer project did not create the corresponding course work, if the requesting user is not permitted to delete the requested course or for access errors. * `FAILED_PRECONDITION` if the requested course work has already been deleted. * `NOT_FOUND` if no course exists with the requested ID. |
| `courses_courseWork_modifyAssignees` | `EXEC` | `courseId, id` | Modifies assignee mode and options of a coursework. Only a teacher of the course that contains the coursework may call this method. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course or course work or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course or course work does not exist. |
| `courses_courseWork_patch` | `EXEC` | `courseId, id` | Updates one or more fields of a course work. See google.classroom.v1.CourseWork for details of which fields may be updated and who may change them. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work item. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting developer project did not create the corresponding course work, if the user is not permitted to make the requested modification to the student submission, or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `FAILED_PRECONDITION` if the requested course work has already been deleted. * `NOT_FOUND` if the requested course, course work, or student submission does not exist. |
