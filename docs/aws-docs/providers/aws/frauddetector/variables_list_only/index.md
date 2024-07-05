---
title: variables_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - variables_list_only
  - frauddetector
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

Lists <code>variables</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/variables/"><code>variables</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>variables_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A resource schema for a Variable in Amazon Fraud Detector.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.frauddetector.variables_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>The name of the variable.</td></tr>
<tr><td><CopyableCode code="data_source" /></td><td><code>string</code></td><td>The source of the data.</td></tr>
<tr><td><CopyableCode code="data_type" /></td><td><code>string</code></td><td>The data type.</td></tr>
<tr><td><CopyableCode code="default_value" /></td><td><code>string</code></td><td>The default value for the variable when no value is received.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The description.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Tags associated with this variable.</td></tr>
<tr><td><CopyableCode code="variable_type" /></td><td><code>string</code></td><td>The variable type. For more information see https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>The ARN of the variable.</td></tr>
<tr><td><CopyableCode code="created_time" /></td><td><code>string</code></td><td>The time when the variable was created.</td></tr>
<tr><td><CopyableCode code="last_updated_time" /></td><td><code>string</code></td><td>The time when the variable was last updated.</td></tr>
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
Lists all <code>variables</code> in a region.
```sql
SELECT
region,
arn
FROM aws.frauddetector.variables_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>variables_list_only</code> resource, see <a href="/providers/aws/frauddetector/variables/#permissions"><code>variables</code></a>


