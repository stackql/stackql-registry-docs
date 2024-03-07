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
Gets an individual <code>standard</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>standard</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>standard</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.securityhub.standard</code></td></tr>
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
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>standard</code> resource, the following permissions are required:

### Read
<pre>
securityhub:GetEnabledStandards,
securityhub:DescribeStandardsControls</pre>

### Update
<pre>
securityhub:GetEnabledStandards,
securityhub:UpdateStandardsControl</pre>

### Delete
<pre>
securityhub:GetEnabledStandards,
securityhub:BatchDisableStandards</pre>


## Example
```sql
SELECT
region,
standards_subscription_arn,
standards_arn,
disabled_standards_controls
FROM awscc.securityhub.standard
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;StandardsSubscriptionArn&gt;'
```
