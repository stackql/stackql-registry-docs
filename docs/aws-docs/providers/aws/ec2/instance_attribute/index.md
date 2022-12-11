---
title: instance_attribute
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_attribute
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
<tr><td><b>Name</b></td><td><code>instance_attribute</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.instance_attribute</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `enclaveOptions` | `object` | Indicates whether the instance is enabled for Amazon Web Services Nitro Enclaves. |
| `disableApiTermination` | `object` | Describes a value for a resource attribute that is a Boolean value. |
| `enaSupport` | `object` | Describes a value for a resource attribute that is a Boolean value. |
| `instanceInitiatedShutdownBehavior` | `object` | Describes a value for a resource attribute that is a String. |
| `sourceDestCheck` | `object` | Describes a value for a resource attribute that is a Boolean value. |
| `groupSet` | `array` | The security groups associated with the instance. |
| `rootDeviceName` | `object` | Describes a value for a resource attribute that is a String. |
| `kernel` | `object` | Describes a value for a resource attribute that is a String. |
| `instanceId` | `string` | The ID of the instance. |
| `sriovNetSupport` | `object` | Describes a value for a resource attribute that is a String. |
| `ramdisk` | `object` | Describes a value for a resource attribute that is a String. |
| `userData` | `object` | Describes a value for a resource attribute that is a String. |
| `instanceType` | `object` | Describes a value for a resource attribute that is a String. |
| `blockDeviceMapping` | `array` | The block device mapping of the instance. |
| `productCodes` | `array` | A list of product codes. |
| `ebsOptimized` | `object` | Describes a value for a resource attribute that is a Boolean value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `instance_attribute_Describe` | `SELECT` | `Attribute, InstanceId` | Describes the specified attribute of the specified instance. You can specify only one attribute at a time. Valid attribute values are: &lt;code&gt;instanceType&lt;/code&gt; \| &lt;code&gt;kernel&lt;/code&gt; \| &lt;code&gt;ramdisk&lt;/code&gt; \| &lt;code&gt;userData&lt;/code&gt; \| &lt;code&gt;disableApiTermination&lt;/code&gt; \| &lt;code&gt;instanceInitiatedShutdownBehavior&lt;/code&gt; \| &lt;code&gt;rootDeviceName&lt;/code&gt; \| &lt;code&gt;blockDeviceMapping&lt;/code&gt; \| &lt;code&gt;productCodes&lt;/code&gt; \| &lt;code&gt;sourceDestCheck&lt;/code&gt; \| &lt;code&gt;groupSet&lt;/code&gt; \| &lt;code&gt;ebsOptimized&lt;/code&gt; \| &lt;code&gt;sriovNetSupport&lt;/code&gt;  |
| `instance_attribute_Modify` | `EXEC` | `InstanceId` | &lt;p&gt;Modifies the specified attribute of the specified instance. You can specify only one attribute at a time.&lt;/p&gt; &lt;p&gt; &lt;b&gt;Note: &lt;/b&gt;Using this action to change the security groups associated with an elastic network interface (ENI) attached to an instance in a VPC can result in an error if the instance has more than one ENI. To change the security groups associated with an ENI attached to an instance that has multiple ENIs, we recommend that you use the &lt;a&gt;ModifyNetworkInterfaceAttribute&lt;/a&gt; action.&lt;/p&gt; &lt;p&gt;To modify some attributes, the instance must be stopped. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_ChangingAttributesWhileInstanceStopped.html"&gt;Modify a stopped instance&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| `instance_attribute_Reset` | `EXEC` | `Attribute, InstanceId` | &lt;p&gt;Resets an attribute of an instance to its default value. To reset the &lt;code&gt;kernel&lt;/code&gt; or &lt;code&gt;ramdisk&lt;/code&gt;, the instance must be in a stopped state. To reset the &lt;code&gt;sourceDestCheck&lt;/code&gt;, the instance can be either running or stopped.&lt;/p&gt; &lt;p&gt;The &lt;code&gt;sourceDestCheck&lt;/code&gt; attribute controls whether source/destination checking is enabled. The default value is &lt;code&gt;true&lt;/code&gt;, which means checking is enabled. This value must be &lt;code&gt;false&lt;/code&gt; for a NAT instance to perform NAT. For more information, see &lt;a href="https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html"&gt;NAT Instances&lt;/a&gt; in the &lt;i&gt;Amazon VPC User Guide&lt;/i&gt;.&lt;/p&gt; |
