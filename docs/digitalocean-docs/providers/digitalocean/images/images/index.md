---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - images
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.images.images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | A unique number that can be used to identify and reference a specific image. |
| `name` | `string` | The display name that has been given to an image.  This is what is shown in the control panel and is generally a descriptive title for the image in question. |
| `description` | `string` | An optional free-form text field to describe an image. |
| `tags` | `array` | A flat array of tag names as strings to be applied to the resource. Tag names may be for either existing or new tags. |
| `regions` | `array` | This attribute is an array of the regions that the image is available in. The regions are represented by their identifying slug values. |
| `type` | `string` | Describes the kind of image. It may be one of `base`, `snapshot`, `backup`, `custom`, or `admin`. Respectively, this specifies whether an image is a DigitalOcean base OS image, user-generated Droplet snapshot, automatically created Droplet backup, user-provided virtual machine image, or an image used for DigitalOcean managed resources (e.g. DOKS worker nodes). |
| `slug` | `string` | A uniquely identifying string that is associated with each of the DigitalOcean-provided public images. These can be used to reference a public image as an alternative to the numeric id. |
| `status` | `string` | A status string indicating the state of a custom image. This may be `NEW`,<br /> `available`, `pending`, `deleted`, or `retired`. |
| `min_disk_size` | `integer` | The minimum disk size in GB required for a Droplet to use this image. |
| `public` | `boolean` | This is a boolean value that indicates whether the image in question is public or not. An image that is public is available to all accounts. A non-public image is only accessible from your account. |
| `created_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the image was created. |
| `distribution` | `string` | The name of a custom image's distribution. Currently, the valid values are  `Arch Linux`, `CentOS`, `CoreOS`, `Debian`, `Fedora`, `Fedora Atomic`,  `FreeBSD`, `Gentoo`, `openSUSE`, `RancherOS`, `Rocky Linux`, `Ubuntu`, and `Unknown`.  Any other value will be accepted but ignored, and `Unknown` will be used in its place. |
| `error_message` | `string` | A string containing information about errors that may occur when importing<br /> a custom image. |
| `size_gigabytes` | `number` | The size of the image in gigabytes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `image_id` | To retrieve information about an image, send a `GET` request to<br />`/v2/images/$IDENTIFIER`.<br /> |
| `list` | `SELECT` |  | To list all of the images available on your account, send a GET request to /v2/images.<br /><br />## Filtering Results<br />-----<br /><br />It's possible to request filtered results by including certain query parameters.<br /><br />**Image Type**<br /><br />Either 1-Click Application or OS Distribution images can be filtered by using the `type` query parameter.<br /><br />&gt; Important: The `type` query parameter does not directly relate to the `type` attribute.<br /><br />To retrieve only ***distribution*** images, include the `type` query parameter set to distribution, `/v2/images?type=distribution`.<br /><br />To retrieve only ***application*** images, include the `type` query parameter set to application, `/v2/images?type=application`.<br /><br />**User Images**<br /><br />To retrieve only the private images of a user, include the `private` query parameter set to true, `/v2/images?private=true`.<br /><br />**Tags**<br /><br />To list all images assigned to a specific tag, include the `tag_name` query parameter set to the name of the tag in your GET request. For example, `/v2/images?tag_name=$TAG_NAME`.<br /> |
| `create_custom` | `INSERT` | `data__name, data__region, data__url` | To create a new custom image, send a POST request to /v2/images.<br />The body must contain a url attribute pointing to a Linux virtual machine<br />image to be imported into DigitalOcean.<br />The image must be in the raw, qcow2, vhdx, vdi, or vmdk format.<br />It may be compressed using gzip or bzip2 and must be smaller than 100 GB after<br /> being decompressed.<br /> |
| `delete` | `DELETE` | `image_id` | To delete a snapshot or custom image, send a `DELETE` request to `/v2/images/$IMAGE_ID`.<br /> |
| `_get` | `EXEC` | `image_id` | To retrieve information about an image, send a `GET` request to<br />`/v2/images/$IDENTIFIER`.<br /> |
| `_list` | `EXEC` |  | To list all of the images available on your account, send a GET request to /v2/images.<br /><br />## Filtering Results<br />-----<br /><br />It's possible to request filtered results by including certain query parameters.<br /><br />**Image Type**<br /><br />Either 1-Click Application or OS Distribution images can be filtered by using the `type` query parameter.<br /><br />&gt; Important: The `type` query parameter does not directly relate to the `type` attribute.<br /><br />To retrieve only ***distribution*** images, include the `type` query parameter set to distribution, `/v2/images?type=distribution`.<br /><br />To retrieve only ***application*** images, include the `type` query parameter set to application, `/v2/images?type=application`.<br /><br />**User Images**<br /><br />To retrieve only the private images of a user, include the `private` query parameter set to true, `/v2/images?private=true`.<br /><br />**Tags**<br /><br />To list all images assigned to a specific tag, include the `tag_name` query parameter set to the name of the tag in your GET request. For example, `/v2/images?tag_name=$TAG_NAME`.<br /> |
| `update` | `EXEC` | `image_id` | To update an image, send a `PUT` request to `/v2/images/$IMAGE_ID`.<br />Set the `name` attribute to the new value you would like to use.<br />For custom images, the `description` and `distribution` attributes may also be updated.<br /> |
