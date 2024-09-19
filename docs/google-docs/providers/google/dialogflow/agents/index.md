---
title: agents
hide_title: false
hide_table_of_contents: false
keywords:
  - agents
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

Creates, updates, deletes, gets or lists a <code>agents</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.agents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique identifier of the agent. Required for the Agents.UpdateAgent method. Agents.CreateAgent populates the name automatically. Format: `projects//locations//agents/`. |
| <CopyableCode code="description" /> | `string` | The description of the agent. The maximum length is 500 characters. If exceeded, the request is rejected. |
| <CopyableCode code="advancedSettings" /> | `object` | Hierarchical advanced settings for agent/flow/page/fulfillment/parameter. Settings exposed at lower level overrides the settings exposed at higher level. Overriding occurs at the sub-setting level. For example, the playback_interruption_settings at fulfillment level only overrides the playback_interruption_settings at the agent level, leaving other settings at the agent level unchanged. DTMF settings does not override each other. DTMF settings set at different levels define DTMF detections running in parallel. Hierarchy: Agent->Flow->Page->Fulfillment/Parameter. |
| <CopyableCode code="answerFeedbackSettings" /> | `object` | Settings for answer feedback collection. |
| <CopyableCode code="avatarUri" /> | `string` | The URI of the agent's avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration. |
| <CopyableCode code="clientCertificateSettings" /> | `object` | Settings for custom client certificates. |
| <CopyableCode code="defaultLanguageCode" /> | `string` | Required. Immutable. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. This field cannot be set by the Agents.UpdateAgent method. |
| <CopyableCode code="displayName" /> | `string` | Required. The human-readable name of the agent, unique within the location. |
| <CopyableCode code="enableMultiLanguageTraining" /> | `boolean` | Optional. Enable training multi-lingual models for this agent. These models will be trained on all the languages supported by the agent. |
| <CopyableCode code="enableSpellCorrection" /> | `boolean` | Indicates if automatic spell correction is enabled in detect intent requests. |
| <CopyableCode code="enableStackdriverLogging" /> | `boolean` | Indicates if stackdriver logging is enabled for the agent. Please use agent.advanced_settings instead. |
| <CopyableCode code="genAppBuilderSettings" /> | `object` | Settings for Gen App Builder. |
| <CopyableCode code="gitIntegrationSettings" /> | `object` | Settings for connecting to Git repository for an agent. |
| <CopyableCode code="locked" /> | `boolean` | Indicates whether the agent is locked for changes. If the agent is locked, modifications to the agent will be rejected except for RestoreAgent. |
| <CopyableCode code="personalizationSettings" /> | `object` | Settings for end user personalization. |
| <CopyableCode code="securitySettings" /> | `string` | Name of the SecuritySettings reference for the agent. Format: `projects//locations//securitySettings/`. |
| <CopyableCode code="speechToTextSettings" /> | `object` | Settings related to speech recognition. |
| <CopyableCode code="startFlow" /> | `string` | Immutable. Name of the start flow in this agent. A start flow will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects//locations//agents//flows/`. |
| <CopyableCode code="supportedLanguageCodes" /> | `array` | The list of all languages supported by the agent (except for the `default_language_code`). |
| <CopyableCode code="textToSpeechSettings" /> | `object` | Settings related to speech synthesizing. |
| <CopyableCode code="timeZone" /> | `string` | Required. The time zone of the agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_get" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Retrieves the specified agent. |
| <CopyableCode code="projects_locations_agents_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Returns the list of all agents in the specified location. |
| <CopyableCode code="projects_locations_agents_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates an agent in the specified location. Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_delete" /> | `DELETE` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Deletes the specified agent. |
| <CopyableCode code="projects_locations_agents_patch" /> | `UPDATE` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Updates the specified agent. Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_export" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Exports the specified agent to a binary file. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: ExportAgentResponse |
| <CopyableCode code="projects_locations_agents_restore" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Restores the specified agent from a binary file. Replaces the current agent with a new one. Note that all existing resources in agent (e.g. intents, entity types, flows) will be removed. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_validate" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Validates the specified agent and creates or updates validation results. The agent in draft version is validated. Please call this API after the training is completed to get the complete validation results. |

## `SELECT` examples

Returns the list of all agents in the specified location.

