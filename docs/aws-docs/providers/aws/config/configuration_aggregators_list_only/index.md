---
title: configuration_aggregators_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_aggregators_list_only
  - config
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

Lists <code>configuration_aggregators</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/configuration_aggregators/"><code>configuration_aggregators</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_aggregators_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Config::ConfigurationAggregator</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.configuration_aggregators_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_aggregation_sources" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="configuration_aggregator_name" /></td><td><code>string</code></td><td>The name of the aggregator.</td></tr>
<tr><td><CopyableCode code="configuration_aggregator_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the aggregator.</td></tr>
<tr><td><CopyableCode code="organization_aggregation_source" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>The tags for the configuration aggregator.</td></tr>
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
Lists all <code>configuration_aggregators</code> in a region.
```sql
SELECT
region,
configuration_aggregator_name
FROM aws.config.configuration_aggregators_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>configuration_aggregators_list_only</code> resource, see <a href="/providers/aws/config/configuration_aggregators/#permissions"><code>configuration_aggregators</code></a>


