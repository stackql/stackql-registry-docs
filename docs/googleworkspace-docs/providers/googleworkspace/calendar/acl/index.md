---
title: acl
hide_title: false
hide_table_of_contents: false
keywords:
  - acl
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
<tr><td><b>Name</b></td><td><code>acl</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.calendar.acl</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the Access Control List (ACL) rule. See Sharing calendars. |
| `role` | `string` | The role assigned to the scope. Possible values are:  <br />- "none" - Provides no access. <br />- "freeBusyReader" - Provides read access to free/busy information. <br />- "reader" - Provides read access to the calendar. Private events will appear to users with reader access, but event details will be hidden. <br />- "writer" - Provides read and write access to the calendar. Private events will appear to users with writer access, and event details will be visible. <br />- "owner" - Provides ownership of the calendar. This role has all of the permissions of the writer role with the additional ability to see and manipulate ACLs. |
| `scope` | `object` | The extent to which calendar access is granted by this ACL rule. |
| `etag` | `string` | ETag of the resource. |
| `kind` | `string` | Type of the resource ("calendar#aclRule"). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `calendarId, ruleId` | Returns an access control rule. |
| `list` | `SELECT` | `calendarId` | Returns the rules in the access control list for the calendar. |
| `insert` | `INSERT` | `calendarId` | Creates an access control rule. |
| `delete` | `DELETE` | `calendarId, ruleId` | Deletes an access control rule. |
| `patch` | `EXEC` | `calendarId, ruleId` | Updates an access control rule. This method supports patch semantics. |
| `update` | `EXEC` | `calendarId, ruleId` | Updates an access control rule. |
| `watch` | `EXEC` | `calendarId` | Watch for changes to ACL resources. |
