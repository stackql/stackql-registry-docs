---
title: object_retentions
hide_title: false
hide_table_of_contents: false
keywords:
  - object_retentions
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
<tr><td><b>Name</b></td><td><code>object_retentions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.object_retentions</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `object_retentions_Get` | `SELECT` | `Key, retention` | &lt;p&gt;Retrieves an object's retention settings. For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html"&gt;Locking Objects&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This action is not supported by Amazon S3 on Outposts.&lt;/p&gt; &lt;p&gt;The following action is related to &lt;code&gt;GetObjectRetention&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html"&gt;GetObjectAttributes&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `object_retentions_Put` | `EXEC` | `Key, retention` | &lt;p&gt;Places an Object Retention configuration on an object. For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html"&gt;Locking Objects&lt;/a&gt;. Users or accounts require the &lt;code&gt;s3:PutObjectRetention&lt;/code&gt; permission in order to place an Object Retention configuration on objects. Bypassing a Governance Retention configuration requires the &lt;code&gt;s3:BypassGovernanceRetention&lt;/code&gt; permission. &lt;/p&gt; &lt;p&gt;This action is not supported by Amazon S3 on Outposts.&lt;/p&gt; |
