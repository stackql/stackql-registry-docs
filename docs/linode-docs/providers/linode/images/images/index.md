---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - images
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.images.images" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The unique ID of this Image. |
| <CopyableCode code="description" /> | `string` | A detailed description of this Image. |
| <CopyableCode code="created" /> | `string` | When this Image was created. |
| <CopyableCode code="created_by" /> | `string` | The name of the User who created this Image, or "linode" for public Images.<br /> |
| <CopyableCode code="deprecated" /> | `boolean` | Whether or not this Image is deprecated. Will only be true for deprecated public Images.<br /> |
| <CopyableCode code="eol" /> | `string` | The date of the public Image's planned end of life. `None` for private Images.<br /> |
| <CopyableCode code="expiry" /> | `string` | Only Images created automatically from a deleted Linode (type=automatic) will expire.<br /> |
| <CopyableCode code="is_public" /> | `boolean` | True if the Image is a public distribution image. False if Image is private Account-specific Image. |
| <CopyableCode code="label" /> | `string` | A short description of the Image.<br /> |
| <CopyableCode code="size" /> | `integer` | The minimum size this Image needs to deploy. Size is in MB.<br /> |
| <CopyableCode code="status" /> | `string` | The current status of this Image.<br /><br />Only Images in an "available" status can be deployed. Images in a "creating" status are being created from a Linode Disk, and will become "available" shortly. Images in a "pending_upload" status are waiting for data to be [uploaded](/docs/api/images/#image-upload), and become "available" after the upload and processing are complete.<br /><br />The "+order_by" and "+order" operators are not available for [filtering](/docs/api/#filtering-and-sorting) on this key.<br /> |
| <CopyableCode code="type" /> | `string` | How the Image was created.<br /><br />"Manual" Images can be created at any time.<br /><br />"Automatic" Images are created automatically from a deleted Linode.<br /> |
| <CopyableCode code="updated" /> | `string` | When this Image was last updated. |
| <CopyableCode code="vendor" /> | `string` | The upstream distribution vendor. `None` for private Images.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getImage" /> | `SELECT` | <CopyableCode code="imageId" /> | Get information about a single Image.<br /><br />* **Public** Images have IDs that begin with "linode/". These distribution images are generally available to<br />all users.<br /><br />* **Private** Images have IDs that begin with "private/". These Images are Account-specific and only<br />accessible to Users with appropriate [Grants](/docs/api/account/#users-grants-view).<br /><br />* To view a public Image, call this endpoint with or without authentication. To view a private Image, call this endpoint with authentication.<br /> |
| <CopyableCode code="getImages" /> | `SELECT` |  | Returns a paginated list of Images.<br /><br />* **Public** Images have IDs that begin with "linode/". These distribution images are generally available to<br />all users.<br /><br />* **Private** Images have IDs that begin with "private/". These Images are Account-specific and only<br />accessible to Users with appropriate [Grants](/docs/api/account/#users-grants-view).<br /><br />* To view only public Images, call this endpoint with or without authentication. To view private Images as well, call this endpoint with authentication.<br /> |
| <CopyableCode code="createImage" /> | `INSERT` | <CopyableCode code="data__disk_id" /> | Captures a private gold-master Image from a Linode Disk.<br /> |
| <CopyableCode code="deleteImage" /> | `DELETE` | <CopyableCode code="imageId" /> | Deletes a private Image you have permission to `read_write`.<br /><br /><br />**Deleting an Image is a destructive action and cannot be undone.**<br /> |
| <CopyableCode code="_getImage" /> | `EXEC` | <CopyableCode code="imageId" /> | Get information about a single Image.<br /><br />* **Public** Images have IDs that begin with "linode/". These distribution images are generally available to<br />all users.<br /><br />* **Private** Images have IDs that begin with "private/". These Images are Account-specific and only<br />accessible to Users with appropriate [Grants](/docs/api/account/#users-grants-view).<br /><br />* To view a public Image, call this endpoint with or without authentication. To view a private Image, call this endpoint with authentication.<br /> |
| <CopyableCode code="_getImages" /> | `EXEC` |  | Returns a paginated list of Images.<br /><br />* **Public** Images have IDs that begin with "linode/". These distribution images are generally available to<br />all users.<br /><br />* **Private** Images have IDs that begin with "private/". These Images are Account-specific and only<br />accessible to Users with appropriate [Grants](/docs/api/account/#users-grants-view).<br /><br />* To view only public Images, call this endpoint with or without authentication. To view private Images as well, call this endpoint with authentication.<br /> |
| <CopyableCode code="post_images_upload" /> | `EXEC` | <CopyableCode code="data__label, data__region" /> | Initiates an Image upload.<br /><br />This endpoint creates a new private Image object and returns it along<br />with the URL to which image data can be uploaded.<br /><br />- Image data must be uploaded within 24 hours of creation or the<br />upload will be cancelled and the image deleted.<br /><br />- Image uploads should be made as an HTTP PUT request to the URL returned in the `upload_to`<br />response parameter, with a `Content-type: application/octet-stream` header included in the<br />request. For example:<br /><br />      curl -v \<br />        -H "Content-Type: application/octet-stream" \<br />        --upload-file example.img.gz \<br />        $UPLOAD_URL \<br />        --progress-bar \<br />        --output /dev/null<br /><br />- Uploaded image data should be compressed in gzip (`.gz`) format. The uncompressed disk should be in raw<br />disk image (`.img`) format. A maximum compressed file size of 5GB is supported for upload at this time.<br /><br />**Note:** To initiate and complete an Image upload in a single step, see our guide on how to [Upload an Image](/docs/products/tools/images/guides/upload-an-image/) using Cloud Manager or the Linode CLI `image-upload` plugin.<br /> |
| <CopyableCode code="updateImage" /> | `EXEC` | <CopyableCode code="imageId" /> | Updates a private Image that you have permission to `read_write`.<br /> |
