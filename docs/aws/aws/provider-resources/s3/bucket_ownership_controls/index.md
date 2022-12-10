---
title: bucket_ownership_controls
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_ownership_controls
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
<tr><td><b>Name</b></td><td><code>bucket_ownership_controls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.bucket_ownership_controls</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bucket_ownership_controls_Get` | `SELECT` | `ownershipControls` | &lt;p&gt;Retrieves &lt;code&gt;OwnershipControls&lt;/code&gt; for an Amazon S3 bucket. To use this operation, you must have the &lt;code&gt;s3:GetBucketOwnershipControls&lt;/code&gt; permission. For more information about Amazon S3 permissions, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html"&gt;Specifying permissions in a policy&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;For information about Amazon S3 Object Ownership, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html"&gt;Using Object Ownership&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;GetBucketOwnershipControls&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PutBucketOwnershipControls&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteBucketOwnershipControls&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `bucket_ownership_controls_Delete` | `DELETE` | `ownershipControls` | &lt;p&gt;Removes &lt;code&gt;OwnershipControls&lt;/code&gt; for an Amazon S3 bucket. To use this operation, you must have the &lt;code&gt;s3:PutBucketOwnershipControls&lt;/code&gt; permission. For more information about Amazon S3 permissions, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/using-with-s3-actions.html"&gt;Specifying Permissions in a Policy&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;For information about Amazon S3 Object Ownership, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/about-object-ownership.html"&gt;Using Object Ownership&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;DeleteBucketOwnershipControls&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetBucketOwnershipControls&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;PutBucketOwnershipControls&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `bucket_ownership_controls_Put` | `EXEC` | `ownershipControls` | &lt;p&gt;Creates or modifies &lt;code&gt;OwnershipControls&lt;/code&gt; for an Amazon S3 bucket. To use this operation, you must have the &lt;code&gt;s3:PutBucketOwnershipControls&lt;/code&gt; permission. For more information about Amazon S3 permissions, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/user-guide/using-with-s3-actions.html"&gt;Specifying permissions in a policy&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;For information about Amazon S3 Object Ownership, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/user-guide/about-object-ownership.html"&gt;Using object ownership&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;PutBucketOwnershipControls&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;GetBucketOwnershipControls&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a&gt;DeleteBucketOwnershipControls&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
