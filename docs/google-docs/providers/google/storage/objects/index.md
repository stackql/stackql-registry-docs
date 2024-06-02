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
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>objects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="storage.objects" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the object, including the bucket name, object name, and generation number. |
| <CopyableCode code="name" /> | `string` | The name of the object. Required if not specified by URL parameter. |
| <CopyableCode code="acl" /> | `array` | Access controls on the object. |
| <CopyableCode code="bucket" /> | `string` | The name of the bucket containing this object. |
| <CopyableCode code="cacheControl" /> | `string` | Cache-Control directive for the object data. If omitted, and the object is accessible to all anonymous users, the default will be public, max-age=3600. |
| <CopyableCode code="componentCount" /> | `integer` | Number of underlying components that make up this object. Components are accumulated by compose operations. |
| <CopyableCode code="contentDisposition" /> | `string` | Content-Disposition of the object data. |
| <CopyableCode code="contentEncoding" /> | `string` | Content-Encoding of the object data. |
| <CopyableCode code="contentLanguage" /> | `string` | Content-Language of the object data. |
| <CopyableCode code="contentType" /> | `string` | Content-Type of the object data. If an object is stored without a Content-Type, it is served as application/octet-stream. |
| <CopyableCode code="crc32c" /> | `string` | CRC32c checksum, as described in RFC 4960, Appendix B; encoded using base64 in big-endian byte order. For more information about using the CRC32c checksum, see Hashes and ETags: Best Practices. |
| <CopyableCode code="customTime" /> | `string` | A timestamp in RFC 3339 format specified by the user for an object. |
| <CopyableCode code="customerEncryption" /> | `object` | Metadata of customer-supplied encryption key, if the object is encrypted by such a key. |
| <CopyableCode code="etag" /> | `string` | HTTP 1.1 Entity tag for the object. |
| <CopyableCode code="eventBasedHold" /> | `boolean` | Whether an object is under event-based hold. Event-based hold is a way to retain objects until an event occurs, which is signified by the hold's release (i.e. this value is set to false). After being released (set to false), such objects will be subject to bucket-level retention (if any). One sample use case of this flag is for banks to hold loan documents for at least 3 years after loan is paid in full. Here, bucket-level retention is 3 years and the event is the loan being paid in full. In this example, these objects will be held intact for any number of years until the event has occurred (event-based hold on the object is released) and then 3 more years after that. That means retention duration of the objects begins from the moment event-based hold transitioned from true to false. |
| <CopyableCode code="generation" /> | `string` | The content generation of this object. Used for object versioning. |
| <CopyableCode code="hardDeleteTime" /> | `string` | This is the time (in the future) when the soft-deleted object will no longer be restorable. It is equal to the soft delete time plus the current soft delete retention duration of the bucket. |
| <CopyableCode code="kind" /> | `string` | The kind of item this is. For objects, this is always storage#object. |
| <CopyableCode code="kmsKeyName" /> | `string` | Not currently supported. Specifying the parameter causes the request to fail with status code 400 - Bad Request. |
| <CopyableCode code="md5Hash" /> | `string` | MD5 hash of the data; encoded using base64. For more information about using the MD5 hash, see Hashes and ETags: Best Practices. |
| <CopyableCode code="mediaLink" /> | `string` | Media download link. |
| <CopyableCode code="metadata" /> | `object` | User-provided metadata, in key/value pairs. |
| <CopyableCode code="metageneration" /> | `string` | The version of the metadata for this object at this generation. Used for preconditions and for detecting changes in metadata. A metageneration number is only meaningful in the context of a particular generation of a particular object. |
| <CopyableCode code="owner" /> | `object` | The owner of the object. This will always be the uploader of the object. |
| <CopyableCode code="retention" /> | `object` | A collection of object level retention parameters. |
| <CopyableCode code="retentionExpirationTime" /> | `string` | A server-determined value that specifies the earliest time that the object's retention period expires. This value is in RFC 3339 format. Note 1: This field is not provided for objects with an active event-based hold, since retention expiration is unknown until the hold is removed. Note 2: This value can be provided even when temporary hold is set (so that the user can reason about policy without having to first unset the temporary hold). |
| <CopyableCode code="selfLink" /> | `string` | The link to this object. |
| <CopyableCode code="size" /> | `string` | Content-Length of the data in bytes. |
| <CopyableCode code="softDeleteTime" /> | `string` | The time at which the object became soft-deleted in RFC 3339 format. |
| <CopyableCode code="storageClass" /> | `string` | Storage class of the object. |
| <CopyableCode code="temporaryHold" /> | `boolean` | Whether an object is under temporary hold. While this flag is set to true, the object is protected against deletion and overwrites. A common use case of this flag is regulatory investigations where objects need to be retained while the investigation is ongoing. Note that unlike event-based hold, temporary hold does not impact retention expiration time of an object. |
| <CopyableCode code="timeCreated" /> | `string` | The creation time of the object in RFC 3339 format. |
| <CopyableCode code="timeDeleted" /> | `string` | The time at which the object became noncurrent in RFC 3339 format. Will be returned if and only if this version of the object has been deleted. |
| <CopyableCode code="timeStorageClassUpdated" /> | `string` | The time at which the object's storage class was last changed. When the object is initially created, it will be set to timeCreated. |
| <CopyableCode code="updated" /> | `string` | The modification time of the object metadata in RFC 3339 format. Set initially to object creation time and then updated whenever any metadata of the object changes. This includes changes made by a requester, such as modifying custom metadata, as well as changes made by Cloud Storage on behalf of a requester, such as changing the storage class based on an Object Lifecycle Configuration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="bucket, object" /> | Retrieves an object or its metadata. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="bucket" /> | Retrieves a list of objects matching the criteria. |
| <CopyableCode code="insert" /> | `INSERT` | <CopyableCode code="bucket" /> | Stores a new object and metadata. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="bucket, object" /> | Deletes an object and its metadata. Deletions are permanent if versioning is not enabled for the bucket, or if the generation parameter is used. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="bucket" /> | Retrieves a list of objects matching the criteria. |
| <CopyableCode code="bulk_restore" /> | `EXEC` | <CopyableCode code="bucket" /> | Initiates a long-running bulk restore operation on the specified bucket. |
| <CopyableCode code="compose" /> | `EXEC` | <CopyableCode code="destinationBucket, destinationObject" /> | Concatenates a list of existing objects into a new object in the same bucket. |
| <CopyableCode code="copy" /> | `EXEC` | <CopyableCode code="destinationBucket, destinationObject, sourceBucket, sourceObject" /> | Copies a source object to a destination object. Optionally overrides metadata. |
| <CopyableCode code="patch" /> | `EXEC` | <CopyableCode code="bucket, object" /> | Patches an object's metadata. |
| <CopyableCode code="restore" /> | `EXEC` | <CopyableCode code="bucket, generation, object" /> | Restores a soft-deleted object. |
| <CopyableCode code="rewrite" /> | `EXEC` | <CopyableCode code="destinationBucket, destinationObject, sourceBucket, sourceObject" /> | Rewrites a source object to a destination object. Optionally overrides metadata. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="bucket, object" /> | Updates an object's metadata. |
| <CopyableCode code="watch_all" /> | `EXEC` | <CopyableCode code="bucket" /> | Watch for changes on all objects in a bucket. |
