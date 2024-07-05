---
title: analysis_templates_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - analysis_templates_list_only
  - cleanrooms
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

Lists <code>analysis_templates</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/analysis_templates/"><code>analysis_templates</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analysis_templates_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a stored analysis within a collaboration</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.analysis_templates_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="collaboration_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An arbitrary set of tags (key-value pairs) for this cleanrooms analysis template.</td></tr>
<tr><td><CopyableCode code="analysis_parameters" /></td><td><code>array</code></td><td>The member who can query can provide this placeholder for a literal data value in an analysis template</td></tr>
<tr><td><CopyableCode code="analysis_template_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="membership_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="membership_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="schema" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="source" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="format" /></td><td><code>string</code></td><td></td></tr>
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
Lists all <code>analysis_templates</code> in a region.
```sql
SELECT
region,
analysis_template_identifier,
membership_identifier
FROM aws.cleanrooms.analysis_templates_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>analysis_templates_list_only</code> resource, see <a href="/providers/aws/cleanrooms/analysis_templates/#permissions"><code>analysis_templates</code></a>


