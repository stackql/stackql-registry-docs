---
title: teamdrives
hide_title: false
hide_table_of_contents: false
keywords:
  - teamdrives
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
<tr><td><b>Name</b></td><td><code>teamdrives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.drive.teamdrives</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of this Team Drive which is also the ID of the top level folder of this Team Drive. |
| `name` | `string` | The name of this Team Drive. |
| `backgroundImageFile` | `object` | An image file and cropping parameters from which a background image for this Team Drive is set. This is a write only field; it can only be set on drive.teamdrives.update requests that don't set themeId. When specified, all fields of the backgroundImageFile must be set. |
| `themeId` | `string` | The ID of the theme from which the background image and color will be set. The set of possible teamDriveThemes can be retrieved from a drive.about.get response. When not specified on a drive.teamdrives.create request, a random theme is chosen from which the background image and color are set. This is a write-only field; it can only be set on requests that don't set colorRgb or backgroundImageFile. |
| `orgUnitId` | `string` | The organizational unit of this shared drive. This field is only populated on drives.list responses when the useDomainAdminAccess parameter is set to true. |
| `restrictions` | `object` | A set of restrictions that apply to this Team Drive or items inside this Team Drive. |
| `createdTime` | `string` | The time at which the Team Drive was created (RFC 3339 date-time). |
| `colorRgb` | `string` | The color of this Team Drive as an RGB hex string. It can only be set on a drive.teamdrives.update request that does not set themeId. |
| `capabilities` | `object` | Capabilities the current user has on this Team Drive. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#teamDrive". |
| `backgroundImageLink` | `string` | A short-lived link to this Team Drive's background image. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `teamDriveId` | Deprecated use drives.get instead. |
| `list` | `SELECT` |  | Deprecated use drives.list instead. |
| `create` | `INSERT` | `requestId` | Deprecated use drives.create instead. |
| `delete` | `DELETE` | `teamDriveId` | Deprecated use drives.delete instead. |
| `update` | `EXEC` | `teamDriveId` | Deprecated use drives.update instead |
