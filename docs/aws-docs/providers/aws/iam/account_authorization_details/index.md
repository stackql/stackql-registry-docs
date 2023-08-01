---
title: account_authorization_details
hide_title: false
hide_table_of_contents: false
keywords:
  - account_authorization_details
  - iam
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
<tr><td><b>Name</b></td><td><code>account_authorization_details</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>aws.iam.account_authorization_details</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `IsTruncated` | `boolean` | A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the &lt;code&gt;Marker&lt;/code&gt; request parameter to retrieve more items. Note that IAM might return fewer than the &lt;code&gt;MaxItems&lt;/code&gt; number of results even when there are more results available. We recommend that you check &lt;code&gt;IsTruncated&lt;/code&gt; after every call to ensure that you receive all your results. |
| `Marker` | `string` | When &lt;code&gt;IsTruncated&lt;/code&gt; is &lt;code&gt;true&lt;/code&gt;, this element is present and contains the value to use for the &lt;code&gt;Marker&lt;/code&gt; parameter in a subsequent pagination request. |
| `Policies` | `array` | A list containing information about managed policies. |
| `RoleDetailList` | `array` | A list containing information about IAM roles. |
| `UserDetailList` | `array` | A list containing information about IAM users. |
| `GroupDetailList` | `array` | A list containing information about IAM groups. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `account_authorization_details_Get` | `SELECT` | `region` |
