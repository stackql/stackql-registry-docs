---
title: object_legal_holds
hide_title: false
hide_table_of_contents: false
keywords:
  - object_legal_holds
  - s3
  - aws    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>object_legal_holds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.s3.object_legal_holds</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `object_legal_holds_Get` | `SELECT` | `Key` | &lt;p&gt;Gets an object's current legal hold status. For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html"&gt;Locking Objects&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This action is not supported by Amazon S3 on Outposts.&lt;/p&gt; &lt;p&gt;The following action is related to &lt;code&gt;GetObjectLegalHold&lt;/code&gt;:&lt;/p&gt; &lt;ul&gt; &lt;li&gt; &lt;p&gt; &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObjectAttributes.html"&gt;GetObjectAttributes&lt;/a&gt; &lt;/p&gt; &lt;/li&gt; &lt;/ul&gt; |
| `object_legal_holds_Put` | `EXEC` | `Key` | &lt;p&gt;Applies a legal hold configuration to the specified object. For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/object-lock.html"&gt;Locking Objects&lt;/a&gt;.&lt;/p&gt; &lt;p&gt;This action is not supported by Amazon S3 on Outposts.&lt;/p&gt; |
