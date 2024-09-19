---
title: test_cases
hide_title: false
hide_table_of_contents: false
keywords:
  - test_cases
  - dialogflow
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

Creates, updates, deletes, gets or lists a <code>test_cases</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>test_cases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.test_cases" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique identifier of the test case. TestCases.CreateTestCase will populate the name automatically. Otherwise use format: `projects//locations//agents//testCases/`. |
| <CopyableCode code="creationTime" /> | `string` | Output only. When the test was created. |
| <CopyableCode code="displayName" /> | `string` | Required. The human-readable name of the test case, unique within the agent. Limit of 200 characters. |
| <CopyableCode code="lastTestResult" /> | `object` | Represents a result from running a test case in an agent environment. |
| <CopyableCode code="notes" /> | `string` | Additional freeform notes about the test case. Limit of 400 characters. |
| <CopyableCode code="tags" /> | `array` | Tags are short descriptions that users may apply to test cases for organizational and filtering purposes. Each tag should start with "#" and has a limit of 30 characters. |
| <CopyableCode code="testCaseConversationTurns" /> | `array` | The conversation turns uttered when the test case was created, in chronological order. These include the canonical set of agent utterances that should occur when the agent is working properly. |
| <CopyableCode code="testConfig" /> | `object` | Represents configurations for a test case. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_test_cases_get" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId, testCasesId" /> | Gets a test case. |
| <CopyableCode code="projects_locations_agents_test_cases_list" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Fetches a list of test cases for a given agent. |
| <CopyableCode code="projects_locations_agents_test_cases_create" /> | `INSERT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Creates a test case for the given agent. |
| <CopyableCode code="projects_locations_agents_test_cases_batch_delete" /> | `DELETE` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Batch deletes test cases. |
| <CopyableCode code="projects_locations_agents_test_cases_patch" /> | `UPDATE` | <CopyableCode code="agentsId, locationsId, projectsId, testCasesId" /> | Updates the specified test case. |
| <CopyableCode code="projects_locations_agents_test_cases_batch_run" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Kicks off a batch run of test cases. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: BatchRunTestCasesMetadata - `response`: BatchRunTestCasesResponse |
| <CopyableCode code="projects_locations_agents_test_cases_calculate_coverage" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Calculates the test coverage for an agent. |
| <CopyableCode code="projects_locations_agents_test_cases_export" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Exports the test cases under the agent to a Cloud Storage bucket or a local file. Filter can be applied to export a subset of test cases. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: ExportTestCasesMetadata - `response`: ExportTestCasesResponse |
| <CopyableCode code="projects_locations_agents_test_cases_import" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Imports the test cases from a Cloud Storage bucket or a local file. It always creates new test cases and won't overwrite any existing ones. The provided ID in the imported test case is neglected. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: ImportTestCasesMetadata - `response`: ImportTestCasesResponse |
| <CopyableCode code="projects_locations_agents_test_cases_run" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId, testCasesId" /> | Kicks off a test case run. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: RunTestCaseMetadata - `response`: RunTestCaseResponse |

## `SELECT` examples

Fetches a list of test cases for a given agent.

```sql
SELECT
name,
creationTime,
displayName,
lastTestResult,
notes,
tags,
testCaseConversationTurns,
testConfig
FROM google.dialogflow.test_cases
WHERE agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>test_cases</code> resource.

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
INSERT INTO google.dialogflow.test_cases (
agentsId,
locationsId,
projectsId,
name,
tags,
displayName,
notes,
testConfig,
testCaseConversationTurns,
lastTestResult
)
SELECT 
'{{ agentsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ tags }}',
'{{ displayName }}',
'{{ notes }}',
'{{ testConfig }}',
'{{ testCaseConversationTurns }}',
'{{ lastTestResult }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: tags
      value:
        - string
    - name: displayName
      value: string
    - name: notes
      value: string
    - name: testConfig
      value:
        - name: trackingParameters
          value:
            - string
        - name: flow
          value: string
        - name: page
          value: string
    - name: testCaseConversationTurns
      value:
        - - name: userInput
            value:
              - name: input
                value:
                  - name: text
                    value:
                      - name: text
                        value: string
                  - name: intent
                    value:
                      - name: intent
                        value: string
                  - name: audio
                    value:
                      - name: config
                        value:
                          - name: audioEncoding
                            value: string
                          - name: sampleRateHertz
                            value: integer
                          - name: enableWordInfo
                            value: boolean
                          - name: phraseHints
                            value:
                              - string
                          - name: model
                            value: string
                          - name: modelVariant
                            value: string
                          - name: singleUtterance
                            value: boolean
                          - name: bargeInConfig
                            value:
                              - name: noBargeInDuration
                                value: string
                              - name: totalDuration
                                value: string
                          - name: optOutConformerModelMigration
                            value: boolean
                      - name: audio
                        value: string
                  - name: event
                    value:
                      - name: event
                        value: string
                  - name: dtmf
                    value:
                      - name: digits
                        value: string
                      - name: finishDigit
                        value: string
                  - name: languageCode
                    value: string
              - name: injectedParameters
                value: object
              - name: isWebhookEnabled
                value: boolean
              - name: enableSentimentAnalysis
                value: boolean
          - name: virtualAgentOutput
            value:
              - name: sessionParameters
                value: object
              - name: differences
                value:
                  - - name: type
                      value: string
                    - name: description
                      value: string
              - name: diagnosticInfo
                value: object
              - name: triggeredIntent
                value:
                  - name: name
                    value: string
                  - name: displayName
                    value: string
                  - name: trainingPhrases
                    value:
                      - - name: id
                          value: string
                        - name: parts
                          value:
                            - - name: text
                                value: string
                              - name: parameterId
                                value: string
                        - name: repeatCount
                          value: integer
                  - name: parameters
                    value:
                      - - name: id
                          value: string
                        - name: entityType
                          value: string
                        - name: isList
                          value: boolean
                        - name: redact
                          value: boolean
                  - name: priority
                    value: integer
                  - name: isFallback
                    value: boolean
                  - name: labels
                    value: object
                  - name: description
                    value: string
              - name: currentPage
                value:
                  - name: name
                    value: string
                  - name: displayName
                    value: string
                  - name: description
                    value: string
                  - name: entryFulfillment
                    value:
                      - name: messages
                        value:
                          - - name: text
                              value:
                                - name: text
                                  value:
                                    - string
                                - name: allowPlaybackInterruption
                                  value: boolean
                            - name: payload
                              value: object
                            - name: conversationSuccess
                              value:
                                - name: metadata
                                  value: object
                            - name: outputAudioText
                              value:
                                - name: text
                                  value: string
                                - name: ssml
                                  value: string
                                - name: allowPlaybackInterruption
                                  value: boolean
                            - name: liveAgentHandoff
                              value:
                                - name: metadata
                                  value: object
                            - name: endInteraction
                              value: []
                            - name: playAudio
                              value:
                                - name: audioUri
                                  value: string
                                - name: allowPlaybackInterruption
                                  value: boolean
                            - name: mixedAudio
                              value:
                                - name: segments
                                  value:
                                    - - name: audio
                                        value: string
                                      - name: uri
                                        value: string
                                      - name: allowPlaybackInterruption
                                        value: boolean
                            - name: telephonyTransferCall
                              value:
                                - name: phoneNumber
                                  value: string
                            - name: knowledgeInfoCard
                              value: []
                            - name: responseType
                              value: string
                            - name: channel
                              value: string
                      - name: webhook
                        value: string
                      - name: returnPartialResponses
                        value: boolean
                      - name: tag
                        value: string
                      - name: setParameterActions
                        value:
                          - - name: parameter
                              value: string
                            - name: value
                              value: any
                      - name: conditionalCases
                        value:
                          - - name: cases
                              value:
                                - - name: condition
                                    value: string
                                  - name: caseContent
                                    value:
                                      - - name: message
                                          value:
                                            - name: payload
                                              value: object
                                            - name: responseType
                                              value: string
                                            - name: channel
                                              value: string
                                        - name: additionalCases
                                          value:
                                            - name: cases
                                              value:
                                                - - name: condition
                                                    value: string
                                                  - name: caseContent
                                                    value:
                                                      - []
                      - name: advancedSettings
                        value:
                          - name: audioExportGcsDestination
                            value:
                              - name: uri
                                value: string
                          - name: speechSettings
                            value:
                              - name: endpointerSensitivity
                                value: integer
                              - name: noSpeechTimeout
                                value: string
                              - name: useTimeoutBasedEndpointing
                                value: boolean
                              - name: models
                                value: object
                          - name: dtmfSettings
                            value:
                              - name: enabled
                                value: boolean
                              - name: maxDigits
                                value: integer
                              - name: finishDigit
                                value: string
                              - name: interdigitTimeoutDuration
                                value: string
                              - name: endpointingTimeoutDuration
                                value: string
                          - name: loggingSettings
                            value:
                              - name: enableStackdriverLogging
                                value: boolean
                              - name: enableInteractionLogging
                                value: boolean
                              - name: enableConsentBasedRedaction
                                value: boolean
                      - name: enableGenerativeFallback
                        value: boolean
                  - name: form
                    value:
                      - name: parameters
                        value:
                          - - name: displayName
                              value: string
                            - name: required
                              value: boolean
                            - name: entityType
                              value: string
                            - name: isList
                              value: boolean
                            - name: fillBehavior
                              value:
                                - name: repromptEventHandlers
                                  value:
                                    - - name: name
                                        value: string
                                      - name: event
                                        value: string
                                      - name: targetPage
                                        value: string
                                      - name: targetFlow
                                        value: string
                                      - name: targetPlaybook
                                        value: string
                            - name: defaultValue
                              value: any
                            - name: redact
                              value: boolean
                  - name: transitionRouteGroups
                    value:
                      - string
                  - name: transitionRoutes
                    value:
                      - - name: name
                          value: string
                        - name: description
                          value: string
                        - name: intent
                          value: string
                        - name: condition
                          value: string
                        - name: targetPage
                          value: string
                        - name: targetFlow
                          value: string
                  - name: eventHandlers
                    value:
                      - - name: name
                          value: string
                        - name: event
                          value: string
                        - name: targetPage
                          value: string
                        - name: targetFlow
                          value: string
                        - name: targetPlaybook
                          value: string
                  - name: knowledgeConnectorSettings
                    value:
                      - name: enabled
                        value: boolean
                      - name: targetPage
                        value: string
                      - name: targetFlow
                        value: string
                      - name: dataStoreConnections
                        value:
                          - - name: dataStoreType
                              value: string
                            - name: dataStore
                              value: string
              - name: textResponses
                value:
                  - - name: text
                      value:
                        - string
                    - name: allowPlaybackInterruption
                      value: boolean
              - name: status
                value:
                  - name: code
                    value: integer
                  - name: message
                    value: string
                  - name: details
                    value:
                      - object
    - name: creationTime
      value: string
    - name: lastTestResult
      value:
        - name: name
          value: string
        - name: environment
          value: string
        - name: conversationTurns
          value:
            - []
        - name: testResult
          value: string
        - name: testTime
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>test_cases</code> resource.

```sql
/*+ update */
UPDATE google.dialogflow.test_cases
SET 
name = '{{ name }}',
tags = '{{ tags }}',
displayName = '{{ displayName }}',
notes = '{{ notes }}',
testConfig = '{{ testConfig }}',
testCaseConversationTurns = '{{ testCaseConversationTurns }}',
lastTestResult = '{{ lastTestResult }}'
WHERE 
agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND testCasesId = '{{ testCasesId }}';
```

## `DELETE` example

Deletes the specified <code>test_cases</code> resource.

```sql
/*+ delete */
DELETE FROM google.dialogflow.test_cases
WHERE agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
