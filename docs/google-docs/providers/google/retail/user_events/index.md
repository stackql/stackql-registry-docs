---
title: user_events
hide_title: false
hide_table_of_contents: false
keywords:
  - user_events
  - retail
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
<tr><td><b>Name</b></td><td><code>user_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.retail.user_events" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="projects_locations_catalogs_user_events_collect" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Writes a single user event from the browser. This uses a GET request to due to browser restriction of POST-ing to a 3rd party domain. This method is used only by the Retail API JavaScript pixel and Google Tag Manager. Users should not call this method directly. |
| <CopyableCode code="projects_locations_catalogs_user_events_import" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Bulk import of User events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events. `Operation.response` is of type `ImportResponse`. Note that it is possible for a subset of the items to be successfully inserted. `Operation.metadata` is of type `ImportMetadata`. |
| <CopyableCode code="projects_locations_catalogs_user_events_purge" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Deletes permanently all user events specified by the filter provided. Depending on the number of events specified by the filter, this operation could take hours or days to complete. To test a filter, use the list command first. |
| <CopyableCode code="projects_locations_catalogs_user_events_rejoin" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Starts a user-event rejoin operation with latest product catalog. Events are not annotated with detailed product information for products that are missing from the catalog when the user event is ingested. These events are stored as unjoined events with limited usage on training and serving. You can use this method to start a join operation on specified events with the latest version of product catalog. You can also use this method to correct events joined with the wrong product catalog. A rejoin operation can take hours or days to complete. |
| <CopyableCode code="projects_locations_catalogs_user_events_write" /> | `EXEC` | <CopyableCode code="catalogsId, locationsId, projectsId" /> | Writes a single user event. |
