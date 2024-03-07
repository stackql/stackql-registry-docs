---
title: workspace
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace
  - aps
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>workspace</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>workspace</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.aps.workspace</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>workspace_id</code></td><td><code>string</code></td><td>Required to identify a specific APS Workspace.</td></tr>
<tr><td><code>alias</code></td><td><code>string</code></td><td>AMP Workspace alias.</td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>Workspace arn.</td></tr>
<tr><td><code>alert_manager_definition</code></td><td><code>string</code></td><td>The AMP Workspace alert manager definition data</td></tr>
<tr><td><code>prometheus_endpoint</code></td><td><code>string</code></td><td>AMP Workspace prometheus endpoint</td></tr>
<tr><td><code>logging_configuration</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>kms_key_arn</code></td><td><code>string</code></td><td>KMS Key ARN used to encrypt and decrypt AMP workspace data.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>workspace</code> resource, the following permissions are required:

### Read
```json
aps:DescribeWorkspace,
aps:ListTagsForResource,
aps:DescribeAlertManagerDefinition,
aps:DescribeLoggingConfiguration
```

### Update
```json
aps:UpdateWorkspaceAlias,
aps:DescribeWorkspace,
aps:TagResource,
aps:UntagResource,
aps:ListTagsForResource,
aps:CreateAlertManagerDefinition,
aps:PutAlertManagerDefinition,
aps:DeleteAlertManagerDefinition,
aps:CreateLoggingConfiguration,
aps:DescribeLoggingConfiguration,
aps:UpdateLoggingConfiguration,
aps:DeleteLoggingConfiguration,
logs:CreateLogDelivery,
logs:GetLogDelivery,
logs:UpdateLogDelivery,
logs:ListLogDeliveries,
logs:DeleteLogDelivery,
logs:PutResourcePolicy
```

### Delete
```json
aps:DeleteWorkspace,
aps:DescribeWorkspace,
aps:DeleteAlertManagerDefinition,
aps:DeleteLoggingConfiguration,
logs:DeleteLogDelivery
```


## Example
```sql
SELECT
region,
workspace_id,
alias,
arn,
alert_manager_definition,
prometheus_endpoint,
logging_configuration,
kms_key_arn,
tags
FROM awscc.aps.workspace
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;Arn&gt;'
```
