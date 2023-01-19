---
title: calendar_list
hide_title: false
hide_table_of_contents: false
keywords:
  - calendar_list
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
<tr><td><b>Name</b></td><td><code>calendar_list</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.calendar.calendar_list</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the calendar. |
| `description` | `string` | Description of the calendar. Optional. Read-only. |
| `conferenceProperties` | `object` |  |
| `hidden` | `boolean` | Whether the calendar has been hidden from the list. Optional. The attribute is only returned when the calendar is hidden, in which case the value is true. |
| `deleted` | `boolean` | Whether this calendar list entry has been deleted from the calendar list. Read-only. Optional. The default is False. |
| `defaultReminders` | `array` | The default reminders that the authenticated user has for this calendar. |
| `backgroundColor` | `string` | The main color of the calendar in the hexadecimal format "#0088aa". This property supersedes the index-based colorId property. To set or change this property, you need to specify colorRgbFormat=true in the parameters of the insert, update and patch methods. Optional. |
| `foregroundColor` | `string` | The foreground color of the calendar in the hexadecimal format "#ffffff". This property supersedes the index-based colorId property. To set or change this property, you need to specify colorRgbFormat=true in the parameters of the insert, update and patch methods. Optional. |
| `timeZone` | `string` | The time zone of the calendar. Optional. Read-only. |
| `accessRole` | `string` | The effective access role that the authenticated user has on the calendar. Read-only. Possible values are:  <br />- "freeBusyReader" - Provides read access to free/busy information. <br />- "reader" - Provides read access to the calendar. Private events will appear to users with reader access, but event details will be hidden. <br />- "writer" - Provides read and write access to the calendar. Private events will appear to users with writer access, and event details will be visible. <br />- "owner" - Provides ownership of the calendar. This role has all of the permissions of the writer role with the additional ability to see and manipulate ACLs. |
| `summary` | `string` | Title of the calendar. Read-only. |
| `notificationSettings` | `object` | The notifications that the authenticated user is receiving for this calendar. |
| `colorId` | `string` | The color of the calendar. This is an ID referring to an entry in the calendar section of the colors definition (see the colors endpoint). This property is superseded by the backgroundColor and foregroundColor properties and can be ignored when using these properties. Optional. |
| `selected` | `boolean` | Whether the calendar content shows up in the calendar UI. Optional. The default is False. |
| `kind` | `string` | Type of the resource ("calendar#calendarListEntry"). |
| `summaryOverride` | `string` | The summary that the authenticated user has set for this calendar. Optional. |
| `etag` | `string` | ETag of the resource. |
| `location` | `string` | Geographic location of the calendar as free-form text. Optional. Read-only. |
| `primary` | `boolean` | Whether the calendar is the primary calendar of the authenticated user. Read-only. Optional. The default is False. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `calendarList_get` | `SELECT` | `calendarId` | Returns a calendar from the user's calendar list. |
| `calendarList_list` | `SELECT` |  | Returns the calendars on the user's calendar list. |
| `calendarList_delete` | `DELETE` | `calendarId` | Removes a calendar from the user's calendar list. |
| `calendarList_insert` | `EXEC` |  | Inserts an existing calendar into the user's calendar list. |
| `calendarList_patch` | `EXEC` | `calendarId` | Updates an existing calendar on the user's calendar list. This method supports patch semantics. |
| `calendarList_update` | `EXEC` | `calendarId` | Updates an existing calendar on the user's calendar list. |
| `calendarList_watch` | `EXEC` |  | Watch for changes to CalendarList resources. |
