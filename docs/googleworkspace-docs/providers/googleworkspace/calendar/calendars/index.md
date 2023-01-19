---
title: calendars
hide_title: false
hide_table_of_contents: false
keywords:
  - calendars
  - calendar
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
<tr><td><b>Name</b></td><td><code>calendars</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.calendar.calendars</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the calendar. To retrieve IDs call the calendarList.list() method. |
| `description` | `string` | Description of the calendar. Optional. |
| `timeZone` | `string` | The time zone of the calendar. (Formatted as an IANA Time Zone Database name, e.g. "Europe/Zurich".) Optional. |
| `conferenceProperties` | `object` |  |
| `etag` | `string` | ETag of the resource. |
| `kind` | `string` | Type of the resource ("calendar#calendar"). |
| `location` | `string` | Geographic location of the calendar as free-form text. Optional. |
| `summary` | `string` | Title of the calendar. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `calendarId` | Returns metadata for a calendar. |
| `insert` | `INSERT` |  | Creates a secondary calendar. |
| `delete` | `DELETE` | `calendarId` | Deletes a secondary calendar. Use calendars.clear for clearing all events on primary calendars. |
| `clear` | `EXEC` | `calendarId` | Clears a primary calendar. This operation deletes all events associated with the primary calendar of an account. |
| `patch` | `EXEC` | `calendarId` | Updates metadata for a calendar. This method supports patch semantics. |
| `update` | `EXEC` | `calendarId` | Updates metadata for a calendar. |
