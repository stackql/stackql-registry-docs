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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>photos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="googleadmin.directory.photos" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID the API uses to uniquely identify the user. |
| <CopyableCode code="etag" /> | `string` | ETag of the resource. |
| <CopyableCode code="height" /> | `integer` | Height of the photo in pixels. |
| <CopyableCode code="kind" /> | `string` | The type of the API resource. For Photo resources, this is `admin#directory#user#photo`. |
| <CopyableCode code="mimeType" /> | `string` | The MIME type of the photo. Allowed values are `JPEG`, `PNG`, `GIF`, `BMP`, `TIFF`, and web-safe base64 encoding. |
| <CopyableCode code="photoData" /> | `string` | The user photo's upload data in [web-safe Base64](https://en.wikipedia.org/wiki/Base64#URL_applications) format in bytes. This means: * The slash (/) character is replaced with the underscore (_) character. * The plus sign (+) character is replaced with the hyphen (-) character. * The equals sign (=) character is replaced with the asterisk (*). * For padding, the period (.) character is used instead of the RFC-4648 baseURL definition which uses the equals sign (=) for padding. This is done to simplify URL-parsing. * Whatever the size of the photo being uploaded, the API downsizes it to 96x96 pixels. |
| <CopyableCode code="primaryEmail" /> | `string` | The user's primary email address. |
| <CopyableCode code="width" /> | `integer` | Width of the photo in pixels. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="userKey" /> | Retrieves the user's photo. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="userKey" /> | Removes the user's photo. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="userKey" /> | Adds a photo for the user. This method supports [patch semantics](/admin-sdk/directory/v1/guides/performance#patch). |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="userKey" /> | Adds a photo for the user. |
