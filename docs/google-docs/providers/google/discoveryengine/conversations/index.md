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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>conversations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.discoveryengine.conversations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. Fully qualified name `project/*/locations/global/collections/&#123;collection&#125;/dataStore/*/conversations/*` |
| `userPseudoId` | `string` | A unique identifier for tracking users. |
| `endTime` | `string` | Output only. The time the conversation finished. |
| `messages` | `array` | Conversation messages. |
| `startTime` | `string` | Output only. The time the conversation started. |
| `state` | `string` | The state of the Conversation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_collections_data_stores_conversations_get` | `SELECT` | `collectionsId, conversationsId, dataStoresId, locationsId, projectsId` | Gets a Conversation. |
| `projects_locations_collections_data_stores_conversations_list` | `SELECT` | `collectionsId, dataStoresId, locationsId, projectsId` | Lists all Conversations by their parent DataStore. |
| `projects_locations_data_stores_conversations_get` | `SELECT` | `conversationsId, dataStoresId, locationsId, projectsId` | Gets a Conversation. |
| `projects_locations_data_stores_conversations_list` | `SELECT` | `dataStoresId, locationsId, projectsId` | Lists all Conversations by their parent DataStore. |
| `projects_locations_collections_data_stores_conversations_create` | `INSERT` | `collectionsId, dataStoresId, locationsId, projectsId` | Creates a Conversation. If the Conversation to create already exists, an ALREADY_EXISTS error is returned. |
| `projects_locations_data_stores_conversations_create` | `INSERT` | `dataStoresId, locationsId, projectsId` | Creates a Conversation. If the Conversation to create already exists, an ALREADY_EXISTS error is returned. |
| `projects_locations_collections_data_stores_conversations_delete` | `DELETE` | `collectionsId, conversationsId, dataStoresId, locationsId, projectsId` | Deletes a Conversation. If the Conversation to delete does not exist, a NOT_FOUND error is returned. |
| `projects_locations_data_stores_conversations_delete` | `DELETE` | `conversationsId, dataStoresId, locationsId, projectsId` | Deletes a Conversation. If the Conversation to delete does not exist, a NOT_FOUND error is returned. |
| `_projects_locations_collections_data_stores_conversations_list` | `EXEC` | `collectionsId, dataStoresId, locationsId, projectsId` | Lists all Conversations by their parent DataStore. |
| `_projects_locations_data_stores_conversations_list` | `EXEC` | `dataStoresId, locationsId, projectsId` | Lists all Conversations by their parent DataStore. |
| `projects_locations_collections_data_stores_conversations_converse` | `EXEC` | `collectionsId, conversationsId, dataStoresId, locationsId, projectsId` | Converses a conversation. |
| `projects_locations_collections_data_stores_conversations_patch` | `EXEC` | `collectionsId, conversationsId, dataStoresId, locationsId, projectsId` | Updates a Conversation. Conversation action type cannot be changed. If the Conversation to update does not exist, a NOT_FOUND error is returned. |
| `projects_locations_data_stores_conversations_converse` | `EXEC` | `conversationsId, dataStoresId, locationsId, projectsId` | Converses a conversation. |
| `projects_locations_data_stores_conversations_patch` | `EXEC` | `conversationsId, dataStoresId, locationsId, projectsId` | Updates a Conversation. Conversation action type cannot be changed. If the Conversation to update does not exist, a NOT_FOUND error is returned. |
