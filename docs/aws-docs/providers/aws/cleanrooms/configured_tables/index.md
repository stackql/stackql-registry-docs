---
title: configured_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - configured_tables
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

Used to retrieve a list of <code>configured_tables</code> in a region or create a <code>configured_tables</code> resource, use <code>configured_table</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configured_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Represents a table that can be associated with collaborations</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.cleanrooms.configured_tables" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="configured_table_identifier" /></td><td><code>string</code></td><td></td></tr>
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
configured_table_identifier
FROM aws.cleanrooms.configured_tables
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>configured_tables</code> resource, the following permissions are required:

### Create
```json
cleanrooms:CreateConfiguredTable,
cleanrooms:DeleteConfiguredTable,
cleanrooms:DeleteConfiguredTableAnalysisRule,
cleanrooms:CreateConfiguredTableAnalysisRule,
cleanrooms:GetConfiguredTable,
cleanrooms:GetConfiguredTableAnalysisRule,
glue:GetDatabase,
glue:GetDatabases,
glue:GetTable,
glue:GetTables,
glue:GetPartition,
glue:GetPartitions,
glue:BatchGetPartition,
glue:GetSchemaVersion,
cleanrooms:ListTagsForResource,
cleanrooms:TagResource,
cleanrooms:ListConfiguredTables
```

### List
```json
cleanrooms:ListConfiguredTables
```
