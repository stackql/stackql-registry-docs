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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>page</code> resource or lists <code>pages</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pages</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.pages" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique identifier of the page. Required for the Pages.UpdatePage method. Pages.CreatePage populates the name automatically. Format: `projects//locations//agents//flows//pages/`. |
| <CopyableCode code="description" /> | `string` | The description of the page. The maximum length is 500 characters. |
| <CopyableCode code="advancedSettings" /> | `object` | Hierarchical advanced settings for agent/flow/page/fulfillment/parameter. Settings exposed at lower level overrides the settings exposed at higher level. Overriding occurs at the sub-setting level. For example, the playback_interruption_settings at fulfillment level only overrides the playback_interruption_settings at the agent level, leaving other settings at the agent level unchanged. DTMF settings does not override each other. DTMF settings set at different levels define DTMF detections running in parallel. Hierarchy: Agent->Flow->Page->Fulfillment/Parameter. |
| <CopyableCode code="displayName" /> | `string` | Required. The human-readable name of the page, unique within the flow. |
| <CopyableCode code="entryFulfillment" /> | `object` | A fulfillment can do one or more of the following actions at the same time: * Generate rich message responses. * Set parameter values. * Call the webhook. Fulfillments can be called at various stages in the Page or Form lifecycle. For example, when a DetectIntentRequest drives a session to enter a new page, the page's entry fulfillment can add a static response to the QueryResult in the returning DetectIntentResponse, call the webhook (for example, to load user data from a database), or both. |
| <CopyableCode code="eventHandlers" /> | `array` | Handlers associated with the page to handle events such as webhook errors, no match or no input. |
| <CopyableCode code="form" /> | `object` | A form is a data model that groups related parameters that can be collected from the user. The process in which the agent prompts the user and collects parameter values from the user is called form filling. A form can be added to a page. When form filling is done, the filled parameters will be written to the session. |
| <CopyableCode code="knowledgeConnectorSettings" /> | `object` | The Knowledge Connector settings for this page or flow. This includes information such as the attached Knowledge Bases, and the way to execute fulfillment. |
| <CopyableCode code="transitionRouteGroups" /> | `array` | Ordered list of `TransitionRouteGroups` added to the page. Transition route groups must be unique within a page. If the page links both flow-level transition route groups and agent-level transition route groups, the flow-level ones will have higher priority and will be put before the agent-level ones. * If multiple transition routes within a page scope refer to the same intent, then the precedence order is: page's transition route -> page's transition route group -> flow's transition routes. * If multiple transition route groups within a page contain the same intent, then the first group in the ordered list takes precedence. Format:`projects//locations//agents//flows//transitionRouteGroups/` or `projects//locations//agents//transitionRouteGroups/` for agent-level groups. |
| <CopyableCode code="transitionRoutes" /> | `array` | A list of transitions for the transition rules of this page. They route the conversation to another page in the same flow, or another flow. When we are in a certain page, the TransitionRoutes are evalauted in the following order: * TransitionRoutes defined in the page with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in flow with intent specified. * TransitionRoutes defined in the transition route groups with intent specified. * TransitionRoutes defined in the page with only condition specified. * TransitionRoutes defined in the transition route groups with only condition specified. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_flows_pages_get" /> | `SELECT` | <CopyableCode code="agentsId, flowsId, locationsId, pagesId, projectsId" /> | Retrieves the specified page. |
| <CopyableCode code="projects_locations_agents_flows_pages_list" /> | `SELECT` | <CopyableCode code="agentsId, flowsId, locationsId, projectsId" /> | Returns the list of all pages in the specified flow. |
| <CopyableCode code="projects_locations_agents_flows_pages_create" /> | `INSERT` | <CopyableCode code="agentsId, flowsId, locationsId, projectsId" /> | Creates a page in the specified flow. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_flows_pages_delete" /> | `DELETE` | <CopyableCode code="agentsId, flowsId, locationsId, pagesId, projectsId" /> | Deletes the specified page. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_flows_pages_patch" /> | `UPDATE` | <CopyableCode code="agentsId, flowsId, locationsId, pagesId, projectsId" /> | Updates the specified page. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |

## `SELECT` examples

Returns the list of all pages in the specified flow.

```sql
SELECT
name,
description,
advancedSettings,
displayName,
entryFulfillment,
eventHandlers,
form,
knowledgeConnectorSettings,
transitionRouteGroups,
transitionRoutes
FROM google.dialogflow.pages
WHERE agentsId = '{{ agentsId }}'
AND flowsId = '{{ flowsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>pages</code> resource.

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
INSERT INTO google.dialogflow.pages (
agentsId,
flowsId,
locationsId,
projectsId,
name,
displayName,
description,
entryFulfillment,
form,
transitionRouteGroups,
transitionRoutes,
eventHandlers,
advancedSettings,
knowledgeConnectorSettings
)
SELECT 
'{{ agentsId }}',
'{{ flowsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ description }}',
'{{ entryFulfillment }}',
'{{ form }}',
'{{ transitionRouteGroups }}',
'{{ transitionRoutes }}',
'{{ eventHandlers }}',
'{{ advancedSettings }}',
'{{ knowledgeConnectorSettings }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
resources:
  - name: instance
    props:
      - name: name
        value: '{{ name }}'
      - name: displayName
        value: '{{ displayName }}'
      - name: description
        value: '{{ description }}'
      - name: entryFulfillment
        value: '{{ entryFulfillment }}'
      - name: form
        value: '{{ form }}'
      - name: transitionRouteGroups
        value: '{{ transitionRouteGroups }}'
      - name: transitionRoutes
        value: '{{ transitionRoutes }}'
      - name: eventHandlers
        value: '{{ eventHandlers }}'
      - name: advancedSettings
        value: '{{ advancedSettings }}'
      - name: knowledgeConnectorSettings
        value: '{{ knowledgeConnectorSettings }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a page only if the necessary resources are available.

```sql
UPDATE google.dialogflow.pages
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
description = '{{ description }}',
entryFulfillment = '{{ entryFulfillment }}',
form = '{{ form }}',
transitionRouteGroups = '{{ transitionRouteGroups }}',
transitionRoutes = '{{ transitionRoutes }}',
eventHandlers = '{{ eventHandlers }}',
advancedSettings = '{{ advancedSettings }}',
knowledgeConnectorSettings = '{{ knowledgeConnectorSettings }}'
WHERE 
agentsId = '{{ agentsId }}'
AND flowsId = '{{ flowsId }}'
AND locationsId = '{{ locationsId }}'
AND pagesId = '{{ pagesId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified page resource.

```sql
DELETE FROM google.dialogflow.pages
WHERE agentsId = '{{ agentsId }}'
AND flowsId = '{{ flowsId }}'
AND locationsId = '{{ locationsId }}'
AND pagesId = '{{ pagesId }}'
AND projectsId = '{{ projectsId }}';
```
