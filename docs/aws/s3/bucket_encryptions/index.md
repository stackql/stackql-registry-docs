---
title: bucket_encryptions
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_encryptions
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
<tr><td><b>Name</b></td><td><code>bucket_encryptions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.bucket_encryptions</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bucket_encryptions_Get` | `SELECT` | `encryption` | &lt;p&gt;Returns the default encryption configuration for an Amazon S3 bucket. If the bucket does not have a default encryption configuration, GetBucketEncryption returns &lt;code&gt;ServerSideEncryptionConfigurationNotFoundError&lt;/code&gt;. &lt;/p&gt; &lt;p&gt;For information about the Amazon S3 default encryption feature, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html"&gt;Amazon S3 Default Bucket Encryption&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; To use this operation, you must have permission to perform the &lt;code&gt;s3:GetEncryptionConfiguration&lt;/code&gt; action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources"&gt;Permissions Related to Bucket Subresource Operations&lt;/a&gt; and &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html"&gt;Managing Access Permissions to Your Amazon S3 Resources&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;GetBucketEncryption&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html"&gt;PutBucketEncryption&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketEncryption.html"&gt;DeleteBucketEncryption&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `bucket_encryptions_Delete` | `DELETE` | `encryption` | &lt;p&gt;This implementation of the DELETE action removes default encryption from the bucket. For information about the Amazon S3 default encryption feature, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html"&gt;Amazon S3 Default Bucket Encryption&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p&gt;To use this operation, you must have permissions to perform the &lt;code&gt;s3:PutEncryptionConfiguration&lt;/code&gt; action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources"&gt;Permissions Related to Bucket Subresource Operations&lt;/a&gt; and &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html"&gt;Managing Access Permissions to your Amazon S3 Resources&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p class="title"&gt; &lt;b&gt;Related Resources&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketEncryption.html"&gt;PutBucketEncryption&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html"&gt;GetBucketEncryption&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `bucket_encryptions_Put` | `EXEC` | `encryption` | &lt;p&gt;This action uses the &lt;code&gt;encryption&lt;/code&gt; subresource to configure default encryption and Amazon S3 Bucket Key for an existing bucket.&lt;/p&gt; &lt;p&gt;Default encryption for a bucket can use server-side encryption with Amazon S3-managed keys (SSE-S3) or customer managed keys (SSE-KMS). If you specify default encryption using SSE-KMS, you can also configure Amazon S3 Bucket Key. When the default encryption is SSE-KMS, if you upload an object to the bucket and do not specify the KMS key to use for encryption, Amazon S3 uses the default Amazon Web Services managed KMS key for your account. For information about default encryption, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-encryption.html"&gt;Amazon S3 default bucket encryption&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;. For more information about S3 Bucket Keys, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/bucket-key.html"&gt;Amazon S3 Bucket Keys&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;This action requires Amazon Web Services Signature Version 4. For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/sig-v4-authenticating-requests.html"&gt; Authenticating Requests (Amazon Web Services Signature Version 4)&lt;/a&gt;. &lt;/p&gt; &lt;/important&gt; &lt;p&gt;To use this operation, you must have permissions to perform the &lt;code&gt;s3:PutEncryptionConfiguration&lt;/code&gt; action. The bucket owner has this permission by default. The bucket owner can grant this permission to others. For more information about permissions, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources"&gt;Permissions Related to Bucket Subresource Operations&lt;/a&gt; and &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html"&gt;Managing Access Permissions to Your Amazon S3 Resources&lt;/a&gt; in the Amazon S3 User Guide. &lt;/p&gt; &lt;p class="title"&gt; &lt;b&gt;Related Resources&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketEncryption.html"&gt;GetBucketEncryption&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketEncryption.html"&gt;DeleteBucketEncryption&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
