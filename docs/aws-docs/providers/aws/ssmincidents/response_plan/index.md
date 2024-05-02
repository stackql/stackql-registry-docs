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
Gets an individual <code>response_plan</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>response_plan</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::SSMIncidents::ResponsePlan</td></tr>
<tr><td><b>Id</b></td><td><code>aws.ssmincidents.response_plan</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td>The ARN of the response plan.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the response plan.</td></tr>
<tr><td><code>display_name</code></td><td><code>string</code></td><td>The display name of the response plan.</td></tr>
<tr><td><code>chat_channel</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>engagements</code></td><td><code>array</code></td><td>The list of engagements to use.</td></tr>
<tr><td><code>actions</code></td><td><code>array</code></td><td>The list of actions.</td></tr>
<tr><td><code>integrations</code></td><td><code>array</code></td><td>The list of integrations.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td>The tags to apply to the response plan.</td></tr>
<tr><td><code>incident_template</code></td><td><code>object</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><code>update_resource</code></td>
    <td><code>UPDATE</code></td>
    <td><code>data__Identifier, data__PatchDocument, region</code></td>
  </tr>
  <tr>
    <td><code>delete_resource</code></td>
    <td><code>DELETE</code></td>
    <td><code>data__Identifier, region</code></td>
  </tr>
  <tr>
    <td><code>get_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>data__Identifier, region</code></td>
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

