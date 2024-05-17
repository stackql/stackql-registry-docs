---
title: vpc_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - vpc_attribute
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>vpc_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.vpc_attribute" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="enableDnsHostnames" /> | `object` | Describes a value for a resource attribute that is a Boolean value. |
| <CopyableCode code="enableDnsSupport" /> | `object` | Describes a value for a resource attribute that is a Boolean value. |
| <CopyableCode code="vpcId" /> | `string` | The ID of the VPC. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="vpc_attribute_Describe" /> | `SELECT` | <CopyableCode code="Attribute, VpcId, region" /> | Describes the specified attribute of the specified VPC. You can specify only one attribute at a time. |
| <CopyableCode code="vpc_attribute_Modify" /> | `EXEC` | <CopyableCode code="VpcId, region" /> | Modifies the specified attribute of the specified VPC. |
