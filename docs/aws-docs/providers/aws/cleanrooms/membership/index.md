---
title: membership
hide_title: false
hide_table_of_contents: false
keywords:
  - membership
  - cleanrooms
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>membership</code> resource, use <code>memberships</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>membership</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents an AWS account that is a part of a collaboration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.membership" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this cleanrooms membership.</td></tr>
<tr><td><CopyableCode code="collaboration_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_creator_account_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="membership_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="query_log_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="default_result_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="payment_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
arn,
tags,
collaboration_arn,
collaboration_creator_account_id,
collaboration_identifier,
membership_identifier,
query_log_status,
default_result_configuration,
payment_configuration
FROM aws.cleanrooms.membership
WHERE region = 'us-east-1' AND data__Identifier = '<MembershipIdentifier>';
```


## Permissions

To operate on the <code>membership</code> resource, the following permissions are required:

### Read
```json
cleanrooms:GetMembership,
cleanrooms:ListTagsForResource,
logs:ListLogDeliveries,
logs:DescribeLogGroups,
logs:DescribeResourcePolicies,
logs:GetLogDelivery
```

### Update
```json
cleanrooms:UpdateMembership,
cleanrooms:GetMembership,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:DeleteLogDelivery,
logs:ListLogDeliveries,
logs:DescribeLogGroups,
logs:DescribeResourcePolicies,
logs:PutResourcePolicy,
logs:CreateLogGroup,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:UntagResource,
iam:PassRole
```

