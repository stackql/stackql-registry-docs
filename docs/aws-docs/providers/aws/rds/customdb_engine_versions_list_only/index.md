---
title: customdb_engine_versions_list_only
hide_title: false
hide_table_of_contents: false
keywords:
  - customdb_engine_versions_list_only
  - rds
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

Lists <code>customdb_engine_versions</code> in a region or regions, for all properties use <a href="/providers/aws/serviceName/customdb_engine_versions/"><code>customdb_engine_versions</code></a>

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customdb_engine_versions_list_only</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Creates a custom DB engine version (CEV).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.rds.customdb_engine_versions_list_only" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="engine" /></td><td><code>string</code></td><td>The database engine to use for your custom engine version (CEV).<br />Valid values:<br />+ <code>custom-oracle-ee</code> <br />+ <code>custom-oracle-ee-cdb</code></td></tr>
<tr><td><CopyableCode code="engine_version" /></td><td><code>string</code></td><td>The name of your CEV. The name format is <code>major version.customized_string</code>. For example, a valid CEV name is <code>19.my_cev1</code>. This setting is required for RDS Custom for Oracle, but optional for Amazon RDS. The combination of <code>Engine</code> and <code>EngineVersion</code> is unique per customer per Region.<br />*Constraints:* Minimum length is 1. Maximum length is 60.<br />*Pattern:* <code>^&#91;a-z0-9_.-&#93;&#123;1,60$</code>&#125;</td></tr>
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
Lists all <code>customdb_engine_versions</code> in a region.
```sql
SELECT
region,
engine,
engine_version
FROM aws.rds.customdb_engine_versions_list_only
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>customdb_engine_versions_list_only</code> resource, see <a href="/providers/aws/rds/customdb_engine_versions/#permissions"><code>customdb_engine_versions</code></a>

