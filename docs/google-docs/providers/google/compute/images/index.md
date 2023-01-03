---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - compute
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `labels` | `object` | Labels to apply to this image. These can be later modified by the setLabels method. |
| `sourceImageId` | `string` | [Output Only] The ID value of the image used to create this image. This value may be used to determine whether the image was taken from the current or a previous instance of a given image name. |
| `sourceImageEncryptionKey` | `object` |  |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `sourceType` | `string` | The type of the image used to create this disk. The default and only valid value is RAW. |
| `licenses` | `array` | Any applicable license URI. |
| `deprecated` | `object` | Deprecation status for a public resource. |
| `family` | `string` | The name of the image family to which this image belongs. You can create disks by specifying an image family instead of a specific image name. The image family always returns its latest image that is not deprecated. The name of the image family must comply with RFC1035. |
| `sourceSnapshot` | `string` | URL of the source snapshot used to create this image. The following are valid formats for the URL: - https://www.googleapis.com/compute/v1/projects/project_id/global/ snapshots/snapshot_name - projects/project_id/global/snapshots/snapshot_name In order to create an image, you must provide the full or partial URL of one of the following: - The rawDisk.source URL - The sourceDisk URL - The sourceImage URL - The sourceSnapshot URL  |
| `sourceDisk` | `string` | URL of the source disk used to create this image. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /disks/disk - projects/project/zones/zone/disks/disk - zones/zone/disks/disk In order to create an image, you must provide the full or partial URL of one of the following: - The rawDisk.source URL - The sourceDisk URL - The sourceImage URL - The sourceSnapshot URL  |
| `architecture` | `string` | The architecture of the image. Valid values are ARM64 or X86_64. |
| `sourceSnapshotId` | `string` | [Output Only] The ID value of the snapshot used to create this image. This value may be used to determine whether the snapshot was taken from the current or a previous instance of a given snapshot name. |
| `rawDisk` | `object` | The parameters of the raw disk image. |
| `shieldedInstanceInitialState` | `object` | Initial State for shielded instance, these are public keys which are safe to store in public |
| `archiveSizeBytes` | `string` | Size of the image tar.gz archive stored in Google Cloud Storage (in bytes). |
| `sourceSnapshotEncryptionKey` | `object` |  |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#image for images. |
| `licenseCodes` | `array` | Integer license codes indicating which licenses are attached to this image. |
| `sourceDiskEncryptionKey` | `object` |  |
| `status` | `string` | [Output Only] The status of the image. An image can be used to create other resources, such as instances, only after the image has been successfully created and the status is set to READY. Possible values are FAILED, PENDING, or READY. |
| `imageEncryptionKey` | `object` |  |
| `sourceImage` | `string` | URL of the source image used to create this image. The following are valid formats for the URL: - https://www.googleapis.com/compute/v1/projects/project_id/global/ images/image_name - projects/project_id/global/images/image_name In order to create an image, you must provide the full or partial URL of one of the following: - The rawDisk.source URL - The sourceDisk URL - The sourceImage URL - The sourceSnapshot URL  |
| `storageLocations` | `array` | Cloud Storage bucket storage location of the image (regional or multi-regional). |
| `diskSizeGb` | `string` | Size of the image when restored onto a persistent disk (in GB). |
| `selfLink` | `string` | [Output Only] Server-defined URL for the resource. |
| `satisfiesPzs` | `boolean` | [Output Only] Reserved for future use. |
| `guestOsFeatures` | `array` | A list of features to enable on the guest operating system. Applicable only for bootable images. To see a list of available options, see the guestOSfeatures[].type parameter. |
| `sourceDiskId` | `string` | [Output Only] The ID value of the disk used to create this image. This value may be used to determine whether the image was taken from the current or a previous instance of a given disk name. |
| `labelFingerprint` | `string` | A fingerprint for the labels being applied to this image, which is essentially a hash of the labels used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve an image. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `image, project` | Returns the specified image. Gets a list of available images by making a list() request. |
| `list` | `SELECT` | `project` | Retrieves the list of custom images available to the specified project. Custom images are images you create that belong to your project. This method does not get any images that belong to other projects, including publicly-available images, like Debian 8. If you want to get a list of publicly-available images, use this method to make a request to the respective image project, such as debian-cloud or windows-cloud. |
| `insert` | `INSERT` | `project` | Creates an image in the specified project using the data included in the request. |
| `delete` | `DELETE` | `image, project` | Deletes the specified image. |
| `deprecate` | `EXEC` | `image, project` | Sets the deprecation status of an image. If an empty request body is given, clears the deprecation status instead. |
| `patch` | `EXEC` | `image, project` | Patches the specified image with the data included in the request. Only the following fields can be modified: family, description, deprecation status. |
| `setLabels` | `EXEC` | `project, resource` | Sets the labels on an image. To learn more about labels, read the Labeling Resources documentation. |
