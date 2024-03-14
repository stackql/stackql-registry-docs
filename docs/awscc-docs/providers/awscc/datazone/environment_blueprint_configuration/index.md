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
Gets an individual <code>environment_blueprint_configuration</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_blueprint_configuration</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>environment_blueprint_configuration</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.datazone.environment_blueprint_configuration</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>regional_parameters</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>provisioning_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>created_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>enabled_regions</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>environment_blueprint_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>environment_blueprint_id</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>updated_at</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>domain_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>manage_access_role_arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Example
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
FROM awscc.datazone.environment_blueprint_configuration
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

