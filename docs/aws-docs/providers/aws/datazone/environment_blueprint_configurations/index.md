---
title: environment_blueprint_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - environment_blueprint_configurations
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
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes or gets an <code>environment_blueprint_configuration</code> resource or lists <code>environment_blueprint_configurations</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_blueprint_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::DataZone::EnvironmentBlueprintConfiguration Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.environment_blueprint_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="regional_parameters" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="DomainIdentifier, EnvironmentBlueprintIdentifier, EnabledRegions, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>environment_blueprint_configurations</code> in a region.
```sql
SELECT
region,
domain_id,
environment_blueprint_id
FROM aws.datazone.environment_blueprint_configurations
WHERE region = 'us-east-1';
```
Gets all properties from an <code>environment_blueprint_configuration</code>.
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
FROM aws.datazone.environment_blueprint_configurations
WHERE region = 'us-east-1' AND data__Identifier = '<DomainId>|<EnvironmentBlueprintId>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>environment_blueprint_configuration</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
      { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="required">

```sql
/*+ create */
INSERT INTO aws.datazone.environment_blueprint_configurations (
 EnabledRegions,
 EnvironmentBlueprintIdentifier,
 DomainIdentifier,
 region
)
SELECT 
'{{ EnabledRegions }}',
 '{{ EnvironmentBlueprintIdentifier }}',
 '{{ DomainIdentifier }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.datazone.environment_blueprint_configurations (
 RegionalParameters,
 ProvisioningRoleArn,
 EnabledRegions,
 EnvironmentBlueprintIdentifier,
 DomainIdentifier,
 ManageAccessRoleArn,
 region
)
SELECT 
 '{{ RegionalParameters }}',
 '{{ ProvisioningRoleArn }}',
 '{{ EnabledRegions }}',
 '{{ EnvironmentBlueprintIdentifier }}',
 '{{ DomainIdentifier }}',
 '{{ ManageAccessRoleArn }}',
 '{{ region }}';
```
</TabItem>
<TabItem value="manifest">

```yaml
version: 1
name: stack name
description: stack description
providers:
  - aws
globals:
  - name: region
    value: '{{ vars.AWS_REGION }}'
resources:
  - name: environment_blueprint_configuration
    props:
      - name: RegionalParameters
        value:
          - Parameters: {}
            Region: '{{ Region }}'
      - name: ProvisioningRoleArn
        value: '{{ ProvisioningRoleArn }}'
      - name: EnabledRegions
        value:
          - '{{ EnabledRegions[0] }}'
      - name: EnvironmentBlueprintIdentifier
        value: '{{ EnvironmentBlueprintIdentifier }}'
      - name: DomainIdentifier
        value: '{{ DomainIdentifier }}'
      - name: ManageAccessRoleArn
        value: '{{ ManageAccessRoleArn }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.datazone.environment_blueprint_configurations
WHERE data__Identifier = '<DomainId|EnvironmentBlueprintId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>environment_blueprint_configurations</code> resource, the following permissions are required:

### Read
```json
datazone:GetEnvironmentBlueprintConfiguration
```

### Create
```json
datazone:ListEnvironmentBlueprints,
iam:PassRole,
datazone:GetEnvironmentBlueprintConfiguration,
datazone:PutEnvironmentBlueprintConfiguration
```

### Update
```json
datazone:DeleteEnvironmentBlueprintConfiguration,
iam:PassRole,
datazone:GetEnvironmentBlueprintConfiguration,
datazone:PutEnvironmentBlueprintConfiguration
```

### List
```json
datazone:ListEnvironmentBlueprintConfigurations
```

### Delete
```json
datazone:GetEnvironmentBlueprintConfiguration,
datazone:DeleteEnvironmentBlueprintConfiguration
```

