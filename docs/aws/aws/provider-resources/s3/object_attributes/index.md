---
title: object_attributes
hide_title: false
hide_table_of_contents: false
keywords:
  - object_attributes
  - s3
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>object_attributes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.object_attributes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `ETag` | `string` | An ETag is an opaque identifier assigned by a web server to a specific version of a resource found at a URL. |
| `ObjectParts` | `object` | A collection of parts associated with a multipart upload. |
| `ObjectSize` | `integer` | The size of the object in bytes. |
| `StorageClass` | `string` | &lt;p&gt;Provides the storage class information of the object. Amazon S3 returns this header for all objects except for S3 Standard storage class objects.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/storage-class-intro.html"&gt;Storage Classes&lt;/a&gt;.&lt;/p&gt; |
| `Checksum` | `object` | Contains all the possible checksum or digest values for an object. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `object_attributes_Get` | `SELECT` | `Key, attributes, x-amz-object-attributes` |
