
---
title: suggestion_deny_list_entries
hide_title: false
hide_table_of_contents: false
keywords:
  - suggestion_deny_list_entries
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

Creates, updates, deletes or gets an <code>suggestion_deny_list_entry</code> resource or lists <code>suggestion_deny_list_entries</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>suggestion_deny_list_entries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.suggestion_deny_list_entries" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_data_stores_suggestion_deny_list_entries_import" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Imports all SuggestionDenyListEntry for a DataStore. |
| <CopyableCode code="projects_locations_collections_data_stores_suggestion_deny_list_entries_purge" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Permanently deletes all SuggestionDenyListEntry for a DataStore. |
| <CopyableCode code="projects_locations_data_stores_suggestion_deny_list_entries_import" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Imports all SuggestionDenyListEntry for a DataStore. |
| <CopyableCode code="projects_locations_data_stores_suggestion_deny_list_entries_purge" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Permanently deletes all SuggestionDenyListEntry for a DataStore. |
