---
title: cursors
hide_title: false
hide_table_of_contents: false
keywords:
  - cursors
  - pubsublite
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cursors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.pubsublite.cursors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
| `partitionCursors` | `array` | The partition cursors from this request. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `cursor_projects_locations_subscriptions_cursors_list` | `SELECT` | `locationsId, projectsId, subscriptionsId` |
