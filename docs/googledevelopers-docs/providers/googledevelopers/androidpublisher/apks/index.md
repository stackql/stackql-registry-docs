---
title: apks
hide_title: false
hide_table_of_contents: false
keywords:
  - apks
  - androidpublisher
  - googledevelopers    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googledevelopers/stackql-googledevelopers-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>apks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.apks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | The kind of this response ("androidpublisher#apksListResponse"). |
| `apks` | `array` | All APKs. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `edits_apks_list` | `SELECT` | `editId, packageName` | Lists all current APKs of the app and edit. |
| `edits_apks_upload` | `EXEC` | `editId, packageName` | Uploads an APK and adds to the current edit. |
