---
title: instance_types
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_types
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
<tr><td><b>Name</b></td><td><code>instance_types</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.instance_types</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `inferenceAcceleratorInfo` | `object` | Describes the Inference accelerators for the instance type. |
| `memoryInfo` | `object` | Describes the memory for the instance type. |
| `instanceStorageInfo` | `object` | Describes the instance store features that are supported by the instance type. |
| `autoRecoverySupported` | `boolean` | Indicates whether auto recovery is supported. |
| `hibernationSupported` | `boolean` | Indicates whether On-Demand hibernation is supported. |
| `freeTierEligible` | `boolean` | Indicates whether the instance type is eligible for the free tier. |
| `hypervisor` | `string` | The hypervisor for the instance type. |
| `gpuInfo` | `object` | Describes the GPU accelerators for the instance type. |
| `networkInfo` | `object` | Describes the networking features of the instance type. |
| `processorInfo` | `object` | Describes the processor used by the instance type. |
| `supportedUsageClasses` | `array` | Indicates whether the instance type is offered for spot or On-Demand. |
| `supportedVirtualizationTypes` | `array` | The supported virtualization types. |
| `ebsInfo` | `object` | Describes the Amazon EBS features supported by the instance type. |
| `dedicatedHostsSupported` | `boolean` | Indicates whether Dedicated Hosts are supported on the instance type. |
| `instanceType` | `string` | The instance type. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html"&gt;Instance types&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;. |
| `instanceStorageSupported` | `boolean` | Indicates whether instance storage is supported. |
| `bareMetal` | `boolean` | Indicates whether the instance is a bare metal instance type. |
| `vCpuInfo` | `object` | Describes the vCPU configurations for the instance type. |
| `fpgaInfo` | `object` | Describes the FPGAs for the instance type. |
| `supportedRootDeviceTypes` | `array` | The supported root device types. |
| `placementGroupInfo` | `object` | Describes the placement group support of the instance type. |
| `supportedBootModes` | `array` | The supported boot modes. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ami-boot.html"&gt;Boot modes&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;. |
| `currentGeneration` | `boolean` | Indicates whether the instance type is current generation. |
| `burstablePerformanceSupported` | `boolean` | Indicates whether the instance type is a burstable performance instance type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `instance_types_Describe` | `SELECT` |  |
