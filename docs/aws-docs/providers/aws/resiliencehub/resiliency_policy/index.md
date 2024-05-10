---
title: resiliency_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - resiliency_policy
  - resiliencehub
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


Gets or updates an individual <code>resiliency_policy</code> resource, use <code>resiliency_policies</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resiliency_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type Definition for Resiliency Policy.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.resiliencehub.resiliency_policy" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="policy_name" /></td><td><code>string</code></td><td>Name of Resiliency Policy.</td></tr>
<tr><td><CopyableCode code="policy_description" /></td><td><code>string</code></td><td>Description of Resiliency Policy.</td></tr>
<tr><td><CopyableCode code="data_location_constraint" /></td><td><code>string</code></td><td>Data Location Constraint of the Policy.</td></tr>
<tr><td><CopyableCode code="tier" /></td><td><code>string</code></td><td>Resiliency Policy Tier.</td></tr>
<tr><td><CopyableCode code="policy" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="policy_arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the Resiliency Policy.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>object</code></td><td></td></tr>
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
policy_name,
policy_description,
data_location_constraint,
tier,
policy,
policy_arn,
tags
FROM aws.resiliencehub.resiliency_policy
WHERE region = 'us-east-1' AND data__Identifier = '<PolicyArn>';
```


## Permissions

To operate on the <code>resiliency_policy</code> resource, the following permissions are required:

### Update
```json
resiliencehub:DescribeResiliencyPolicy,
resiliencehub:UpdateResiliencyPolicy,
resiliencehub:TagResource,
resiliencehub:UntagResource,
resiliencehub:ListTagsForResource
```

### Read
```json
resiliencehub:DescribeResiliencyPolicy,
resiliencehub:ListTagsForResource
```

