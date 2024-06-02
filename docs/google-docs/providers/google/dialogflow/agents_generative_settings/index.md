---
title: agents_generative_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - agents_generative_settings
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
<tr><td><b>Name</b></td><td><code>agents_generative_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dialogflow.agents_generative_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Format: `projects//locations//agents//generativeSettings`. |
| <CopyableCode code="fallbackSettings" /> | `object` | Settings for Generative Fallback. |
| <CopyableCode code="generativeSafetySettings" /> | `object` | Settings for Generative Safety. |
| <CopyableCode code="knowledgeConnectorSettings" /> | `object` | Settings for knowledge connector. These parameters are used for LLM prompt like "You are . You are a helpful and verbose at , . Your task is to help humans on ". |
| <CopyableCode code="languageCode" /> | `string` | Language for this settings. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_get_generative_settings" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Gets the generative settings for the agent. |
| <CopyableCode code="projects_locations_agents_update_generative_settings" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Updates the generative settings for the agent. |
