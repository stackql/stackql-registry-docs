---
title: expansionfiles
hide_title: false
hide_table_of_contents: false
keywords:
  - expansionfiles
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
<tr><td><b>Name</b></td><td><code>expansionfiles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.androidpublisher.expansionfiles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `fileSize` | `string` | If set, this field indicates that this APK has an expansion file uploaded to it: this APK does not reference another APK's expansion file. The field's value is the size of the uploaded expansion file in bytes. |
| `referencesVersion` | `integer` | If set, this APK's expansion file references another APK's expansion file. The file_size field will not be set. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `edits_expansionfiles_get` | `SELECT` | `apkVersionCode, editId, expansionFileType, packageName` | Fetches the expansion file configuration for the specified APK. |
| `edits_expansionfiles_patch` | `EXEC` | `apkVersionCode, editId, expansionFileType, packageName` | Patches the APK's expansion file configuration to reference another APK's expansion file. To add a new expansion file use the Upload method. |
| `edits_expansionfiles_update` | `EXEC` | `apkVersionCode, editId, expansionFileType, packageName` | Updates the APK's expansion file configuration to reference another APK's expansion file. To add a new expansion file use the Upload method. |
| `edits_expansionfiles_upload` | `EXEC` | `apkVersionCode, editId, expansionFileType, packageName` | Uploads a new expansion file and attaches to the specified APK. |
