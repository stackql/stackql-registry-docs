---
title: configuration_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - configuration_tags
  - amazonmq
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

Expands all tag keys and values for <code>configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configuration_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AmazonMQ::Configuration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amazonmq.configuration_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the Amazon MQ configuration.</td></tr>
<tr><td><CopyableCode code="authentication_strategy" /></td><td><code>string</code></td><td>The authentication strategy associated with the configuration. The default is SIMPLE.</td></tr>
<tr><td><CopyableCode code="engine_type" /></td><td><code>string</code></td><td>The type of broker engine. Note: Currently, Amazon MQ only supports ACTIVEMQ for creating and editing broker configurations.</td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td>The version of the broker engine.</td></tr>
<tr><td><CopyableCode code="data" /></td><td><code>string</code></td><td>The base64-encoded XML configuration.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description of the configuration.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>The ID of the Amazon MQ configuration.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the configuration.</td></tr>
<tr><td><CopyableCode code="revision" /></td><td><code>string</code></td><td>The revision number of the configuration.</td></tr>
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
Expands tags for all <code>configurations</code> in a region.
```sql
SELECT
region,
arn,
authentication_strategy,
engine_type,
engine_version,
data,
description,
id,
name,
revision,
tag_key,
tag_value
FROM aws.amazonmq.configuration_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>configuration_tags</code> resource, see <a href="/providers/aws/amazonmq/configurations/#permissions"><code>configurations</code></a>

