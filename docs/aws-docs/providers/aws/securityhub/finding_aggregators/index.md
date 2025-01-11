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
<tr><td><b>Description</b></td><td>The <code>AWS::SecurityHub::FindingAggregator</code> resource enables cross-Region aggregation. When cross-Region aggregation is enabled, you can aggregate findings, finding updates, insights, control compliance statuses, and security scores from one or more linked Regions to a single aggregation Region. You can then view and manage all of this data from the aggregation Region. For more details about cross-Region aggregation, see &#91;Cross-Region aggregation&#93;(https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html) in the *User Guide* <br />This resource must be created in the Region that you want to designate as your aggregation Region.<br />Cross-Region aggregation is also a prerequisite for using &#91;central configuration&#93;(https://docs.aws.amazon.com/securityhub/latest/userguide/central-configuration-intro.html) in ASH.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.finding_aggregators" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="finding_aggregator_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region_linking_mode" /></td><td><code>string</code></td><td>Indicates whether to aggregate findings from all of the available Regions in the current partition. Also determines whether to automatically aggregate findings from new Regions as Security Hub supports them and you opt into them.<br />The selected option also determines how to use the Regions provided in the Regions list.<br />The options are as follows:<br />+ <code>ALL_REGIONS</code> - Aggregates findings from all of the Regions where Security Hub is enabled. When you choose this option, Security Hub also automatically aggregates findings from new Regions as Security Hub supports them and you opt into them. <br />+ <code>ALL_REGIONS_EXCEPT_SPECIFIED</code> - Aggregates findings from all of the Regions where Security Hub is enabled, except for the Regions listed in the <code>Regions</code> parameter. When you choose this option, Security Hub also automatically aggregates findings from new Regions as Security Hub supports them and you opt into them. <br />+ <code>SPECIFIED_REGIONS</code> - Aggregates findings only from the Regions listed in the <code>Regions</code> parameter. Security Hub does not automatically aggregate findings from new Regions. <br />+ <code>NO_REGIONS</code> - Aggregates no data because no Regions are selected as linked Regions.</td></tr>
<tr><td><CopyableCode code="regions" /></td><td><code>array</code></td><td>If <code>RegionLinkingMode</code> is <code>ALL_REGIONS_EXCEPT_SPECIFIED</code>, then this is a space-separated list of Regions that don't replicate and send findings to the home Region.<br />If <code>RegionLinkingMode</code> is <code>SPECIFIED_REGIONS</code>, then this is a space-separated list of Regions that do replicate and send findings to the home Region. <br />An <code>InvalidInputException</code> error results if you populate this field while <code>RegionLinkingMode</code> is <code>NO_REGIONS</code>.</td></tr>
<tr><td><CopyableCode code="finding_aggregation_region" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-findingaggregator.html"><code>AWS::SecurityHub::FindingAggregator</code></a>.

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
Gets all <code>finding_aggregators</code> in a region.
```sql
SELECT
region,
finding_aggregator_arn,
region_linking_mode,
regions,
finding_aggregation_region
FROM aws.securityhub.finding_aggregators
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>finding_aggregator</code>.
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
