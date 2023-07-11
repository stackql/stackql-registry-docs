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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>calendars</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.calendars</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resourceId` | `string` | The unique ID for the calendar resource. |
| `userVisibleDescription` | `string` | Description of the resource, visible to users and admins. |
| `resourceCategory` | `string` | The category of the calendar resource. Either CONFERENCE_ROOM or OTHER. Legacy data is set to CATEGORY_UNKNOWN. |
| `kind` | `string` | The type of the resource. For calendar resources, the value is `admin#directory#resources#calendars#CalendarResource`. |
| `resourceEmail` | `string` | The read-only email for the calendar resource. Generated as part of creating a new calendar resource. |
| `generatedResourceName` | `string` | The read-only auto-generated name of the calendar resource which includes metadata about the resource such as building name, floor, capacity, etc. For example, "NYC-2-Training Room 1A (16)". |
| `floorName` | `string` | Name of the floor a resource is located on. |
| `resourceDescription` | `string` | Description of the resource, visible only to admins. |
| `floorSection` | `string` | Name of the section within a floor a resource is located in. |
| `etags` | `string` | ETag of the resource. |
| `buildingId` | `string` | Unique ID for the building a resource is located in. |
| `featureInstances` | `any` | Instances of features for the calendar resource. |
| `resourceType` | `string` | The type of the calendar resource, intended for non-room resources. |
| `capacity` | `integer` | Capacity of a resource, number of seats in a room. |
| `resourceName` | `string` | The name of the calendar resource. For example, "Training Room 1A". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `calendarResourceId, customer` | Retrieves a calendar resource. |
| `list` | `SELECT` | `customer` | Retrieves a list of calendar resources for an account. |
| `insert` | `INSERT` | `customer` | Inserts a calendar resource. |
| `delete` | `DELETE` | `calendarResourceId, customer` | Deletes a calendar resource. |
| `patch` | `EXEC` | `calendarResourceId, customer` | Patches a calendar resource. |
| `update` | `EXEC` | `calendarResourceId, customer` | Updates a calendar resource. This method supports patch semantics, meaning you only need to include the fields you wish to update. Fields that are not present in the request will be preserved. |
