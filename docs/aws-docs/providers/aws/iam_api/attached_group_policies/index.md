---
title: attached_group_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - attached_group_policies
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
<tr><td><b>Name</b></td><td><code>attached_group_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iam_api.attached_group_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="PolicyArn" /> | `string` | &lt;p&gt;The Amazon Resource Name (ARN). ARNs are unique identifiers for Amazon Web Services resources.&lt;/p&gt; &lt;p&gt;For more information about ARNs, go to &lt;a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"&gt;Amazon Resource Names (ARNs)&lt;/a&gt; in the &lt;i&gt;Amazon Web Services General Reference&lt;/i&gt;. &lt;/p&gt; |
| <CopyableCode code="PolicyName" /> | `string` | The friendly name of the attached policy. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="attached_group_policies_List" /> | `SELECT` | <CopyableCode code="GroupName, region" /> |
