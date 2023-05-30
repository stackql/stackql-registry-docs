---
title: buckets
hide_title: false
hide_table_of_contents: false
keywords:
  - buckets
  - object_storage
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>buckets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.object_storage.buckets</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `hostname` | `string` | The hostname where this bucket can be accessed. This hostname can be accessed through a browser if the bucket is made public.<br /> |
| `label` | `string` | The name of this bucket. |
| `objects` | `integer` | The number of objects stored in this bucket.<br /> |
| `size` | `integer` | The size of the bucket in bytes. |
| `cluster` | `string` | The ID of the Object Storage Cluster this bucket is in. |
| `created` | `string` | When this bucket was created. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getObjectStorageBucket` | `SELECT` | `bucket, clusterId` | Returns a single Object Storage Bucket.<br /><br /><br />This endpoint is available for convenience. It is recommended that instead you<br />use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly.<br /> |
| `getObjectStorageBucketinCluster` | `SELECT` | `clusterId` | Returns a list of Buckets in this cluster belonging to this Account.<br /><br /><br />This endpoint is available for convenience. It is recommended that instead you<br />use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly.<br /> |
| `getObjectStorageBuckets` | `SELECT` |  | Returns a paginated list of all Object Storage Buckets that you own.<br /><br /><br />This endpoint is available for convenience. It is recommended that instead you<br />use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/serviceops/#list-buckets) directly.<br /> |
| `createObjectStorageBucket` | `INSERT` | `data__cluster, data__label` | Creates an Object Storage Bucket in the specified cluster.<br /><br />Accounts with negative balances cannot access this command.<br /><br />If the bucket already exists and is owned by you, this endpoint returns a `200` response with that bucket as if it had just been created.<br /><br />This endpoint is available for convenience. It is recommended that instead you use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket) directly.<br /> |
| `deleteObjectStorageBucket` | `DELETE` | `bucket, clusterId` | Removes a single bucket.<br /><br />Bucket objects must be removed prior to removing the bucket. While buckets containing objects _may_ be<br />deleted using the [s3cmd command-line tool](/docs/products/storage/object-storage/guides/s3cmd/#delete-a-bucket), such operations<br />can fail if the bucket contains too many objects. The recommended<br />way to empty large buckets is to use the [S3 API to configure lifecycle policies](https://docs.ceph.com/en/latest/radosgw/bucketpolicy/#) that<br />remove all objects, then delete the bucket.<br /><br />This endpoint is available for convenience. It is recommended that instead you<br />use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#delete-bucket) directly.<br /> |
| `_getObjectStorageBucket` | `EXEC` | `bucket, clusterId` | Returns a single Object Storage Bucket.<br /><br /><br />This endpoint is available for convenience. It is recommended that instead you<br />use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly.<br /> |
| `_getObjectStorageBucketinCluster` | `EXEC` | `clusterId` | Returns a list of Buckets in this cluster belonging to this Account.<br /><br /><br />This endpoint is available for convenience. It is recommended that instead you<br />use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#get-bucket) directly.<br /> |
| `_getObjectStorageBuckets` | `EXEC` |  | Returns a paginated list of all Object Storage Buckets that you own.<br /><br /><br />This endpoint is available for convenience. It is recommended that instead you<br />use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/serviceops/#list-buckets) directly.<br /> |
| `_viewObjectStorageBucketACL` | `EXEC` | `bucket, clusterId` | View an Object's configured Access Control List (ACL) in this Object Storage bucket.<br />ACLs define who can access your buckets and objects and specify the level of access<br />granted to those users.<br /><br /><br />This endpoint is available for convenience. It is recommended that instead you<br />use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object-acl) directly.<br /> |
| `modifyObjectStorageBucketAccess` | `EXEC` | `bucket, clusterId` | Allows changing basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings.<br />Only allows enabling/disabling CORS for all origins, and/or setting canned ACLs.<br /><br /><br />For more fine-grained control of both systems, please use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl) directly.<br /> |
| `updateObjectStorageBucketACL` | `EXEC` | `bucket, clusterId, data__acl, data__name` | Update an Object's configured Access Control List (ACL) in this Object Storage bucket.<br />ACLs define who can access your buckets and objects and specify the level of access<br />granted to those users.<br /><br /><br />This endpoint is available for convenience. It is recommended that instead you<br />use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#set-object-acl) directly.<br /> |
| `updateObjectStorageBucketAccess` | `EXEC` | `bucket, clusterId` | Allows changing basic Cross-origin Resource Sharing (CORS) and Access Control Level (ACL) settings.<br />Only allows enabling/disabling CORS for all origins, and/or setting canned ACLs.<br /><br /><br />For more fine-grained control of both systems, please use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/bucketops/#put-bucket-acl) directly.<br /> |
| `viewObjectStorageBucketACL` | `EXEC` | `bucket, clusterId` | View an Object's configured Access Control List (ACL) in this Object Storage bucket.<br />ACLs define who can access your buckets and objects and specify the level of access<br />granted to those users.<br /><br /><br />This endpoint is available for convenience. It is recommended that instead you<br />use the more [fully-featured S3 API](https://docs.ceph.com/en/latest/radosgw/s3/objectops/#get-object-acl) directly.<br /> |