---
title: photos
hide_title: false
hide_table_of_contents: false
keywords:
  - photos
  - directory
  - googleadmin    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query and manage Google Workspace users and groups using SQL.
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>photos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleadmin.directory.photos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID the API uses to uniquely identify the user. |
| `kind` | `string` | The type of the API resource. For Photo resources, this is `admin#directory#user#photo`. |
| `mimeType` | `string` | The MIME type of the photo. Allowed values are `JPEG`, `PNG`, `GIF`, `BMP`, `TIFF`, and web-safe base64 encoding. |
| `photoData` | `string` | The user photo's upload data in [web-safe Base64](https://en.wikipedia.org/wiki/Base64#URL_applications) format in bytes. This means: * The slash (/) character is replaced with the underscore (_) character. * The plus sign (+) character is replaced with the hyphen (-) character. * The equals sign (=) character is replaced with the asterisk (*). * For padding, the period (.) character is used instead of the RFC-4648 baseURL definition which uses the equals sign (=) for padding. This is done to simplify URL-parsing. * Whatever the size of the photo being uploaded, the API downsizes it to 96x96 pixels. |
| `primaryEmail` | `string` | The user's primary email address. |
| `width` | `integer` | Width of the photo in pixels. |
| `etag` | `string` | ETag of the resource. |
| `height` | `integer` | Height of the photo in pixels. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `userKey` | Retrieves the user's photo. |
| `delete` | `DELETE` | `userKey` | Removes the user's photo. |
| `patch` | `EXEC` | `userKey` | Adds a photo for the user. This method supports [patch semantics](/admin-sdk/directory/v1/guides/performance#patch). |
| `update` | `EXEC` | `userKey` | Adds a photo for the user. |
