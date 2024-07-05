---
title: bot_versions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - bot_versions_list_only
  - lex
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

Lists <code>bot_versions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/bot_versions/"><code>bot_versions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>bot_versions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>A version is a numbered snapshot of your work that you can publish for use in different parts of your workflow, such as development, beta deployment, and production.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lex.bot_versions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="bot_id" /></td><td><code>string</code></td><td>Unique ID of resource</td></tr>
<tr><td><CopyableCode code="bot_version" /></td><td><code>object</code></td><td>A version is a numbered snapshot of your work that you can publish for use in different parts of your workflow, such as development, beta deployment, and production.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the version. Use the description to help identify the version in lists.</td></tr>
<tr><td><CopyableCode code="bot_version_locale_specification" /></td><td><code>array</code></td><td>Specifies the locales that Amazon Lex adds to this version. You can choose the Draft version or any other previously published version for each locale.</td></tr>
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
Lists all <code>bot_versions</code> in a region.
```sql
SELECT
region,
bot_id,
bot_version
FROM aws.lex.bot_versions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>bot_versions_list_only</code> resource, see <a href="/providers/aws/lex/bot_versions/#permissions"><code>bot_versions</code></a>


