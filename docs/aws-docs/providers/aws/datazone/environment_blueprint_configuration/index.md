---
title: environment_blueprint_configuration
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_blueprint_configuration
  - datazone
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

Gets or operates on an individual <code>environment_blueprint_configuration</code> resource, use <code>environment_blueprint_configurations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_blueprint_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::DataZone::EnvironmentBlueprintConfiguration Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.environment_blueprint_configuration" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="regional_parameters" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="provisioning_role_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="created_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enabled_regions" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_blueprint_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_blueprint_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="updated_at" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="manage_access_role_arn" /></td><td><code>string</code></td><td></td></tr>
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
regional_parameters,
provisioning_role_arn,
domain_id,
created_at,
enabled_regions,
environment_blueprint_identifier,
environment_blueprint_id,
updated_at,
domain_identifier,
manage_access_role_arn
FROM aws.datazone.environment_blueprint_configuration
WHERE data__Identifier = '<DomainId>|<EnvironmentBlueprintId>';
```

## Permissions

To operate on the <code>environment_blueprint_configuration</code> resource, the following permissions are required:

### Read
```json
datazone:GetEnvironmentBlueprintConfiguration
```

### Update
```json
datazone:DeleteEnvironmentBlueprintConfiguration,
iam:PassRole,
datazone:GetEnvironmentBlueprintConfiguration,
datazone:PutEnvironmentBlueprintConfiguration
```

### Delete
```json
datazone:GetEnvironmentBlueprintConfiguration,
datazone:DeleteEnvironmentBlueprintConfiguration
```

