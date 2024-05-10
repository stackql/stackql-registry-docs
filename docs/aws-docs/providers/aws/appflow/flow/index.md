---
title: flow
hide_title: false
hide_table_of_contents: false
keywords:
  - flow
  - appflow
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


Gets or updates an individual <code>flow</code> resource, use <code>flows</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>flow</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::AppFlow::Flow.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appflow.flow" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="flow_arn" /></td><td><code>string</code></td><td>ARN identifier of the flow.</td></tr>
<tr><td><CopyableCode code="flow_name" /></td><td><code>string</code></td><td>Name of the flow.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the flow.</td></tr>
<tr><td><CopyableCode code="kms_arn" /></td><td><code>string</code></td><td>The ARN of the AWS Key Management Service (AWS KMS) key that's used to encrypt your function's environment variables. If it's not provided, AWS Lambda uses a default service key.</td></tr>
<tr><td><CopyableCode code="trigger_config" /></td><td><code>object</code></td><td>Trigger settings of the flow.</td></tr>
<tr><td><CopyableCode code="flow_status" /></td><td><code>string</code></td><td>Flow activation status for Scheduled- and Event-triggered flows</td></tr>
<tr><td><CopyableCode code="source_flow_config" /></td><td><code>object</code></td><td>Configurations of Source connector of the flow.</td></tr>
<tr><td><CopyableCode code="destination_flow_config_list" /></td><td><code>array</code></td><td>List of Destination connectors of the flow.</td></tr>
<tr><td><CopyableCode code="tasks" /></td><td><code>array</code></td><td>List of tasks for the flow.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>List of Tags.</td></tr>
<tr><td><CopyableCode code="metadata_catalog_config" /></td><td><code>object</code></td><td>Configurations of metadata catalog of the flow.</td></tr>
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
flow_arn,
flow_name,
description,
kms_arn,
trigger_config,
flow_status,
source_flow_config,
destination_flow_config_list,
tasks,
tags,
metadata_catalog_config
FROM aws.appflow.flow
WHERE region = 'us-east-1' AND data__Identifier = '<FlowName>';
```


## Permissions

To operate on the <code>flow</code> resource, the following permissions are required:

### Read
```json
appflow:DescribeFlow,
appflow:ListTagsForResource
```

### Update
```json
appflow:UpdateFlow,
appflow:StartFlow,
appflow:StopFlow,
appflow:TagResource,
appflow:UntagResource,
appflow:ListTagsForResource,
appflow:UseConnectorProfile,
iam:PassRole,
s3:ListAllMyBuckets,
s3:GetBucketLocation,
s3:GetBucketPolicy,
kms:ListGrants,
secretsmanager:CreateSecret,
secretsmanager:PutResourcePolicy
```

