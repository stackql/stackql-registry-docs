---
title: entities_for_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - entities_for_policies
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>entities_for_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam_api.entities_for_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `GroupId` | `string` | The stable and unique string identifying the group. For more information about IDs, see &lt;a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html"&gt;IAM identifiers&lt;/a&gt; in the &lt;i&gt;IAM User Guide&lt;/i&gt;. |
| `GroupName` | `string` | The name (friendly name, not ARN) identifying the group. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `entities_for_policies_List` | `SELECT` | `PolicyArn, region` |
