---
title: sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions
  - fitness
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.fitness.sessions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `session` | `array` | Sessions with an end time that is between startTime and endTime of the request. |
| `deletedSession` | `array` | If includeDeleted is set to true in the request, and startTime and endTime are omitted, this will include sessions which were deleted since the last sync. |
| `hasMoreData` | `boolean` | Flag to indicate server has more data to transfer. DO NOT USE THIS FIELD. It is never populated in responses from the server. |
| `nextPageToken` | `string` | The sync token which is used to sync further changes. This will only be provided if both startTime and endTime are omitted from the request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `users_sessions_list` | `SELECT` | `userId` | Lists sessions previously created. |
| `users_sessions_delete` | `DELETE` | `sessionId, userId` | Deletes a session specified by the given session ID. |
| `users_sessions_update` | `EXEC` | `sessionId, userId` | Updates or insert a given session. |
