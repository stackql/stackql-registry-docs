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


Used to retrieve a list of <code>trackers</code> in a region or to create or delete a <code>trackers</code> resource, use <code>tracker</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trackers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Location::Tracker Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.location.trackers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="tracker_name" /></td><td><code>string</code></td><td></td></tr>
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
tracker_name
FROM aws.location.trackers
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>tracker</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- tracker.iql (required properties only)
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
-- tracker.iql (all properties)
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

## `DELETE` Example

```sql
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

### Delete
```json
geo:DeleteTracker,
geo:DescribeTracker
```

### List
```json
geo:ListTrackers
```

