---
title: listings
hide_title: false
hide_table_of_contents: false
keywords:
  - listings
  - analyticshub
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
<tr><td><b>Name</b></td><td><code>listings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.analyticshub.listings</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_dataExchanges_listings_get` | `SELECT` | `dataExchangesId, listingsId, locationsId, projectsId` | Gets the details of a listing. |
| `projects_locations_dataExchanges_listings_list` | `SELECT` | `dataExchangesId, locationsId, projectsId` | Lists all listings in a given project and location. |
| `projects_locations_dataExchanges_listings_create` | `INSERT` | `dataExchangesId, locationsId, projectsId` | Creates a new listing. |
| `projects_locations_dataExchanges_listings_delete` | `DELETE` | `dataExchangesId, listingsId, locationsId, projectsId` | Deletes a listing. |
| `projects_locations_dataExchanges_listings_patch` | `EXEC` | `dataExchangesId, listingsId, locationsId, projectsId` | Updates an existing listing. |
| `projects_locations_dataExchanges_listings_subscribe` | `EXEC` | `dataExchangesId, listingsId, locationsId, projectsId` | Subscribes to a listing. Currently, with Analytics Hub, you can create listings that reference only BigQuery datasets. Upon subscription to a listing for a BigQuery dataset, Analytics Hub creates a linked dataset in the subscriber's project. |
