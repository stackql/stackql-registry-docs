---
title: access_key_last_useds
hide_title: false
hide_table_of_contents: false
keywords:
  - access_key_last_useds
  - iam
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
<tr><td><b>Name</b></td><td><code>access_key_last_useds</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.access_key_last_useds</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `AccessKeyLastUsed` | `object` | &lt;p&gt;Contains information about the last time an Amazon Web Services access key was used since IAM began tracking this information on April 22, 2015.&lt;/p&gt; &lt;p&gt;This data type is used as a response element in the &lt;a&gt;GetAccessKeyLastUsed&lt;/a&gt; operation.&lt;/p&gt; |
| `UserName` | `string` | &lt;p&gt;The name of the IAM user that owns this access key.&lt;/p&gt; &lt;p/&gt; |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `access_key_last_useds_Get` | `SELECT` | `AccessKeyId, region` |
