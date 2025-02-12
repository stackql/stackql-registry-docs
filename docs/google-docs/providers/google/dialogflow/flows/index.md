---
title: flows
hide_title: false
hide_table_of_contents: false
keywords:
  - flows
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

Creates, updates, deletes, gets or lists a <code>flows</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.flows" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique identifier of the flow. Format: `projects//locations//agents//flows/`. |
| <CopyableCode code="description" /> | `string` | The description of the flow. The maximum length is 500 characters. If exceeded, the request is rejected. |
| <CopyableCode code="advancedSettings" /> | `object` | Hierarchical advanced settings for agent/flow/page/fulfillment/parameter. Settings exposed at lower level overrides the settings exposed at higher level. Overriding occurs at the sub-setting level. For example, the playback_interruption_settings at fulfillment level only overrides the playback_interruption_settings at the agent level, leaving other settings at the agent level unchanged. DTMF settings does not override each other. DTMF settings set at different levels define DTMF detections running in parallel. Hierarchy: Agent->Flow->Page->Fulfillment/Parameter. |
| <CopyableCode code="displayName" /> | `string` | Required. The human-readable name of the flow. |
| <CopyableCode code="eventHandlers" /> | `array` | A flow's event handlers serve two purposes: * They are responsible for handling events (e.g. no match, webhook errors) in the flow. * They are inherited by every page's event handlers, which can be used to handle common events regardless of the current page. Event handlers defined in the page have higher priority than those defined in the flow. Unlike transition_routes, these handlers are evaluated on a first-match basis. The first one that matches the event get executed, with the rest being ignored. |
| <CopyableCode code="knowledgeConnectorSettings" /> | `object` | The Knowledge Connector settings for this page or flow. This includes information such as the attached Knowledge Bases, and the way to execute fulfillment. |
| <CopyableCode code="locked" /> | `boolean` | Indicates whether the flow is locked for changes. If the flow is locked, modifications to the flow will be rejected. |
| <CopyableCode code="multiLanguageSettings" /> | `object` | Settings for multi-lingual agents. |
| <CopyableCode code="nluSettings" /> | `object` | Settings related to NLU. |
| <CopyableCode code="transitionRouteGroups" /> | `array` | A flow's transition route group serve two purposes: * They are responsible for matching the user's first utterances in the flow. * They are inherited by every page's transition route groups. Transition route groups defined in the page have higher priority than those defined in the flow. Format: `projects//locations//agents//flows//transitionRouteGroups/` or `projects//locations//agents//transitionRouteGroups/` for agent-level groups. |
| <CopyableCode code="transitionRoutes" /> | `array` | A flow's transition routes serve two purposes: * They are responsible for matching the user's first utterances in the flow. * They are inherited by every page's transition routes and can support use cases such as the user saying "help" or "can I talk to a human?", which can be handled in a common way regardless of the current page. Transition routes defined in the page have higher priority than those defined in the flow. TransitionRoutes are evalauted in the following order: * TransitionRoutes with intent specified. * TransitionRoutes with only condition specified. TransitionRoutes with intent specified are inherited by pages in the flow. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_flows_get" /> | `SELECT` | <CopyableCode code="agentsId, flowsId, locationsId, projectsId" /> | Retrieves the specified flow. |
| <CopyableCode code="projects_locations_agents_flows_list" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Returns the list of all flows in the specified agent. |
| <CopyableCode code="projects_locations_agents_flows_create" /> | `INSERT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Creates a flow in the specified agent. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_flows_delete" /> | `DELETE` | <CopyableCode code="agentsId, flowsId, locationsId, projectsId" /> | Deletes a specified flow. |
| <CopyableCode code="projects_locations_agents_flows_patch" /> | `UPDATE` | <CopyableCode code="agentsId, flowsId, locationsId, projectsId" /> | Updates the specified flow. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_flows_export" /> | `EXEC` | <CopyableCode code="agentsId, flowsId, locationsId, projectsId" /> | Exports the specified flow to a binary file. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: ExportFlowResponse Note that resources (e.g. intents, entities, webhooks) that the flow references will also be exported. |
| <CopyableCode code="projects_locations_agents_flows_import" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Imports the specified flow to the specified agent from a binary file. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: ImportFlowResponse Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_flows_train" /> | `EXEC` | <CopyableCode code="agentsId, flowsId, locationsId, projectsId" /> | Trains the specified flow. Note that only the flow in 'draft' environment is trained. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_flows_validate" /> | `EXEC` | <CopyableCode code="agentsId, flowsId, locationsId, projectsId" /> | Validates the specified flow and creates or updates validation results. Please call this API after the training is completed to get the complete validation results. |

## `SELECT` examples

Returns the list of all flows in the specified agent.

```sql
SELECT
name,
description,
advancedSettings,
displayName,
eventHandlers,
knowledgeConnectorSettings,
locked,
multiLanguageSettings,
nluSettings,
transitionRouteGroups,
transitionRoutes
FROM google.dialogflow.flows
WHERE agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>flows</code> resource.

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
INSERT INTO google.dialogflow.flows (
agentsId,
locationsId,
projectsId,
name,
displayName,
description,
transitionRoutes,
eventHandlers,
transitionRouteGroups,
nluSettings,
advancedSettings,
knowledgeConnectorSettings,
multiLanguageSettings,
locked
)
SELECT 
'{{ agentsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ transitionRoutes }}',
'{{ eventHandlers }}',
'{{ transitionRouteGroups }}',
'{{ nluSettings }}',
'{{ advancedSettings }}',
'{{ knowledgeConnectorSettings }}',
'{{ multiLanguageSettings }}',
{{ locked }}
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: name
      value: string
    - name: displayName
      value: string
    - name: description
      value: string
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
          - name: triggerFulfillment
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
    - name: transitionRouteGroups
      value:
        - string
    - name: nluSettings
      value:
        - name: modelType
          value: string
        - name: classificationThreshold
          value: number
        - name: modelTrainingMode
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
    - name: multiLanguageSettings
      value:
        - name: enableMultiLanguageDetection
          value: boolean
        - name: supportedResponseLanguageCodes
          value:
            - string
    - name: locked
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>flows</code> resource.

```sql
/*+ update */
UPDATE google.dialogflow.flows
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
transitionRoutes = '{{ transitionRoutes }}',
eventHandlers = '{{ eventHandlers }}',
transitionRouteGroups = '{{ transitionRouteGroups }}',
nluSettings = '{{ nluSettings }}',
advancedSettings = '{{ advancedSettings }}',
knowledgeConnectorSettings = '{{ knowledgeConnectorSettings }}',
multiLanguageSettings = '{{ multiLanguageSettings }}',
locked = true|false
WHERE 
agentsId = '{{ agentsId }}'
AND flowsId = '{{ flowsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>flows</code> resource.

```sql
/*+ delete */
DELETE FROM google.dialogflow.flows
WHERE agentsId = '{{ agentsId }}'
AND flowsId = '{{ flowsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
