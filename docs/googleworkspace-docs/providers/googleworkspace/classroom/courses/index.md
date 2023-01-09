---
title: courses
hide_title: false
hide_table_of_contents: false
keywords:
  - courses
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
<tr><td><b>Name</b></td><td><code>courses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.classroom.courses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier for this course assigned by Classroom. When creating a course, you may optionally set this identifier to an alias string in the request to create a corresponding alias. The `id` is still assigned by Classroom and cannot be updated after the course is created. Specifying this field in a course update mask results in an error. |
| `name` | `string` | Name of the course. For example, "10th Grade Biology". The name is required. It must be between 1 and 750 characters and a valid UTF-8 string. |
| `description` | `string` | Optional description. For example, "We'll be learning about the structure of living creatures from a combination of textbooks, guest lectures, and lab work. Expect to be excited!" If set, this field must be a valid UTF-8 string and no longer than 30,000 characters. |
| `courseGroupEmail` | `string` | The email address of a Google group containing all members of the course. This group does not accept email and can only be used for permissions. Read-only. |
| `courseMaterialSets` | `array` | Sets of materials that appear on the "about" page of this course. Read-only. |
| `alternateLink` | `string` | Absolute link to this course in the Classroom web UI. Read-only. |
| `updateTime` | `string` | Time of the most recent update to this course. Specifying this field in a course update mask results in an error. Read-only. |
| `creationTime` | `string` | Creation time of the course. Specifying this field in a course update mask results in an error. Read-only. |
| `ownerId` | `string` | The identifier of the owner of a course. When specified as a parameter of a create course request, this field is required. The identifier can be one of the following: * the numeric identifier for the user * the email address of the user * the string literal `"me"`, indicating the requesting user This must be set in a create request. Admins can also specify this field in a patch course request to transfer ownership. In other contexts, it is read-only. |
| `guardiansEnabled` | `boolean` | Whether or not guardian notifications are enabled for this course. Read-only. |
| `section` | `string` | Section of the course. For example, "Period 2". If set, this field must be a valid UTF-8 string and no longer than 2800 characters. |
| `calendarId` | `string` | The Calendar ID for a calendar that all course members can see, to which Classroom adds events for course work and announcements in the course. Read-only. |
| `room` | `string` | Optional room location. For example, "301". If set, this field must be a valid UTF-8 string and no longer than 650 characters. |
| `courseState` | `string` | State of the course. If unspecified, the default state is `PROVISIONED`. |
| `teacherGroupEmail` | `string` | The email address of a Google group containing all teachers of the course. This group does not accept email and can only be used for permissions. Read-only. |
| `teacherFolder` | `object` | Representation of a Google Drive folder. |
| `enrollmentCode` | `string` | Enrollment code to use when joining this course. Specifying this field in a course update mask results in an error. Read-only. |
| `gradebookSettings` | `object` | The gradebook settings for a course. See the [help center article](https://support.google.com/edu/classroom/answer/9184995) for details. |
| `descriptionHeading` | `string` | Optional heading for the description. For example, "Welcome to 10th Grade Biology." If set, this field must be a valid UTF-8 string and no longer than 3600 characters. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id` | Returns a course. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to access the requested course or for access errors. * `NOT_FOUND` if no course exists with the requested ID. |
| `list` | `SELECT` |  | Returns a list of courses that the requesting user is permitted to view, restricted to those that match the request. Returned courses are ordered by creation time, with the most recently created coming first. This method returns the following error codes: * `PERMISSION_DENIED` for access errors. * `INVALID_ARGUMENT` if the query argument is malformed. * `NOT_FOUND` if any users specified in the query arguments do not exist. |
| `create` | `INSERT` |  | Creates a course. The user specified in `ownerId` is the owner of the created course and added as a teacher. A non-admin requesting user can only create a course with themselves as the owner. Domain admins can create courses owned by any user within their domain. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to create courses or for access errors. * `NOT_FOUND` if the primary teacher is not a valid user. * `FAILED_PRECONDITION` if the course owner's account is disabled or for the following request errors: * UserGroupsMembershipLimitReached * `ALREADY_EXISTS` if an alias was specified in the `id` and already exists. |
| `delete` | `DELETE` | `id` | Deletes a course. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to delete the requested course or for access errors. * `NOT_FOUND` if no course exists with the requested ID. |
| `patch` | `EXEC` | `id` | Updates one or more fields in a course. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to modify the requested course or for access errors. * `NOT_FOUND` if no course exists with the requested ID. * `INVALID_ARGUMENT` if invalid fields are specified in the update mask or if no update mask is supplied. * `FAILED_PRECONDITION` for the following request errors: * CourseNotModifiable * InactiveCourseOwner * IneligibleOwner |
| `update` | `EXEC` | `id` | Updates a course. This method returns the following error codes: * `PERMISSION_DENIED` if the requesting user is not permitted to modify the requested course or for access errors. * `NOT_FOUND` if no course exists with the requested ID. * `FAILED_PRECONDITION` for the following request errors: * CourseNotModifiable |
