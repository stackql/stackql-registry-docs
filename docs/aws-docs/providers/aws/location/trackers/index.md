---
title: trackers
hide_title: false
hide_table_of_contents: false
keywords:
  - trackers
  - location
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

Creates, updates, deletes or gets a <code>tracker</code> resource or lists <code>trackers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trackers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::Tracker Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.trackers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="create_time" /></td><td><code>string</code></td><td>The datetime value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ss.sssZ)</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="event_bridge_enabled" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_enable_geospatial_queries" /></td><td><code>boolean</code></td><td></td></tr>
<tr><td><CopyableCode code="kms_key_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="position_filtering" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pricing_plan" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pricing_plan_data_source" /></td><td><code>string</code></td><td>This shape is deprecated since 2022-02-01: Deprecated. No longer allowed.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="tracker_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tracker_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="update_time" /></td><td><code>string</code></td><td>The datetime value in ISO 8601 format. The timezone is always UTC. (YYYY-MM-DDThh:mm:ss.sssZ)</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="TrackerName, region" /></td>
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
    <td><CopyableCode code="list_resource" /></td>
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
List all <code>trackers</code> in a region.
```sql
SELECT
region,
tracker_name
FROM aws.location.trackers
WHERE region = 'us-east-1';
```
Gets all properties from a <code>tracker</code>.
```sql
SELECT
region,
create_time,
description,
event_bridge_enabled,
kms_key_enable_geospatial_queries,
kms_key_id,
position_filtering,
pricing_plan,
pricing_plan_data_source,
tags,
tracker_arn,
tracker_name,
update_time,
arn
FROM aws.location.trackers
WHERE region = 'us-east-1' AND data__Identifier = '<TrackerName>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>tracker</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.location.trackers (
 TrackerName,
 region
)
SELECT 
'{{ TrackerName }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.location.trackers (
 Description,
 EventBridgeEnabled,
 KmsKeyEnableGeospatialQueries,
 KmsKeyId,
 PositionFiltering,
 PricingPlan,
 PricingPlanDataSource,
 Tags,
 TrackerName,
 region
)
SELECT 
 '{{ Description }}',
 '{{ EventBridgeEnabled }}',
 '{{ KmsKeyEnableGeospatialQueries }}',
 '{{ KmsKeyId }}',
 '{{ PositionFiltering }}',
 '{{ PricingPlan }}',
 '{{ PricingPlanDataSource }}',
 '{{ Tags }}',
 '{{ TrackerName }}',
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
  - name: tracker
    props:
      - name: Description
        value: '{{ Description }}'
      - name: EventBridgeEnabled
        value: '{{ EventBridgeEnabled }}'
      - name: KmsKeyEnableGeospatialQueries
        value: '{{ KmsKeyEnableGeospatialQueries }}'
      - name: KmsKeyId
        value: '{{ KmsKeyId }}'
      - name: PositionFiltering
        value: '{{ PositionFiltering }}'
      - name: PricingPlan
        value: '{{ PricingPlan }}'
      - name: PricingPlanDataSource
        value: '{{ PricingPlanDataSource }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: TrackerName
        value: '{{ TrackerName }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.location.trackers
WHERE data__Identifier = '<TrackerName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>trackers</code> resource, the following permissions are required:

### Create
```json
geo:CreateTracker,
geo:DescribeTracker,
geo:TagResource,
geo:UntagResource,
kms:DescribeKey,
kms:CreateGrant
```

### Read
```json
geo:DescribeTracker,
kms:DescribeKey
```

### Update
```json
geo:CreateTracker,
geo:DescribeTracker,
geo:TagResource,
geo:UntagResource,
kms:DescribeKey,
kms:CreateGrant,
geo:UpdateTracker
```

### Delete
```json
geo:DeleteTracker,
geo:DescribeTracker
```

### List
```json
geo:ListTrackers
```

