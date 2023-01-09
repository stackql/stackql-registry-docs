---
title: version_headers
hide_title: false
hide_table_of_contents: false
keywords:
  - version_headers
  - tagmanager
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
<tr><td><b>Name</b></td><td><code>version_headers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.tagmanager.version_headers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `containerVersionHeader` | `array` | All container version headers of a GTM Container. |
| `nextPageToken` | `string` | Continuation token for fetching the next page of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `accounts_containers_version_headers_list` | `SELECT` | `accountsId, containersId` | Lists all Container Versions of a GTM Container. |
| `accounts_containers_version_headers_latest` | `EXEC` | `accountsId, containersId` | Gets the latest container version header |
