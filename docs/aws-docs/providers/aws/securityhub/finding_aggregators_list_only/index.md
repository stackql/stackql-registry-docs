---
title: finding_aggregators_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - finding_aggregators_list_only
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

Lists <code>finding_aggregators</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/finding_aggregators/"><code>finding_aggregators</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>finding_aggregators_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::SecurityHub::FindingAggregator resource represents the AWS Security Hub Finding Aggregator in your account. One finding aggregator resource is created for each account in non opt-in region in which you configure region linking mode.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.finding_aggregators_list_only" /></td></tr>
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
    <td><CopyableCode code="list_resources" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
Lists all <code>finding_aggregators</code> in a region.
```sql
SELECT
region,
finding_aggregator_arn
FROM aws.securityhub.finding_aggregators_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>finding_aggregators_list_only</code> resource, see <a href="/providers/aws/securityhub/finding_aggregators/#permissions"><code>finding_aggregators</code></a>


