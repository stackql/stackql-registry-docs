---
title: analyzer_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - analyzer_tags
  - accessanalyzer
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

Expands all tag keys and values for <code>analyzers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>analyzer_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AccessAnalyzer::Analyzer type specifies an analyzer of the user's account</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.accessanalyzer.analyzer_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="analyzer_name" /></td><td><code>string</code></td><td>Analyzer name</td></tr>
<tr><td><CopyableCode code="archive_rules" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td>Amazon Resource Name (ARN) of the analyzer</td></tr>
<tr><td><CopyableCode code="type" /></td><td><code>string</code></td><td>The type of the analyzer, must be one of ACCOUNT, ORGANIZATION, ACCOUNT_UNUSED_ACCESS or ORGANIZATION_UNUSED_ACCESS</td></tr>
<tr><td><CopyableCode code="analyzer_configuration" /></td><td><code>object</code></td><td>The configuration for the analyzer</td></tr>
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
Expands tags for all <code>analyzers</code> in a region.
```sql
SELECT
region,
analyzer_name,
archive_rules,
arn,
type,
analyzer_configuration,
tag_key,
tag_value
FROM aws.accessanalyzer.analyzer_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>analyzer_tags</code> resource, see <a href="/providers/aws/accessanalyzer/analyzers/#permissions"><code>analyzers</code></a>

