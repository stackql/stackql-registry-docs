---
title: standard
hide_title: false
hide_table_of_contents: false
keywords:
  - standard
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
Gets or operates on an individual <code>standard</code> resource, use <code>standards</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>standard</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The ``AWS::SecurityHub::Standard`` resource specifies the enablement of a security standard. The standard is identified by the ``StandardsArn`` property. To view a list of ASH standards and their Amazon Resource Names (ARNs), use the &#91;DescribeStandards&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;securityhub&#x2F;1.0&#x2F;APIReference&#x2F;API_DescribeStandards.html) API operation.&lt;br&#x2F;&gt; You must create a separate ``AWS::SecurityHub::Standard`` resource for each standard that you want to enable.&lt;br&#x2F;&gt; For more information about ASH standards, see &#91;standards reference&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;securityhub&#x2F;latest&#x2F;userguide&#x2F;standards-reference.html) in the *User Guide*.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.securityhub.standard</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>standards_subscription_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>standards_arn</code></td><td><code>string</code></td><td>The ARN of the standard that you want to enable. To view a list of available ASH standards and their ARNs, use the &#91;DescribeStandards&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;securityhub&#x2F;1.0&#x2F;APIReference&#x2F;API_DescribeStandards.html) API operation.</td></tr>
<tr><td><code>disabled_standards_controls</code></td><td><code>array</code></td><td>Specifies which controls are to be disabled in a standard. &lt;br&#x2F;&gt; *Maximum*: ``100``</td></tr>
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
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
standards_subscription_arn,
standards_arn,
disabled_standards_controls
FROM aws.securityhub.standard
WHERE data__Identifier = '<StandardsSubscriptionArn>';
```

## Permissions

To operate on the <code>standard</code> resource, the following permissions are required:

### Read
```json
securityhub:GetEnabledStandards,
securityhub:DescribeStandardsControls
```

### Update
```json
securityhub:GetEnabledStandards,
securityhub:UpdateStandardsControl
```

### Delete
```json
securityhub:GetEnabledStandards,
securityhub:BatchDisableStandards
```

