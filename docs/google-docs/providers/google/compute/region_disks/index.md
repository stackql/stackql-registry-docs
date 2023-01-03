---
title: region_disks
hide_title: false
hide_table_of_contents: false
keywords:
  - region_disks
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
<tr><td><b>Name</b></td><td><code>region_disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.compute.region_disks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | [Output Only] The unique identifier for the resource. This identifier is defined by the server. |
| `name` | `string` | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| `description` | `string` | An optional description of this resource. Provide this property when you create the resource. |
| `labels` | `object` | Labels to apply to this disk. These can be later modified by the setLabels method. |
| `sourceSnapshotId` | `string` | [Output Only] The unique ID of the snapshot used to create this disk. This value identifies the exact snapshot that was used to create this persistent disk. For example, if you created the persistent disk from a snapshot that was later deleted and recreated under the same name, the source snapshot ID would identify the exact version of the snapshot that was used. |
| `sourceDisk` | `string` | The source disk used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone /disks/disk - https://www.googleapis.com/compute/v1/projects/project/regions/region /disks/disk - projects/project/zones/zone/disks/disk - projects/project/regions/region/disks/disk - zones/zone/disks/disk - regions/region/disks/disk  |
| `selfLink` | `string` | [Output Only] Server-defined fully-qualified URL for this resource. |
| `guestOsFeatures` | `array` | A list of features to enable on the guest operating system. Applicable only for bootable images. Read Enabling guest operating system features to see a list of available options. |
| `status` | `string` | [Output Only] The status of disk creation. - CREATING: Disk is provisioning. - RESTORING: Source data is being copied into the disk. - FAILED: Disk creation failed. - READY: Disk is ready for use. - DELETING: Disk is deleting.  |
| `diskEncryptionKey` | `object` |  |
| `licenses` | `array` | A list of publicly visible licenses. Reserved for Google's use. |
| `type` | `string` | URL of the disk type resource describing which disk type to use to create the disk. Provide this when creating the disk. For example: projects/project /zones/zone/diskTypes/pd-ssd . See Persistent disk types. |
| `licenseCodes` | `array` | Integer license codes indicating which licenses are attached to this disk. |
| `sourceImageId` | `string` | [Output Only] The ID value of the image used to create this disk. This value identifies the exact image that was used to create this persistent disk. For example, if you created the persistent disk from an image that was later deleted and recreated under the same name, the source image ID would identify the exact version of the image that was used. |
| `replicaZones` | `array` | URLs of the zones where the disk should be replicated to. Only applicable for regional resources. |
| `sourceImage` | `string` | The source image used to create this disk. If the source image is deleted, this field will not be set. To create a disk with one of the public operating system images, specify the image by its family name. For example, specify family/debian-9 to use the latest Debian 9 image: projects/debian-cloud/global/images/family/debian-9 Alternatively, use a specific version of a public operating system image: projects/debian-cloud/global/images/debian-9-stretch-vYYYYMMDD To create a disk with a custom image that you created, specify the image name in the following format: global/images/my-custom-image You can also specify a custom image by its image family, which returns the latest version of the image in that family. Replace the image name with family/family-name: global/images/family/my-image-family  |
| `sourceImageEncryptionKey` | `object` |  |
| `satisfiesPzs` | `boolean` | [Output Only] Reserved for future use. |
| `architecture` | `string` | The architecture of the disk. Valid values are ARM64 or X86_64. |
| `lastAttachTimestamp` | `string` | [Output Only] Last attach timestamp in RFC3339 text format. |
| `kind` | `string` | [Output Only] Type of the resource. Always compute#disk for disks. |
| `resourcePolicies` | `array` | Resource policies applied to this disk for automatic snapshot creations. |
| `sourceSnapshot` | `string` | The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project /global/snapshots/snapshot - projects/project/global/snapshots/snapshot - global/snapshots/snapshot  |
| `sourceStorageObject` | `string` | The full Google Cloud Storage URI where the disk image is stored. This file must be a gzip-compressed tarball whose name ends in .tar.gz or virtual machine disk whose name ends in vmdk. Valid URIs may start with gs:// or https://storage.googleapis.com/. This flag is not optimized for creating multiple disks from a source storage object. To create many disks from a source storage object, use gcloud compute images import instead. |
| `labelFingerprint` | `string` | A fingerprint for the labels being applied to this disk, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a disk. |
| `region` | `string` | [Output Only] URL of the region where the disk resides. Only applicable for regional resources. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `locationHint` | `string` | An opaque location hint used to place the disk close to other resources. This field is for use by internal tools that use the public API. |
| `lastDetachTimestamp` | `string` | [Output Only] Last detach timestamp in RFC3339 text format. |
| `sizeGb` | `string` | Size, in GB, of the persistent disk. You can specify this field when creating a persistent disk using the sourceImage, sourceSnapshot, or sourceDisk parameter, or specify it alone to create an empty persistent disk. If you specify this field along with a source, the value of sizeGb must not be less than the size of the source. Acceptable values are 1 to 65536, inclusive. |
| `users` | `array` | [Output Only] Links to the users of the disk (attached instances) in form: projects/project/zones/zone/instances/instance |
| `sourceDiskId` | `string` | [Output Only] The unique ID of the disk used to create this disk. This value identifies the exact disk that was used to create this persistent disk. For example, if you created the persistent disk from a disk that was later deleted and recreated under the same name, the source disk ID would identify the exact version of the disk that was used. |
| `sourceSnapshotEncryptionKey` | `object` |  |
| `creationTimestamp` | `string` | [Output Only] Creation timestamp in RFC3339 text format. |
| `physicalBlockSizeBytes` | `string` | Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used. The currently supported size is 4096, other sizes may be added in the future. If an unsupported value is requested, the error message will list the supported values for the caller's project. |
| `options` | `string` | Internal use only. |
| `zone` | `string` | [Output Only] URL of the zone where the disk resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| `provisionedIops` | `string` | Indicates how many IOPS to provision for the disk. This sets the number of I/O operations per second that the disk can handle. Values must be between 10,000 and 120,000. For more details, see the Extreme persistent disk documentation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `regionDisks_get` | `SELECT` | `disk, project, region` | Returns a specified regional persistent disk. |
| `regionDisks_list` | `SELECT` | `project, region` | Retrieves the list of persistent disks contained within the specified region. |
| `regionDisks_insert` | `INSERT` | `project, region` | Creates a persistent regional disk in the specified project using the data included in the request. |
| `regionDisks_delete` | `DELETE` | `disk, project, region` | Deletes the specified regional persistent disk. Deleting a regional disk removes all the replicas of its data permanently and is irreversible. However, deleting a disk does not delete any snapshots previously made from the disk. You must separately delete snapshots. |
| `regionDisks_resize` | `EXEC` | `disk, project, region` | Resizes the specified regional persistent disk. |
| `regionDisks_setLabels` | `EXEC` | `project, region, resource` | Sets the labels on the target regional disk. |
