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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.logging.links" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The resource name of the link. The name can have up to 100 characters. A valid link id (at the end of the link name) must only have alphanumeric characters and underscores within it. "projects/[PROJECT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "organizations/[ORGANIZATION_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" "folders/[FOLDER_ID]/locations/[LOCATION_ID]/buckets/[BUCKET_ID]/links/[LINK_ID]" For example:`projects/my-project/locations/global/buckets/my-bucket/links/my_link |
| <CopyableCode code="description" /> | `string` | Describes this link.The maximum length of the description is 8000 characters. |
| <CopyableCode code="bigqueryDataset" /> | `object` | Describes a BigQuery dataset that was created by a link. |
| <CopyableCode code="createTime" /> | `string` | Output only. The creation timestamp of the link. |
| <CopyableCode code="lifecycleState" /> | `string` | Output only. The resource lifecycle state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="billing_accounts_locations_buckets_links_get" /> | `SELECT` | <CopyableCode code="billingAccountsId, bucketsId, linksId, locationsId" /> | Gets a link. |
| <CopyableCode code="billing_accounts_locations_buckets_links_list" /> | `SELECT` | <CopyableCode code="billingAccountsId, bucketsId, locationsId" /> | Lists links. |
| <CopyableCode code="folders_locations_buckets_links_get" /> | `SELECT` | <CopyableCode code="bucketsId, foldersId, linksId, locationsId" /> | Gets a link. |
| <CopyableCode code="folders_locations_buckets_links_list" /> | `SELECT` | <CopyableCode code="bucketsId, foldersId, locationsId" /> | Lists links. |
| <CopyableCode code="locations_buckets_links_list" /> | `SELECT` | <CopyableCode code="parent, parentType" /> | Lists links. |
| <CopyableCode code="organizations_locations_buckets_links_get" /> | `SELECT` | <CopyableCode code="bucketsId, linksId, locationsId, organizationsId" /> | Gets a link. |
| <CopyableCode code="organizations_locations_buckets_links_list" /> | `SELECT` | <CopyableCode code="bucketsId, locationsId, organizationsId" /> | Lists links. |
| <CopyableCode code="projects_locations_buckets_links_get" /> | `SELECT` | <CopyableCode code="bucketsId, linksId, locationsId, projectsId" /> | Gets a link. |
| <CopyableCode code="projects_locations_buckets_links_list" /> | `SELECT` | <CopyableCode code="bucketsId, locationsId, projectsId" /> | Lists links. |
| <CopyableCode code="billing_accounts_locations_buckets_links_create" /> | `INSERT` | <CopyableCode code="billingAccountsId, bucketsId, locationsId" /> | Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link. |
| <CopyableCode code="folders_locations_buckets_links_create" /> | `INSERT` | <CopyableCode code="bucketsId, foldersId, locationsId" /> | Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link. |
| <CopyableCode code="locations_buckets_links_create" /> | `INSERT` | <CopyableCode code="parent, parentType" /> | Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link. |
| <CopyableCode code="organizations_locations_buckets_links_create" /> | `INSERT` | <CopyableCode code="bucketsId, locationsId, organizationsId" /> | Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link. |
| <CopyableCode code="projects_locations_buckets_links_create" /> | `INSERT` | <CopyableCode code="bucketsId, locationsId, projectsId" /> | Asynchronously creates a linked dataset in BigQuery which makes it possible to use BigQuery to read the logs stored in the log bucket. A log bucket may currently only contain one link. |
| <CopyableCode code="billing_accounts_locations_buckets_links_delete" /> | `DELETE` | <CopyableCode code="billingAccountsId, bucketsId, linksId, locationsId" /> | Deletes a link. This will also delete the corresponding BigQuery linked dataset. |
| <CopyableCode code="folders_locations_buckets_links_delete" /> | `DELETE` | <CopyableCode code="bucketsId, foldersId, linksId, locationsId" /> | Deletes a link. This will also delete the corresponding BigQuery linked dataset. |
| <CopyableCode code="organizations_locations_buckets_links_delete" /> | `DELETE` | <CopyableCode code="bucketsId, linksId, locationsId, organizationsId" /> | Deletes a link. This will also delete the corresponding BigQuery linked dataset. |
| <CopyableCode code="projects_locations_buckets_links_delete" /> | `DELETE` | <CopyableCode code="bucketsId, linksId, locationsId, projectsId" /> | Deletes a link. This will also delete the corresponding BigQuery linked dataset. |
| <CopyableCode code="_billing_accounts_locations_buckets_links_list" /> | `EXEC` | <CopyableCode code="billingAccountsId, bucketsId, locationsId" /> | Lists links. |
| <CopyableCode code="_folders_locations_buckets_links_list" /> | `EXEC` | <CopyableCode code="bucketsId, foldersId, locationsId" /> | Lists links. |
| <CopyableCode code="_locations_buckets_links_list" /> | `EXEC` | <CopyableCode code="parent, parentType" /> | Lists links. |
| <CopyableCode code="_organizations_locations_buckets_links_list" /> | `EXEC` | <CopyableCode code="bucketsId, locationsId, organizationsId" /> | Lists links. |
| <CopyableCode code="_projects_locations_buckets_links_list" /> | `EXEC` | <CopyableCode code="bucketsId, locationsId, projectsId" /> | Lists links. |
