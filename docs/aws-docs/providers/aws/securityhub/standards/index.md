---
title: standards
hide_title: false
hide_table_of_contents: false
keywords:
  - standards
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
Retrieves a list of <code>standards</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>standards</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::SecurityHub::Standard`` resource specifies the enablement of a security standard. The standard is identified by the ``StandardsArn`` property. To view a list of ASH standards and their Amazon Resource Names (ARNs), use the &#91;DescribeStandards&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;securityhub&#x2F;1.0&#x2F;APIReference&#x2F;API_DescribeStandards.html) API operation.&lt;br&#x2F;&gt; You must create a separate ``AWS::SecurityHub::Standard`` resource for each standard that you want to enable.&lt;br&#x2F;&gt; For more information about ASH standards, see &#91;standards reference&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;securityhub&#x2F;latest&#x2F;userguide&#x2F;standards-reference.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.securityhub.standards</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>standards_subscription_arn</code></td><td><code>string</code></td><td></td></tr>
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
standards_subscription_arn
FROM aws.securityhub.standards
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>standards</code> resource, the following permissions are required:

### Create
```json
securityhub:GetEnabledStandards,
securityhub:BatchEnableStandards,
securityhub:UpdateStandardsControl
```

### List
```json
securityhub:GetEnabledStandards
```

