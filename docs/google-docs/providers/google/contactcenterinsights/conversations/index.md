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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>conversations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>conversations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.contactcenterinsights.conversations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the conversation. Format: projects/{project}/locations/{location}/conversations/{conversation} |
| <CopyableCode code="agentId" /> | `string` | An opaque, user-specified string representing the human agent who handled the conversation. |
| <CopyableCode code="callMetadata" /> | `object` | Call-specific metadata. |
| <CopyableCode code="createTime" /> | `string` | Output only. The time at which the conversation was created. |
| <CopyableCode code="dataSource" /> | `object` | The conversation source, which is a combination of transcript and audio. |
| <CopyableCode code="dialogflowIntents" /> | `object` | Output only. All the matched Dialogflow intents in the call. The key corresponds to a Dialogflow intent, format: projects/{project}/agent/{agent}/intents/{intent} |
| <CopyableCode code="duration" /> | `string` | Output only. The duration of the conversation. |
| <CopyableCode code="expireTime" /> | `string` | The time at which this conversation should expire. After this time, the conversation data and any associated analyses will be deleted. |
| <CopyableCode code="labels" /> | `object` | A map for the user to specify any custom fields. A maximum of 20 labels per conversation is allowed, with a maximum of 256 characters per entry. |
| <CopyableCode code="languageCode" /> | `string` | A user-specified language code for the conversation. |
| <CopyableCode code="latestAnalysis" /> | `object` | The analysis resource. |
| <CopyableCode code="latestSummary" /> | `object` | Conversation summarization suggestion data. |
| <CopyableCode code="medium" /> | `string` | Immutable. The conversation medium, if unspecified will default to PHONE_CALL. |
| <CopyableCode code="metadataJson" /> | `string` | Input only. JSON Metadata encoded as a string. This field is primarily used by Insights integrations with various telphony systems and must be in one of Insights' supported formats. |
| <CopyableCode code="obfuscatedUserId" /> | `string` | Obfuscated user ID which the customer sent to us. |
| <CopyableCode code="qualityMetadata" /> | `object` | Conversation metadata related to quality management. |
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
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a conversation. Does not support audio transcription or DLP redaction. Use `conversations.upload` instead. |
| <CopyableCode code="bulk_delete" /> | `DELETE` | <CopyableCode code="locationsId, projectsId" /> | Deletes multiple conversations in a single request. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="conversationsId, locationsId, projectsId" /> | Deletes a conversation. |
| <CopyableCode code="patch" /> | `UPDATE` | <CopyableCode code="conversationsId, locationsId, projectsId" /> | Updates a conversation. |
| <CopyableCode code="bulk_analyze" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Analyzes multiple conversations in a single request. |
| <CopyableCode code="calculate_stats" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Gets conversation statistics. |
| <CopyableCode code="ingest" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Imports conversations and processes them according to the user's configuration. |
| <CopyableCode code="upload" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Create a long-running conversation upload operation. This method differs from `CreateConversation` by allowing audio transcription and optional DLP redaction. |

## `SELECT` examples

Lists conversations.

```sql
SELECT
name,
agentId,
callMetadata,
createTime,
dataSource,
dialogflowIntents,
duration,
expireTime,
labels,
languageCode,
latestAnalysis,
latestSummary,
medium,
metadataJson,
obfuscatedUserId,
qualityMetadata,
runtimeAnnotations,
startTime,
transcript,
ttl,
turnCount,
updateTime
FROM google.contactcenterinsights.conversations
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>conversations</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO google.contactcenterinsights.conversations (
locationsId,
projectsId,
transcript,
latestSummary,
expireTime,
startTime,
updateTime,
runtimeAnnotations,
turnCount,
qualityMetadata,
duration,
dataSource,
latestAnalysis,
metadataJson,
name,
labels,
createTime,
callMetadata,
obfuscatedUserId,
medium,
dialogflowIntents,
languageCode,
ttl,
agentId
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ transcript }}',
'{{ latestSummary }}',
'{{ expireTime }}',
'{{ startTime }}',
'{{ updateTime }}',
'{{ runtimeAnnotations }}',
'{{ turnCount }}',
'{{ qualityMetadata }}',
'{{ duration }}',
'{{ dataSource }}',
'{{ latestAnalysis }}',
'{{ metadataJson }}',
'{{ name }}',
'{{ labels }}',
'{{ createTime }}',
'{{ callMetadata }}',
'{{ obfuscatedUserId }}',
'{{ medium }}',
'{{ dialogflowIntents }}',
'{{ languageCode }}',
'{{ ttl }}',
'{{ agentId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: transcript
        value: '{{ transcript }}'
      - name: latestSummary
        value: '{{ latestSummary }}'
      - name: expireTime
        value: '{{ expireTime }}'
      - name: startTime
        value: '{{ startTime }}'
      - name: updateTime
        value: '{{ updateTime }}'
      - name: runtimeAnnotations
        value: '{{ runtimeAnnotations }}'
      - name: turnCount
        value: '{{ turnCount }}'
      - name: qualityMetadata
        value: '{{ qualityMetadata }}'
      - name: duration
        value: '{{ duration }}'
      - name: dataSource
        value: '{{ dataSource }}'
      - name: latestAnalysis
        value: '{{ latestAnalysis }}'
      - name: metadataJson
        value: '{{ metadataJson }}'
      - name: name
        value: '{{ name }}'
      - name: labels
        value: '{{ labels }}'
      - name: createTime
        value: '{{ createTime }}'
      - name: callMetadata
        value: '{{ callMetadata }}'
      - name: obfuscatedUserId
        value: '{{ obfuscatedUserId }}'
      - name: medium
        value: '{{ medium }}'
      - name: dialogflowIntents
        value: '{{ dialogflowIntents }}'
      - name: languageCode
        value: '{{ languageCode }}'
      - name: ttl
        value: '{{ ttl }}'
      - name: agentId
        value: '{{ agentId }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>conversations</code> resource.

```sql
/*+ update */
UPDATE google.contactcenterinsights.conversations
SET 
transcript = '{{ transcript }}',
latestSummary = '{{ latestSummary }}',
expireTime = '{{ expireTime }}',
startTime = '{{ startTime }}',
updateTime = '{{ updateTime }}',
runtimeAnnotations = '{{ runtimeAnnotations }}',
turnCount = '{{ turnCount }}',
qualityMetadata = '{{ qualityMetadata }}',
duration = '{{ duration }}',
dataSource = '{{ dataSource }}',
latestAnalysis = '{{ latestAnalysis }}',
metadataJson = '{{ metadataJson }}',
name = '{{ name }}',
labels = '{{ labels }}',
createTime = '{{ createTime }}',
callMetadata = '{{ callMetadata }}',
obfuscatedUserId = '{{ obfuscatedUserId }}',
medium = '{{ medium }}',
dialogflowIntents = '{{ dialogflowIntents }}',
languageCode = '{{ languageCode }}',
ttl = '{{ ttl }}',
agentId = '{{ agentId }}'
WHERE 
conversationsId = '{{ conversationsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>conversations</code> resource.

```sql
/*+ delete */
DELETE FROM google.contactcenterinsights.conversations
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
