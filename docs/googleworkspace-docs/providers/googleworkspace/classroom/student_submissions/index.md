---
title: student_submissions
hide_title: false
hide_table_of_contents: false
keywords:
  - student_submissions
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
<tr><td><b>Name</b></td><td><code>student_submissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.classroom.student_submissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Classroom-assigned Identifier for the student submission. This is unique among submissions for the relevant course work. Read-only. |
| `draftGrade` | `number` | Optional pending grade. If unset, no grade was set. This value must be non-negative. Decimal (that is, non-integer) values are allowed, but are rounded to two decimal places. This is only visible to and modifiable by course teachers. |
| `courseWorkType` | `string` | Type of course work this submission is for. Read-only. |
| `courseId` | `string` | Identifier of the course. Read-only. |
| `multipleChoiceSubmission` | `object` | Student work for a multiple-choice question. |
| `userId` | `string` | Identifier for the student that owns this submission. Read-only. |
| `assignedGrade` | `number` | Optional grade. If unset, no grade was set. This value must be non-negative. Decimal (that is, non-integer) values are allowed, but are rounded to two decimal places. This may be modified only by course teachers. |
| `state` | `string` | State of this submission. Read-only. |
| `courseWorkId` | `string` | Identifier for the course work this corresponds to. Read-only. |
| `creationTime` | `string` | Creation time of this submission. This may be unset if the student has not accessed this item. Read-only. |
| `late` | `boolean` | Whether this submission is late. Read-only. |
| `updateTime` | `string` | Last update time of this submission. This may be unset if the student has not accessed this item. Read-only. |
| `associatedWithDeveloper` | `boolean` | Whether this student submission is associated with the Developer Console project making the request. See CreateCourseWork for more details. Read-only. |
| `alternateLink` | `string` | Absolute link to the submission in the Classroom web UI. Read-only. |
| `submissionHistory` | `array` | The history of the submission (includes state and grade histories). Read-only. |
| `shortAnswerSubmission` | `object` | Student work for a short answer question. |
| `assignmentSubmission` | `object` | Student work for an assignment. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `courses_courseWork_studentSubmissions_get` | `SELECT` | `courseId, courseWorkId, id` | Returns a student submission. * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course, course work, or student submission or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course, course work, or student submission does not exist. |
| `courses_courseWork_studentSubmissions_list` | `SELECT` | `courseId, courseWorkId` | Returns a list of student submissions that the requester is permitted to view, factoring in the OAuth scopes of the request. `-` may be specified as the `course_work_id` to include student submissions for multiple course work items. Course students may only view their own work. Course teachers and domain administrators may view all student submissions. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course or course work, or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course does not exist. |
| `courses_courseWork_studentSubmissions_modifyAttachments` | `EXEC` | `courseId, courseWorkId, id` | Modifies attachments of student submission. Attachments may only be added to student submissions belonging to course work objects with a `workType` of `ASSIGNMENT`. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work item. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course or course work, if the user is not permitted to modify attachments on the requested student submission, or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course, course work, or student submission does not exist. |
| `courses_courseWork_studentSubmissions_patch` | `EXEC` | `courseId, courseWorkId, id` | Updates one or more fields of a student submission. See google.classroom.v1.StudentSubmission for details of which fields may be updated and who may change them. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work item. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting developer project did not create the corresponding course work, if the user is not permitted to make the requested modification to the student submission, or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course, course work, or student submission does not exist. |
| `courses_courseWork_studentSubmissions_reclaim` | `EXEC` | `courseId, courseWorkId, id` | Reclaims a student submission on behalf of the student that owns it. Reclaiming a student submission transfers ownership of attached Drive files to the student and updates the submission state. Only the student that owns the requested student submission may call this method, and only for a student submission that has been turned in. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work item. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course or course work, unsubmit the requested student submission, or for access errors. * `FAILED_PRECONDITION` if the student submission has not been turned in. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course, course work, or student submission does not exist. |
| `courses_courseWork_studentSubmissions_return` | `EXEC` | `courseId, courseWorkId, id` | Returns a student submission. Returning a student submission transfers ownership of attached Drive files to the student and may also update the submission state. Unlike the Classroom application, returning a student submission does not set assignedGrade to the draftGrade value. Only a teacher of the course that contains the requested student submission may call this method. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work item. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course or course work, return the requested student submission, or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course, course work, or student submission does not exist. |
| `courses_courseWork_studentSubmissions_turnIn` | `EXEC` | `courseId, courseWorkId, id` | Turns in a student submission. Turning in a student submission transfers ownership of attached Drive files to the teacher and may also update the submission state. This may only be called by the student that owns the specified student submission. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding course work item. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course or course work, turn in the requested student submission, or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course, course work, or student submission does not exist. |
