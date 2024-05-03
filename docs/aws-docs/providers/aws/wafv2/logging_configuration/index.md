---
title: logging_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - logging_configuration
  - wafv2
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

Gets or operates on an individual <code>logging_configuration</code> resource, use <code>logging_configurations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>logging_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A WAFv2 Logging Configuration Resource Provider</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.logging_configuration" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the web ACL that you want to associate with LogDestinationConfigs.</td></tr>
<tr><td><CopyableCode code="log_destination_configs" /></td><td><code>array</code></td><td>The Amazon Resource Names (ARNs) of the logging destinations that you want to associate with the web ACL.</td></tr>
<tr><td><CopyableCode code="redacted_fields" /></td><td><code>array</code></td><td>The parts of the request that you want to keep out of the logs. For example, if you redact the HEADER field, the HEADER field in the firehose will be xxx.</td></tr>
<tr><td><CopyableCode code="managed_by_firewall_manager" /></td><td><code>boolean</code></td><td>Indicates whether the logging configuration was created by AWS Firewall Manager, as part of an AWS WAF policy configuration. If true, only Firewall Manager can modify or delete the configuration.</td></tr>
<tr><td><CopyableCode code="logging_filter" /></td><td><code>object</code></td><td>Filtering that specifies which web requests are kept in the logs and which are dropped. You can filter on the rule action and on the web request labels that were applied by matching rules during web ACL evaluation.</td></tr>
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
resource_arn,
log_destination_configs,
redacted_fields,
managed_by_firewall_manager,
logging_filter
FROM aws.wafv2.logging_configuration
WHERE data__Identifier = '<ResourceArn>';
```

## Permissions

To operate on the <code>logging_configuration</code> resource, the following permissions are required:

### Read
```json
wafv2:GetLoggingConfiguration
```

### Update
```json
wafv2:PutLoggingConfiguration,
wafv2:GetLoggingConfiguration,
firehose:ListDeliveryStreams,
iam:CreateServiceLinkedRole,
iam:DescribeOrganization,
logs:CreateLogDelivery,
s3:PutBucketPolicy,
s3:GetBucketPolicy,
logs:PutResourcePolicy,
logs:DescribeResourcePolicies,
logs:DescribeLogGroups
```

### Delete
```json
wafv2:DeleteLoggingConfiguration,
wafv2:GetLoggingConfiguration,
logs:DeleteLogDelivery
```

