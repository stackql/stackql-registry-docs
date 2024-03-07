---
title: account_audit_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - account_audit_configuration
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
Gets an individual <code>account_audit_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>account_audit_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>account_audit_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.iot.account_audit_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>account_id</code></td><td><code>string</code></td><td>Your 12-digit account ID (used as the primary identifier for the CloudFormation resource).</td></tr>
<tr><td><code>audit_check_configurations</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>audit_notification_target_configurations</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>role_arn</code></td><td><code>string</code></td><td>The ARN of the role that grants permission to AWS IoT to access information about your devices, policies, certificates and other items as required when performing an audit.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
```sql
SELECT
region,
account_id,
audit_check_configurations,
audit_notification_target_configurations,
role_arn
FROM awscc.iot.account_audit_configuration
WHERE region = 'us-east-1'
AND data__Identifier = '{AccountId}';
```

## Permissions

To operate on the <code>account_audit_configuration</code> resource, the following permissions are required:

### Read
```json
iot:DescribeAccountAuditConfiguration
```

### Update
```json
iot:UpdateAccountAuditConfiguration,
iot:DescribeAccountAuditConfiguration,
iam:PassRole
```

### Delete
```json
iot:DescribeAccountAuditConfiguration,
iot:DeleteAccountAuditConfiguration
```

