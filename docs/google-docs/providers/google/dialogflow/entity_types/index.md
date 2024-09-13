
---
title: entity_types
hide_title: false
hide_table_of_contents: false
keywords:
  - entity_types
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

Creates, updates, deletes or gets an <code>entity_type</code> resource or lists <code>entity_types</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entity_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.entity_types" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Required. The unique identifier of the session entity type. Format: `projects//locations//agents//sessions//entityTypes/` or `projects//locations//agents//environments//sessions//entityTypes/`. If `Environment ID` is not specified, we assume default 'draft' environment. |
| <CopyableCode code="entities" /> | `array` | Required. The collection of entities to override or supplement the custom entity type. |
| <CopyableCode code="entityOverrideMode" /> | `string` | Required. Indicates whether the additional data should override or supplement the custom entity type definition. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_entity_types_get" /> | `SELECT` | <CopyableCode code="agentsId, entityTypesId, locationsId, projectsId" /> | Retrieves the specified entity type. |
| <CopyableCode code="projects_locations_agents_entity_types_list" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Returns the list of all entity types in the specified agent. |
| <CopyableCode code="projects_locations_agents_environments_sessions_entity_types_get" /> | `SELECT` | <CopyableCode code="agentsId, entityTypesId, environmentsId, locationsId, projectsId, sessionsId" /> | Retrieves the specified session entity type. |
| <CopyableCode code="projects_locations_agents_environments_sessions_entity_types_list" /> | `SELECT` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId, sessionsId" /> | Returns the list of all session entity types in the specified session. |
| <CopyableCode code="projects_locations_agents_sessions_entity_types_get" /> | `SELECT` | <CopyableCode code="agentsId, entityTypesId, locationsId, projectsId, sessionsId" /> | Retrieves the specified session entity type. |
| <CopyableCode code="projects_locations_agents_sessions_entity_types_list" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId, sessionsId" /> | Returns the list of all session entity types in the specified session. |
| <CopyableCode code="projects_locations_agents_entity_types_create" /> | `INSERT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Creates an entity type in the specified agent. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_environments_sessions_entity_types_create" /> | `INSERT` | <CopyableCode code="agentsId, environmentsId, locationsId, projectsId, sessionsId" /> | Creates a session entity type. |
| <CopyableCode code="projects_locations_agents_sessions_entity_types_create" /> | `INSERT` | <CopyableCode code="agentsId, locationsId, projectsId, sessionsId" /> | Creates a session entity type. |
| <CopyableCode code="projects_locations_agents_entity_types_delete" /> | `DELETE` | <CopyableCode code="agentsId, entityTypesId, locationsId, projectsId" /> | Deletes the specified entity type. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_environments_sessions_entity_types_delete" /> | `DELETE` | <CopyableCode code="agentsId, entityTypesId, environmentsId, locationsId, projectsId, sessionsId" /> | Deletes the specified session entity type. |
| <CopyableCode code="projects_locations_agents_sessions_entity_types_delete" /> | `DELETE` | <CopyableCode code="agentsId, entityTypesId, locationsId, projectsId, sessionsId" /> | Deletes the specified session entity type. |
| <CopyableCode code="projects_locations_agents_entity_types_patch" /> | `UPDATE` | <CopyableCode code="agentsId, entityTypesId, locationsId, projectsId" /> | Updates the specified entity type. Note: You should always train a flow prior to sending it queries. See the [training documentation](https://cloud.google.com/dialogflow/cx/docs/concept/training). |
| <CopyableCode code="projects_locations_agents_environments_sessions_entity_types_patch" /> | `UPDATE` | <CopyableCode code="agentsId, entityTypesId, environmentsId, locationsId, projectsId, sessionsId" /> | Updates the specified session entity type. |
| <CopyableCode code="projects_locations_agents_sessions_entity_types_patch" /> | `UPDATE` | <CopyableCode code="agentsId, entityTypesId, locationsId, projectsId, sessionsId" /> | Updates the specified session entity type. |
| <CopyableCode code="projects_locations_agents_entity_types_export" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Exports the selected entity types. |
| <CopyableCode code="projects_locations_agents_entity_types_import" /> | `EXEC` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Imports the specified entitytypes into the agent. |

## `SELECT` examples

Returns the list of all entity types in the specified agent.

```sql
SELECT
name,
entities,
entityOverrideMode
FROM google.dialogflow.entity_types
WHERE agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>entity_types</code> resource.

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
INSERT INTO google.dialogflow.entity_types (
agentsId,
locationsId,
projectsId,
name,
displayName,
kind,
autoExpansionMode,
entities,
excludedPhrases,
enableFuzzyExtraction,
redact
)
SELECT 
'{{ agentsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ kind }}',
'{{ autoExpansionMode }}',
'{{ entities }}',
'{{ excludedPhrases }}',
true|false,
true|false
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
      - name: kind
        value: '{{ kind }}'
      - name: autoExpansionMode
        value: '{{ autoExpansionMode }}'
      - name: entities
        value: '{{ entities }}'
      - name: excludedPhrases
        value: '{{ excludedPhrases }}'
      - name: enableFuzzyExtraction
        value: '{{ enableFuzzyExtraction }}'
      - name: redact
        value: '{{ redact }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a entity_type only if the necessary resources are available.

```sql
UPDATE google.dialogflow.entity_types
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
kind = '{{ kind }}',
autoExpansionMode = '{{ autoExpansionMode }}',
entities = '{{ entities }}',
excludedPhrases = '{{ excludedPhrases }}',
enableFuzzyExtraction = true|false,
redact = true|false
WHERE 
agentsId = '{{ agentsId }}'
AND entityTypesId = '{{ entityTypesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified entity_type resource.

```sql
DELETE FROM google.dialogflow.entity_types
WHERE agentsId = '{{ agentsId }}'
AND entityTypesId = '{{ entityTypesId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
