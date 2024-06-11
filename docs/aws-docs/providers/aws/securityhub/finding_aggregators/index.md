---
title: finding_aggregators
hide_title: false
hide_table_of_contents: false
keywords:
  - finding_aggregators
  - securityhub
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

Creates, updates, deletes or gets a <code>finding_aggregator</code> resource or lists <code>finding_aggregators</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>finding_aggregators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::FindingAggregator resource represents the AWS Security Hub Finding Aggregator in your account. One finding aggregator resource is created for each account in non opt-in region in which you configure region linking mode.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.finding_aggregators" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="finding_aggregator_arn" /></td><td><code>string</code></td><td>The ARN of the FindingAggregator being created and assigned as the unique identifier</td></tr>
<tr><td><CopyableCode code="region_linking_mode" /></td><td><code>string</code></td><td>Indicates whether to link all Regions, all Regions except for a list of excluded Regions, or a list of included Regions</td></tr>
<tr><td><CopyableCode code="regions" /></td><td><code>array</code></td><td>The list of excluded Regions or included Regions</td></tr>
<tr><td><CopyableCode code="finding_aggregation_region" /></td><td><code>string</code></td><td>The aggregation Region of the FindingAggregator</td></tr>
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
    <td><CopyableCode code="RegionLinkingMode, region" /></td>
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
List all <code>finding_aggregators</code> in a region.
```sql
SELECT
region,
finding_aggregator_arn
FROM aws.securityhub.finding_aggregators
WHERE region = 'us-east-1';
```
Gets all properties from a <code>finding_aggregator</code>.
```sql
SELECT
region,
finding_aggregator_arn,
region_linking_mode,
regions,
finding_aggregation_region
FROM aws.securityhub.finding_aggregators
WHERE region = 'us-east-1' AND data__Identifier = '<FindingAggregatorArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>finding_aggregator</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.securityhub.finding_aggregators (
 RegionLinkingMode,
 region
)
SELECT 
'{{ RegionLinkingMode }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.securityhub.finding_aggregators (
 RegionLinkingMode,
 Regions,
 region
)
SELECT 
 '{{ RegionLinkingMode }}',
 '{{ Regions }}',
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
  - name: finding_aggregator
    props:
      - name: RegionLinkingMode
        value: '{{ RegionLinkingMode }}'
      - name: Regions
        value:
          - '{{ Regions[0] }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.securityhub.finding_aggregators
WHERE data__Identifier = '<FindingAggregatorArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>finding_aggregators</code> resource, the following permissions are required:

### Create
```json
securityhub:CreateFindingAggregator
```

### Read
```json
securityhub:GetFindingAggregator
```

### Update
```json
securityhub:UpdateFindingAggregator
```

### Delete
```json
securityhub:DeleteFindingAggregator
```

### List
```json
securityhub:ListFindingAggregators
```

