---
title: bucket_cors
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_cors
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
<tr><td><b>Name</b></td><td><code>bucket_cors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.bucket_cors</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bucket_cors_Get` | `SELECT` | `cors` | &lt;p&gt;Returns the Cross-Origin Resource Sharing (CORS) configuration information set for the bucket.&lt;/p&gt; &lt;p&gt; To use this operation, you must have permission to perform the &lt;code&gt;s3:GetBucketCORS&lt;/code&gt; action. By default, the bucket owner has this permission and can grant it to others.&lt;/p&gt; &lt;p&gt; For more information about CORS, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html"&gt; Enabling Cross-Origin Resource Sharing&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;GetBucketCors&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketCors.html"&gt;PutBucketCors&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketCors.html"&gt;DeleteBucketCors&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `bucket_cors_Delete` | `DELETE` | `cors` | &lt;p&gt;Deletes the &lt;code&gt;cors&lt;/code&gt; configuration information set for the bucket.&lt;/p&gt; &lt;p&gt;To use this operation, you must have permission to perform the &lt;code&gt;s3:PutBucketCORS&lt;/code&gt; action. The bucket owner has this permission by default and can grant this permission to others. &lt;/p&gt; &lt;p&gt;For information about &lt;code&gt;cors&lt;/code&gt;, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html"&gt;Enabling Cross-Origin Resource Sharing&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p class="title"&gt; &lt;b&gt;Related Resources:&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketCors.html"&gt;PutBucketCors&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/RESTOPTIONSobject.html"&gt;RESTOPTIONSobject&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `bucket_cors_Put` | `EXEC` | `cors` | &lt;p&gt;Sets the &lt;code&gt;cors&lt;/code&gt; configuration for your bucket. If the configuration exists, Amazon S3 replaces it.&lt;/p&gt; &lt;p&gt;To use this operation, you must be allowed to perform the &lt;code&gt;s3:PutBucketCORS&lt;/code&gt; action. By default, the bucket owner has this permission and can grant it to others.&lt;/p&gt; &lt;p&gt;You set this configuration on a bucket so that the bucket can service cross-origin requests. For example, you might want to enable a request whose origin is &lt;code&gt;http://www.example.com&lt;/code&gt; to access your Amazon S3 bucket at &lt;code&gt;my.example.bucket.com&lt;/code&gt; by using the browser's &lt;code&gt;XMLHttpRequest&lt;/code&gt; capability.&lt;/p&gt; &lt;p&gt;To enable cross-origin resource sharing (CORS) on a bucket, you add the &lt;code&gt;cors&lt;/code&gt; subresource to the bucket. The &lt;code&gt;cors&lt;/code&gt; subresource is an XML document in which you configure rules that identify origins and the HTTP methods that can be executed on your bucket. The document is limited to 64 KB in size. &lt;/p&gt; &lt;p&gt;When Amazon S3 receives a cross-origin request (or a pre-flight OPTIONS request) against a bucket, it evaluates the &lt;code&gt;cors&lt;/code&gt; configuration on the bucket and uses the first &lt;code&gt;CORSRule&lt;/code&gt; rule that matches the incoming browser request to enable a cross-origin request. For a rule to match, the following conditions must be met:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The request's &lt;code&gt;Origin&lt;/code&gt; header must match &lt;code&gt;AllowedOrigin&lt;/code&gt; elements.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The request method (for example, GET, PUT, HEAD, and so on) or the &lt;code&gt;Access-Control-Request-Method&lt;/code&gt; header in case of a pre-flight &lt;code&gt;OPTIONS&lt;/code&gt; request must be one of the &lt;code&gt;AllowedMethod&lt;/code&gt; elements. &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;Every header specified in the &lt;code&gt;Access-Control-Request-Headers&lt;/code&gt; request header of a pre-flight request must match an &lt;code&gt;AllowedHeader&lt;/code&gt; element. &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt; For more information about CORS, go to &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html"&gt;Enabling Cross-Origin Resource Sharing&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;p class="title"&gt; &lt;b&gt;Related Resources&lt;/b&gt; &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketCors.html"&gt;GetBucketCors&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketCors.html"&gt;DeleteBucketCors&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/RESTOPTIONSobject.html"&gt;RESTOPTIONSobject&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
