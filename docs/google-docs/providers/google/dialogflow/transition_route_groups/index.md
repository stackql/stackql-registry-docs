---
title: transition_route_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - transition_route_groups
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

Creates, updates, deletes or gets an <code>transition_route_group</code> resource or lists <code>transition_route_groups</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>transition_route_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.transition_route_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique identifier of the transition route group. TransitionRouteGroups.CreateTransitionRouteGroup populates the name automatically. Format: `projects//locations//agents//flows//transitionRouteGroups/` . |
| <CopyableCode code="displayName" /> | `string` | Required. The human-readable name of the transition route group, unique within the flow. The display name can be no longer than 30 characters. |
| <CopyableCode code="transitionRoutes" /> | `array` | Transition routes associated with the TransitionRouteGroup. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_flows_transition_route_groups_get" /> | `SELECT` | <CopyableCode code="agentsId, flowsId, locationsId, projectsId, transitionRouteGroupsId" /> | Retrieves the specified TransitionRouteGroup. |
| <CopyableCode code="projects_locations_agents_flows_transition_route_groups_list" /> | `SELECT` | <CopyableCode code="agentsId, flowsId, locationsId, projectsId" /> | Returns the list of all transition route groups in the specified flow. |
| <CopyableCode code="projects_locations_agents_transition_route_groups_get" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId, transitionRouteGroupsId" /> | Retrieves the specified TransitionRouteGroup. |
| <CopyableCode code="projects_locations_agents_transition_route_groups_list" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Returns the list of all transition route groups in the specified flow. |
| <CopyableCode code="projects_locations_agents_flows_transition_route_groups_create" /> | `INSERT` | <CopyableCode code="agentsId, flowsId, locationsId, projectsId" /> | Creates an TransitionRouteGroup in the specified flow. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_transition_route_groups_create" /> | `INSERT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Creates an TransitionRouteGroup in the specified flow. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_flows_transition_route_groups_delete" /> | `DELETE` | <CopyableCode code="agentsId, flowsId, locationsId, projectsId, transitionRouteGroupsId" /> | Deletes the specified TransitionRouteGroup. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_transition_route_groups_delete" /> | `DELETE` | <CopyableCode code="agentsId, locationsId, projectsId, transitionRouteGroupsId" /> | Deletes the specified TransitionRouteGroup. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_flows_transition_route_groups_patch" /> | `UPDATE` | <CopyableCode code="agentsId, flowsId, locationsId, projectsId, transitionRouteGroupsId" /> | Updates the specified TransitionRouteGroup. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_transition_route_groups_patch" /> | `UPDATE` | <CopyableCode code="agentsId, locationsId, projectsId, transitionRouteGroupsId" /> | Updates the specified TransitionRouteGroup. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |

## `SELECT` examples

Returns the list of all transition route groups in the specified flow.

```sql
SELECT
name,
displayName,
transitionRoutes
FROM google.dialogflow.transition_route_groups
WHERE agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>transition_route_groups</code> resource.

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
INSERT INTO google.dialogflow.transition_route_groups (
agentsId,
locationsId,
projectsId,
name,
displayName,
transitionRoutes
)
SELECT 
'{{ agentsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ transitionRoutes }}'
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
      - name: transitionRoutes
        value: '{{ transitionRoutes }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a transition_route_group only if the necessary resources are available.

```sql
UPDATE google.dialogflow.transition_route_groups
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
transitionRoutes = '{{ transitionRoutes }}'
WHERE 
agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND transitionRouteGroupsId = '{{ transitionRouteGroupsId }}';
```

## `DELETE` example

Deletes the specified transition_route_group resource.

```sql
DELETE FROM google.dialogflow.transition_route_groups
WHERE agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'
AND transitionRouteGroupsId = '{{ transitionRouteGroupsId }}';
```
