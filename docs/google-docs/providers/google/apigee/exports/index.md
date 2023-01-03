---
title: exports
hide_title: false
hide_table_of_contents: false
keywords:
  - exports
  - apigee
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
<tr><td><b>Name</b></td><td><code>exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.apigee.exports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Display name of the export job. |
| `description` | `string` | Description of the export job. |
| `datastoreName` | `string` | Name of the datastore that is the destination of the export job [datastore] |
| `error` | `string` | Output only. Error is set when export fails |
| `state` | `string` | Output only. Status of the export job. Valid values include `enqueued`, `running`, `completed`, and `failed`. |
| `updated` | `string` | Output only. Time the export job was last updated. |
| `executionTime` | `string` | Output only. Execution time for this export job. If the job is still in progress, it will be set to the amount of time that has elapsed since`created`, in seconds. Else, it will set to (`updated` - `created`), in seconds. |
| `created` | `string` | Output only. Time the export job was created. |
| `self` | `string` | Output only. Self link of the export job. A URI that can be used to retrieve the status of an export job. Example: `/organizations/myorg/environments/myenv/analytics/exports/9cfc0d85-0f30-46d6-ae6f-318d0cb961bd` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_environments_analytics_exports_get` | `SELECT` | `environmentsId, exportsId, organizationsId` | Gets the details and status of an analytics export job. If the export job is still in progress, its `state` is set to "running". After the export job has completed successfully, its `state` is set to "completed". If the export job fails, its `state` is set to `failed`. |
| `organizations_environments_analytics_exports_list` | `SELECT` | `environmentsId, organizationsId` | Lists the details and status of all analytics export jobs belonging to the parent organization and environment. |
| `organizations_environments_analytics_exports_create` | `INSERT` | `environmentsId, organizationsId` | Submit a data export job to be processed in the background. If the request is successful, the API returns a 201 status, a URI that can be used to retrieve the status of the export job, and the `state` value of "enqueued". |
