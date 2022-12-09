---
title: bucket_taggings
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_taggings
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
<tr><td><b>Name</b></td><td><code>bucket_taggings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.bucket_taggings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `Key` | `string` | Name of the object key. |
| `Value` | `string` | Value of the tag. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bucket_taggings_Get` | `SELECT` | `tagging` | &lt;p&gt;Returns the tag set associated with the bucket.&lt;/p&gt; &lt;p&gt;To use this operation, you must have permission to perform the &lt;code&gt;s3:GetBucketTagging&lt;/code&gt; action. By default, the bucket owner has this permission and can grant this permission to others.&lt;/p&gt; &lt;p&gt; &lt;code&gt;GetBucketTagging&lt;/code&gt; has the following special error:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Error code: &lt;code&gt;NoSuchTagSet&lt;/code&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Description: There is no tag set associated with the bucket.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The following operations are related to &lt;code&gt;GetBucketTagging&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html"&gt;PutBucketTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html"&gt;DeleteBucketTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `bucket_taggings_Delete` | `DELETE` | `tagging` | &lt;p&gt;Deletes the tags from the bucket.&lt;/p&gt; &lt;p&gt;To use this operation, you must have permission to perform the &lt;code&gt;s3:PutBucketTagging&lt;/code&gt; action. By default, the bucket owner has this permission and can grant this permission to others. &lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;DeleteBucketTagging&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html"&gt;GetBucketTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html"&gt;PutBucketTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `bucket_taggings_Put` | `EXEC` | `tagging` | &lt;p&gt;Sets the tags for a bucket.&lt;/p&gt; &lt;p&gt;Use tags to organize your Amazon Web Services bill to reflect your own cost structure. To do this, sign up to get your Amazon Web Services account bill with tag key values included. Then, to see the cost of combined resources, organize your billing information according to resources with the same tag key values. For example, you can tag several resources with a specific application name, and then organize your billing information to see the total cost of that application across several services. For more information, see &lt;a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html"&gt;Cost Allocation and Tagging&lt;/a&gt; and &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/CostAllocTagging.html"&gt;Using Cost Allocation in Amazon S3 Bucket Tags&lt;/a&gt;.&lt;/p&gt; &lt;note&gt; &lt;p&gt; When this operation sets the tags for a bucket, it will overwrite any current tags the bucket already has. You cannot use this operation to add tags to an existing list of tags.&lt;/p&gt; &lt;/note&gt; &lt;p&gt;To use this operation, you must have permissions to perform the &lt;code&gt;s3:PutBucketTagging&lt;/code&gt; action. The bucket owner has this permission by default and can grant this permission to others. For more information about permissions, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-with-s3-actions.html#using-with-s3-actions-related-to-bucket-subresources"&gt;Permissions Related to Bucket Subresource Operations&lt;/a&gt; and &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-access-control.html"&gt;Managing Access Permissions to Your Amazon S3 Resources&lt;/a&gt;.&lt;/p&gt; &lt;p&gt; &lt;code&gt;PutBucketTagging&lt;/code&gt; has the following special errors:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Error code: &lt;code&gt;InvalidTagError&lt;/code&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Description: The tag provided was not a valid tag. This error can occur if the tag did not pass input validation. For information about tag restrictions, see &lt;a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html"&gt;User-Defined Tag Restrictions&lt;/a&gt; and &lt;a href="https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/aws-tag-restrictions.html"&gt;Amazon Web Services-Generated Cost Allocation Tag Restrictions&lt;/a&gt;.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Error code: &lt;code&gt;MalformedXMLError&lt;/code&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Description: The XML provided does not match the schema.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Error code: &lt;code&gt;OperationAbortedError &lt;/code&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Description: A conflicting conditional action is currently in progress against this resource. Please try again.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Error code: &lt;code&gt;InternalError&lt;/code&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;Description: The service was unable to apply the provided tag to the bucket.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;The following operations are related to &lt;code&gt;PutBucketTagging&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketTagging.html"&gt;GetBucketTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html"&gt;DeleteBucketTagging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
