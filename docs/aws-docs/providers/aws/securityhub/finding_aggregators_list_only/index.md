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
<tr><td><b>Description</b></td><td>The <code>AWS::SecurityHub::FindingAggregator</code> resource enables cross-Region aggregation. When cross-Region aggregation is enabled, you can aggregate findings, finding updates, insights, control compliance statuses, and security scores from one or more linked Regions to a single aggregation Region. You can then view and manage all of this data from the aggregation Region. For more details about cross-Region aggregation, see &#91;Cross-Region aggregation&#93;(https://docs.aws.amazon.com/securityhub/latest/userguide/finding-aggregation.html) in the *User Guide* <br />This resource must be created in the Region that you want to designate as your aggregation Region.<br />Cross-Region aggregation is also a prerequisite for using &#91;central configuration&#93;(https://docs.aws.amazon.com/securityhub/latest/userguide/central-configuration-intro.html) in ASH.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.securityhub.finding_aggregators_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="finding_aggregator_arn" /></td><td><code>string</code></td><td></td></tr>
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

