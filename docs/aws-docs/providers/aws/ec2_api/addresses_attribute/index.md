---
title: addresses_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - addresses_attribute
  - ec2_api
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
<tr><td><b>Name</b></td><td><code>addresses_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2_api.addresses_attribute</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `allocationId` | `string` | [EC2-VPC] The allocation ID. |
| `ptrRecord` | `string` | The pointer (PTR) record for the IP address. |
| `ptrRecordUpdate` | `object` | The status of an updated pointer (PTR) record for an Elastic IP address. |
| `publicIp` | `string` | The public IP address. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `addresses_attribute_Describe` | `SELECT` | `region` |
