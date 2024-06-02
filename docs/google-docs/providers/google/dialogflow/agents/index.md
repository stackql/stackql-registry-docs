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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dialogflow.agents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique identifier of the agent. Required for the Agents.UpdateAgent method. Agents.CreateAgent populates the name automatically. Format: `projects//locations//agents/`. |
| <CopyableCode code="description" /> | `string` | The description of the agent. The maximum length is 500 characters. If exceeded, the request is rejected. |
| <CopyableCode code="advancedSettings" /> | `object` | Hierarchical advanced settings for agent/flow/page/fulfillment/parameter. Settings exposed at lower level overrides the settings exposed at higher level. Overriding occurs at the sub-setting level. For example, the playback_interruption_settings at fulfillment level only overrides the playback_interruption_settings at the agent level, leaving other settings at the agent level unchanged. DTMF settings does not override each other. DTMF settings set at different levels define DTMF detections running in parallel. Hierarchy: Agent-&gt;Flow-&gt;Page-&gt;Fulfillment/Parameter. |
| <CopyableCode code="answerFeedbackSettings" /> | `object` | Settings for answer feedback collection. |
| <CopyableCode code="avatarUri" /> | `string` | The URI of the agent's avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration. |
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
| <CopyableCode code="_projects_locations_agents_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Returns the list of all agents in the specified location. |
| <CopyableCode code="projects_locations_agents_export" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Exports the specified agent to a binary file. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: ExportAgentResponse |
| <CopyableCode code="projects_locations_agents_patch" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Updates the specified agent. Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_restore" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Restores the specified agent from a binary file. Replaces the current agent with a new one. Note that all existing resources in agent (e.g. intents, entity types, flows) will be removed. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_validate" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Validates the specified agent and creates or updates validation results. The agent in draft version is validated. Please call this API after the training is completed to get the complete validation results. |
