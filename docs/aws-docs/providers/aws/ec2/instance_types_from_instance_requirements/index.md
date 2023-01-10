---
title: instance_types_from_instance_requirements
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_types_from_instance_requirements
  - ec2
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
<tr><td><b>Name</b></td><td><code>instance_types_from_instance_requirements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.instance_types_from_instance_requirements</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `instance_types_from_instance_requirements_Get` | `SELECT` | `ArchitectureType, InstanceRequirements, VirtualizationType` |
