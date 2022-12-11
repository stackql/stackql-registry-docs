---
title: bucket_versionings
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_versionings
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
<tr><td><b>Name</b></td><td><code>bucket_versionings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.bucket_versionings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `MfaDelete` | `string` | Specifies whether MFA delete is enabled in the bucket versioning configuration. This element is only returned if the bucket has been configured with MFA delete. If the bucket has never been so configured, this element is not returned. |
| `Status` | `string` | The versioning state of the bucket. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bucket_versionings_Get` | `SELECT` | `versioning` | &lt;p&gt;Returns the versioning state of a bucket.&lt;/p&gt; &lt;p&gt;To retrieve the versioning state of a bucket, you must be the bucket owner.&lt;/p&gt; &lt;p&gt;This implementation also returns the MFA Delete status of the versioning state. If the MFA Delete status is &lt;code&gt;enabled&lt;/code&gt;, the bucket owner must use an authentication device to change the versioning state of the bucket.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;GetBucketVersioning&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html"&gt;GetObject&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html"&gt;PutObject&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteObject.html"&gt;DeleteObject&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `bucket_versionings_Put` | `EXEC` | `versioning` | &lt;p&gt;Sets the versioning state of an existing bucket.&lt;/p&gt; &lt;p&gt;You can set the versioning state with one of the following values:&lt;/p&gt; &lt;p&gt; &lt;b&gt;Enabled&lt;/b&gt;—Enables versioning for the objects in the bucket. All objects added to the bucket receive a unique version ID.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Suspended&lt;/b&gt;—Disables versioning for the objects in the bucket. All objects added to the bucket receive the version ID null.&lt;/p&gt; &lt;p&gt;If the versioning state has never been set on a bucket, it has no versioning state; a &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html"&gt;GetBucketVersioning&lt;/a&gt; request does not return a versioning state value.&lt;/p&gt; &lt;p&gt;In order to enable MFA Delete, you must be the bucket owner. If you are the bucket owner and want to enable MFA Delete in the bucket versioning configuration, you must include the &lt;code&gt;x-amz-mfa request&lt;/code&gt; header and the &lt;code&gt;Status&lt;/code&gt; and the &lt;code&gt;MfaDelete&lt;/code&gt; request elements in a request to set the versioning state of the bucket.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If you have an object expiration lifecycle policy in your non-versioned bucket and you want to maintain the same permanent delete behavior when you enable versioning, you must add a noncurrent expiration policy. The noncurrent expiration lifecycle policy will manage the deletes of the noncurrent object versions in the version-enabled bucket. (A version-enabled bucket maintains one current and zero or more noncurrent object versions.) For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html#lifecycle-and-other-bucket-config"&gt;Lifecycle and Versioning&lt;/a&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p class="title"&gt; &lt;b&gt;Related Resources&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html"&gt;CreateBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html"&gt;DeleteBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketVersioning.html"&gt;GetBucketVersioning&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
