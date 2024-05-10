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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>workspace</code> resource, use <code>workspaces</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>workspace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::APS::Workspace</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.aps.workspace" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="workspace_id" /></td><td><code>string</code></td><td>Required to identify a specific APS Workspace.</td></tr>
<tr><td><CopyableCode code="alias" /></td><td><code>string</code></td><td>AMP Workspace alias.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Workspace arn.</td></tr>
<tr><td><CopyableCode code="alert_manager_definition" /></td><td><code>string</code></td><td>The AMP Workspace alert manager definition data</td></tr>
<tr><td><CopyableCode code="prometheus_endpoint" /></td><td><code>string</code></td><td>AMP Workspace prometheus endpoint</td></tr>
<tr><td><CopyableCode code="logging_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_arn" /></td><td><code>string</code></td><td>KMS Key ARN used to encrypt and decrypt AMP workspace data.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
workspace_id,
alias,
arn,
alert_manager_definition,
prometheus_endpoint,
logging_configuration,
kms_key_arn,
tags
FROM aws.aps.workspace
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```


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

