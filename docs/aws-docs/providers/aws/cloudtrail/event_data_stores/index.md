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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>event_data_stores</code> in a region or create a <code>event_data_stores</code> resource, use <code>event_data_store</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_data_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A storage lake of event data against which you can run complex SQL-based queries. An event data store can include events that you have logged on your account from the last 7 to 2557 or 3653 days (about seven or ten years) depending on the selected BillingMode.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudtrail.event_data_stores" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="event_data_store_arn" /></td><td><code>string</code></td><td>The ARN of the event data store.</td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="data__DesiredState, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
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

