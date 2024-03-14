---
title: event_data_store
hide_title: false
hide_table_of_contents: false
keywords:
  - event_data_store
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
Gets an individual <code>event_data_store</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>event_data_store</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>event_data_store</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.cloudtrail.event_data_store</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>advanced_event_selectors</code></td><td><code>array</code></td><td>The advanced event selectors that were used to select events for the data store.</td></tr>
<tr><td><code>created_timestamp</code></td><td><code>string</code></td><td>The timestamp of the event data store's creation.</td></tr>
<tr><td><code>event_data_store_arn</code></td><td><code>string</code></td><td>The ARN of the event data store.</td></tr>
<tr><td><code>federation_enabled</code></td><td><code>boolean</code></td><td>Indicates whether federation is enabled on an event data store.</td></tr>
<tr><td><code>federation_role_arn</code></td><td><code>string</code></td><td>The ARN of the role used for event data store federation.</td></tr>
<tr><td><code>multi_region_enabled</code></td><td><code>boolean</code></td><td>Indicates whether the event data store includes events from all regions, or only from the region in which it was created.</td></tr>
<tr><td><code>name</code></td><td><code>string</code></td><td>The name of the event data store.</td></tr>
<tr><td><code>organization_enabled</code></td><td><code>boolean</code></td><td>Indicates that an event data store is collecting logged events for an organization.</td></tr>
<tr><td><code>billing_mode</code></td><td><code>string</code></td><td>The mode that the event data store will use to charge for event storage.</td></tr>
<tr><td><code>retention_period</code></td><td><code>integer</code></td><td>The retention period, in days.</td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td>The status of an event data store. Values are STARTING_INGESTION, ENABLED, STOPPING_INGESTION, STOPPED_INGESTION and PENDING_DELETION.</td></tr>
<tr><td><code>termination_protection_enabled</code></td><td><code>boolean</code></td><td>Indicates whether the event data store is protected from termination.</td></tr>
<tr><td><code>updated_timestamp</code></td><td><code>string</code></td><td>The timestamp showing when an event data store was updated, if applicable. UpdatedTimestamp is always either the same or newer than the time shown in CreatedTimestamp.</td></tr>
<tr><td><code>kms_key_id</code></td><td><code>string</code></td><td>Specifies the KMS key ID to use to encrypt the events delivered by CloudTrail. The value can be an alias name prefixed by 'alias&#x2F;', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.</td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>insight_selectors</code></td><td><code>array</code></td><td>Lets you enable Insights event logging by specifying the Insights selectors that you want to enable on an existing event data store. Both InsightSelectors and InsightsDestination need to have a value in order to enable Insights events on an event data store.</td></tr>
<tr><td><code>insights_destination</code></td><td><code>string</code></td><td>Specifies the ARN of the event data store that will collect Insights events. Both InsightSelectors and InsightsDestination need to have a value in order to enable Insights events on an event data store</td></tr>
<tr><td><code>ingestion_enabled</code></td><td><code>boolean</code></td><td>Indicates whether the event data store is ingesting events.</td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.cloudtrail.event_data_store
WHERE data__Identifier = '<EventDataStoreArn>';
```

## Permissions

To operate on the <code>event_data_store</code> resource, the following permissions are required:

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

