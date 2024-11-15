---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - images
  - digitalocean
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage digitalocean resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>images</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.images.images" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | A unique number that can be used to identify and reference a specific image. |
| <CopyableCode code="name" /> | `string` | The display name that has been given to an image. This is what is shown in the control panel and is generally a descriptive title for the image in question. |
| <CopyableCode code="description" /> | `string` | An optional free-form text field to describe an image. |
| <CopyableCode code="created_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the image was created. |
| <CopyableCode code="distribution" /> | `string` | The name of a custom image's distribution. Currently, the valid values are `Arch Linux`, `CentOS`, `CoreOS`, `Debian`, `Fedora`, `Fedora Atomic`, `FreeBSD`, `Gentoo`, `openSUSE`, `RancherOS`, `Rocky Linux`, `Ubuntu`, and `Unknown`. Any other value will be accepted but ignored, and `Unknown` will be used in its place. |
| <CopyableCode code="error_message" /> | `string` | A string containing information about errors that may occur when importing a custom image. |
| <CopyableCode code="min_disk_size" /> | `integer` | The minimum disk size in GB required for a Droplet to use this image. |
| <CopyableCode code="public" /> | `boolean` | This is a boolean value that indicates whether the image in question is public or not. An image that is public is available to all accounts. A non-public image is only accessible from your account. |
| <CopyableCode code="regions" /> | `array` | This attribute is an array of the regions that the image is available in. The regions are represented by their identifying slug values. |
| <CopyableCode code="size_gigabytes" /> | `number` | The size of the image in gigabytes. |
| <CopyableCode code="slug" /> | `string` | A uniquely identifying string that is associated with each of the DigitalOcean-provided public images. These can be used to reference a public image as an alternative to the numeric id. |
| <CopyableCode code="status" /> | `string` | A status string indicating the state of a custom image. This may be `NEW`, `available`, `pending`, `deleted`, or `retired`. |
| <CopyableCode code="tags" /> | `array` | A flat array of tag names as strings to be applied to the resource. Tag names may be for either existing or new tags. |
| <CopyableCode code="type" /> | `string` | Describes the kind of image. It may be one of `base`, `snapshot`, `backup`, `custom`, or `admin`. Respectively, this specifies whether an image is a DigitalOcean base OS image, user-generated Droplet snapshot, automatically created Droplet backup, user-provided virtual machine image, or an image used for DigitalOcean managed resources (e.g. DOKS worker nodes). |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="images_get" /> | `SELECT` | <CopyableCode code="image_id" /> | To retrieve information about an image, send a `GET` request to `/v2/images/$IDENTIFIER`. |
| <CopyableCode code="images_list" /> | `SELECT` | <CopyableCode code="" /> | To list all of the images available on your account, send a GET request to /v2/images. ## Filtering Results ----- It's possible to request filtered results by including certain query parameters. **Image Type** Either 1-Click Application or OS Distribution images can be filtered by using the `type` query parameter. > Important: The `type` query parameter does not directly relate to the `type` attribute. To retrieve only ***distribution*** images, include the `type` query parameter set to distribution, `/v2/images?type=distribution`. To retrieve only ***application*** images, include the `type` query parameter set to application, `/v2/images?type=application`. **User Images** To retrieve only the private images of a user, include the `private` query parameter set to true, `/v2/images?private=true`. **Tags** To list all images assigned to a specific tag, include the `tag_name` query parameter set to the name of the tag in your GET request. For example, `/v2/images?tag_name=$TAG_NAME`. |
| <CopyableCode code="images_create_custom" /> | `INSERT` | <CopyableCode code="" /> | To create a new custom image, send a POST request to /v2/images. The body must contain a url attribute pointing to a Linux virtual machine image to be imported into DigitalOcean. The image must be in the raw, qcow2, vhdx, vdi, or vmdk format. It may be compressed using gzip or bzip2 and must be smaller than 100 GB after being decompressed. |
| <CopyableCode code="images_delete" /> | `DELETE` | <CopyableCode code="image_id" /> | To delete a snapshot or custom image, send a `DELETE` request to `/v2/images/$IMAGE_ID`. |
| <CopyableCode code="images_update" /> | `EXEC` | <CopyableCode code="image_id" /> | To update an image, send a `PUT` request to `/v2/images/$IMAGE_ID`. Set the `name` attribute to the new value you would like to use. For custom images, the `description` and `distribution` attributes may also be updated. |

## `SELECT` examples

To list all of the images available on your account, send a GET request to /v2/images. ## Filtering Results ----- It's possible to request filtered results by including certain query parameters. **Image Type** Either 1-Click Application or OS Distribution images can be filtered by using the `type` query parameter. > Important: The `type` query parameter does not directly relate to the `type` attribute. To retrieve only ***distribution*** images, include the `type` query parameter set to distribution, `/v2/images?type=distribution`. To retrieve only ***application*** images, include the `type` query parameter set to application, `/v2/images?type=application`. **User Images** To retrieve only the private images of a user, include the `private` query parameter set to true, `/v2/images?private=true`. **Tags** To list all images assigned to a specific tag, include the `tag_name` query parameter set to the name of the tag in your GET request. For example, `/v2/images?tag_name=$TAG_NAME`.


```sql
SELECT
id,
name,
description,
created_at,
distribution,
error_message,
min_disk_size,
public,
regions,
size_gigabytes,
slug,
status,
tags,
type
FROM digitalocean.images.images
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>images</code> resource.

<Tabs
    defaultValue="all"
    values={[
        
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO digitalocean.images.images (
data__name,
data__distribution,
data__description,
data__url,
data__region,
data__tags
)
SELECT 
'{{ name }}',
'{{ distribution }}',
'{{ description }}',
'{{ url }}',
'{{ region }}',
'{{ tags }}'
;
```
</TabItem>

<TabItem value="manifest">

```yaml
- name: images
  props:
    - name: name
      value: string
    - name: distribution
      value: string
    - name: description
      value: string
    - name: url
      value: string
    - name: region
      value: string
    - name: tags
      value: array

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>images</code> resource.

```sql
/*+ delete */
DELETE FROM digitalocean.images.images
WHERE image_id = '{{ image_id }}';
```
