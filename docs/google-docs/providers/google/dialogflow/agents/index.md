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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.agents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique identifier of the agent. Required for the Agents.UpdateAgent method. Agents.CreateAgent populates the name automatically. Format: `projects//locations//agents/`. |
| `description` | `string` | The description of the agent. The maximum length is 500 characters. If exceeded, the request is rejected. |
| `defaultLanguageCode` | `string` | Required. Immutable. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. This field cannot be set by the Agents.UpdateAgent method. |
| `avatarUri` | `string` | The URI of the agent's avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration. |
| `advancedSettings` | `object` | Hierarchical advanced settings for agent/flow/page/fulfillment/parameter. Settings exposed at lower level overrides the settings exposed at higher level. Overriding occurs at the sub-setting level. For example, the playback_interruption_settings at fulfillment level only overrides the playback_interruption_settings at the agent level, leaving other settings at the agent level unchanged. DTMF settings does not override each other. DTMF settings set at different levels define DTMF detections running in parallel. Hierarchy: Agent-&gt;Flow-&gt;Page-&gt;Fulfillment/Parameter. |
| `locked` | `boolean` | Indicates whether the agent is locked for changes. If the agent is locked, modifications to the agent will be rejected except for RestoreAgent. |
| `enableStackdriverLogging` | `boolean` | Indicates if stackdriver logging is enabled for the agent. Please use agent.advanced_settings instead. |
| `enableSpellCorrection` | `boolean` | Indicates if automatic spell correction is enabled in detect intent requests. |
| `speechToTextSettings` | `object` | Settings related to speech recognition. |
| `supportedLanguageCodes` | `array` | The list of all languages supported by the agent (except for the `default_language_code`). |
| `timeZone` | `string` | Required. The time zone of the agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris. |
| `startFlow` | `string` | Immutable. Name of the start flow in this agent. A start flow will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects//locations//agents//flows/`. |
| `displayName` | `string` | Required. The human-readable name of the agent, unique within the location. |
| `securitySettings` | `string` | Name of the SecuritySettings reference for the agent. Format: `projects//locations//securitySettings/`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_get` | `SELECT` | `agentsId, locationsId, projectsId` | Retrieves the specified agent. |
| `projects_locations_agents_list` | `SELECT` | `locationsId, projectsId` | Returns the list of all agents in the specified location. |
| `projects_locations_agents_create` | `INSERT` | `locationsId, projectsId` | Creates an agent in the specified location. Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_delete` | `DELETE` | `agentsId, locationsId, projectsId` | Deletes the specified agent. |
| `projects_locations_agents_export` | `EXEC` | `agentsId, locationsId, projectsId` | Exports the specified agent to a binary file. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: ExportAgentResponse |
| `projects_locations_agents_patch` | `EXEC` | `agentsId, locationsId, projectsId` | Updates the specified agent. Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_restore` | `EXEC` | `agentsId, locationsId, projectsId` | Restores the specified agent from a binary file. Replaces the current agent with a new one. Note that all existing resources in agent (e.g. intents, entity types, flows) will be removed. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) Note: You should always train flows prior to sending them queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_validate` | `EXEC` | `agentsId, locationsId, projectsId` | Validates the specified agent and creates or updates validation results. The agent in draft version is validated. Please call this API after the training is completed to get the complete validation results. |
