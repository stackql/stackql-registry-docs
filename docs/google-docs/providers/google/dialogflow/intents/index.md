---
title: intents
hide_title: false
hide_table_of_contents: false
keywords:
  - intents
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
<tr><td><b>Name</b></td><td><code>intents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.intents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique identifier of the intent. Required for the Intents.UpdateIntent method. Intents.CreateIntent populates the name automatically. Format: `projects//locations//agents//intents/`. |
| <CopyableCode code="description" /> | `string` | Human readable description for better understanding an intent like its scope, content, result etc. Maximum character limit: 140 characters. |
| <CopyableCode code="displayName" /> | `string` | Required. The human-readable name of the intent, unique within the agent. |
| <CopyableCode code="isFallback" /> | `boolean` | Indicates whether this is a fallback intent. Currently only default fallback intent is allowed in the agent, which is added upon agent creation. Adding training phrases to fallback intent is useful in the case of requests that are mistakenly matched, since training phrases assigned to fallback intents act as negative examples that triggers no-match event. |
| <CopyableCode code="labels" /> | `object` | The key/value metadata to label an intent. Labels can contain lowercase letters, digits and the symbols '-' and '_'. International characters are allowed, including letters from unicase alphabets. Keys must start with a letter. Keys and values can be no longer than 63 characters and no more than 128 bytes. Prefix "sys-" is reserved for Dialogflow defined labels. Currently allowed Dialogflow defined labels include: * sys-head * sys-contextual The above labels do not require value. "sys-head" means the intent is a head intent. "sys.contextual" means the intent is a contextual intent. |
| <CopyableCode code="parameters" /> | `array` | The collection of parameters associated with the intent. |
| <CopyableCode code="priority" /> | `integer` | The priority of this intent. Higher numbers represent higher priorities. - If the supplied value is unspecified or 0, the service translates the value to 500,000, which corresponds to the `Normal` priority in the console. - If the supplied value is negative, the intent is ignored in runtime detect intent requests. |
| <CopyableCode code="trainingPhrases" /> | `array` | The collection of training phrases the agent is trained on to identify the intent. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_intents_get" /> | `SELECT` | <CopyableCode code="agentsId, intentsId, locationsId, projectsId" /> | Retrieves the specified intent. |
| <CopyableCode code="projects_locations_agents_intents_list" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Returns the list of all intents in the specified agent. |
| <CopyableCode code="projects_locations_agents_intents_create" /> | `INSERT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Creates an intent in the specified agent. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_intents_delete" /> | `DELETE` | <CopyableCode code="agentsId, intentsId, locationsId, projectsId" /> | Deletes the specified intent. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="_projects_locations_agents_intents_list" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Returns the list of all intents in the specified agent. |
| <CopyableCode code="projects_locations_agents_intents_patch" /> | `EXEC` | <CopyableCode code="agentsId, intentsId, locationsId, projectsId" /> | Updates the specified intent. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
