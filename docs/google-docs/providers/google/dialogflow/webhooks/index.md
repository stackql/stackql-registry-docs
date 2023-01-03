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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webhooks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.webhooks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique identifier of the webhook. Required for the Webhooks.UpdateWebhook method. Webhooks.CreateWebhook populates the name automatically. Format: `projects//locations//agents//webhooks/`. |
| `genericWebService` | `object` | Represents configuration for a generic web service. |
| `serviceDirectory` | `object` | Represents configuration for a [Service Directory](https://cloud.google.com/service-directory) service. |
| `timeout` | `string` | Webhook execution timeout. Execution is considered failed if Dialogflow doesn't receive a response from webhook at the end of the timeout period. Defaults to 5 seconds, maximum allowed timeout is 30 seconds. |
| `disabled` | `boolean` | Indicates whether the webhook is disabled. |
| `displayName` | `string` | Required. The human-readable name of the webhook, unique within the agent. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_webhooks_get` | `SELECT` | `agentsId, locationsId, projectsId, webhooksId` | Retrieves the specified webhook. |
| `projects_locations_agents_webhooks_list` | `SELECT` | `agentsId, locationsId, projectsId` | Returns the list of all webhooks in the specified agent. |
| `projects_locations_agents_webhooks_create` | `INSERT` | `agentsId, locationsId, projectsId` | Creates a webhook in the specified agent. |
| `projects_locations_agents_webhooks_delete` | `DELETE` | `agentsId, locationsId, projectsId, webhooksId` | Deletes the specified webhook. |
| `projects_locations_agents_webhooks_patch` | `EXEC` | `agentsId, locationsId, projectsId, webhooksId` | Updates the specified webhook. |
