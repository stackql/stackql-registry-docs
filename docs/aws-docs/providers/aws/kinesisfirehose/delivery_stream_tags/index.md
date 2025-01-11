---
title: delivery_stream_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - delivery_stream_tags
  - kinesisfirehose
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

Expands all tag keys and values for <code>delivery_streams</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>delivery_stream_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::KinesisFirehose::DeliveryStream</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kinesisfirehose.delivery_stream_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="delivery_stream_encryption_configuration_input" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="delivery_stream_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="delivery_stream_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="elasticsearch_destination_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="amazonopensearchservice_destination_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="amazon_open_search_serverless_destination_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="extended_s3_destination_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="database_source_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="kinesis_stream_source_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="msk_source_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="redshift_destination_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="s3_destination_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="splunk_destination_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="http_endpoint_destination_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="snowflake_destination_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="iceberg_destination_configuration" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>delivery_streams</code> in a region.
```sql
SELECT
region,
arn,
delivery_stream_encryption_configuration_input,
delivery_stream_name,
delivery_stream_type,
elasticsearch_destination_configuration,
amazonopensearchservice_destination_configuration,
amazon_open_search_serverless_destination_configuration,
extended_s3_destination_configuration,
database_source_configuration,
kinesis_stream_source_configuration,
msk_source_configuration,
redshift_destination_configuration,
s3_destination_configuration,
splunk_destination_configuration,
http_endpoint_destination_configuration,
snowflake_destination_configuration,
iceberg_destination_configuration,
tag_key,
tag_value
FROM aws.kinesisfirehose.delivery_stream_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>delivery_stream_tags</code> resource, see <a href="/providers/aws/kinesisfirehose/delivery_streams/#permissions"><code>delivery_streams</code></a>

