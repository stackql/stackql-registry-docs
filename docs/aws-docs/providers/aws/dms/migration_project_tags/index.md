---
title: migration_project_tags
hide_title: false
hide_table_of_contents: false
keywords:
  - migration_project_tags
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

Expands all tag keys and values for <code>migration_projects</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>migration_project_tags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DMS::MigrationProject</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dms.migration_project_tags" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="migration_project_name" /></td><td><code>string</code></td><td>The property describes a name to identify the migration project.</td></tr>
<tr><td><CopyableCode code="migration_project_identifier" /></td><td><code>string</code></td><td>The property describes an identifier for the migration project. It is used for describing/deleting/modifying can be name/arn</td></tr>
<tr><td><CopyableCode code="migration_project_arn" /></td><td><code>string</code></td><td>The property describes an ARN of the migration project.</td></tr>
<tr><td><CopyableCode code="migration_project_creation_time" /></td><td><code>string</code></td><td>The property describes a creating time of the migration project.</td></tr>
<tr><td><CopyableCode code="instance_profile_identifier" /></td><td><code>string</code></td><td>The property describes an instance profile identifier for the migration project. For create</td></tr>
<tr><td><CopyableCode code="instance_profile_name" /></td><td><code>string</code></td><td>The property describes an instance profile name for the migration project. For read</td></tr>
<tr><td><CopyableCode code="instance_profile_arn" /></td><td><code>string</code></td><td>The property describes an instance profile arn for the migration project. For read</td></tr>
<tr><td><CopyableCode code="transformation_rules" /></td><td><code>string</code></td><td>The property describes transformation rules for the migration project.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>The optional description of the migration project.</td></tr>
<tr><td><CopyableCode code="schema_conversion_application_attributes" /></td><td><code>object</code></td><td>The property describes schema conversion application attributes for the migration project.</td></tr>
<tr><td><CopyableCode code="source_data_provider_descriptors" /></td><td><code>array</code></td><td>The property describes source data provider descriptors for the migration project.</td></tr>
<tr><td><CopyableCode code="target_data_provider_descriptors" /></td><td><code>array</code></td><td>The property describes target data provider descriptors for the migration project.</td></tr>
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
Expands tags for all <code>migration_projects</code> in a region.
```sql
SELECT
region,
migration_project_name,
migration_project_identifier,
migration_project_arn,
migration_project_creation_time,
instance_profile_identifier,
instance_profile_name,
instance_profile_arn,
transformation_rules,
description,
schema_conversion_application_attributes,
source_data_provider_descriptors,
target_data_provider_descriptors,
tag_key,
tag_value
FROM aws.dms.migration_project_tags
WHERE region = 'us-east-1';
```


## Permissions

For permissions required to operate on the <code>migration_project_tags</code> resource, see <a href="/providers/aws/dms/migration_projects/#permissions"><code>migration_projects</code></a>

