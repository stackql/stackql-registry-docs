---
title: serial_console_access
hide_title: false
hide_table_of_contents: false
keywords:
  - serial_console_access
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
<tr><td><b>Name</b></td><td><code>serial_console_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ec2.serial_console_access</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `serial_console_access_Disable` | `EXEC` |  | Disables access to the EC2 serial console of all instances for your account. By default, access to the EC2 serial console is disabled for your account. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-access-to-serial-console.html#serial-console-account-access"&gt;Manage account access to the EC2 serial console&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;. |
| `serial_console_access_Enable` | `EXEC` |  | Enables access to the EC2 serial console of all instances for your account. By default, access to the EC2 serial console is disabled for your account. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-access-to-serial-console.html#serial-console-account-access"&gt;Manage account access to the EC2 serial console&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;. |
