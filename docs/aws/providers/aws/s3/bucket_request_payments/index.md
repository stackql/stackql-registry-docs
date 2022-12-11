---
title: bucket_request_payments
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_request_payments
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
<tr><td><b>Name</b></td><td><code>bucket_request_payments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.bucket_request_payments</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bucket_request_payments_Get` | `SELECT` | `requestPayment` | &lt;p&gt;Returns the request payment configuration of a bucket. To use this version of the operation, you must be the bucket owner. For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html"&gt;Requester Pays Buckets&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;GetBucketRequestPayment&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjects.html"&gt;ListObjects&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `bucket_request_payments_Put` | `EXEC` | `requestPayment` | &lt;p&gt;Sets the request payment configuration for a bucket. By default, the bucket owner pays for downloads from the bucket. This configuration parameter enables the bucket owner (only) to specify that the person requesting the download will be charged for the download. For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/RequesterPaysBuckets.html"&gt;Requester Pays Buckets&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;PutBucketRequestPayment&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html"&gt;CreateBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketRequestPayment.html"&gt;GetBucketRequestPayment&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
