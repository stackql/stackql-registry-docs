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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flows</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.flows</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique identifier of the flow. Format: `projects//locations//agents//flows/`. |
| `description` | `string` | The description of the flow. The maximum length is 500 characters. If exceeded, the request is rejected. |
| `nluSettings` | `object` | Settings related to NLU. |
| `transitionRouteGroups` | `array` | A flow's transition route group serve two purposes: * They are responsible for matching the user's first utterances in the flow. * They are inherited by every page's transition route groups. Transition route groups defined in the page have higher priority than those defined in the flow. Format:`projects//locations//agents//flows//transitionRouteGroups/`. |
| `transitionRoutes` | `array` | A flow's transition routes serve two purposes: * They are responsible for matching the user's first utterances in the flow. * They are inherited by every page's transition routes and can support use cases such as the user saying "help" or "can I talk to a human?", which can be handled in a common way regardless of the current page. Transition routes defined in the page have higher priority than those defined in the flow. TransitionRoutes are evalauted in the following order: * TransitionRoutes with intent specified. * TransitionRoutes with only condition specified. TransitionRoutes with intent specified are inherited by pages in the flow. |
| `displayName` | `string` | Required. The human-readable name of the flow. |
| `eventHandlers` | `array` | A flow's event handlers serve two purposes: * They are responsible for handling events (e.g. no match, webhook errors) in the flow. * They are inherited by every page's event handlers, which can be used to handle common events regardless of the current page. Event handlers defined in the page have higher priority than those defined in the flow. Unlike transition_routes, these handlers are evaluated on a first-match basis. The first one that matches the event get executed, with the rest being ignored. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_flows_get` | `SELECT` | `agentsId, flowsId, locationsId, projectsId` | Retrieves the specified flow. |
| `projects_locations_agents_flows_list` | `SELECT` | `agentsId, locationsId, projectsId` | Returns the list of all flows in the specified agent. |
| `projects_locations_agents_flows_create` | `INSERT` | `agentsId, locationsId, projectsId` | Creates a flow in the specified agent. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_flows_delete` | `DELETE` | `agentsId, flowsId, locationsId, projectsId` | Deletes a specified flow. |
| `projects_locations_agents_flows_export` | `EXEC` | `agentsId, flowsId, locationsId, projectsId` | Exports the specified flow to a binary file. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: ExportFlowResponse Note that resources (e.g. intents, entities, webhooks) that the flow references will also be exported. |
| `projects_locations_agents_flows_import` | `EXEC` | `agentsId, locationsId, projectsId` | Imports the specified flow to the specified agent from a binary file. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: ImportFlowResponse Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_flows_patch` | `EXEC` | `agentsId, flowsId, locationsId, projectsId` | Updates the specified flow. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_flows_train` | `EXEC` | `agentsId, flowsId, locationsId, projectsId` | Trains the specified flow. Note that only the flow in 'draft' environment is trained. This method is a [long-running operation](https://cloud.google.com/dialogflow/cx/docs/how/long-running-operation). The returned `Operation` type has the following method-specific fields: - `metadata`: An empty [Struct message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct) - `response`: An [Empty message](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty) Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_flows_validate` | `EXEC` | `agentsId, flowsId, locationsId, projectsId` | Validates the specified flow and creates or updates validation results. Please call this API after the training is completed to get the complete validation results. |
