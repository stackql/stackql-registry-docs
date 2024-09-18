---
title: conversations
hide_title: false
hide_table_of_contents: false
keywords:
  - conversations
  - discoveryengine
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

Creates, updates, deletes, gets or lists a <code>conversations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>conversations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.conversations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Fully qualified name `projects/{project}/locations/global/collections/{collection}/dataStore/*/conversations/*` or `projects/{project}/locations/global/collections/{collection}/engines/*/conversations/*`. |
| <CopyableCode code="endTime" /> | `string` | Output only. The time the conversation finished. |
| <CopyableCode code="messages" /> | `array` | Conversation messages. |
| <CopyableCode code="startTime" /> | `string` | Output only. The time the conversation started. |
| <CopyableCode code="state" /> | `string` | The state of the Conversation. |
| <CopyableCode code="userPseudoId" /> | `string` | A unique identifier for tracking users. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_data_stores_conversations_get" /> | `SELECT` | <CopyableCode code="collectionsId, conversationsId, dataStoresId, locationsId, projectsId" /> | Gets a Conversation. |
| <CopyableCode code="projects_locations_collections_data_stores_conversations_list" /> | `SELECT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Lists all Conversations by their parent DataStore. |
| <CopyableCode code="projects_locations_collections_engines_conversations_get" /> | `SELECT` | <CopyableCode code="collectionsId, conversationsId, enginesId, locationsId, projectsId" /> | Gets a Conversation. |
| <CopyableCode code="projects_locations_collections_engines_conversations_list" /> | `SELECT` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId" /> | Lists all Conversations by their parent DataStore. |
| <CopyableCode code="projects_locations_data_stores_conversations_get" /> | `SELECT` | <CopyableCode code="conversationsId, dataStoresId, locationsId, projectsId" /> | Gets a Conversation. |
| <CopyableCode code="projects_locations_data_stores_conversations_list" /> | `SELECT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Lists all Conversations by their parent DataStore. |
| <CopyableCode code="projects_locations_collections_data_stores_conversations_create" /> | `INSERT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Creates a Conversation. If the Conversation to create already exists, an ALREADY_EXISTS error is returned. |
| <CopyableCode code="projects_locations_collections_engines_conversations_create" /> | `INSERT` | <CopyableCode code="collectionsId, enginesId, locationsId, projectsId" /> | Creates a Conversation. If the Conversation to create already exists, an ALREADY_EXISTS error is returned. |
| <CopyableCode code="projects_locations_data_stores_conversations_create" /> | `INSERT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Creates a Conversation. If the Conversation to create already exists, an ALREADY_EXISTS error is returned. |
| <CopyableCode code="projects_locations_collections_data_stores_conversations_delete" /> | `DELETE` | <CopyableCode code="collectionsId, conversationsId, dataStoresId, locationsId, projectsId" /> | Deletes a Conversation. If the Conversation to delete does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_collections_engines_conversations_delete" /> | `DELETE` | <CopyableCode code="collectionsId, conversationsId, enginesId, locationsId, projectsId" /> | Deletes a Conversation. If the Conversation to delete does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_data_stores_conversations_delete" /> | `DELETE` | <CopyableCode code="conversationsId, dataStoresId, locationsId, projectsId" /> | Deletes a Conversation. If the Conversation to delete does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_collections_data_stores_conversations_patch" /> | `UPDATE` | <CopyableCode code="collectionsId, conversationsId, dataStoresId, locationsId, projectsId" /> | Updates a Conversation. Conversation action type cannot be changed. If the Conversation to update does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_collections_engines_conversations_patch" /> | `UPDATE` | <CopyableCode code="collectionsId, conversationsId, enginesId, locationsId, projectsId" /> | Updates a Conversation. Conversation action type cannot be changed. If the Conversation to update does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_data_stores_conversations_patch" /> | `UPDATE` | <CopyableCode code="conversationsId, dataStoresId, locationsId, projectsId" /> | Updates a Conversation. Conversation action type cannot be changed. If the Conversation to update does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_collections_data_stores_conversations_converse" /> | `EXEC` | <CopyableCode code="collectionsId, conversationsId, dataStoresId, locationsId, projectsId" /> | Converses a conversation. |
| <CopyableCode code="projects_locations_collections_engines_conversations_converse" /> | `EXEC` | <CopyableCode code="collectionsId, conversationsId, enginesId, locationsId, projectsId" /> | Converses a conversation. |
| <CopyableCode code="projects_locations_data_stores_conversations_converse" /> | `EXEC` | <CopyableCode code="conversationsId, dataStoresId, locationsId, projectsId" /> | Converses a conversation. |

## `SELECT` examples

Lists all Conversations by their parent DataStore.

```sql
SELECT
name,
endTime,
messages,
startTime,
state,
userPseudoId
FROM google.discoveryengine.conversations
WHERE dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}'; 
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>conversations</code> resource.

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
INSERT INTO google.discoveryengine.conversations (
dataStoresId,
locationsId,
projectsId,
name,
state,
userPseudoId,
messages
)
SELECT 
'{{ dataStoresId }}',
'{{ locationsId }}',
'{{ projectsId }}',
'{{ name }}',
'{{ state }}',
'{{ userPseudoId }}',
'{{ messages }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
name: string
state: string
userPseudoId: string
messages:
  - userInput:
      input: string
      context:
        contextDocuments:
          - type: string
        activeDocument: string
    reply:
      summary:
        summaryText: string
        summarySkippedReasons:
          - type: string
            enumDescriptions: string
            enum: string
        safetyAttributes:
          categories:
            - type: string
          scores:
            - type: string
              format: string
        summaryWithMetadata:
          summary: string
          citationMetadata:
            citations:
              - startIndex: string
                endIndex: string
                sources:
                  - referenceIndex: string
          references:
            - title: string
              document: string
              uri: string
              chunkContents:
                - content: string
                  pageIdentifier: string
    createTime: string
startTime: string
endTime: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>conversations</code> resource.

```sql
/*+ update */
UPDATE google.discoveryengine.conversations
SET 
name = '{{ name }}',
state = '{{ state }}',
userPseudoId = '{{ userPseudoId }}',
messages = '{{ messages }}'
WHERE 
conversationsId = '{{ conversationsId }}'
AND dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```

## `DELETE` example

Deletes the specified <code>conversations</code> resource.

```sql
/*+ delete */
DELETE FROM google.discoveryengine.conversations
WHERE conversationsId = '{{ conversationsId }}'
AND dataStoresId = '{{ dataStoresId }}'
AND locationsId = '{{ locationsId }}'
AND projectsId = '{{ projectsId }}';
```
