---
title: instance_type_offerings
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_type_offerings
  - ec2
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
<tr><td><b>Name</b></td><td><code>instance_type_offerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.instance_type_offerings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `instanceType` | `string` | The instance type. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html"&gt;Instance types&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;. |
| `location` | `string` | The identifier for the location. This depends on the location type. For example, if the location type is &lt;code&gt;region&lt;/code&gt;, the location is the Region code (for example, &lt;code&gt;us-east-2&lt;/code&gt;.) |
| `locationType` | `string` | The location type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `instance_type_offerings_Describe` | `SELECT` |  |
