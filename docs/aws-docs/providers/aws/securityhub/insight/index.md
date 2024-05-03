---
title: insight
hide_title: false
hide_table_of_contents: false
keywords:
  - insight
  - securityhub
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

Gets or operates on an individual <code>insight</code> resource, use <code>insights</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>insight</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::Insight resource represents the AWS Security Hub Insight in your account. An AWS Security Hub insight is a collection of related findings.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.insight" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="insight_arn" /></td><td><code>string</code></td><td>The ARN of a Security Hub insight</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of a Security Hub insight</td></tr>
<tr><td><CopyableCode code="filters" /></td><td><code>object</code></td><td>One or more attributes used to filter the findings included in the insight</td></tr>
<tr><td><CopyableCode code="group_by_attribute" /></td><td><code>string</code></td><td>The grouping attribute for the insight's findings</td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
insight_arn,
name,
filters,
group_by_attribute
FROM aws.securityhub.insight
WHERE data__Identifier = '<InsightArn>';
```

## Permissions

To operate on the <code>insight</code> resource, the following permissions are required:

### Read
```json
securityhub:GetInsights
```

### Update
```json
securityhub:UpdateInsight
```

### Delete
```json
securityhub:GetInsights,
securityhub:DeleteInsight
```

