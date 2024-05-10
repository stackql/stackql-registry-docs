---
title: schema_version
hide_title: false
hide_table_of_contents: false
keywords:
  - schema_version
  - glue
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


Gets or updates an individual <code>schema_version</code> resource, use <code>schema_versions</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schema_version</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>This resource represents an individual schema version of a schema defined in Glue Schema Registry.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.glue.schema_version" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="schema" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="schema_definition" /></td><td><code>string</code></td><td>Complete definition of the schema in plain-text.</td></tr>
<tr><td><CopyableCode code="version_id" /></td><td><code>string</code></td><td>Represents the version ID associated with the schema version.</td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
schema,
schema_definition,
version_id
FROM aws.glue.schema_version
WHERE region = 'us-east-1' AND data__Identifier = '<VersionId>';
```


## Permissions

To operate on the <code>schema_version</code> resource, the following permissions are required:

### Read
```json
glue:GetSchemaVersion
```

