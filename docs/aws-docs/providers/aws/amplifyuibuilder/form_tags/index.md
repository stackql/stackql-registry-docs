---
title: form_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - form_tags
  - amplifyuibuilder
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

Expands all tag keys and values for <code>forms</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>form_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::AmplifyUIBuilder::Form Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.amplifyuibuilder.form_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="app_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="cta" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="data_type" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="fields" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="form_action_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="label_decorator" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="schema_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="sectional_elements" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="style" /></td><td><code>object</code></td><td></td></tr>
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
Expands tags for all <code>forms</code> in a region.
```sql
SELECT
region,
app_id,
cta,
data_type,
environment_name,
fields,
form_action_type,
id,
label_decorator,
name,
schema_version,
sectional_elements,
style,
tag_key,
tag_value
FROM aws.amplifyuibuilder.form_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>form_tags</code> resource, see <a href="/providers/aws/amplifyuibuilder/forms/#permissions"><code>forms</code></a>

