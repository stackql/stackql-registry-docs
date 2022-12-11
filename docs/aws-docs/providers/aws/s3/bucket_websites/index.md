---
title: bucket_websites
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_websites
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
<tr><td><b>Name</b></td><td><code>bucket_websites</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.bucket_websites</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `ErrorDocument` | `object` | The error information. |
| `IndexDocument` | `object` | Container for the &lt;code&gt;Suffix&lt;/code&gt; element. |
| `RedirectAllRequestsTo` | `object` | Specifies the redirect behavior of all requests to a website endpoint of an Amazon S3 bucket. |
| `RoutingRules` | `array` | Rules that define when a redirect is applied and the redirect behavior. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bucket_websites_Get` | `SELECT` | `website` | &lt;p&gt;Returns the website configuration for a bucket. To host website on Amazon S3, you can configure a bucket as website by adding a website configuration. For more information about hosting websites, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html"&gt;Hosting Websites on Amazon S3&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;This GET action requires the &lt;code&gt;S3:GetBucketWebsite&lt;/code&gt; permission. By default, only the bucket owner can read the bucket website configuration. However, bucket owners can allow other users to read the website configuration by writing a bucket policy granting them the &lt;code&gt;S3:GetBucketWebsite&lt;/code&gt; permission.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;DeleteBucketWebsite&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketWebsite.html"&gt;DeleteBucketWebsite&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketWebsite.html"&gt;PutBucketWebsite&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `bucket_websites_Delete` | `DELETE` | `website` | &lt;p&gt;This action removes the website configuration for a bucket. Amazon S3 returns a &lt;code&gt;200 OK&lt;/code&gt; response upon successfully deleting a website configuration on the specified bucket. You will get a &lt;code&gt;200 OK&lt;/code&gt; response if the website configuration you are trying to delete does not exist on the bucket. Amazon S3 returns a &lt;code&gt;404&lt;/code&gt; response if the bucket specified in the request does not exist.&lt;/p&gt; &lt;p&gt;This DELETE action requires the &lt;code&gt;S3:DeleteBucketWebsite&lt;/code&gt; permission. By default, only the bucket owner can delete the website configuration attached to a bucket. However, bucket owners can grant other users permission to delete the website configuration by writing a bucket policy granting them the &lt;code&gt;S3:DeleteBucketWebsite&lt;/code&gt; permission. &lt;/p&gt; &lt;p&gt;For more information about hosting websites, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html"&gt;Hosting Websites on Amazon S3&lt;/a&gt;. &lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;DeleteBucketWebsite&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketWebsite.html"&gt;GetBucketWebsite&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketWebsite.html"&gt;PutBucketWebsite&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `bucket_websites_Put` | `EXEC` | `website` | &lt;p&gt;Sets the configuration of the website that is specified in the &lt;code&gt;website&lt;/code&gt; subresource. To configure a bucket as a website, you can add this subresource on the bucket with website configuration information such as the file name of the index document and any redirect rules. For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html"&gt;Hosting Websites on Amazon S3&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This PUT action requires the &lt;code&gt;S3:PutBucketWebsite&lt;/code&gt; permission. By default, only the bucket owner can configure the website attached to a bucket; however, bucket owners can allow other users to set the website configuration by writing a bucket policy that grants them the &lt;code&gt;S3:PutBucketWebsite&lt;/code&gt; permission.&lt;/p&gt; &lt;p&gt;To redirect all website requests sent to the bucket's website endpoint, you add a website configuration with the following elements. Because all requests are sent to another website, you don't need to provide index document name for the bucket.&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WebsiteConfiguration&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RedirectAllRequestsTo&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HostName&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Protocol&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;If you want granular control over redirects, you can use the following elements to add routing rules that describe conditions for redirecting requests and information about the redirect destination. In this case, the website configuration must provide an index document for the bucket, because some requests might not be redirected. &lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;WebsiteConfiguration&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;IndexDocument&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Suffix&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ErrorDocument&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Key&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RoutingRules&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;RoutingRule&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Condition&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HttpErrorCodeReturnedEquals&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;KeyPrefixEquals&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Redirect&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;Protocol&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HostName&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ReplaceKeyPrefixWith&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;ReplaceKeyWith&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;code&gt;HttpRedirectCode&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;Amazon S3 has a limitation of 50 routing rules per website configuration. If you require more than 50 routing rules, you can use object redirect. For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/how-to-page-redirect.html"&gt;Configuring an Object Redirect&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; |
