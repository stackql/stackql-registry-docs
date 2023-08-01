---
title: links
hide_title: false
hide_table_of_contents: false
keywords:
  - links
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
<tr><td><b>Name</b></td><td><code>links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.logging.links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the link. The name can have up to 100 characters. A valid link id (at the end of the link name) must only have alphanumeric characters and underscores within it. "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" For example:`projects/my-project/locations/global/buckets/my-bucket/links/my_link |
| `description` | `string` | Describes this link.The maximum length of the description is 8000 characters. |
| `bigqueryDataset` | `object` | Describes a BigQuery dataset that was created by a link. |
| `createTime` | `string` | Output only. The creation timestamp of the link. |
| `lifecycleState` | `string` | Output only. The resource lifecycle state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `billing_accounts_locations_buckets_links_get` | `SELECT` | `billingAccountsId, bucketsId, linksId, locationsId` | Gets a link. |
| `billing_accounts_locations_buckets_links_list` | `SELECT` | `billingAccountsId, bucketsId, locationsId` | Lists links. |
| `folders_locations_buckets_links_get` | `SELECT` | `bucketsId, foldersId, linksId, locationsId` | Gets a link. |
| `folders_locations_buckets_links_list` | `SELECT` | `bucketsId, foldersId, locationsId` | Lists links. |
| `locations_buckets_links_list` | `SELECT` | `parent` | Lists links. |
| `organizations_locations_buckets_links_get` | `SELECT` | `bucketsId, linksId, locationsId, organizationsId` | Gets a link. |
| `organizations_locations_buckets_links_list` | `SELECT` | `bucketsId, locationsId, organizationsId` | Lists links. |
| `projects_locations_buckets_links_get` | `SELECT` | `bucketsId, linksId, locationsId, projectsId` | Gets a link. |
| `projects_locations_buckets_links_list` | `SELECT` | `bucketsId, locationsId, projectsId` | Lists links. |
| `billing_accounts_locations_buckets_links_create` | `INSERT` | `billingAccountsId, bucketsId, locationsId` | Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link. |
| `folders_locations_buckets_links_create` | `INSERT` | `bucketsId, foldersId, locationsId` | Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link. |
| `locations_buckets_links_create` | `INSERT` | `parent` | Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link. |
| `organizations_locations_buckets_links_create` | `INSERT` | `bucketsId, locationsId, organizationsId` | Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link. |
| `projects_locations_buckets_links_create` | `INSERT` | `bucketsId, locationsId, projectsId` | Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link. |
| `billing_accounts_locations_buckets_links_delete` | `DELETE` | `billingAccountsId, bucketsId, linksId, locationsId` | Deletes a link. This will also delete the corresponding BigQuery linked dataset. |
| `folders_locations_buckets_links_delete` | `DELETE` | `bucketsId, foldersId, linksId, locationsId` | Deletes a link. This will also delete the corresponding BigQuery linked dataset. |
| `organizations_locations_buckets_links_delete` | `DELETE` | `bucketsId, linksId, locationsId, organizationsId` | Deletes a link. This will also delete the corresponding BigQuery linked dataset. |
| `projects_locations_buckets_links_delete` | `DELETE` | `bucketsId, linksId, locationsId, projectsId` | Deletes a link. This will also delete the corresponding BigQuery linked dataset. |
