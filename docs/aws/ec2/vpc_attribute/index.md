---
title: vpc_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_attribute
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
<tr><td><b>Name</b></td><td><code>vpc_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.vpc_attribute</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `enableDnsHostnames` | `object` | Describes a value for a resource attribute that is a Boolean value. |
| `enableDnsSupport` | `object` | Describes a value for a resource attribute that is a Boolean value. |
| `vpcId` | `string` | The ID of the VPC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `vpc_attribute_Describe` | `SELECT` | `Attribute, VpcId` | Describes the specified attribute of the specified VPC. You can specify only one attribute at a time. |
| `vpc_attribute_Modify` | `EXEC` | `VpcId` | Modifies the specified attribute of the specified VPC. |
