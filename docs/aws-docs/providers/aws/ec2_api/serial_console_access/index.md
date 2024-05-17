---
title: serial_console_access
hide_title: false
hide_table_of_contents: false
keywords:
  - serial_console_access
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
<tr><td><b>Name</b></td><td><code>serial_console_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.serial_console_access" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="serial_console_access_Disable" /> | `EXEC` | <CopyableCode code="region" /> | Disables access to the EC2 serial console of all instances for your account. By default, access to the EC2 serial console is disabled for your account. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-access-to-serial-console.html#serial-console-account-access"&gt;Manage account access to the EC2 serial console&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;. |
| <CopyableCode code="serial_console_access_Enable" /> | `EXEC` | <CopyableCode code="region" /> | Enables access to the EC2 serial console of all instances for your account. By default, access to the EC2 serial console is disabled for your account. For more information, see &lt;a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-access-to-serial-console.html#serial-console-account-access"&gt;Manage account access to the EC2 serial console&lt;/a&gt; in the &lt;i&gt;Amazon EC2 User Guide&lt;/i&gt;. |
