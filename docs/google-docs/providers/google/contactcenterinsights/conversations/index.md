---
title: conversations
hide_title: false
hide_table_of_contents: false
keywords:
  - conversations
  - contactcenterinsights
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
<tr><td><b>Name</b></td><td><code>conversations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.contactcenterinsights.conversations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `conversations` | `array` | The conversations that match the request. |
| `nextPageToken` | `string` | A token which can be sent as `page_token` to retrieve the next page. If this field is set, it means there is another page available. If it is not set, it means no other pages are available. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `conversationsId, locationsId, projectsId` | Gets a conversation. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists conversations. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a conversation. |
| `delete` | `DELETE` | `conversationsId, locationsId, projectsId` | Deletes a conversation. |
| `bulk_analyze` | `EXEC` | `locationsId, projectsId` | Analyzes multiple conversations in a single request. |
| `calculate_stats` | `EXEC` | `locationsId, projectsId` | Gets conversation statistics. |
| `ingest` | `EXEC` | `locationsId, projectsId` | Imports conversations and processes them according to the user's configuration. |
| `patch` | `EXEC` | `conversationsId, locationsId, projectsId` | Updates a conversation. |
| `upload` | `EXEC` | `locationsId, projectsId` | Create a longrunning conversation upload operation. This method differs from CreateConversation by allowing audio transcription and optional DLP redaction. |
