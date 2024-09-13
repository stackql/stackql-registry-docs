---
title: generators
hide_title: false
hide_table_of_contents: false
keywords:
  - generators
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

Creates, updates, deletes or gets an <code>generator</code> resource or lists <code>generators</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>generators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.dialogflow.generators" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The unique identifier of the generator. Must be set for the Generators.UpdateGenerator method. Generators.CreateGenerate populates the name automatically. Format: `projects//locations//agents//generators/`. |
| <CopyableCode code="displayName" /> | `string` | Required. The human-readable name of the generator, unique within the agent. The prompt contains pre-defined parameters such as $conversation, $last-user-utterance, etc. populated by Dialogflow. It can also contain custom placeholders which will be resolved during fulfillment. |
| <CopyableCode code="placeholders" /> | `array` | Optional. List of custom placeholders in the prompt text. |
| <CopyableCode code="promptText" /> | `object` | Text input which can be used for prompt or banned phrases. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_agents_generators_get" /> | `SELECT` | <CopyableCode code="agentsId, generatorsId, locationsId, projectsId" /> | Retrieves the specified generator. |
| <CopyableCode code="projects_locations_agents_generators_list" /> | `SELECT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Returns the list of all generators in the specified agent. |
| <CopyableCode code="projects_locations_agents_generators_create" /> | `INSERT` | <CopyableCode code="agentsId, locationsId, projectsId" /> | Creates a generator in the specified agent. |
| <CopyableCode code="projects_locations_agents_generators_delete" /> | `DELETE` | <CopyableCode code="agentsId, generatorsId, locationsId, projectsId" /> | Deletes the specified generators. |
| <CopyableCode code="projects_locations_agents_generators_patch" /> | `UPDATE` | <CopyableCode code="agentsId, generatorsId, locationsId, projectsId" /> | Update the specified generator. |

## `SELECT` examples

Returns the list of all generators in the specified agent.

```sql
SELECT
name,
displayName,
placeholders,
promptText
FROM google.dialogflow.generators
WHERE agentsId = '{{ agentsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>generators</code> resource.

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
INSERT INTO google.dialogflow.generators (
agentsId,
locationsId,
projectsId,
name,
displayName,
promptText,
placeholders
)
SELECT 
'{{ agentsId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ displayName }}',
'{{ promptText }}',
'{{ placeholders }}'
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
      - name: promptText
        value: '{{ promptText }}'
      - name: placeholders
        value: '{{ placeholders }}'

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a generator only if the necessary resources are available.

```sql
UPDATE google.dialogflow.generators
SET 
name = '{{ name }}',
displayName = '{{ displayName }}',
promptText = '{{ promptText }}',
placeholders = '{{ placeholders }}'
WHERE 
agentsId = '{{ agentsId }}'
AND generatorsId = '{{ generatorsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified generator resource.

```sql
DELETE FROM google.dialogflow.generators
WHERE agentsId = '{{ agentsId }}'
AND generatorsId = '{{ generatorsId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
