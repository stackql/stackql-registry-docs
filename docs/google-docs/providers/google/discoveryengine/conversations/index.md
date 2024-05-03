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




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>conversations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.conversations" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. Fully qualified name `project/*/locations/global/collections/&#123;collection&#125;/dataStore/*/conversations/*` |
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
| <CopyableCode code="projects_locations_data_stores_conversations_get" /> | `SELECT` | <CopyableCode code="conversationsId, dataStoresId, locationsId, projectsId" /> | Gets a Conversation. |
| <CopyableCode code="projects_locations_data_stores_conversations_list" /> | `SELECT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Lists all Conversations by their parent DataStore. |
| <CopyableCode code="projects_locations_collections_data_stores_conversations_create" /> | `INSERT` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Creates a Conversation. If the Conversation to create already exists, an ALREADY_EXISTS error is returned. |
| <CopyableCode code="projects_locations_data_stores_conversations_create" /> | `INSERT` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Creates a Conversation. If the Conversation to create already exists, an ALREADY_EXISTS error is returned. |
| <CopyableCode code="projects_locations_collections_data_stores_conversations_delete" /> | `DELETE` | <CopyableCode code="collectionsId, conversationsId, dataStoresId, locationsId, projectsId" /> | Deletes a Conversation. If the Conversation to delete does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_data_stores_conversations_delete" /> | `DELETE` | <CopyableCode code="conversationsId, dataStoresId, locationsId, projectsId" /> | Deletes a Conversation. If the Conversation to delete does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="_projects_locations_collections_data_stores_conversations_list" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Lists all Conversations by their parent DataStore. |
| <CopyableCode code="_projects_locations_data_stores_conversations_list" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Lists all Conversations by their parent DataStore. |
| <CopyableCode code="projects_locations_collections_data_stores_conversations_converse" /> | `EXEC` | <CopyableCode code="collectionsId, conversationsId, dataStoresId, locationsId, projectsId" /> | Converses a conversation. |
| <CopyableCode code="projects_locations_collections_data_stores_conversations_patch" /> | `EXEC` | <CopyableCode code="collectionsId, conversationsId, dataStoresId, locationsId, projectsId" /> | Updates a Conversation. Conversation action type cannot be changed. If the Conversation to update does not exist, a NOT_FOUND error is returned. |
| <CopyableCode code="projects_locations_data_stores_conversations_converse" /> | `EXEC` | <CopyableCode code="conversationsId, dataStoresId, locationsId, projectsId" /> | Converses a conversation. |
| <CopyableCode code="projects_locations_data_stores_conversations_patch" /> | `EXEC` | <CopyableCode code="conversationsId, dataStoresId, locationsId, projectsId" /> | Updates a Conversation. Conversation action type cannot be changed. If the Conversation to update does not exist, a NOT_FOUND error is returned. |
