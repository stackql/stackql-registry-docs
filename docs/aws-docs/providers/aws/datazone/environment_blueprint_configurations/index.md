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


Used to retrieve a list of <code>environment_blueprint_configurations</code> in a region or to create or delete a <code>environment_blueprint_configurations</code> resource, use <code>environment_blueprint_configuration</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>environment_blueprint_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::DataZone::EnvironmentBlueprintConfiguration Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.datazone.environment_blueprint_configurations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="domain_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_blueprint_id" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
domain_id,
environment_blueprint_id
FROM aws.datazone.environment_blueprint_configurations
WHERE region = 'us-east-1';
```

## `INSERT` Example

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
-- environment_blueprint_configuration.iql (required properties only)
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
-- environment_blueprint_configuration.iql (all properties)
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

## `DELETE` Example

```sql
DELETE FROM aws.datazone.environment_blueprint_configurations
WHERE data__Identifier = '<DomainId|EnvironmentBlueprintId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>environment_blueprint_configurations</code> resource, the following permissions are required:

### Create
```json
datazone:ListEnvironmentBlueprints,
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

