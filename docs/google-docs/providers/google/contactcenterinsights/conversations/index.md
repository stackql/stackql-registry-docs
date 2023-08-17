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
| `name` | `string` | Immutable. The resource name of the conversation. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/conversations/&#123;conversation&#125; |
| `obfuscatedUserId` | `string` | Obfuscated user ID which the customer sent to us. |
| `latestAnalysis` | `object` | The analysis resource. |
| `turnCount` | `integer` | Output only. The number of turns in the conversation. |
| `createTime` | `string` | Output only. The time at which the conversation was created. |
| `latestSummary` | `object` | Conversation summarization suggestion data. |
| `expireTime` | `string` | The time at which this conversation should expire. After this time, the conversation data and any associated analyses will be deleted. |
| `dialogflowIntents` | `object` | Output only. All the matched Dialogflow intents in the call. The key corresponds to a Dialogflow intent, format: projects/&#123;project&#125;/agent/&#123;agent&#125;/intents/&#123;intent&#125; |
| `duration` | `string` | Output only. The duration of the conversation. |
| `updateTime` | `string` | Output only. The most recent time at which the conversation was updated. |
| `languageCode` | `string` | A user-specified language code for the conversation. |
| `startTime` | `string` | The time at which the conversation started. |
| `transcript` | `object` | A message representing the transcript of a conversation. |
| `runtimeAnnotations` | `array` | Output only. The annotations that were generated during the customer and agent interaction. |
| `callMetadata` | `object` | Call-specific metadata. |
| `dataSource` | `object` | The conversation source, which is a combination of transcript and audio. |
| `labels` | `object` | A map for the user to specify any custom fields. A maximum of 20 labels per conversation is allowed, with a maximum of 256 characters per entry. |
| `agentId` | `string` | An opaque, user-specified string representing the human agent who handled the conversation. |
| `medium` | `string` | Immutable. The conversation medium, if unspecified will default to PHONE_CALL. |
| `ttl` | `string` | Input only. The TTL for this resource. If specified, then this TTL will be used to calculate the expire time. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `conversationsId, locationsId, projectsId` | Gets a conversation. |
| `list` | `SELECT` | `locationsId, projectsId` | Lists conversations. |
| `create` | `INSERT` | `locationsId, projectsId` | Creates a conversation. |
| `delete` | `DELETE` | `conversationsId, locationsId, projectsId` | Deletes a conversation. |
| `_list` | `EXEC` | `locationsId, projectsId` | Lists conversations. |
| `bulk_analyze` | `EXEC` | `locationsId, projectsId` | Analyzes multiple conversations in a single request. |
| `calculate_stats` | `EXEC` | `locationsId, projectsId` | Gets conversation statistics. |
| `ingest` | `EXEC` | `locationsId, projectsId` | Imports conversations and processes them according to the user's configuration. |
| `patch` | `EXEC` | `conversationsId, locationsId, projectsId` | Updates a conversation. |
| `upload` | `EXEC` | `locationsId, projectsId` | Create a longrunning conversation upload operation. This method differs from CreateConversation by allowing audio transcription and optional DLP redaction. |
