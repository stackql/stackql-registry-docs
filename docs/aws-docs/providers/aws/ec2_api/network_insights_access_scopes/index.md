---
title: network_insights_access_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - network_insights_access_scopes
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
<tr><td><b>Name</b></td><td><code>network_insights_access_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2_api.network_insights_access_scopes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="createdDate" /> | `string` | The creation date. |
| <CopyableCode code="networkInsightsAccessScopeArn" /> | `string` | The Amazon Resource Name (ARN) of the Network Access Scope. |
| <CopyableCode code="networkInsightsAccessScopeId" /> | `string` | The ID of the Network Access Scope. |
| <CopyableCode code="tagSet" /> | `array` | The tags. |
| <CopyableCode code="updatedDate" /> | `string` | The last updated date. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="network_insights_access_scopes_Describe" /> | `SELECT` | <CopyableCode code="region" /> | Describes the specified Network Access Scopes. |
| <CopyableCode code="network_insights_access_scope_Create" /> | `INSERT` | <CopyableCode code="ClientToken, region" /> | &lt;p&gt;Creates a Network Access Scope.&lt;/p&gt; &lt;p&gt;Amazon Web Services Network Access Analyzer enables cloud networking and cloud operations teams to verify that their networks on Amazon Web Services conform to their network security and governance objectives. For more information, see the &lt;a href="https://docs.aws.amazon.com/vpc/latest/network-access-analyzer/"&gt;Amazon Web Services Network Access Analyzer Guide&lt;/a&gt;.&lt;/p&gt; |
| <CopyableCode code="network_insights_access_scope_Delete" /> | `DELETE` | <CopyableCode code="NetworkInsightsAccessScopeId, region" /> | Deletes the specified Network Access Scope. |
