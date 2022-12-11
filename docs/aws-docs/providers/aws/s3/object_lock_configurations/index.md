---
title: object_lock_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - object_lock_configurations
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
<tr><td><b>Name</b></td><td><code>object_lock_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.object_lock_configurations</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `object_lock_configurations_Get` | `SELECT` | `object-lock` | &lt;p&gt;Gets the Object Lock configuration for a bucket. The rule specified in the Object Lock configuration will be applied by default to every new object placed in the specified bucket. For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html"&gt;Locking Objects&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;The following action is related to &lt;code&gt;GetObjectLockConfiguration&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html"&gt;GetObjectAttributes&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `object_lock_configurations_Put` | `EXEC` | `object-lock` | &lt;p&gt;Places an Object Lock configuration on the specified bucket. The rule specified in the Object Lock configuration will be applied by default to every new object placed in the specified bucket. For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html"&gt;Locking Objects&lt;/a&gt;. &lt;/p&gt; &lt;note&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;DefaultRetention&lt;/code&gt; settings require both a mode and a period.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;The &lt;code&gt;DefaultRetention&lt;/code&gt; period can be either &lt;code&gt;Days&lt;/code&gt; or &lt;code&gt;Years&lt;/code&gt; but you must select one. You cannot specify &lt;code&gt;Days&lt;/code&gt; and &lt;code&gt;Years&lt;/code&gt; at the same time.&lt;/p&gt; &lt;/li&gt; &lt;li&gt; &lt;p&gt;You can only enable Object Lock for new buckets. If you want to turn on Object Lock for an existing bucket, contact Amazon Web Services Support.&lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; &lt;/note&gt; |
