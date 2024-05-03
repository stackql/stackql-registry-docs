---
title: webhooks
hide_title: false
hide_table_of_contents: false
keywords:
  - webhooks
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
<tr><td><b>Name</b></td><td><code>webhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.webhooks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique identifier of the webhook. Required for the Webhooks.UpdateWebhook method. Webhooks.CreateWebhook populates the name automatically. Format: `projects//locations//agents//webhooks/`. |
| <CopyableCode code="disabled" /> | `boolean` | Indicates whether the webhook is disabled. |
| <CopyableCode code="displayName" /> | `string` | Required. The human-readable name of the webhook, unique within the agent. |
| <CopyableCode code="genericWebService" /> | `object` | Represents configuration for a generic web service. |
| <CopyableCode code="serviceDirectory" /> | `object` | Represents configuration for a [Service Directory](https://cloud.google.com/service-directory) service. |
| <CopyableCode code="timeout" /> | `string` | Webhook execution timeout. Execution is considered failed if Dialogflow doesn't receive a response from webhook at the end of the timeout period. Defaults to 5 seconds, maximum allowed timeout is 30 seconds. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_webhooks_get" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId, webhooksId" /> | Retrieves the specified webhook. |
| <CopyableCode code="projects_locations_agents_webhooks_list" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Returns the list of all webhooks in the specified agent. |
| <CopyableCode code="projects_locations_agents_webhooks_create" /> | `INSERT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Creates a webhook in the specified agent. |
| <CopyableCode code="projects_locations_agents_webhooks_delete" /> | `DELETE` | <CopyableCode code="agentsId, locationsId, projectsId, webhooksId" /> | Deletes the specified webhook. |
| <CopyableCode code="_projects_locations_agents_webhooks_list" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Returns the list of all webhooks in the specified agent. |
| <CopyableCode code="projects_locations_agents_webhooks_patch" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId, webhooksId" /> | Updates the specified webhook. |
