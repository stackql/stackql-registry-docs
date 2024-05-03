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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>conversations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contactcenterinsights.conversations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the conversation. Format: projects/&#123;project&#125;/locations/&#123;location&#125;/conversations/&#123;conversation&#125; |
| <CopyableCode code="agentId" /> | `string` | An opaque, user-specified string representing the human agent who handled the conversation. |
| <CopyableCode code="callMetadata" /> | `object` | Call-specific metadata. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the conversation was created. |
| <CopyableCode code="dataSource" /> | `object` | The conversation source, which is a combination of transcript and audio. |
| <CopyableCode code="dialogflowIntents" /> | `object` | Output only. All the matched Dialogflow intents in the call. The key corresponds to a Dialogflow intent, format: projects/&#123;project&#125;/agent/&#123;agent&#125;/intents/&#123;intent&#125; |
| <CopyableCode code="duration" /> | `string` | Output only. The duration of the conversation. |
| <CopyableCode code="expireTime" /> | `string` | The time at which this conversation should expire. After this time, the conversation data and any associated analyses will be deleted. |
| <CopyableCode code="labels" /> | `object` | A map for the user to specify any custom fields. A maximum of 20 labels per conversation is allowed, with a maximum of 256 characters per entry. |
| <CopyableCode code="languageCode" /> | `string` | A user-specified language code for the conversation. |
| <CopyableCode code="latestAnalysis" /> | `object` | The analysis resource. |
| <CopyableCode code="latestSummary" /> | `object` | Conversation summarization suggestion data. |
| <CopyableCode code="medium" /> | `string` | Immutable. The conversation medium, if unspecified will default to PHONE_CALL. |
| <CopyableCode code="obfuscatedUserId" /> | `string` | Obfuscated user ID which the customer sent to us. |
| <CopyableCode code="runtimeAnnotations" /> | `array` | Output only. The annotations that were generated during the customer and agent interaction. |
| <CopyableCode code="startTime" /> | `string` | The time at which the conversation started. |
| <CopyableCode code="transcript" /> | `object` | A message representing the transcript of a conversation. |
| <CopyableCode code="ttl" /> | `string` | Input only. The TTL for this resource. If specified, then this TTL will be used to calculate the expire time. |
| <CopyableCode code="turnCount" /> | `integer` | Output only. The number of turns in the conversation. |
| <CopyableCode code="updateTime" /> | `string` | Output only. The most recent time at which the conversation was updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="conversationsId, locationsId, projectsId" /> | Gets a conversation. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists conversations. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a conversation. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="conversationsId, locationsId, projectsId" /> | Deletes a conversation. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists conversations. |
| <CopyableCode code="bulk_analyze" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Analyzes multiple conversations in a single request. |
| <CopyableCode code="calculate_stats" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Gets conversation statistics. |
| <CopyableCode code="ingest" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Imports conversations and processes them according to the user's configuration. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="conversationsId, locationsId, projectsId" /> | Updates a conversation. |
| <CopyableCode code="upload" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Create a longrunning conversation upload operation. This method differs from CreateConversation by allowing audio transcription and optional DLP redaction. |
