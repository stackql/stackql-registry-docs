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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Used to retrieve a list of <code>event_data_stores</code> in a region or to create or delete a <code>event_data_stores</code> resource, use <code>event_data_store</code> to read or update an individual resource.

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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },

    ]
}>
<TabItem value="required">

```sql
<<<json
{}
>>>
--required properties only
INSERT INTO aws.cloudtrail.event_data_stores (
 ,
 region
)
SELECT 
{{  }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "AdvancedEventSelectors": [
  {
   "Name": "{{ Name }}",
   "FieldSelectors": [
    {
     "Field": "{{ Field }}",
     "Equals": [
      "{{ Equals[0] }}"
     ],
     "StartsWith": [
      "{{ StartsWith[0] }}"
     ],
     "EndsWith": [
      "{{ EndsWith[0] }}"
     ],
     "NotEquals": [
      "{{ NotEquals[0] }}"
     ],
     "NotStartsWith": [
      "{{ NotStartsWith[0] }}"
     ],
     "NotEndsWith": [
      "{{ NotEndsWith[0] }}"
     ]
    }
   ]
  }
 ],
 "FederationEnabled": "{{ FederationEnabled }}",
 "FederationRoleArn": "{{ FederationRoleArn }}",
 "MultiRegionEnabled": "{{ MultiRegionEnabled }}",
 "Name": "{{ Name }}",
 "OrganizationEnabled": "{{ OrganizationEnabled }}",
 "BillingMode": "{{ BillingMode }}",
 "RetentionPeriod": "{{ RetentionPeriod }}",
 "TerminationProtectionEnabled": "{{ TerminationProtectionEnabled }}",
 "KmsKeyId": "{{ KmsKeyId }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "InsightSelectors": [
  {
   "InsightType": "{{ InsightType }}"
  }
 ],
 "InsightsDestination": "{{ InsightsDestination }}",
 "IngestionEnabled": "{{ IngestionEnabled }}"
}
>>>
--all properties
INSERT INTO aws.cloudtrail.event_data_stores (
 AdvancedEventSelectors,
 FederationEnabled,
 FederationRoleArn,
 MultiRegionEnabled,
 Name,
 OrganizationEnabled,
 BillingMode,
 RetentionPeriod,
 TerminationProtectionEnabled,
 KmsKeyId,
 Tags,
 InsightSelectors,
 InsightsDestination,
 IngestionEnabled,
 region
)
SELECT 
 {{ AdvancedEventSelectors }},
 {{ FederationEnabled }},
 {{ FederationRoleArn }},
 {{ MultiRegionEnabled }},
 {{ Name }},
 {{ OrganizationEnabled }},
 {{ BillingMode }},
 {{ RetentionPeriod }},
 {{ TerminationProtectionEnabled }},
 {{ KmsKeyId }},
 {{ Tags }},
 {{ InsightSelectors }},
 {{ InsightsDestination }},
 {{ IngestionEnabled }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.cloudtrail.event_data_stores
WHERE data__Identifier = '<EventDataStoreArn>'
AND region = 'us-east-1';
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

### Delete
```json
CloudTrail:DeleteEventDataStore,
CloudTrail:GetEventDataStore,
CloudTrail:DisableFederation,
glue:DeleteTable,
lakeformation:DeregisterResource
```

### List
```json
CloudTrail:ListEventDataStores,
CloudTrail:GetEventDataStore,
CloudTrail:GetInsightSelectors,
CloudTrail:ListTags
```

