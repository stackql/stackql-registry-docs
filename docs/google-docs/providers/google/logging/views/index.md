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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | The resource name of the view.For example:projects/my-project/locations/global/buckets/my-bucket/views/my-view |
| `description` | `string` | Describes this view. |
| `updateTime` | `string` | Output only. The last update timestamp of the view. |
| `createTime` | `string` | Output only. The creation timestamp of the view. |
| `filter` | `string` | Filter that restricts which log entries in a bucket are visible in this view.Filters are restricted to be a logical AND of ==/!= of any of the following: originating project/folder/organization/billing account. resource type log idFor example:SOURCE("projects/myproject") AND resource.type = "gce_instance" AND LOG_ID("stdout") |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billingAccounts_locations_buckets_views_get` | `SELECT` | `billingAccountsId, bucketsId, locationsId, viewsId` | Gets a view on a log bucket.. |
| `billingAccounts_locations_buckets_views_list` | `SELECT` | `billingAccountsId, bucketsId, locationsId` | Lists views on a log bucket. |
| `folders_locations_buckets_views_get` | `SELECT` | `bucketsId, foldersId, locationsId, viewsId` | Gets a view on a log bucket.. |
| `folders_locations_buckets_views_list` | `SELECT` | `bucketsId, foldersId, locationsId` | Lists views on a log bucket. |
| `locations_buckets_views_list` | `SELECT` | `parent` | Lists views on a log bucket. |
| `organizations_locations_buckets_views_get` | `SELECT` | `bucketsId, locationsId, organizationsId, viewsId` | Gets a view on a log bucket.. |
| `organizations_locations_buckets_views_list` | `SELECT` | `bucketsId, locationsId, organizationsId` | Lists views on a log bucket. |
| `projects_locations_buckets_views_get` | `SELECT` | `bucketsId, locationsId, projectsId, viewsId` | Gets a view on a log bucket.. |
| `projects_locations_buckets_views_list` | `SELECT` | `bucketsId, locationsId, projectsId` | Lists views on a log bucket. |
| `billingAccounts_locations_buckets_views_create` | `INSERT` | `billingAccountsId, bucketsId, locationsId` | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| `folders_locations_buckets_views_create` | `INSERT` | `bucketsId, foldersId, locationsId` | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| `locations_buckets_views_create` | `INSERT` | `parent` | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| `organizations_locations_buckets_views_create` | `INSERT` | `bucketsId, locationsId, organizationsId` | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| `projects_locations_buckets_views_create` | `INSERT` | `bucketsId, locationsId, projectsId` | Creates a view over log entries in a log bucket. A bucket may contain a maximum of 30 views. |
| `billingAccounts_locations_buckets_views_delete` | `DELETE` | `billingAccountsId, bucketsId, locationsId, viewsId` | Deletes a view on a log bucket. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes. |
| `folders_locations_buckets_views_delete` | `DELETE` | `bucketsId, foldersId, locationsId, viewsId` | Deletes a view on a log bucket. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes. |
| `organizations_locations_buckets_views_delete` | `DELETE` | `bucketsId, locationsId, organizationsId, viewsId` | Deletes a view on a log bucket. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes. |
| `projects_locations_buckets_views_delete` | `DELETE` | `bucketsId, locationsId, projectsId, viewsId` | Deletes a view on a log bucket. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can delete the view. If this occurs, please try again in a few minutes. |
| `billingAccounts_locations_buckets_views_patch` | `EXEC` | `billingAccountsId, bucketsId, locationsId, viewsId` | Updates a view on a log bucket. This method replaces the following fields in the existing view with values from the new view: filter. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes. |
| `folders_locations_buckets_views_patch` | `EXEC` | `bucketsId, foldersId, locationsId, viewsId` | Updates a view on a log bucket. This method replaces the following fields in the existing view with values from the new view: filter. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes. |
| `organizations_locations_buckets_views_patch` | `EXEC` | `bucketsId, locationsId, organizationsId, viewsId` | Updates a view on a log bucket. This method replaces the following fields in the existing view with values from the new view: filter. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes. |
| `projects_locations_buckets_views_patch` | `EXEC` | `bucketsId, locationsId, projectsId, viewsId` | Updates a view on a log bucket. This method replaces the following fields in the existing view with values from the new view: filter. If an UNAVAILABLE error is returned, this indicates that system is not in a state where it can update the view. If this occurs, please try again in a few minutes. |
