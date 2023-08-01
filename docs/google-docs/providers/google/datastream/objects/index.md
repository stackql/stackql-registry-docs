---
title: objects
hide_title: false
hide_table_of_contents: false
keywords:
  - objects
  - datastream
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
<tr><td><b>Name</b></td><td><code>objects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datastream.objects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. |
| `streamObjects` | `array` | List of stream objects. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, objectsId, projectsId, streamsId` | Use this method to get details about a stream object. |
| `list` | `SELECT` | `locationsId, projectsId, streamsId` | Use this method to list the objects of a specific stream. |
| `lookup` | `EXEC` | `locationsId, projectsId, streamsId` | Use this method to look up a stream object by its source object identifier. |
| `start_backfill_job` | `EXEC` | `locationsId, objectsId, projectsId, streamsId` | Use this method to start a backfill job for the specified stream object. |
| `stop_backfill_job` | `EXEC` | `locationsId, objectsId, projectsId, streamsId` | Use this method to stop a backfill job for the specified stream object. |
