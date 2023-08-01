---
title: streams
hide_title: false
hide_table_of_contents: false
keywords:
  - streams
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
<tr><td><b>Name</b></td><td><code>streams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datastream.streams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `streams` | `array` | List of streams |
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `locationsId, projectsId, streamsId` | Use this method to get details about a stream. |
| `list` | `SELECT` | `locationsId, projectsId` | Use this method to list streams in a project and location. |
| `create` | `INSERT` | `locationsId, projectsId` | Use this method to create a stream. |
| `delete` | `DELETE` | `locationsId, projectsId, streamsId` | Use this method to delete a stream. |
| `patch` | `EXEC` | `locationsId, projectsId, streamsId` | Use this method to update the configuration of a stream. |
| `run` | `EXEC` | `locationsId, projectsId, streamsId` | Use this method to start, resume or recover a stream with a non default CDC strategy. |
