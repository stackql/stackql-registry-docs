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
| `partition` | `string` | The partition this is for. |
| `cursor` | `object` | A cursor that describes the position of a message within a topic partition. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `cursor_projects_locations_subscriptions_cursors_list` | `SELECT` | `locationsId, projectsId, subscriptionsId` |
| `_cursor_projects_locations_subscriptions_cursors_list` | `EXEC` | `locationsId, projectsId, subscriptionsId` |