```sql
SELECT
name,
description,
advancedSettings,
answerFeedbackSettings,
avatarUri,
clientCertificateSettings,
defaultLanguageCode,
displayName,
enableMultiLanguageTraining,
enableSpellCorrection,
enableStackdriverLogging,
genAppBuilderSettings,
gitIntegrationSettings,
locked,
personalizationSettings,
securitySettings,
speechToTextSettings,
startFlow,
supportedLanguageCodes,
textToSpeechSettings,
timeZone
FROM google.dialogflow.agents
WHERE locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>agents</code> resource.

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
INSERT INTO google.dialogflow.agents (
locationsId,
projectsId,
name,
displayName,
defaultLanguageCode,
supportedLanguageCodes,
timeZone,
description,
avatarUri,
speechToTextSettings,
startFlow,
securitySettings,
enableStackdriverLogging,
enableSpellCorrection,
enableMultiLanguageTraining,
locked,
advancedSettings,
gitIntegrationSettings,
textToSpeechSettings,
genAppBuilderSettings,
answerFeedbackSettings,
personalizationSettings,
clientCertificateSettings
)
SELECT 
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ defaultLanguageCode }}',
'{{ supportedLanguageCodes }}',
'{{ timeZone }}',
'{{ description }}',
'{{ avatarUri }}',
'{{ speechToTextSettings }}',
'{{ startFlow }}',
'{{ securitySettings }}',
{{ enableStackdriverLogging }},
{{ enableSpellCorrection }},
{{ enableMultiLanguageTraining }},
{{ locked }},
'{{ advancedSettings }}',
'{{ gitIntegrationSettings }}',
'{{ textToSpeechSettings }}',
'{{ genAppBuilderSettings }}',
'{{ answerFeedbackSettings }}',
'{{ personalizationSettings }}',
'{{ clientCertificateSettings }}'
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
    - name: defaultLanguageCode
      value: string
    - name: supportedLanguageCodes
      value:
        - string
    - name: timeZone
      value: string
    - name: description
      value: string
    - name: avatarUri
      value: string
    - name: speechToTextSettings
      value:
        - name: enableSpeechAdaptation
          value: boolean
    - name: startFlow
      value: string
    - name: securitySettings
      value: string
    - name: enableStackdriverLogging
      value: boolean
    - name: enableSpellCorrection
      value: boolean
    - name: enableMultiLanguageTraining
      value: boolean
    - name: locked
      value: boolean
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
    - name: gitIntegrationSettings
      value:
        - name: githubSettings
          value:
            - name: displayName
              value: string
            - name: repositoryUri
              value: string
            - name: trackingBranch
              value: string
            - name: accessToken
              value: string
            - name: branches
              value:
                - string
    - name: textToSpeechSettings
      value:
        - name: synthesizeSpeechConfigs
          value: object
    - name: genAppBuilderSettings
      value:
        - name: engine
          value: string
    - name: answerFeedbackSettings
      value:
        - name: enableAnswerFeedback
          value: boolean
    - name: personalizationSettings
      value:
        - name: defaultEndUserMetadata
          value: object
    - name: clientCertificateSettings
      value:
        - name: sslCertificate
          value: string
        - name: privateKey
          value: string
        - name: passphrase
          value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>agents</code> resource.

```sql
/*+ update */
UPDATE google.dialogflow.agents
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
defaultLanguageCode = '{{ defaultLanguageCode }}',
supportedLanguageCodes = '{{ supportedLanguageCodes }}',
timeZone = '{{ timeZone }}',
description = '{{ description }}',
avatarUri = '{{ avatarUri }}',
speechToTextSettings = '{{ speechToTextSettings }}',
startFlow = '{{ startFlow }}',
securitySettings = '{{ securitySettings }}',
enableStackdriverLogging = true|false,
enableSpellCorrection = true|false,
enableMultiLanguageTraining = true|false,
locked = true|false,
advancedSettings = '{{ advancedSettings }}',
gitIntegrationSettings = '{{ gitIntegrationSettings }}',
textToSpeechSettings = '{{ textToSpeechSettings }}',
genAppBuilderSettings = '{{ genAppBuilderSettings }}',
answerFeedbackSettings = '{{ answerFeedbackSettings }}',
personalizationSettings = '{{ personalizationSettings }}',
clientCertificateSettings = '{{ clientCertificateSettings }}'
WHERE 
agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>agents</code> resource.

```sql
/*+ delete */
DELETE FROM google.dialogflow.agents
WHERE agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
