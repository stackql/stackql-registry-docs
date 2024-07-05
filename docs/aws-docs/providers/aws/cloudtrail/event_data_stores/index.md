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

Creates, updates, deletes or gets an <code>event_data_store</code> resource or lists <code>event_data_stores</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_data_stores</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A storage lake of event data against which you can run complex SQL-based queries. An event data store can include events that you have logged on your account from the last 7 to 2557 or 3653 days (about seven or ten years) depending on the selected BillingMode.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cloudtrail.event_data_stores" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="advanced_event_selectors" /></td><td><code>array</code></td><td>The advanced event selectors that were used to select events for the data store.</td></tr>
<tr><td><CopyableCode code="created_timestamp" /></td><td><code>string</code></td><td>The timestamp of the event data store's creation.</td></tr>
<tr><td><CopyableCode code="event_data_store_arn" /></td><td><code>string</code></td><td>The ARN of the event data store.</td></tr>
<tr><td><CopyableCode code="federation_enabled" /></td><td><code>boolean</code></td><td>Indicates whether federation is enabled on an event data store.</td></tr>
<tr><td><CopyableCode code="federation_role_arn" /></td><td><code>string</code></td><td>The ARN of the role used for event data store federation.</td></tr>
<tr><td><CopyableCode code="multi_region_enabled" /></td><td><code>boolean</code></td><td>Indicates whether the event data store includes events from all regions, or only from the region in which it was created.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the event data store.</td></tr>
<tr><td><CopyableCode code="organization_enabled" /></td><td><code>boolean</code></td><td>Indicates that an event data store is collecting logged events for an organization.</td></tr>
<tr><td><CopyableCode code="billing_mode" /></td><td><code>string</code></td><td>The mode that the event data store will use to charge for event storage.</td></tr>
<tr><td><CopyableCode code="retention_period" /></td><td><code>integer</code></td><td>The retention period, in days.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>The status of an event data store. Values are STARTING_INGESTION, ENABLED, STOPPING_INGESTION, STOPPED_INGESTION and PENDING_DELETION.</td></tr>
<tr><td><CopyableCode code="termination_protection_enabled" /></td><td><code>boolean</code></td><td>Indicates whether the event data store is protected from termination.</td></tr>
<tr><td><CopyableCode code="updated_timestamp" /></td><td><code>string</code></td><td>The timestamp showing when an event data store was updated, if applicable. UpdatedTimestamp is always either the same or newer than the time shown in CreatedTimestamp.</td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td>Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="insight_selectors" /></td><td><code>array</code></td><td>Lets you enable Insights event logging by specifying the Insights selectors that you want to enable on an existing event data store. Both InsightSelectors and InsightsDestination need to have a value in order to enable Insights events on an event data store.</td></tr>
<tr><td><CopyableCode code="insights_destination" /></td><td><code>string</code></td><td>Specifies the ARN of the event data store that will collect Insights events. Both InsightSelectors and InsightsDestination need to have a value in order to enable Insights events on an event data store</td></tr>
<tr><td><CopyableCode code="ingestion_enabled" /></td><td><code>boolean</code></td><td>Indicates whether the event data store is ingesting events.</td></tr>
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
    <td><CopyableCode code=", region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Gets all <code>event_data_stores</code> in a region.
```sql
SELECT
region,
advanced_event_selectors,
created_timestamp,
event_data_store_arn,
federation_enabled,
federation_role_arn,
multi_region_enabled,
name,
organization_enabled,
billing_mode,
retention_period,
status,
termination_protection_enabled,
updated_timestamp,
kms_key_id,
tags,
insight_selectors,
insights_destination,
ingestion_enabled
FROM aws.cloudtrail.event_data_stores
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>event_data_store</code>.
```sql
SELECT
region,
advanced_event_selectors,
created_timestamp,
event_data_store_arn,
federation_enabled,
federation_role_arn,
multi_region_enabled,
name,
organization_enabled,
billing_mode,
retention_period,
status,
termination_protection_enabled,
updated_timestamp,
kms_key_id,
tags,
insight_selectors,
insights_destination,
ingestion_enabled
FROM aws.cloudtrail.event_data_stores
WHERE region = 'us-east-1' AND data__Identifier = '<EventDataStoreArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>event_data_store</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.cloudtrail.event_data_stores (
 ,
 region
)
SELECT 
'{{  }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ AdvancedEventSelectors }}',
 '{{ FederationEnabled }}',
 '{{ FederationRoleArn }}',
 '{{ MultiRegionEnabled }}',
 '{{ Name }}',
 '{{ OrganizationEnabled }}',
 '{{ BillingMode }}',
 '{{ RetentionPeriod }}',
 '{{ TerminationProtectionEnabled }}',
 '{{ KmsKeyId }}',
 '{{ Tags }}',
 '{{ InsightSelectors }}',
 '{{ InsightsDestination }}',
 '{{ IngestionEnabled }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: event_data_store
    props:
      - name: AdvancedEventSelectors
        value:
          - Name: '{{ Name }}'
            FieldSelectors:
              - Field: '{{ Field }}'
                Equals:
                  - '{{ Equals[0] }}'
                StartsWith:
                  - '{{ StartsWith[0] }}'
                EndsWith:
                  - '{{ EndsWith[0] }}'
                NotEquals:
                  - '{{ NotEquals[0] }}'
                NotStartsWith:
                  - '{{ NotStartsWith[0] }}'
                NotEndsWith:
                  - '{{ NotEndsWith[0] }}'
      - name: FederationEnabled
        value: '{{ FederationEnabled }}'
      - name: FederationRoleArn
        value: '{{ FederationRoleArn }}'
      - name: MultiRegionEnabled
        value: '{{ MultiRegionEnabled }}'
      - name: Name
        value: '{{ Name }}'
      - name: OrganizationEnabled
        value: '{{ OrganizationEnabled }}'
      - name: BillingMode
        value: '{{ BillingMode }}'
      - name: RetentionPeriod
        value: '{{ RetentionPeriod }}'
      - name: TerminationProtectionEnabled
        value: '{{ TerminationProtectionEnabled }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: InsightSelectors
        value:
          - InsightType: '{{ InsightType }}'
      - name: InsightsDestination
        value: '{{ InsightsDestination }}'
      - name: IngestionEnabled
        value: '{{ IngestionEnabled }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
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

### Read
```json
CloudTrail:GetEventDataStore,
CloudTrail:ListEventDataStores,
CloudTrail:GetInsightSelectors,
CloudTrail:ListTags
```

### Update
```json
CloudTrail:UpdateEventDataStore,
CloudTrail:RestoreEventDataStore,
CloudTrail:AddTags,
CloudTrail:RemoveTags,
CloudTrail:StartEventDataStoreIngestion,
CloudTrail:StopEventDataStoreIngestion,
CloudTrail:GetEventDataStore,
CloudTrail:PutInsightSelectors,
CloudTrail:GetInsightSelectors,
CloudTrail:EnableFederation,
CloudTrail:DisableFederation,
iam:PassRole,
iam:GetRole,
iam:CreateServiceLinkedRole,
organizations:DescribeOrganization,
organizations:ListAWSServiceAccessForOrganization,
glue:CreateDatabase,
glue:CreateTable,
glue:PassConnection,
lakeformation:RegisterResource,
glue:DeleteTable,
lakeformation:DeregisterResource,
kms:DescribeKey
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

