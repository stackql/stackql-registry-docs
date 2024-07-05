---
title: campaigns
hide_title: false
hide_table_of_contents: false
keywords:
  - campaigns
  - iotfleetwise
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

Creates, updates, deletes or gets a <code>campaign</code> resource or lists <code>campaigns</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>campaigns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::IoTFleetWise::Campaign Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotfleetwise.campaigns" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="action" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="creation_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="compression" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="priority" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="signals_to_collect" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="data_destination_configs" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="start_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="expiry_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="last_modification_time" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="spooling_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="signal_catalog_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="post_trigger_collection_duration" /></td><td><code>number</code></td><td></td></tr>
<tr><td><CopyableCode code="data_extra_dimensions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="diagnostics_mode" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="target_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collection_scheme" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="Name, Action, CollectionScheme, SignalCatalogArn, TargetArn, region" /></td>
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
Gets all <code>campaigns</code> in a region.
```sql
SELECT
region,
status,
action,
creation_time,
compression,
description,
priority,
signals_to_collect,
data_destination_configs,
start_time,
name,
expiry_time,
last_modification_time,
spooling_mode,
signal_catalog_arn,
post_trigger_collection_duration,
data_extra_dimensions,
diagnostics_mode,
target_arn,
arn,
collection_scheme,
tags
FROM aws.iotfleetwise.campaigns
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>campaign</code>.
```sql
SELECT
region,
status,
action,
creation_time,
compression,
description,
priority,
signals_to_collect,
data_destination_configs,
start_time,
name,
expiry_time,
last_modification_time,
spooling_mode,
signal_catalog_arn,
post_trigger_collection_duration,
data_extra_dimensions,
diagnostics_mode,
target_arn,
arn,
collection_scheme,
tags
FROM aws.iotfleetwise.campaigns
WHERE region = 'us-east-1' AND data__Identifier = '<Name>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>campaign</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.iotfleetwise.campaigns (
 Action,
 Name,
 SignalCatalogArn,
 TargetArn,
 CollectionScheme,
 region
)
SELECT 
'{{ Action }}',
 '{{ Name }}',
 '{{ SignalCatalogArn }}',
 '{{ TargetArn }}',
 '{{ CollectionScheme }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.iotfleetwise.campaigns (
 Action,
 Compression,
 Description,
 Priority,
 SignalsToCollect,
 DataDestinationConfigs,
 StartTime,
 Name,
 ExpiryTime,
 SpoolingMode,
 SignalCatalogArn,
 PostTriggerCollectionDuration,
 DataExtraDimensions,
 DiagnosticsMode,
 TargetArn,
 CollectionScheme,
 Tags,
 region
)
SELECT 
 '{{ Action }}',
 '{{ Compression }}',
 '{{ Description }}',
 '{{ Priority }}',
 '{{ SignalsToCollect }}',
 '{{ DataDestinationConfigs }}',
 '{{ StartTime }}',
 '{{ Name }}',
 '{{ ExpiryTime }}',
 '{{ SpoolingMode }}',
 '{{ SignalCatalogArn }}',
 '{{ PostTriggerCollectionDuration }}',
 '{{ DataExtraDimensions }}',
 '{{ DiagnosticsMode }}',
 '{{ TargetArn }}',
 '{{ CollectionScheme }}',
 '{{ Tags }}',
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
  - name: campaign
    props:
      - name: Action
        value: '{{ Action }}'
      - name: Compression
        value: '{{ Compression }}'
      - name: Description
        value: '{{ Description }}'
      - name: Priority
        value: '{{ Priority }}'
      - name: SignalsToCollect
        value:
          - MaxSampleCount: null
            Name: '{{ Name }}'
            MinimumSamplingIntervalMs: null
      - name: DataDestinationConfigs
        value:
          - null
      - name: StartTime
        value: '{{ StartTime }}'
      - name: Name
        value: '{{ Name }}'
      - name: ExpiryTime
        value: '{{ ExpiryTime }}'
      - name: SpoolingMode
        value: '{{ SpoolingMode }}'
      - name: SignalCatalogArn
        value: '{{ SignalCatalogArn }}'
      - name: PostTriggerCollectionDuration
        value: null
      - name: DataExtraDimensions
        value:
          - '{{ DataExtraDimensions[0] }}'
      - name: DiagnosticsMode
        value: '{{ DiagnosticsMode }}'
      - name: TargetArn
        value: '{{ TargetArn }}'
      - name: CollectionScheme
        value: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.iotfleetwise.campaigns
WHERE data__Identifier = '<Name>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>campaigns</code> resource, the following permissions are required:

### Read
```json
iotfleetwise:GetCampaign,
iotfleetwise:ListTagsForResource
```

### Create
```json
iotfleetwise:CreateCampaign,
iotfleetwise:GetCampaign,
iotfleetwise:ListTagsForResource,
iotfleetwise:TagResource,
iam:PassRole,
timestream:DescribeEndpoints,
timestream:DescribeTable
```

### Update
```json
iotfleetwise:GetCampaign,
iotfleetwise:ListTagsForResource,
iotfleetwise:UpdateCampaign,
iotfleetwise:TagResource,
iotfleetwise:UntagResource
```

### List
```json
iotfleetwise:ListCampaigns,
iotfleetwise:GetCampaign
```

### Delete
```json
iotfleetwise:DeleteCampaign,
iotfleetwise:GetCampaign
```

