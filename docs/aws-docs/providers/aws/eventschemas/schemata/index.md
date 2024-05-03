---
title: schemata
hide_title: false
hide_table_of_contents: false
keywords:
  - schemata
  - eventschemas
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

Used to retrieve a list of <code>schemata</code> in a region or create a <code>schemata</code> resource, use <code>schema</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schemata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::EventSchemas::Schema</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.eventschemas.schemata" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="schema_arn" /></td><td><code>string</code></td><td>The ARN of the schema.</td></tr>
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
schema_arn
FROM aws.eventschemas.schemata
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>schemata</code> resource, the following permissions are required:

### Create
```json
schemas:DescribeSchema,
schemas:CreateSchema,
schemas:TagResource
```

### List
```json
schemas:ListSchemas,
schemas:ListSchemaVersions
```

