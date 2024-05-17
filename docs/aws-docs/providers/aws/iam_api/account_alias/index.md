---
title: account_alias
hide_title: false
hide_table_of_contents: false
keywords:
  - account_alias
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
<tr><td><b>Name</b></td><td><code>account_alias</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam_api.account_alias" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="account_alias_Create" /> | `INSERT` | <CopyableCode code="AccountAlias, region" /> | Creates an alias for your Amazon Web Services account. For information about using an Amazon Web Services account alias, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/AccountAlias.html"&gt;Using an alias for your Amazon Web Services account ID&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
| <CopyableCode code="account_alias_Delete" /> | `DELETE` | <CopyableCode code="AccountAlias, region" /> |  Deletes the specified Amazon Web Services account alias. For information about using an Amazon Web Services account alias, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/AccountAlias.html"&gt;Using an alias for your Amazon Web Services account ID&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
