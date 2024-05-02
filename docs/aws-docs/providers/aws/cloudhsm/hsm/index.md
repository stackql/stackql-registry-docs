---
title: hsm
hide_title: false
hide_table_of_contents: false
keywords:
  - hsm
  - cloudhsm
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
<tr><td><b>Name</b></td><td><code>hsm</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudhsm.hsm</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `create_hsm` | `INSERT` | `X-Amz-Target, data__AvailabilityZone, data__ClusterId, region` | Creates a new hardware security module (HSM) in the specified AWS CloudHSM cluster. |
| `delete_hsm` | `DELETE` | `X-Amz-Target, data__ClusterId, region` | Deletes the specified HSM. To specify an HSM, you can use its identifier (ID), the IP address of the HSM's elastic network interface (ENI), or the ID of the HSM's ENI. You need to specify only one of these values. To find these values, use &lt;a&gt;DescribeClusters&lt;/a&gt;. |
