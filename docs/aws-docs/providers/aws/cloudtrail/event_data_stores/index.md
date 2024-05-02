---
title: event_data_stores
hide_title: false
hide_table_of_contents: false
keywords:
  - event_data_stores
  - cloudtrail
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Retrieves a list of <code>event_data_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_data_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A storage lake of event data against which you can run complex SQL-based queries. An event data store can include events that you have logged on your account from the last 7 to 2557 or 3653 days (about seven or ten years) depending on the selected BillingMode.</td></tr>
<tr><td><b>Id</b></td><td><code>aws.cloudtrail.event_data_stores</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>event_data_store_arn</code></td><td><code>string</code></td><td>The ARN of the event data store.</td></tr>
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
    <td><code>create_resource</code></td>
    <td><code>INSERT</code></td>
    <td><code>data__DesiredState, region</code></td>
  </tr>
  <tr>
    <td><code>list_resource</code></td>
    <td><code>SELECT</code></td>
    <td><code>region</code></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
event_data_store_arn
FROM aws.cloudtrail.event_data_stores
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>event_data_stores</code> resource, the following permissions are required:

### Create
```json
CloudTrail:CreateEventDataStore,
CloudTrail:AddTags,
CloudTrail:PutInsightSelectors,
CloudTrail:EnableFederation,
CloudTrail:GetEventDataStore,
iam:PassRole,
iam:GetRole,
iam:CreateServiceLinkedRole,
organizations:DescribeOrganization,
organizations:ListAWSServiceAccessForOrganization,
kms:GenerateDataKey,
kms:Decrypt,
glue:CreateDatabase,
glue:CreateTable,
glue:PassConnection,
lakeformation:RegisterResource
```

### List
```json
CloudTrail:ListEventDataStores,
CloudTrail:GetEventDataStore,
CloudTrail:GetInsightSelectors,
CloudTrail:ListTags
```

