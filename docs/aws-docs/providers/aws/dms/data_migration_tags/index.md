---
title: data_migration_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - data_migration_tags
  - dms
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

Expands all tag keys and values for <code>data_migrations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_migration_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DMS::DataMigration.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dms.data_migration_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="data_migration_name" /></td><td><code>string</code></td><td>The property describes a name to identify the data migration.</td></tr>
<tr><td><CopyableCode code="data_migration_arn" /></td><td><code>string</code></td><td>The property describes an ARN of the data migration.</td></tr>
<tr><td><CopyableCode code="data_migration_identifier" /></td><td><code>string</code></td><td>The property describes an ARN of the data migration.</td></tr>
<tr><td><CopyableCode code="data_migration_create_time" /></td><td><code>string</code></td><td>The property describes the create time of the data migration.</td></tr>
<tr><td><CopyableCode code="service_access_role_arn" /></td><td><code>string</code></td><td>The property describes Amazon Resource Name (ARN) of the service access role.</td></tr>
<tr><td><CopyableCode code="migration_project_identifier" /></td><td><code>string</code></td><td>The property describes an identifier for the migration project. It is used for describing/deleting/modifying can be name/arn</td></tr>
<tr><td><CopyableCode code="data_migration_type" /></td><td><code>string</code></td><td>The property describes the type of migration.</td></tr>
<tr><td><CopyableCode code="data_migration_settings" /></td><td><code>object</code></td><td>The property describes the settings for the data migration.</td></tr>
<tr><td><CopyableCode code="source_data_settings" /></td><td><code>array</code></td><td>The property describes the settings for the data migration.</td></tr>
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
Expands tags for all <code>data_migrations</code> in a region.
```sql
SELECT
region,
data_migration_name,
data_migration_arn,
data_migration_identifier,
data_migration_create_time,
service_access_role_arn,
migration_project_identifier,
data_migration_type,
data_migration_settings,
source_data_settings,
tag_key,
tag_value
FROM aws.dms.data_migration_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>data_migration_tags</code> resource, see <a href="/providers/aws/dms/data_migrations/#permissions"><code>data_migrations</code></a>

