---
title: ipam_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - ipam_scopes
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
<tr><td><b>Name</b></td><td><code>ipam_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.ipam_scopes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="description" /> | `string` | The description of the scope. |
| <CopyableCode code="ipamArn" /> | `string` | The ARN of the IPAM. |
| <CopyableCode code="ipamRegion" /> | `string` | The Amazon Web Services Region of the IPAM scope. |
| <CopyableCode code="ipamScopeArn" /> | `string` | The ARN of the scope. |
| <CopyableCode code="ipamScopeId" /> | `string` | The ID of the scope. |
| <CopyableCode code="ipamScopeType" /> | `string` | The type of the scope. |
| <CopyableCode code="isDefault" /> | `boolean` | Defines if the scope is the default scope or not. |
| <CopyableCode code="ownerId" /> | `string` | The Amazon Web Services account ID of the owner of the scope. |
| <CopyableCode code="poolCount" /> | `integer` | The number of pools in the scope. |
| <CopyableCode code="state" /> | `string` | The state of the IPAM scope. |
| <CopyableCode code="tagSet" /> | `array` | The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key &lt;code&gt;Owner&lt;/code&gt; and the value &lt;code&gt;TeamA&lt;/code&gt;, specify &lt;code&gt;tag:Owner&lt;/code&gt; for the filter name and &lt;code&gt;TeamA&lt;/code&gt; for the filter value. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="ipam_scopes_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Get information about your IPAM scopes. |
| <CopyableCode code="ipam_scope_Create" /> | `INSERT` | <CopyableCode code="IpamId, region" /> | &lt;p&gt;Create an IPAM scope. In IPAM, a scope is the highest-level container within IPAM. An IPAM contains two default scopes. Each scope represents the IP space for a single network. The private scope is intended for all private IP address space. The public scope is intended for all public IP address space. Scopes enable you to reuse IP addresses across multiple unconnected networks without causing IP address overlap or conflict.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/add-scope-ipam.html"&gt;Add a scope&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;.&lt;/p&gt; |
| <CopyableCode code="ipam_scope_Delete" /> | `DELETE` | <CopyableCode code="IpamScopeId, region" /> | &lt;p&gt;Delete the scope for an IPAM. You cannot delete the default scopes.&lt;/p&gt; &lt;p&gt;For more information, see &lt;a href="/vpc/latest/ipam/delete-scope-ipam.html"&gt;Delete a scope&lt;/a&gt; in the &lt;i&gt;Amazon VPC IPAM User Guide&lt;/i&gt;. &lt;/p&gt; |
| <CopyableCode code="ipam_scope_Modify" /> | `EXEC` | <CopyableCode code="IpamScopeId, region" /> | Modify an IPAM scope. |
