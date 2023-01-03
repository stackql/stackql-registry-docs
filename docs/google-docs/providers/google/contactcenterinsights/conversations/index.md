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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Immutable. The resource name of the conversation. Format: projects/{project}/locations/{location}/conversations/{conversation} |
| `dataSource` | `object` | The conversation source, which is a combination of transcript and audio. |
| `duration` | `string` | Output only. The duration of the conversation. |
| `ttl` | `string` | Input only. The TTL for this resource. If specified, then this TTL will be used to calculate the expire time. |
| `medium` | `string` | Immutable. The conversation medium, if unspecified will default to PHONE_CALL. |
| `createTime` | `string` | Output only. The time at which the conversation was created. |
| `agentId` | `string` | An opaque, user-specified string representing the human agent who handled the conversation. |
| `callMetadata` | `object` | Call-specific metadata. |
| `runtimeAnnotations` | `array` | Output only. The annotations that were generated during the customer and agent interaction. |
| `startTime` | `string` | The time at which the conversation started. |
| `labels` | `object` | A map for the user to specify any custom fields. A maximum of 20 labels per conversation is allowed, with a maximum of 256 characters per entry. |
| `obfuscatedUserId` | `string` | Obfuscated user ID which the customer sent to us. |
| `expireTime` | `string` | The time at which this conversation should expire. After this time, the conversation data and any associated analyses will be deleted. |
| `dialogflowIntents` | `object` | Output only. All the matched Dialogflow intents in the call. The key corresponds to a Dialogflow intent, format: projects/{project}/agent/{agent}/intents/{intent} |
| `transcript` | `object` | A message representing the transcript of a conversation. |
| `languageCode` | `string` | A user-specified language code for the conversation. |
| `turnCount` | `integer` | Output only. The number of turns in the conversation. |
| `latestAnalysis` | `object` | The analysis resource. |
| `updateTime` | `string` | Output only. The most recent time at which the conversation was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_conversations_get` | `SELECT` | `conversationsId, locationsId, projectsId` | Gets a conversation. |
| `projects_locations_conversations_list` | `SELECT` | `locationsId, projectsId` | Lists conversations. |
| `projects_locations_conversations_create` | `INSERT` | `locationsId, projectsId` | Creates a conversation. |
| `projects_locations_conversations_delete` | `DELETE` | `conversationsId, locationsId, projectsId` | Deletes a conversation. |
| `projects_locations_conversations_calculateStats` | `EXEC` | `locationsId, projectsId` | Gets conversation statistics. |
| `projects_locations_conversations_patch` | `EXEC` | `conversationsId, locationsId, projectsId` | Updates a conversation. |
