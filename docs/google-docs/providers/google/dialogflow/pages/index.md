---
title: pages
hide_title: false
hide_table_of_contents: false
keywords:
  - pages
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
<tr><td><b>Name</b></td><td><code>pages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dialogflow.pages</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique identifier of the page. Required for the Pages.UpdatePage method. Pages.CreatePage populates the name automatically. Format: `projects//locations//agents//flows//pages/`. |
| `eventHandlers` | `array` | Handlers associated with the page to handle events such as webhook errors, no match or no input. |
| `form` | `object` | A form is a data model that groups related parameters that can be collected from the user. The process in which the agent prompts the user and collects parameter values from the user is called form filling. A form can be added to a page. When form filling is done, the filled parameters will be written to the session. |
| `transitionRouteGroups` | `array` | Ordered list of `TransitionRouteGroups` associated with the page. Transition route groups must be unique within a page. * If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -&gt; page's transition route group -&gt; flow's transition routes. * If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence. Format:`projects//locations//agents//flows//transitionRouteGroups/`. |
| `transitionRoutes` | `array` | A list of transitions for the transition rules of this page. They route the conversation to another page in the same flow, or another flow. When we are in a certain page, the TransitionRoutes are evalauted in the following order: * TransitionRoutes defined in the page with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in flow with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in the page with only condition specified. * TransitionRoutes defined in the transition route groups with only condition specified. |
| `displayName` | `string` | Required. The human-readable name of the page, unique within the flow. |
| `entryFulfillment` | `object` | A fulfillment can do one or more of the following actions at the same time: * Generate rich message responses. * Set parameter values. * Call the webhook. Fulfillments can be called at various stages in the Page or Form lifecycle. For example, when a DetectIntentRequest drives a session to enter a new page, the page's entry fulfillment can add a static response to the QueryResult in the returning DetectIntentResponse, call the webhook (for example, to load user data from a database), or both. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_agents_flows_pages_get` | `SELECT` | `agentsId, flowsId, locationsId, pagesId, projectsId` | Retrieves the specified page. |
| `projects_locations_agents_flows_pages_list` | `SELECT` | `agentsId, flowsId, locationsId, projectsId` | Returns the list of all pages in the specified flow. |
| `projects_locations_agents_flows_pages_create` | `INSERT` | `agentsId, flowsId, locationsId, projectsId` | Creates a page in the specified flow. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_flows_pages_delete` | `DELETE` | `agentsId, flowsId, locationsId, pagesId, projectsId` | Deletes the specified page. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| `projects_locations_agents_flows_pages_patch` | `EXEC` | `agentsId, flowsId, locationsId, pagesId, projectsId` | Updates the specified page. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
