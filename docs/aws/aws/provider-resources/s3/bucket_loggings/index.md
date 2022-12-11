---
title: bucket_loggings
hide_title: false
hide_table_of_contents: false
keywords:
  - bucket_loggings
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
<tr><td><b>Name</b></td><td><code>bucket_loggings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.bucket_loggings</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `bucket_loggings_Get` | `SELECT` | `logging` | &lt;p&gt;Returns the logging status of a bucket and the permissions users have to view and modify that status. To use GET, you must be the bucket owner.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;GetBucketLogging&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html"&gt;CreateBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketLogging.html"&gt;PutBucketLogging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `bucket_loggings_Put` | `EXEC` | `logging` | &lt;p&gt;Set the logging parameters for a bucket and to specify permissions for who can view and modify the logging parameters. All logs are saved to buckets in the same Amazon Web Services Region as the source bucket. To set the logging status of a bucket, you must be the bucket owner.&lt;/p&gt; &lt;p&gt;The bucket owner is automatically granted FULL_CONTROL to all logs. You use the &lt;code&gt;Grantee&lt;/code&gt; request element to grant access to other people. The &lt;code&gt;Permissions&lt;/code&gt; request element specifies the kind of access the grantee has to the logs.&lt;/p&gt; &lt;important&gt; &lt;p&gt;If the target bucket for log delivery uses the bucket owner enforced setting for S3 Object Ownership, you can't use the &lt;code&gt;Grantee&lt;/code&gt; request element to grant access to others. Permissions can only be granted using policies. For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html#grant-log-delivery-permissions-general"&gt;Permissions for server access log delivery&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;.&lt;/p&gt; &lt;/important&gt; &lt;p&gt; &lt;b&gt;Grantee Values&lt;/b&gt; &lt;/p&gt; &lt;p&gt;You can specify the person (grantee) to whom you're assigning access rights (using request elements) in the following ways:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;By the person's ID:&lt;/p&gt; &lt;p&gt; &lt;code&gt;&lt;Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="CanonicalUser"&gt;&lt;ID&gt;&lt;&gt;ID&lt;&gt;&lt;/ID&gt;&lt;DisplayName&gt;&lt;&gt;GranteesEmail&lt;&gt;&lt;/DisplayName&gt; &lt;/Grantee&gt;&lt;/code&gt; &lt;/p&gt; &lt;p&gt;DisplayName is optional and ignored in the request.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;By Email address:&lt;/p&gt; &lt;p&gt; &lt;code&gt; &lt;Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="AmazonCustomerByEmail"&gt;&lt;EmailAddress&gt;&lt;&gt;Grantees@email.com&lt;&gt;&lt;/EmailAddress&gt;&lt;/Grantee&gt;&lt;/code&gt; &lt;/p&gt; &lt;p&gt;The grantee is resolved to the CanonicalUser and, in a response to a GET Object acl request, appears as the CanonicalUser.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;By URI:&lt;/p&gt; &lt;p&gt; &lt;code&gt;&lt;Grantee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="Group"&gt;&lt;URI&gt;&lt;&gt;http://acs.amazonaws.com/groups/global/AuthenticatedUsers&lt;&gt;&lt;/URI&gt;&lt;/Grantee&gt;&lt;/code&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;p&gt;To enable logging, you use LoggingEnabled and its children request elements. To disable logging, you use an empty BucketLoggingStatus request element:&lt;/p&gt; &lt;p&gt; &lt;code&gt;&lt;BucketLoggingStatus xmlns="http://doc.s3.amazonaws.com/2006-03-01" /&gt;&lt;/code&gt; &lt;/p&gt; &lt;p&gt;For more information about server access logging, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html"&gt;Server Access Logging&lt;/a&gt; in the &lt;i&gt;Amazon S3 User Guide&lt;/i&gt;. &lt;/p&gt; &lt;p&gt;For more information about creating a bucket, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html"&gt;CreateBucket&lt;/a&gt;. For more information about returning the logging status of a bucket, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLogging.html"&gt;GetBucketLogging&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The following operations are related to &lt;code&gt;PutBucketLogging&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html"&gt;PutObject&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html"&gt;DeleteBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_CreateBucket.html"&gt;CreateBucket&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetBucketLogging.html"&gt;GetBucketLogging&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
