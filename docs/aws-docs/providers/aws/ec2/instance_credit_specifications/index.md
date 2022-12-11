---
title: instance_credit_specifications
hide_title: false
hide_table_of_contents: false
keywords:
  - instance_credit_specifications
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
<tr><td><b>Name</b></td><td><code>instance_credit_specifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.instance_credit_specifications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `cpuCredits` | `string` | The credit option for CPU usage of the instance. Valid values are &lt;code&gt;standard&lt;/code&gt; and &lt;code&gt;unlimited&lt;/code&gt;. |
| `instanceId` | `string` | The ID of the instance. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `instance_credit_specifications_Describe` | `SELECT` |  | &lt;p&gt;Describes the credit option for CPU usage of the specified burstable performance instances. The credit options are &lt;code&gt;standard&lt;/code&gt; and &lt;code&gt;unlimited&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;If you do not specify an instance ID, Amazon EC2 returns burstable performance instances with the &lt;code&gt;unlimited&lt;/code&gt; credit option, as well as instances that were previously configured as T2, T3, and T3a with the &lt;code&gt;unlimited&lt;/code&gt; credit option. For example, if you resize a T2 instance, while it is configured as &lt;code&gt;unlimited&lt;/code&gt;, to an M4 instance, Amazon EC2 returns the M4 instance.&lt;/p&gt; &lt;p&gt;If you specify one or more instance IDs, Amazon EC2 returns the credit option (&lt;code&gt;standard&lt;/code&gt; or &lt;code&gt;unlimited&lt;/code&gt;) of those instances. If you specify an instance ID that is not valid, such as an instance that is not a burstable performance instance, an error is returned.&lt;/p&gt; &lt;p&gt;Recently terminated instances might appear in the returned results. This interval is usually less than one hour.&lt;/p&gt; &lt;p&gt;If an Availability Zone is experiencing a service disruption and you specify instance IDs in the affected zone, or do not specify any instance IDs at all, the call fails. If you specify only instance IDs in an unaffected zone, the call works normally.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html"&gt;Burstable performance instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
| `instance_credit_specification_Modify` | `EXEC` | `InstanceCreditSpecification` | &lt;p&gt;Modifies the credit option for CPU usage on a running or stopped burstable performance instance. The credit options are &lt;code&gt;standard&lt;/code&gt; and &lt;code&gt;unlimited&lt;/code&gt;.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html"&gt;Burstable performance instances&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;.&lt;/p&gt; |
