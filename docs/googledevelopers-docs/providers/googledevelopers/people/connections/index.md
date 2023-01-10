---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - people
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
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.people.connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `nextSyncToken` | `string` | A token, which can be sent as `sync_token` to retrieve changes since the last request. Request must set `request_sync_token` to return the sync token. When the response is paginated, only the last page will contain `nextSyncToken`. |
| `totalItems` | `integer` | The total number of items in the list without pagination. |
| `totalPeople` | `integer` | **DEPRECATED** (Please use totalItems) The total number of people in the list without pagination. |
| `connections` | `array` | The list of people that the requestor is connected to. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `people_connections_list` | `SELECT` | `peopleId` |
