---
title: instance_types_from_instance_requirements
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_types_from_instance_requirements
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
<tr><td><b>Name</b></td><td><code>instance_types_from_instance_requirements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.instance_types_from_instance_requirements" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="instance_types_from_instance_requirements_Get" /> | `SELECT` | <CopyableCode code="ArchitectureType, InstanceRequirements, VirtualizationType, region" /> |
