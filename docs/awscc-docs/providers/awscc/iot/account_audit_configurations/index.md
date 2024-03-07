---
title: account_audit_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - account_audit_configurations
  - iot
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>account_audit_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_audit_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>account_audit_configurations</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.account_audit_configurations</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td>Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>account_audit_configurations</code> resource, the following permissions are required:

### Create
<pre>
iot:UpdateAccountAuditConfiguration,
iot:DescribeAccountAuditConfiguration,
iam:PassRole</pre>

### List
<pre>
iot:DescribeAccountAuditConfiguration</pre>


## Example
```sql
SELECT
region,
account_id
FROM awscc.iot.account_audit_configurations
WHERE region = 'us-east-1'
```
