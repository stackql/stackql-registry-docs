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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>user_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.retail.user_events</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_catalogs_userEvents_collect` | `EXEC` | `catalogsId, locationsId, projectsId` | Writes a single user event from the browser. This uses a GET request to due to browser restriction of POST-ing to a 3rd party domain. This method is used only by the Retail API JavaScript pixel and Google Tag Manager. Users should not call this method directly. |
| `projects_locations_catalogs_userEvents_import` | `EXEC` | `catalogsId, locationsId, projectsId` | Bulk import of User events. Request processing might be synchronous. Events that already exist are skipped. Use this method for backfilling historical user events. Operation.response is of type ImportResponse. Note that it is possible for a subset of the items to be successfully inserted. Operation.metadata is of type ImportMetadata. |
| `projects_locations_catalogs_userEvents_purge` | `EXEC` | `catalogsId, locationsId, projectsId` | Deletes permanently all user events specified by the filter provided. Depending on the number of events specified by the filter, this operation could take hours or days to complete. To test a filter, use the list command first. |
| `projects_locations_catalogs_userEvents_rejoin` | `EXEC` | `catalogsId, locationsId, projectsId` | Starts a user event rejoin operation with latest product catalog. Events will not be annotated with detailed product information if product is missing from the catalog at the time the user event is ingested, and these events are stored as unjoined events with a limited usage on training and serving. This method can be used to start a join operation on specified events with latest version of product catalog. It can also be used to correct events joined with the wrong product catalog. A rejoin operation can take hours or days to complete. |
| `projects_locations_catalogs_userEvents_write` | `EXEC` | `catalogsId, locationsId, projectsId` | Writes a single user event. |
