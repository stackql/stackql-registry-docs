---
title: views
hide_title: false
hide_table_of_contents: false
keywords:
  - views
  - logging
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
<tr><td><b>Name</b></td><td><code>views</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.views</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | If there might be more results than appear in this response, then nextPageToken is included. To get the next set of results, call the same method again using the value of nextPageToken as pageToken. |
| `views` | `array` | A list of views. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billing_accounts_locations_buckets_views_get` | `SELECT` | `billingAccountsId, bucketsId, locationsId, viewsId` | Gets a view on a log bucket.. |
| `billing_accounts_locations_buckets_views_list` | `SELECT` | `billingAccountsId, bucketsId, locationsId` | Lists views on a log bucket. |
| `folders_locations_buckets_views_get` | `SELECT` | `bucketsId, foldersId, locationsId, viewsId` | Gets a view on a log bucket.. |
| `folders_locations_buckets_views_list` | `SELECT` | `bucketsId, foldersId, locationsId` | Lists views on a log bucket. |
| `locations_buckets_views_list` | `SELECT` | `parent` | Lists views on a log bucket. |
| `organizations_locations_buckets_views_get` | `SELECT` | `bucketsId, locationsId, organizationsId, viewsId` | Gets a view on a log bucket.. |
| `organizations_locations_buckets_views_list` | `SELECT` | `bucketsId, locationsId, organizationsId` | Lists views on a log bucket. |
| `projects_locations_buckets_views_get` | `SELECT` | `bucketsId, locationsId, projectsId, viewsId` | Gets a view on a log bucket.. |
| `projects_locations_buckets_views_list` | `SELECT` | `bucketsId, locationsId, projectsId` | Lists views on a log bucket. |
| `billing_accounts_locations_buckets_views_create` | `INSERT` | `billingAccountsId, bucketsId, locationsId` | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| `folders_locations_buckets_views_create` | `INSERT` | `bucketsId, foldersId, locationsId` | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| `locations_buckets_views_create` | `INSERT` | `parent` | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| `organizations_locations_buckets_views_create` | `INSERT` | `bucketsId, locationsId, organizationsId` | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| `projects_locations_buckets_views_create` | `INSERT` | `bucketsId, locationsId, projectsId` | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| `billing_accounts_locations_buckets_views_delete` | `DELETE` | `billingAccountsId, bucketsId, locationsId, viewsId` | Deletes a view on a log bucket. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes. |
| `folders_locations_buckets_views_delete` | `DELETE` | `bucketsId, foldersId, locationsId, viewsId` | Deletes a view on a log bucket. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes. |
| `organizations_locations_buckets_views_delete` | `DELETE` | `bucketsId, locationsId, organizationsId, viewsId` | Deletes a view on a log bucket. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes. |
| `projects_locations_buckets_views_delete` | `DELETE` | `bucketsId, locationsId, projectsId, viewsId` | Deletes a view on a log bucket. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes. |
| `billing_accounts_locations_buckets_views_patch` | `EXEC` | `billingAccountsId, bucketsId, locationsId, viewsId` | Updates a view on a log bucket. This method replaces the following fields in the existing view with values from the new view: filter. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes. |
| `folders_locations_buckets_views_patch` | `EXEC` | `bucketsId, foldersId, locationsId, viewsId` | Updates a view on a log bucket. This method replaces the following fields in the existing view with values from the new view: filter. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes. |
| `organizations_locations_buckets_views_patch` | `EXEC` | `bucketsId, locationsId, organizationsId, viewsId` | Updates a view on a log bucket. This method replaces the following fields in the existing view with values from the new view: filter. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes. |
| `projects_locations_buckets_views_patch` | `EXEC` | `bucketsId, locationsId, projectsId, viewsId` | Updates a view on a log bucket. This method replaces the following fields in the existing view with values from the new view: filter. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes. |
