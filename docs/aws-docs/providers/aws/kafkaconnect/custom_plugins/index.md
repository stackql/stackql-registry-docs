---
title: custom_plugins
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_plugins
  - kafkaconnect
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

Used to retrieve a list of <code>custom_plugins</code> in a region or create a <code>custom_plugins</code> resource, use <code>custom_plugin</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_plugins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.kafkaconnect.custom_plugins" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="custom_plugin_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the custom plugin to use.</td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
custom_plugin_arn
FROM aws.kafkaconnect.custom_plugins
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>custom_plugins</code> resource, the following permissions are required:

### Create
```json
kafkaconnect:DescribeCustomPlugin,
kafkaconnect:ListTagsForResource,
kafkaconnect:CreateCustomPlugin,
kafkaconnect:TagResource,
s3:GetObject,
s3:GetObjectVersion,
s3:GetObjectAttributes,
s3:GetObjectVersionAttributes
```

### List
```json
kafkaconnect:ListCustomPlugins
```

