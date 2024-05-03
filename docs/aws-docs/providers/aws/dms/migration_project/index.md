---
title: migration_project
hide_title: false
hide_table_of_contents: false
keywords:
  - migration_project
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

Gets or operates on an individual <code>migration_project</code> resource, use <code>migration_projects</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>migration_project</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource schema for AWS::DMS::MigrationProject</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.dms.migration_project" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="migration_project_name" /></td><td><code>string</code></td><td>The property describes a name to identify the migration project.</td></tr>
<tr><td><CopyableCode code="migration_project_identifier" /></td><td><code>string</code></td><td>The property describes an identifier for the migration project. It is used for describing&#x2F;deleting&#x2F;modifying can be name&#x2F;arn</td></tr>
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
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
tags
FROM aws.dms.migration_project
WHERE data__Identifier = '<MigrationProjectArn>';
```

## Permissions

To operate on the <code>migration_project</code> resource, the following permissions are required:

### Read
```json
dms:DescribeMigrationProjects,
dms:ListMigrationProjects,
dms:ListTagsForResource
```

### Update
```json
dms:UpdateMigrationProject,
dms:ModifyMigrationProject,
dms:AddTagsToResource,
dms:RemoveTagsToResource,
dms:ListTagsForResource,
iam:PassRole
```

### Delete
```json
dms:DeleteMigrationProject
```

