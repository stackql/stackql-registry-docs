---
title: uploads
hide_title: false
hide_table_of_contents: false
keywords:
  - uploads
  - analytics
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>uploads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.uploads</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | A unique ID for this upload. |
| `accountId` | `string` | Account Id to which this upload belongs. |
| `customDataSourceId` | `string` | Custom data source Id to which this data import belongs. |
| `errors` | `array` | Data import errors collection. |
| `kind` | `string` | Resource type for Analytics upload. |
| `status` | `string` | Upload status. Possible values: PENDING, COMPLETED, FAILED, DELETING, DELETED. |
| `uploadTime` | `string` | Time this file is uploaded. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `management_uploads_get` | `SELECT` | `accountId, customDataSourceId, uploadId, webPropertyId` | List uploads to which the user has access. |
| `management_uploads_list` | `SELECT` | `accountId, customDataSourceId, webPropertyId` | List uploads to which the user has access. |
| `management_uploads_uploadData` | `EXEC` | `accountId, customDataSourceId, webPropertyId` | Upload data for a custom data source. |
