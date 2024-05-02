---
title: insights
hide_title: false
hide_table_of_contents: false
keywords:
  - insights
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
Retrieves a list of <code>insights</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>insights</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::Insight resource represents the AWS Security Hub Insight in your account. An AWS Security Hub insight is a collection of related findings.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.securityhub.insights</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>insight_arn</code></td><td><code>string</code></td><td>The ARN of a Security Hub insight</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
insight_arn
FROM aws.securityhub.insights
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>insights</code> resource, the following permissions are required:

### Create
```json
securityhub:CreateInsight
```

### List
```json
securityhub:GetInsights
```

