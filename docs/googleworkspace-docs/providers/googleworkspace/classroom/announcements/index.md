---
title: announcements
hide_title: false
hide_table_of_contents: false
keywords:
  - announcements
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
<tr><td><b>Name</b></td><td><code>announcements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.classroom.announcements</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Classroom-assigned identifier of this announcement, unique per course. Read-only. |
| `updateTime` | `string` | Timestamp of the most recent change to this announcement. Read-only. |
| `assigneeMode` | `string` | Assignee mode of the announcement. If unspecified, the default value is `ALL_STUDENTS`. |
| `materials` | `array` | Additional materials. Announcements must have no more than 20 material items. |
| `state` | `string` | Status of this announcement. If unspecified, the default state is `DRAFT`. |
| `text` | `string` | Description of this announcement. The text must be a valid UTF-8 string containing no more than 30,000 characters. |
| `courseId` | `string` | Identifier of the course. Read-only. |
| `individualStudentsOptions` | `object` | Assignee details about a coursework/announcement. This field is set if and only if `assigneeMode` is `INDIVIDUAL_STUDENTS`. |
| `scheduledTime` | `string` | Optional timestamp when this announcement is scheduled to be published. |
| `alternateLink` | `string` | Absolute link to this announcement in the Classroom web UI. This is only populated if `state` is `PUBLISHED`. Read-only. |
| `creationTime` | `string` | Timestamp when this announcement was created. Read-only. |
| `creatorUserId` | `string` | Identifier for the user that created the announcement. Read-only. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `courses_announcements_get` | `SELECT` | `courseId, id` | Returns an announcement. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course or announcement, or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course or announcement does not exist. |
| `courses_announcements_list` | `SELECT` | `courseId` | Returns a list of announcements that the requester is permitted to view. Course students may only view `PUBLISHED` announcements. Course teachers and domain administrators may view all announcements. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course does not exist. |
| `courses_announcements_create` | `INSERT` | `courseId` | Creates an announcement. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course, create announcements in the requested course, share a Drive attachment, or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course does not exist. * `FAILED_PRECONDITION` for the following request error: * AttachmentNotVisible |
| `courses_announcements_delete` | `DELETE` | `courseId, id` | Deletes an announcement. This request must be made by the Developer Console project of the [OAuth client ID](https://support.google.com/cloud/answer/6158849) used to create the corresponding announcement item. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting developer project did not create the corresponding announcement, if the requesting user is not permitted to delete the requested course or for access errors. * `FAILED_PRECONDITION` if the requested announcement has already been deleted. * `NOT_FOUND` if no course exists with the requested ID. |
| `courses_announcements_modifyAssignees` | `EXEC` | `courseId, id` | Modifies assignee mode and options of an announcement. Only a teacher of the course that contains the announcement may call this method. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course or course work or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `NOT_FOUND` if the requested course or course work does not exist. |
| `courses_announcements_patch` | `EXEC` | `courseId, id` | Updates one or more fields of an announcement. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting developer project did not create the corresponding announcement or for access errors. * `INVALID_ARGUMENT` if the request is malformed. * `FAILED_PRECONDITION` if the requested announcement has already been deleted. * `NOT_FOUND` if the requested course or announcement does not exist |
