---
title: user_events
hide_title: false
hide_table_of_contents: false
keywords:
  - user_events
  - recommendationengine
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
<tr><td><b>Name</b></td><td><code>user_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.recommendationengine.user_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `productEventDetail` | `object` | ProductEventDetail captures user event information specific to retail products. |
| `userInfo` | `object` | Information of end users. |
| `eventDetail` | `object` | User event details shared by all recommendation types. |
| `eventSource` | `string` | Optional. This field should *not* be set when using JavaScript pixel or the Recommendations AI Tag. Defaults to `EVENT_SOURCE_UNSPECIFIED`. |
| `eventTime` | `string` | Optional. Only required for ImportUserEvents method. Timestamp of user event created. |
| `eventType` | `string` | Required. User event type. Allowed values are: * `add-to-cart` Products being added to cart. * `add-to-list` Items being added to a list (shopping list, favorites etc). * `category-page-view` Special pages such as sale or promotion pages viewed. * `checkout-start` User starting a checkout process. * `detail-page-view` Products detail page viewed. * `home-page-view` Homepage viewed. * `page-visit` Generic page visits not included in the event types above. * `purchase-complete` User finishing a purchase. * `refund` Purchased items being refunded or returned. * `remove-from-cart` Products being removed from cart. * `remove-from-list` Items being removed from a list. * `search` Product search. * `shopping-cart-page-view` User viewing a shopping cart. * `impression` List of items displayed. Used by Google Tag Manager. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_event_stores_user_events_list` | `SELECT` | `catalogsId, eventStoresId, locationsId, projectsId` | Gets a list of user events within a time range, with potential filtering. The method does not list unjoined user events. Unjoined user event definition: when a user event is ingested from Recommendations AI User Event APIs, the catalog item included in the user event is connected with the current catalog. If a catalog item of the ingested event is not in the current catalog, it could lead to degraded model quality. This is called an unjoined event. |
| `_projects_locations_catalogs_event_stores_user_events_list` | `EXEC` | `catalogsId, eventStoresId, locationsId, projectsId` | Gets a list of user events within a time range, with potential filtering. The method does not list unjoined user events. Unjoined user event definition: when a user event is ingested from Recommendations AI User Event APIs, the catalog item included in the user event is connected with the current catalog. If a catalog item of the ingested event is not in the current catalog, it could lead to degraded model quality. This is called an unjoined event. |
| `projects_locations_catalogs_event_stores_user_events_collect` | `EXEC` | `catalogsId, eventStoresId, locationsId, projectsId` | Writes a single user event from the browser. This uses a GET request to due to browser restriction of POST-ing to a 3rd party domain. This method is used only by the Recommendations AI JavaScript pixel. Users should not call this method directly. |
| `projects_locations_catalogs_event_stores_user_events_import` | `EXEC` | `catalogsId, eventStoresId, locationsId, projectsId` | Bulk import of User events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events. Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully inserted. Operation.metadata is of type ImportMetadata. |
| `projects_locations_catalogs_event_stores_user_events_purge` | `EXEC` | `catalogsId, eventStoresId, locationsId, projectsId` | Deletes permanently all user events specified by the filter provided. Depending on the number of events specified by the filter, this operation could take hours or days to complete. To test a filter, use the list command first. |
| `projects_locations_catalogs_event_stores_user_events_rejoin` | `EXEC` | `catalogsId, eventStoresId, locationsId, projectsId` | Triggers a user event rejoin operation with latest catalog data. Events will not be annotated with detailed catalog information if catalog item is missing at the time the user event is ingested, and these events are stored as unjoined events with a limited usage on training and serving. This API can be used to trigger a 'join' operation on specified events with latest version of catalog items. It can also be used to correct events joined with wrong catalog items. |
| `projects_locations_catalogs_event_stores_user_events_write` | `EXEC` | `catalogsId, eventStoresId, locationsId, projectsId` | Writes a single user event. |
