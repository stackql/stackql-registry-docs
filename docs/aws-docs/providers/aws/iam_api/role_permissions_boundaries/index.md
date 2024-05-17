---
title: role_permissions_boundaries
hide_title: false
hide_table_of_contents: false
keywords:
  - role_permissions_boundaries
  - iam_api
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
<tr><td><b>Name</b></td><td><code>role_permissions_boundaries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam_api.role_permissions_boundaries" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="role_permissions_boundaries_Delete" /> | `DELETE` | <CopyableCode code="RoleName, region" /> | &lt;p&gt;Deletes the permissions boundary for the specified IAM role. &lt;/p&gt; &lt;important&gt; &lt;p&gt;Deleting the permissions boundary for a role might increase its permissions. For example, it might allow anyone who assumes the role to perform all the actions granted in its permissions policies. &lt;/p&gt; &lt;/important&gt; |
| <CopyableCode code="role_permissions_boundaries_Put" /> | `EXEC` | <CopyableCode code="PermissionsBoundary, RoleName, region" /> | &lt;p&gt;Adds or updates the policy that is specified as the IAM role's permissions boundary. You can use an Amazon Web Services managed policy or a customer managed policy to set the boundary for a role. Use the boundary to control the maximum permissions that the role can have. Setting a permissions boundary is an advanced feature that can affect the permissions for the role.&lt;/p&gt; &lt;p&gt;You cannot set the boundary for a service-linked role. &lt;/p&gt; &lt;important&gt; &lt;p&gt;Policies used as permissions boundaries do not provide permissions. You must also attach a permissions policy to the role. To learn how the effective permissions for a role are evaluated, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html"&gt;IAM JSON policy evaluation logic&lt;/a&gt; in the IAM User Guide. &lt;/p&gt; &lt;/important&gt; |
