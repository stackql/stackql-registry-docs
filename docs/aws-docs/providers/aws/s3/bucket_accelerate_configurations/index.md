---
title: bucket_accelerate_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_accelerate_configurations
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
<tr><td><b>Name</b></td><td><code>bucket_accelerate_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.bucket_accelerate_configurations</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bucket_accelerate_configurations_Get` | `SELECT` | `accelerate` | &lt;p&gt;This implementation of the GET action uses the &lt;code&gt;accelerate&lt;/code&gt; subresource to return the Transfer Acceleration state of a bucket, which is either &lt;code&gt;Enabled&lt;/code&gt; or &lt;code&gt;Suspended&lt;/code&gt;. Amazon S3 Transfer Acceleration is a bucket-level feature that enables you to perform faster data transfers to and from Amazon S3.&lt;/p&gt; &lt;p&gt;To use this operation, you must have permission to perform the &lt;code&gt;s3:GetAccelerateConfiguration&lt;/code&gt; action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources"&gt;Permissions Related to Bucket Subresource Operations&lt;/a&gt; and &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html"&gt;Managing Access Permissions to your Amazon S3 Resources&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;You set the Transfer Acceleration state of an existing bucket to &lt;code&gt;Enabled&lt;/code&gt; or &lt;code&gt;Suspended&lt;/code&gt; by using the &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAccelerateConfiguration.html"&gt;PutBucketAccelerateConfiguration&lt;/a&gt; operation. &lt;/p&gt; &lt;p&gt;A GET &lt;code&gt;accelerate&lt;/code&gt; request does not return a state value for a bucket that has no transfer acceleration state. A bucket has no Transfer Acceleration state if a state has never been set on the bucket. &lt;/p&gt; &lt;p&gt;For more information about transfer acceleration, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html"&gt;Transfer Acceleration&lt;/a&gt; in the Amazon S3 User Guide.&lt;/p&gt; &lt;p class="title"&gt; &lt;b&gt;Related Resources&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketAccelerateConfiguration.html"&gt;PutBucketAccelerateConfiguration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `bucket_accelerate_configurations_Put` | `EXEC` | `accelerate` | &lt;p&gt;Sets the accelerate configuration of an existing bucket. Amazon S3 Transfer Acceleration is a bucket-level feature that enables you to perform faster data transfers to Amazon S3.&lt;/p&gt; &lt;p&gt; To use this operation, you must have permission to perform the &lt;code&gt;s3:PutAccelerateConfiguration&lt;/code&gt; action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources"&gt;Permissions Related to Bucket Subresource Operations&lt;/a&gt; and &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html"&gt;Managing Access Permissions to Your Amazon S3 Resources&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; The Transfer Acceleration state of a bucket can be set to one of the following two values:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; Enabled – Enables accelerated data transfers to the bucket.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; Suspended – Disables accelerated data transfers to the bucket.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAccelerateConfiguration.html"&gt;GetBucketAccelerateConfiguration&lt;/a&gt; action returns the transfer acceleration state of a bucket.&lt;/p&gt; &lt;p&gt;After setting the Transfer Acceleration state of a bucket to Enabled, it might take up to thirty minutes before the data transfer rates to the bucket increase.&lt;/p&gt; &lt;p&gt; The name of the bucket used for Transfer Acceleration must be DNS-compliant and must not contain periods (".").&lt;/p&gt; &lt;p&gt; For more information about transfer acceleration, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/transfer-acceleration.html"&gt;Transfer Acceleration&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;PutBucketAccelerateConfiguration&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketAccelerateConfiguration.html"&gt;GetBucketAccelerateConfiguration&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html"&gt;CreateBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
