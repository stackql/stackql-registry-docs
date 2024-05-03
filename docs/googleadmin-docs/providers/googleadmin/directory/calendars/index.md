---
title: calendars
hide_title: false
hide_table_of_contents: false
keywords:
  - calendars
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>calendars</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.calendars" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="buildingId" /> | `string` | Unique ID for the building a resource is located in. |
| <CopyableCode code="capacity" /> | `integer` | Capacity of a resource, number of seats in a room. |
| <CopyableCode code="etags" /> | `string` | ETag of the resource. |
| <CopyableCode code="featureInstances" /> | `any` | Instances of features for the calendar resource. |
| <CopyableCode code="floorName" /> | `string` | Name of the floor a resource is located on. |
| <CopyableCode code="floorSection" /> | `string` | Name of the section within a floor a resource is located in. |
| <CopyableCode code="generatedResourceName" /> | `string` | The read-only auto-generated name of the calendar resource which includes metadata about the resource such as building name, floor, capacity, etc. For example, "NYC-2-Training Room 1A (16)". |
| <CopyableCode code="kind" /> | `string` | The type of the resource. For calendar resources, the value is `admin#directory#resources#calendars#CalendarResource`. |
| <CopyableCode code="resourceCategory" /> | `string` | The category of the calendar resource. Either CONFERENCE_ROOM or OTHER. Legacy data is set to CATEGORY_UNKNOWN. |
| <CopyableCode code="resourceDescription" /> | `string` | Description of the resource, visible only to admins. |
| <CopyableCode code="resourceEmail" /> | `string` | The read-only email for the calendar resource. Generated as part of creating a new calendar resource. |
| <CopyableCode code="resourceId" /> | `string` | The unique ID for the calendar resource. |
| <CopyableCode code="resourceName" /> | `string` | The name of the calendar resource. For example, "Training Room 1A". |
| <CopyableCode code="resourceType" /> | `string` | The type of the calendar resource, intended for non-room resources. |
| <CopyableCode code="userVisibleDescription" /> | `string` | Description of the resource, visible to users and admins. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="calendarResourceId, customer" /> | Retrieves a calendar resource. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="customer" /> | Retrieves a list of calendar resources for an account. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="customer" /> | Inserts a calendar resource. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="calendarResourceId, customer" /> | Deletes a calendar resource. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="calendarResourceId, customer" /> | Patches a calendar resource. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="calendarResourceId, customer" /> | Updates a calendar resource. This method supports patch semantics, meaning you only need to include the fields you wish to update. Fields that are not present in the request will be preserved. |
