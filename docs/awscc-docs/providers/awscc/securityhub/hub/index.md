---
title: hub
hide_title: false
hide_table_of_contents: false
keywords:
  - hub
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
Gets an individual <code>hub</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>hub</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>hub</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.securityhub.hub</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>a_rn</code></td><td><code>string</code></td><td>An ARN is automatically created for the customer.</td></tr>
<tr><td><code>enable_default_standards</code></td><td><code>boolean</code></td><td>Whether to enable the security standards that Security Hub has designated as automatically enabled.</td></tr>
<tr><td><code>control_finding_generator</code></td><td><code>string</code></td><td>This field, used when enabling Security Hub, specifies whether the calling account has consolidated control findings turned on. If the value for this field is set to SECURITY_CONTROL, Security Hub generates a single finding for a control check even when the check applies to multiple enabled standards.  If the value for this field is set to STANDARD_CONTROL, Security Hub generates separate findings for a control check when the check applies to multiple enabled standards.</td></tr>
<tr><td><code>auto_enable_controls</code></td><td><code>boolean</code></td><td>Whether to automatically enable new controls when they are added to standards that are enabled</td></tr>
<tr><td><code>tags</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>subscribed_at</code></td><td><code>string</code></td><td>The date and time when Security Hub was enabled in the account.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>hub</code> resource, the following permissions are required:

### Read
<pre>
securityhub:DescribeHub,
securityhub:ListTagsForResource</pre>

### Update
<pre>
securityhub:DescribeHub,
securityhub:UpdateSecurityHubConfiguration,
securityhub:TagResource,
securityhub:UntagResource,
securityhub:ListTagsForResource</pre>

### Delete
<pre>
securityhub:DisableSecurityHub</pre>


## Example
```sql
SELECT
region,
a_rn,
enable_default_standards,
control_finding_generator,
auto_enable_controls,
tags,
subscribed_at
FROM awscc.securityhub.hub
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;ARN&gt;'
```
