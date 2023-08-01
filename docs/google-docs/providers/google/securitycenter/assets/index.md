---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
  - securitycenter
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
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.securitycenter.assets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results. |
| `readTime` | `string` | Time used for executing the list request. |
| `totalSize` | `integer` | The total number of assets matching the query. |
| `listAssetsResults` | `array` | Assets matching the list request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `folders_assets_list` | `SELECT` | `foldersId` | Lists an organization's assets. |
| `organizations_assets_list` | `SELECT` | `organizationsId` | Lists an organization's assets. |
| `projects_assets_list` | `SELECT` | `projectsId` | Lists an organization's assets. |
| `folders_assets_group` | `EXEC` | `foldersId` | Filters an organization's assets and groups them by their specified properties. |
| `organizations_assets_group` | `EXEC` | `organizationsId` | Filters an organization's assets and groups them by their specified properties. |
| `organizations_assets_run_discovery` | `EXEC` | `organizationsId` | Runs asset discovery. The discovery is tracked with a long-running operation. This API can only be called with limited frequency for an organization. If it is called too frequently the caller will receive a TOO_MANY_REQUESTS error. |
| `projects_assets_group` | `EXEC` | `projectsId` | Filters an organization's assets and groups them by their specified properties. |
