---
title: public_access_blocks
hide_title: false
hide_table_of_contents: false
keywords:
  - public_access_blocks
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
<tr><td><b>Name</b></td><td><code>public_access_blocks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.public_access_blocks</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `public_access_blocks_Get` | `SELECT` | `publicAccessBlock` | &lt;p&gt;Retrieves the &lt;code&gt;PublicAccessBlock&lt;/code&gt; configuration for an Amazon S3 bucket. To use this operation, you must have the &lt;code&gt;s3:GetBucketPublicAccessBlock&lt;/code&gt; permission. For more information about Amazon S3 permissions, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html"&gt;Specifying Permissions in a Policy&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When Amazon S3 evaluates the &lt;code&gt;PublicAccessBlock&lt;/code&gt; configuration for a bucket or an object, it checks the &lt;code&gt;PublicAccessBlock&lt;/code&gt; configuration for both the bucket (or the bucket that contains the object) and the bucket owner's account. If the &lt;code&gt;PublicAccessBlock&lt;/code&gt; settings are different between the bucket and the account, Amazon S3 uses the most restrictive combination of the bucket-level and account-level settings.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about when Amazon S3 considers a bucket or an object public, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status"&gt;The Meaning of "Public"&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;GetPublicAccessBlock&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html"&gt;Using Amazon S3 Block Public Access&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html"&gt;PutPublicAccessBlock&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html"&gt;GetPublicAccessBlock&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeletePublicAccessBlock.html"&gt;DeletePublicAccessBlock&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `public_access_blocks_Delete` | `DELETE` | `publicAccessBlock` | &lt;p&gt;Removes the &lt;code&gt;PublicAccessBlock&lt;/code&gt; configuration for an Amazon S3 bucket. To use this operation, you must have the &lt;code&gt;s3:PutBucketPublicAccessBlock&lt;/code&gt; permission. For more information about permissions, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources"&gt;Permissions Related to Bucket Subresource Operations&lt;/a&gt; and &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html"&gt;Managing Access Permissions to Your Amazon S3 Resources&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;DeletePublicAccessBlock&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html"&gt;Using Amazon S3 Block Public Access&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html"&gt;GetPublicAccessBlock&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutPublicAccessBlock.html"&gt;PutPublicAccessBlock&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicyStatus.html"&gt;GetBucketPolicyStatus&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `public_access_blocks_Put` | `EXEC` | `publicAccessBlock` | &lt;p&gt;Creates or modifies the &lt;code&gt;PublicAccessBlock&lt;/code&gt; configuration for an Amazon S3 bucket. To use this operation, you must have the &lt;code&gt;s3:PutBucketPublicAccessBlock&lt;/code&gt; permission. For more information about Amazon S3 permissions, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html"&gt;Specifying Permissions in a Policy&lt;/a&gt;.&lt;/p&gt; &lt;important&gt; &lt;p&gt;When Amazon S3 evaluates the &lt;code&gt;PublicAccessBlock&lt;/code&gt; configuration for a bucket or an object, it checks the &lt;code&gt;PublicAccessBlock&lt;/code&gt; configuration for both the bucket (or the bucket that contains the object) and the bucket owner's account. If the &lt;code&gt;PublicAccessBlock&lt;/code&gt; configurations are different between the bucket and the account, Amazon S3 uses the most restrictive combination of the bucket-level and account-level settings.&lt;/p&gt; &lt;/important&gt; &lt;p&gt;For more information about when Amazon S3 considers a bucket or an object public, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status"&gt;The Meaning of "Public"&lt;/a&gt;.&lt;/p&gt; &lt;p class="title"&gt; &lt;b&gt;Related Resources&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetPublicAccessBlock.html"&gt;GetPublicAccessBlock&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeletePublicAccessBlock.html"&gt;DeletePublicAccessBlock&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketPolicyStatus.html"&gt;GetBucketPolicyStatus&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html"&gt;Using Amazon S3 Block Public Access&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
