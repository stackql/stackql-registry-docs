---
title: user_events
hide_title: false
hide_table_of_contents: false
keywords:
  - user_events
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

Creates, updates, deletes or gets an <code>user_event</code> resource or lists <code>user_events</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.discoveryengine.user_events" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_collections_data_stores_user_events_collect" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Writes a single user event from the browser. This uses a GET request to due to browser restriction of POST-ing to a third-party domain. This method is used only by the Discovery Engine API JavaScript pixel and Google Tag Manager. Users should not call this method directly. |
| <CopyableCode code="projects_locations_collections_data_stores_user_events_import" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Bulk import of user events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events. Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully inserted. Operation.metadata is of type ImportMetadata. |
| <CopyableCode code="projects_locations_collections_data_stores_user_events_purge" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Deletes permanently all user events specified by the filter provided. Depending on the number of events specified by the filter, this operation could take hours or days to complete. To test a filter, use the list command first. |
| <CopyableCode code="projects_locations_collections_data_stores_user_events_write" /> | `EXEC` | <CopyableCode code="collectionsId, dataStoresId, locationsId, projectsId" /> | Writes a single user event. |
| <CopyableCode code="projects_locations_data_stores_user_events_collect" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Writes a single user event from the browser. This uses a GET request to due to browser restriction of POST-ing to a third-party domain. This method is used only by the Discovery Engine API JavaScript pixel and Google Tag Manager. Users should not call this method directly. |
| <CopyableCode code="projects_locations_data_stores_user_events_import" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Bulk import of user events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events. Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully inserted. Operation.metadata is of type ImportMetadata. |
| <CopyableCode code="projects_locations_data_stores_user_events_purge" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Deletes permanently all user events specified by the filter provided. Depending on the number of events specified by the filter, this operation could take hours or days to complete. To test a filter, use the list command first. |
| <CopyableCode code="projects_locations_data_stores_user_events_write" /> | `EXEC` | <CopyableCode code="dataStoresId, locationsId, projectsId" /> | Writes a single user event. |
| <CopyableCode code="projects_locations_user_events_collect" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Writes a single user event from the browser. This uses a GET request to due to browser restriction of POST-ing to a third-party domain. This method is used only by the Discovery Engine API JavaScript pixel and Google Tag Manager. Users should not call this method directly. |
| <CopyableCode code="projects_locations_user_events_write" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Writes a single user event. |
