---
title: about
hide_title: false
hide_table_of_contents: false
keywords:
  - about
  - drive
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
<tr><td><b>Name</b></td><td><code>about</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.drive.about</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#about". |
| `exportFormats` | `object` | A map of source MIME type to possible targets for all supported exports. |
| `importFormats` | `object` | A map of source MIME type to possible targets for all supported imports. |
| `driveThemes` | `array` | A list of themes that are supported for shared drives. |
| `maxUploadSize` | `string` | The maximum upload size in bytes. |
| `storageQuota` | `object` | The user's storage quota limits and usage. All fields are measured in bytes. |
| `appInstalled` | `boolean` | Whether the user has installed the requesting app. |
| `folderColorPalette` | `array` | The currently supported folder colors as RGB hex strings. |
| `maxImportSizes` | `object` | A map of maximum import sizes by MIME type, in bytes. |
| `teamDriveThemes` | `array` | Deprecated - use driveThemes instead. |
| `user` | `object` | Information about a Drive user. |
| `canCreateTeamDrives` | `boolean` | Deprecated - use canCreateDrives instead. |
| `canCreateDrives` | `boolean` | Whether the user can create shared drives. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` |  |
