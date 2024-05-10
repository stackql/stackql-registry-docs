---
title: association
hide_title: false
hide_table_of_contents: false
keywords:
  - association
  - ssm
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


Gets or updates an individual <code>association</code> resource, use <code>associations</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SSM::Association resource associates an SSM document in AWS Systems Manager with EC2 instances that contain a configuration agent to process the document.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssm.association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="association_name" /></td><td><code>string</code></td><td>The name of the association.</td></tr>
<tr><td><CopyableCode code="calendar_names" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="schedule_expression" /></td><td><code>string</code></td><td>A Cron or Rate expression that specifies when the association is applied to the target.</td></tr>
<tr><td><CopyableCode code="max_errors" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>object</code></td><td>Parameter values that the SSM document uses at runtime.</td></tr>
<tr><td><CopyableCode code="instance_id" /></td><td><code>string</code></td><td>The ID of the instance that the SSM document is associated with.</td></tr>
<tr><td><CopyableCode code="wait_for_success_timeout_seconds" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="max_concurrency" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="compliance_severity" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="targets" /></td><td><code>array</code></td><td>The targets that the SSM document sends commands to.</td></tr>
<tr><td><CopyableCode code="sync_compliance" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="output_location" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="schedule_offset" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the SSM document.</td></tr>
<tr><td><CopyableCode code="apply_only_at_cron_interval" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="document_version" /></td><td><code>string</code></td><td>The version of the SSM document to associate with the target.</td></tr>
<tr><td><CopyableCode code="association_id" /></td><td><code>string</code></td><td>Unique identifier of the association.</td></tr>
<tr><td><CopyableCode code="automation_target_parameter_name" /></td><td><code>string</code></td><td></td></tr>
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
association_name,
calendar_names,
schedule_expression,
max_errors,
parameters,
instance_id,
wait_for_success_timeout_seconds,
max_concurrency,
compliance_severity,
targets,
sync_compliance,
output_location,
schedule_offset,
name,
apply_only_at_cron_interval,
document_version,
association_id,
automation_target_parameter_name
FROM aws.ssm.association
WHERE region = 'us-east-1' AND data__Identifier = '<AssociationId>';
```


## Permissions

To operate on the <code>association</code> resource, the following permissions are required:

### Read
```json
ssm:DescribeAssociation,
resource-groups:GetGroupQuery,
resource-groups:ListGroups,
resource-groups:ListGroupResources
```

### Update
```json
iam:PassRole,
ssm:UpdateAssociation,
ssm:GetCalendarState
```

