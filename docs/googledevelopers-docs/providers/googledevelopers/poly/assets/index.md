---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
  - poly
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
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googledevelopers.poly.assets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The unique identifier for the asset in the form: `assets/&#123;ASSET_ID&#125;`. |
| `description` | `string` | The human-readable description, set by the asset's author. |
| `displayName` | `string` | The human-readable name, set by the asset's author. |
| `createTime` | `string` | For published assets, the time when the asset was published. For unpublished assets, the time when the asset was created. |
| `visibility` | `string` | The visibility of the asset and who can access it. |
| `isCurated` | `boolean` | Whether this asset has been curated by the Poly team. |
| `remixInfo` | `object` | Info about the sources of this asset (i.e. assets that were remixed to create this asset). |
| `thumbnail` | `object` | Represents a file in Poly, which can be a root, resource, or thumbnail file. |
| `updateTime` | `string` | The time when the asset was last modified. For published assets, whose contents are immutable, the update time changes only when metadata properties, such as visibility, are updated. |
| `license` | `string` | The license under which the author has made the asset available for use, if any. |
| `formats` | `array` | A list of Formats where each format describes one representation of the asset. |
| `authorName` | `string` | The author's publicly visible name. Use this name when giving credit to the author. For more information, see [Licensing](/poly/discover/licensing). |
| `metadata` | `string` | Application-defined opaque metadata for this asset. This field is only returned when querying for the signed-in user's own assets, not for public assets. This string is limited to 1K chars. It is up to the creator of the asset to define the format for this string (for example, JSON). |
| `presentationParams` | `object` | Hints for displaying the asset, based on information available when the asset was uploaded. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `assetsId` | Returns detailed information about an asset given its name. PRIVATE assets are returned only if the currently authenticated user (via OAuth token) is the author of the asset. |
| `list` | `SELECT` |  | Lists all public, remixable assets. These are assets with an access level of PUBLIC and published under the CC-By license. |
| `users_assets_list` | `SELECT` | `usersId` | Lists assets authored by the given user. Only the value 'me', representing the currently-authenticated user, is supported. May include assets with an access level of PRIVATE or UNLISTED and assets which are All Rights Reserved for the currently-authenticated user. |
