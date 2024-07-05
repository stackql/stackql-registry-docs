---
title: configuration_aggregator_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_aggregator_tags
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

Expands all tag keys and values for <code>configuration_aggregators</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_aggregator_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Config::ConfigurationAggregator</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.config.configuration_aggregator_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="account_aggregation_sources" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="configuration_aggregator_name" /></td><td><code>string</code></td><td>The name of the aggregator.</td></tr>
<tr><td><CopyableCode code="configuration_aggregator_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the aggregator.</td></tr>
<tr><td><CopyableCode code="organization_aggregation_source" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="tag_key" /></td><td><code>string</code></td><td>Tag key.</td></tr>
<tr><td><CopyableCode code="tag_value" /></td><td><code>string</code></td><td>Tag value.</td></tr>
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
Expands tags for all <code>configuration_aggregators</code> in a region.
```sql
SELECT
region,
account_aggregation_sources,
configuration_aggregator_name,
configuration_aggregator_arn,
organization_aggregation_source,
tag_key,
tag_value
FROM aws.config.configuration_aggregator_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>configuration_aggregator_tags</code> resource, see <a href="/providers/aws/config/configuration_aggregators/#permissions"><code>configuration_aggregators</code></a>


