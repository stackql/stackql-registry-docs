---
title: assets
hide_title: false
hide_table_of_contents: false
keywords:
  - assets
  - repos
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>assets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.assets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="name" /> | `string` | The file name of the asset. |
| <CopyableCode code="browser_download_url" /> | `string` |  |
| <CopyableCode code="content_type" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="download_count" /> | `integer` |  |
| <CopyableCode code="label" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="size" /> | `integer` |  |
| <CopyableCode code="state" /> | `string` | State of the release asset. |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="uploader" /> | `object` | A GitHub user. |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_release_asset" /> | `SELECT` | <CopyableCode code="asset_id, owner, repo" /> | To download the asset's binary content, set the `Accept` header of the request to [`application/octet-stream`](https://docs.github.com/rest/overview/media-types). The API will either redirect the client to the location, or stream it directly if possible. API clients should handle both a `200` or `302` response. |
| <CopyableCode code="list_release_assets" /> | `SELECT` | <CopyableCode code="owner, release_id, repo" /> |  |
| <CopyableCode code="delete_release_asset" /> | `DELETE` | <CopyableCode code="asset_id, owner, repo" /> |  |
| <CopyableCode code="update_release_asset" /> | `EXEC` | <CopyableCode code="asset_id, owner, repo" /> | Users with push access to the repository can edit a release asset. |
| <CopyableCode code="upload_release_asset" /> | `EXEC` | <CopyableCode code="name, owner, release_id, repo" /> | This endpoint makes use of [a Hypermedia relation](https://docs.github.com/rest/overview/resources-in-the-rest-api#hypermedia) to determine which URL to access. The endpoint you call to upload release assets is specific to your release. Use the `upload_url` returned in<br />the response of the [Create a release endpoint](https://docs.github.com/rest/releases/releases#create-a-release) to upload a release asset.<br /><br />You need to use an HTTP client which supports [SNI](http://en.wikipedia.org/wiki/Server_Name_Indication) to make calls to this endpoint.<br /><br />Most libraries will set the required `Content-Length` header automatically. Use the required `Content-Type` header to provide the media type of the asset. For a list of media types, see [Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml). For example: <br /><br />`application/zip`<br /><br />GitHub expects the asset data in its raw binary form, rather than JSON. You will send the raw binary content of the asset as the request body. Everything else about the endpoint is the same as the rest of the API. For example,<br />you'll still need to pass your authentication to be able to upload an asset.<br /><br />When an upstream failure occurs, you will receive a `502 Bad Gateway` status. This may leave an empty asset with a state of `starter`. It can be safely deleted.<br /><br />**Notes:**<br />*   GitHub renames asset filenames that have special characters, non-alphanumeric characters, and leading or trailing periods. The "[List release assets](https://docs.github.com/rest/releases/assets#list-release-assets)"<br />endpoint lists the renamed filenames. For more information and help, contact [GitHub Support](https://support.github.com/contact?tags=dotcom-rest-api).<br />*   To find the `release_id` query the [`GET /repos/&#123;owner&#125;/&#123;repo&#125;/releases/latest` endpoint](https://docs.github.com/rest/releases/releases#get-the-latest-release). <br />*   If you upload an asset with the same filename as another uploaded asset, you'll receive an error and must delete the old file before you can re-upload the new asset. |
