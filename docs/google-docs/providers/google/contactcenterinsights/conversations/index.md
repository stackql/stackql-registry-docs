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
agentId,
name,
expireTime,
languageCode,
ttl,
obfuscatedUserId,
metadataJson,
medium,
callMetadata,
startTime,
qualityMetadata,
labels,
dataSource
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ agentId }}',
'{{ name }}',
'{{ expireTime }}',
'{{ languageCode }}',
'{{ ttl }}',
'{{ obfuscatedUserId }}',
'{{ metadataJson }}',
'{{ medium }}',
'{{ callMetadata }}',
'{{ startTime }}',
'{{ qualityMetadata }}',
'{{ labels }}',
'{{ dataSource }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: latestSummary
      value:
        - name: textSections
          value: object
        - name: metadata
          value: object
        - name: conversationModel
          value: string
        - name: confidence
          value: number
        - name: answerRecord
          value: string
        - name: text
          value: string
    - name: dialogflowIntents
      value: object
    - name: agentId
      value: string
    - name: name
      value: string
    - name: expireTime
      value: string
    - name: languageCode
      value: string
    - name: ttl
      value: string
    - name: obfuscatedUserId
      value: string
    - name: createTime
      value: string
    - name: transcript
      value:
        - name: transcriptSegments
          value:
            - - name: sentiment
                value:
                  - name: score
                    value: number
                  - name: magnitude
                    value: number
              - name: channelTag
                value: integer
              - name: dialogflowSegmentMetadata
                value:
                  - name: smartReplyAllowlistCovered
                    value: boolean
              - name: text
                value: string
              - name: segmentParticipant
                value:
                  - name: obfuscatedExternalUserId
                    value: string
                  - name: dialogflowParticipant
                    value: string
                  - name: userId
                    value: string
                  - name: role
                    value: string
                  - name: dialogflowParticipantName
                    value: string
              - name: languageCode
                value: string
              - name: words
                value:
                  - - name: endOffset
                      value: string
                    - name: startOffset
                      value: string
                    - name: confidence
                      value: number
                    - name: word
                      value: string
              - name: confidence
                value: number
              - name: messageTime
                value: string
    - name: metadataJson
      value: string
    - name: medium
      value: string
    - name: callMetadata
      value:
        - name: agentChannel
          value: integer
        - name: customerChannel
          value: integer
    - name: runtimeAnnotations
      value:
        - - name: smartComposeSuggestion
            value:
              - name: suggestion
                value: string
              - name: queryRecord
                value: string
              - name: metadata
                value: object
              - name: confidenceScore
                value: number
          - name: faqAnswer
            value:
              - name: source
                value: string
              - name: confidenceScore
                value: number
              - name: metadata
                value: object
              - name: queryRecord
                value: string
              - name: question
                value: string
              - name: answer
                value: string
          - name: dialogflowInteraction
            value:
              - name: confidence
                value: number
              - name: dialogflowIntentId
                value: string
          - name: articleSuggestion
            value:
              - name: source
                value: string
              - name: metadata
                value: object
              - name: uri
                value: string
              - name: title
                value: string
              - name: queryRecord
                value: string
              - name: confidenceScore
                value: number
          - name: endBoundary
            value:
              - name: wordIndex
                value: integer
              - name: transcriptIndex
                value: integer
          - name: annotationId
            value: string
          - name: createTime
            value: string
          - name: smartReply
            value:
              - name: metadata
                value: object
              - name: reply
                value: string
              - name: confidenceScore
                value: number
              - name: queryRecord
                value: string
          - name: answerFeedback
            value:
              - name: correctnessLevel
                value: string
              - name: clicked
                value: boolean
              - name: displayed
                value: boolean
          - name: userInput
            value:
              - name: querySource
                value: string
              - name: query
                value: string
              - name: generatorName
                value: string
    - name: startTime
      value: string
    - name: qualityMetadata
      value:
        - name: agentInfo
          value:
            - - name: agentId
                value: string
              - name: displayName
                value: string
              - name: team
                value: string
              - name: dispositionCode
                value: string
        - name: waitDuration
          value: string
        - name: menuPath
          value: string
        - name: customerSatisfactionRating
          value: integer
    - name: updateTime
      value: string
    - name: turnCount
      value: integer
    - name: labels
      value: object
    - name: dataSource
      value:
        - name: dialogflowSource
          value:
            - name: audioUri
              value: string
            - name: dialogflowConversation
              value: string
        - name: gcsSource
          value:
            - name: transcriptUri
              value: string
            - name: audioUri
              value: string
    - name: duration
      value: string
    - name: latestAnalysis
      value:
        - name: analysisResult
          value:
            - name: endTime
              value: string
            - name: callAnalysisMetadata
              value:
                - name: sentiments
                  value:
                    - - name: channelTag
                        value: integer
                - name: silence
                  value:
                    - name: silenceDuration
                      value: string
                    - name: silencePercentage
                      value: number
                - name: intents
                  value: object
                - name: entities
                  value: object
                - name: issueModelResult
                  value:
                    - name: issues
                      value:
                        - - name: score
                            value: number
                          - name: displayName
                            value: string
                          - name: issue
                            value: string
                    - name: issueModel
                      value: string
                - name: phraseMatchers
                  value: object
                - name: annotations
                  value:
                    - - name: silenceData
                        value: []
                      - name: entityMentionData
                        value:
                          - name: entityUniqueId
                            value: string
                          - name: type
                            value: string
                      - name: channelTag
                        value: integer
                      - name: interruptionData
                        value: []
                      - name: phraseMatchData
                        value:
                          - name: phraseMatcher
                            value: string
                          - name: displayName
                            value: string
                      - name: issueMatchData
                        value:
                          - name: issueAssignment
                            value:
                              - name: score
                                value: number
                              - name: displayName
                                value: string
                              - name: issue
                                value: string
                      - name: holdData
                        value: []
                      - name: intentMatchData
                        value:
                          - name: intentUniqueId
                            value: string
        - name: name
          value: string
        - name: createTime
          value: string
        - name: requestTime
          value: string
        - name: annotatorSelector
          value:
            - name: runSummarizationAnnotator
              value: boolean
            - name: runSentimentAnnotator
              value: boolean
            - name: issueModels
              value:
                - string
            - name: runIntentAnnotator
              value: boolean
            - name: runEntityAnnotator
              value: boolean
            - name: runPhraseMatcherAnnotator
              value: boolean
            - name: runInterruptionAnnotator
              value: boolean
            - name: runSilenceAnnotator
              value: boolean
            - name: runIssueModelAnnotator
              value: boolean
            - name: summarizationConfig
              value:
                - name: summarizationModel
                  value: string
                - name: conversationProfile
                  value: string
            - name: phraseMatchers
              value:
                - string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>conversations</code> resource.

```sql
/*+ update */
UPDATE google.contactcenterinsights.conversations
SET 
agentId = '{{ agentId }}',
name = '{{ name }}',
expireTime = '{{ expireTime }}',
languageCode = '{{ languageCode }}',
ttl = '{{ ttl }}',
obfuscatedUserId = '{{ obfuscatedUserId }}',
metadataJson = '{{ metadataJson }}',
medium = '{{ medium }}',
callMetadata = '{{ callMetadata }}',
startTime = '{{ startTime }}',
qualityMetadata = '{{ qualityMetadata }}',
labels = '{{ labels }}',
dataSource = '{{ dataSource }}'
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
