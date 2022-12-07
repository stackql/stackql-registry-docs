---
title: address_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - address_attribute
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
<tr><td><b>Name</b></td><td><code>address_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.address_attribute</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `address_attribute_Modify` | `EXEC` | `AllocationId` | Modifies an attribute of the specified Elastic IP address. For requirements, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#Using_Elastic_Addressing_Reverse_DNS"&gt;Using reverse DNS for email applications&lt;/a&gt;. |
| `address_attribute_Reset` | `EXEC` | `AllocationId, Attribute` | Resets the attribute of the specified IP address. For requirements, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html#Using_Elastic_Addressing_Reverse_DNS"&gt;Using reverse DNS for email applications&lt;/a&gt;. |
