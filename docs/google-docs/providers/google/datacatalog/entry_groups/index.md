---
title: entry_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - entry_groups
  - datacatalog
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
<tr><td><b>Name</b></td><td><code>entry_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.datacatalog.entry_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The resource name of the entry group in URL format. Note: The entry group itself and its child resources might not be stored in the location specified in its name. |
| `description` | `string` | Entry group description. Can consist of several sentences or paragraphs that describe the entry group contents. Default value is an empty string. |
| `displayName` | `string` | A short name to identify the entry group, for example, "analytics data - jan 2011". Default value is an empty string. |
| `dataCatalogTimestamps` | `object` | Timestamps associated with this resource in a particular system. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_entryGroups_get` | `SELECT` | `entryGroupsId, locationsId, projectsId` | Gets an entry group. |
| `projects_locations_entryGroups_list` | `SELECT` | `locationsId, projectsId` | Lists entry groups. |
| `projects_locations_entryGroups_create` | `INSERT` | `locationsId, projectsId` | Creates an entry group. An entry group contains logically related entries together with [Cloud Identity and Access Management](/data-catalog/docs/concepts/iam) policies. These policies specify users who can create, edit, and view entries within entry groups. Data Catalog automatically creates entry groups with names that start with the `@` symbol for the following resources: * BigQuery entries (`@bigquery`) * Pub/Sub topics (`@pubsub`) * Dataproc Metastore services (`@dataproc_metastore_{SERVICE_NAME_HASH}`) You can create your own entry groups for Cloud Storage fileset entries and custom entries together with the corresponding IAM policies. User-created entry groups can't contain the `@` symbol, it is reserved for automatically created groups. Entry groups, like entries, can be searched. A maximum of 10,000 entry groups may be created per organization across all locations. You must enable the Data Catalog API in the project identified by the `parent` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
| `projects_locations_entryGroups_delete` | `DELETE` | `entryGroupsId, locationsId, projectsId` | Deletes an entry group. You must enable the Data Catalog API in the project identified by the `name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
| `projects_locations_entryGroups_patch` | `EXEC` | `entryGroupsId, locationsId, projectsId` | Updates an entry group. You must enable the Data Catalog API in the project identified by the `entry_group.name` parameter. For more information, see [Data Catalog resource project](https://cloud.google.com/data-catalog/docs/concepts/resource-project). |
