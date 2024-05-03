---
title: response_plan
hide_title: false
hide_table_of_contents: false
keywords:
  - response_plan
  - ssmincidents
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

Gets or operates on an individual <code>response_plan</code> resource, use <code>response_plans</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>response_plan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::SSMIncidents::ResponsePlan</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ssmincidents.response_plan" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the response plan.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the response plan.</td></tr>
<tr><td><CopyableCode code="display_name" /></td><td><code>string</code></td><td>The display name of the response plan.</td></tr>
<tr><td><CopyableCode code="chat_channel" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="engagements" /></td><td><code>array</code></td><td>The list of engagements to use.</td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>array</code></td><td>The list of actions.</td></tr>
<tr><td><CopyableCode code="integrations" /></td><td><code>array</code></td><td>The list of integrations.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags to apply to the response plan.</td></tr>
<tr><td><CopyableCode code="incident_template" /></td><td><code>object</code></td><td></td></tr>
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
arn,
name,
display_name,
chat_channel,
engagements,
actions,
integrations,
tags,
incident_template
FROM aws.ssmincidents.response_plan
WHERE data__Identifier = '<Arn>';
```

## Permissions

To operate on the <code>response_plan</code> resource, the following permissions are required:

### Read
```json
ssm-incidents:GetResponsePlan,
ssm-incidents:ListTagsForResource
```

### Update
```json
ssm-incidents:UpdateResponsePlan,
ssm-incidents:GetResponsePlan,
ssm-incidents:TagResource,
ssm-incidents:UntagResource,
ssm-incidents:ListTagsForResource,
iam:PassRole,
secretsmanager:GetSecretValue,
kms:Decrypt,
kms:GenerateDataKey*
```

### Delete
```json
ssm-incidents:DeleteResponsePlan,
ssm-incidents:GetResponsePlan
```

