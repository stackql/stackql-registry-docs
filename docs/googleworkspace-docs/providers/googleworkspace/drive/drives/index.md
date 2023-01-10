---
title: drives
hide_title: false
hide_table_of_contents: false
keywords:
  - drives
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
<tr><td><b>Name</b></td><td><code>drives</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.drive.drives</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of this shared drive which is also the ID of the top level folder of this shared drive. |
| `name` | `string` | The name of this shared drive. |
| `capabilities` | `object` | Capabilities the current user has on this shared drive. |
| `backgroundImageLink` | `string` | A short-lived link to this shared drive's background image. |
| `colorRgb` | `string` | The color of this shared drive as an RGB hex string. It can only be set on a drive.drives.update request that does not set themeId. |
| `createdTime` | `string` | The time at which the shared drive was created (RFC 3339 date-time). |
| `hidden` | `boolean` | Whether the shared drive is hidden from default view. |
| `backgroundImageFile` | `object` | An image file and cropping parameters from which a background image for this shared drive is set. This is a write only field; it can only be set on drive.drives.update requests that don't set themeId. When specified, all fields of the backgroundImageFile must be set. |
| `orgUnitId` | `string` | The organizational unit of this shared drive. This field is only populated on drives.list responses when the useDomainAdminAccess parameter is set to true. |
| `themeId` | `string` | The ID of the theme from which the background image and color will be set. The set of possible driveThemes can be retrieved from a drive.about.get response. When not specified on a drive.drives.create request, a random theme is chosen from which the background image and color are set. This is a write-only field; it can only be set on requests that don't set colorRgb or backgroundImageFile. |
| `kind` | `string` | Identifies what kind of resource this is. Value: the fixed string "drive#drive". |
| `restrictions` | `object` | A set of restrictions that apply to this shared drive or items inside this shared drive. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `driveId` | Gets a shared drive's metadata by ID. |
| `list` | `SELECT` |  | Lists the user's shared drives. |
| `create` | `INSERT` | `requestId` | Creates a shared drive. |
| `delete` | `DELETE` | `driveId` | Permanently deletes a shared drive for which the user is an organizer. The shared drive cannot contain any untrashed items. |
| `hide` | `EXEC` | `driveId` | Hides a shared drive from the default view. |
| `unhide` | `EXEC` | `driveId` | Restores a shared drive to the default view. |
| `update` | `EXEC` | `driveId` | Updates the metadate for a shared drive. |
