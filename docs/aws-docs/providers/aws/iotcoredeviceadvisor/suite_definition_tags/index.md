---
title: suite_definition_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - suite_definition_tags
  - iotcoredeviceadvisor
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

Expands all tag keys and values for <code>suite_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>suite_definition_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotcoredeviceadvisor.suite_definition_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="suite_definition_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="suite_definition_id" /></td><td><code>string</code></td><td>The unique identifier for the suite definition.</td></tr>
<tr><td><CopyableCode code="suite_definition_arn" /></td><td><code>string</code></td><td>The Amazon Resource name for the suite definition.</td></tr>
<tr><td><CopyableCode code="suite_definition_version" /></td><td><code>string</code></td><td>The suite definition version of a test suite.</td></tr>
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
Expands tags for all <code>suite_definitions</code> in a region.
```sql
SELECT
region,
suite_definition_configuration,
suite_definition_id,
suite_definition_arn,
suite_definition_version,
tag_key,
tag_value
FROM aws.iotcoredeviceadvisor.suite_definition_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>suite_definition_tags</code> resource, see <a href="/providers/aws/iotcoredeviceadvisor/suite_definitions/#permissions"><code>suite_definitions</code></a>

