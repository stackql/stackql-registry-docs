---
title: exports
hide_title: false
hide_table_of_contents: false
keywords:
  - exports
  - vault
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.vault.exports</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Output only. The generated export ID. |
| `name` | `string` | The export name. Don't use special characters (~!$'(),;@:/?) in the name, they can prevent you from downloading exports. |
| `status` | `string` | Output only. The status of the export. |
| `matterId` | `string` | Output only. The matter ID. |
| `requester` | `object` | User's information. |
| `cloudStorageSink` | `object` | Export sink for Cloud Storage files. |
| `exportOptions` | `object` | Additional options for exports |
| `createTime` | `string` | Output only. The time when the export was created. |
| `query` | `object` | The query definition used for search and export. |
| `stats` | `object` | Progress information for an export. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `matters_exports_get` | `SELECT` | `exportId, matterId` | Gets an export. |
| `matters_exports_list` | `SELECT` | `matterId` | Lists details about the exports in the specified matter. |
| `matters_exports_create` | `INSERT` | `matterId` | Creates an export. |
| `matters_exports_delete` | `DELETE` | `exportId, matterId` | Deletes an export. |
