---
title: objects
hide_title: false
hide_table_of_contents: false
keywords:
  - objects
  - storage
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
<tr><td><b>Name</b></td><td><code>objects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.storage.objects</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of the object, including the bucket name, object name, and generation number. |
| `name` | `string` | The name of the object. Required if not specified by URL parameter. |
| `contentEncoding` | `string` | Content-Encoding of the object data. |
| `kmsKeyName` | `string` | Not currently supported. Specifying the parameter causes the request to fail with status code 400 - Bad Request. |
| `retentionExpirationTime` | `string` | A server-determined value that specifies the earliest time that the object's retention period expires. This value is in RFC 3339 format. Note 1: This field is not provided for objects with an active event-based hold, since retention expiration is unknown until the hold is removed. Note 2: This value can be provided even when temporary hold is set (so that the user can reason about policy without having to first unset the temporary hold). |
| `cacheControl` | `string` | Cache-Control directive for the object data. If omitted, and the object is accessible to all anonymous users, the default will be public, max-age=3600. |
| `contentType` | `string` | Content-Type of the object data. If an object is stored without a Content-Type, it is served as application/octet-stream. |
| `etag` | `string` | HTTP 1.1 Entity tag for the object. |
| `mediaLink` | `string` | Media download link. |
| `size` | `string` | Content-Length of the data in bytes. |
| `kind` | `string` | The kind of item this is. For objects, this is always storage#object. |
| `storageClass` | `string` | Storage class of the object. |
| `eventBasedHold` | `boolean` | Whether an object is under event-based hold. Event-based hold is a way to retain objects until an event occurs, which is signified by the hold's release (i.e. this value is set to false). After being released (set to false), such objects will be subject to bucket-level retention (if any). One sample use case of this flag is for banks to hold loan documents for at least 3 years after loan is paid in full. Here, bucket-level retention is 3 years and the event is the loan being paid in full. In this example, these objects will be held intact for any number of years until the event has occurred (event-based hold on the object is released) and then 3 more years after that. That means retention duration of the objects begins from the moment event-based hold transitioned from true to false. |
| `acl` | `array` | Access controls on the object. |
| `md5Hash` | `string` | MD5 hash of the data; encoded using base64. For more information about using the MD5 hash, see Hashes and ETags: Best Practices. |
| `timeStorageClassUpdated` | `string` | The time at which the object's storage class was last changed. When the object is initially created, it will be set to timeCreated. |
| `customTime` | `string` | A timestamp in RFC 3339 format specified by the user for an object. |
| `selfLink` | `string` | The link to this object. |
| `generation` | `string` | The content generation of this object. Used for object versioning. |
| `componentCount` | `integer` | Number of underlying components that make up this object. Components are accumulated by compose operations. |
| `updated` | `string` | The modification time of the object metadata in RFC 3339 format. Set initially to object creation time and then updated whenever any metadata of the object changes. This includes changes made by a requester, such as modifying custom metadata, as well as changes made by Cloud Storage on behalf of a requester, such as changing the storage class based on an Object Lifecycle Configuration. |
| `crc32c` | `string` | CRC32c checksum, as described in RFC 4960, Appendix B; encoded using base64 in big-endian byte order. For more information about using the CRC32c checksum, see Hashes and ETags: Best Practices. |
| `bucket` | `string` | The name of the bucket containing this object. |
| `metadata` | `object` | User-provided metadata, in key/value pairs. |
| `timeCreated` | `string` | The creation time of the object in RFC 3339 format. |
| `temporaryHold` | `boolean` | Whether an object is under temporary hold. While this flag is set to true, the object is protected against deletion and overwrites. A common use case of this flag is regulatory investigations where objects need to be retained while the investigation is ongoing. Note that unlike event-based hold, temporary hold does not impact retention expiration time of an object. |
| `contentDisposition` | `string` | Content-Disposition of the object data. |
| `owner` | `object` | The owner of the object. This will always be the uploader of the object. |
| `metageneration` | `string` | The version of the metadata for this object at this generation. Used for preconditions and for detecting changes in metadata. A metageneration number is only meaningful in the context of a particular generation of a particular object. |
| `timeDeleted` | `string` | The deletion time of the object in RFC 3339 format. Will be returned if and only if this version of the object has been deleted. |
| `customerEncryption` | `object` | Metadata of customer-supplied encryption key, if the object is encrypted by such a key. |
| `contentLanguage` | `string` | Content-Language of the object data. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `bucket, object` | Retrieves an object or its metadata. |
| `list` | `SELECT` | `bucket` | Retrieves a list of objects matching the criteria. |
| `insert` | `INSERT` | `bucket` | Stores a new object and metadata. |
| `delete` | `DELETE` | `bucket, object` | Deletes an object and its metadata. Deletions are permanent if versioning is not enabled for the bucket, or if the generation parameter is used. |
| `compose` | `EXEC` | `destinationBucket, destinationObject` | Concatenates a list of existing objects into a new object in the same bucket. |
| `copy` | `EXEC` | `destinationBucket, destinationObject, sourceBucket, sourceObject` | Copies a source object to a destination object. Optionally overrides metadata. |
| `patch` | `EXEC` | `bucket, object` | Patches an object's metadata. |
| `rewrite` | `EXEC` | `destinationBucket, destinationObject, sourceBucket, sourceObject` | Rewrites a source object to a destination object. Optionally overrides metadata. |
| `update` | `EXEC` | `bucket, object` | Updates an object's metadata. |
| `watchAll` | `EXEC` | `bucket` | Watch for changes on all objects in a bucket. |
