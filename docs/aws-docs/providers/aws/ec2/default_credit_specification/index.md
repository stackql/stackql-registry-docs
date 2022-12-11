---
title: default_credit_specification
hide_title: false
hide_table_of_contents: false
keywords:
  - default_credit_specification
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
<tr><td><b>Name</b></td><td><code>default_credit_specification</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.default_credit_specification</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `instanceFamily` | `string` | The instance family. |
| `cpuCredits` | `string` | The default credit option for CPU usage of the instance family. Valid values are &lt;code&gt;standard&lt;/code&gt; and &lt;code&gt;unlimited&lt;/code&gt;. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `default_credit_specification_Get` | `SELECT` | `InstanceFamily` | &lt;p&gt;Describes the default credit option for CPU usage of a burstable performance instance family.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html"&gt;Burstable performance instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| `default_credit_specification_Modify` | `EXEC` | `CpuCredits, InstanceFamily` | &lt;p&gt;Modifies the default credit option for CPU usage of burstable performance instances. The default credit option is set at the account level per Amazon Web Services Region, and is specified per instance family. All new burstable performance instances in the account launch using the default credit option.&lt;/p&gt; &lt;p&gt; &lt;code&gt;ModifyDefaultCreditSpecification&lt;/code&gt; is an asynchronous operation, which works at an Amazon Web Services Region level and modifies the credit option for each Availability Zone. All zones in a Region are updated within five minutes. But if instances are launched during this operation, they might not get the new credit option until the zone is updated. To verify whether the update has occurred, you can call &lt;code&gt;GetDefaultCreditSpecification&lt;/code&gt; and check &lt;code&gt;DefaultCreditSpecification&lt;/code&gt; for updates.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html"&gt;Burstable performance instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
