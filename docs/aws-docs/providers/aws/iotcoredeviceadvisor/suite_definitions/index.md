---
title: suite_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - suite_definitions
  - iotcoredeviceadvisor
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


Used to retrieve a list of <code>suite_definitions</code> in a region or to create or delete a <code>suite_definitions</code> resource, use <code>suite_definition</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>suite_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotcoredeviceadvisor.suite_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="suite_definition_id" /></td><td><code>string</code></td><td>The unique identifier for the suite definition.</td></tr>
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
suite_definition_id
FROM aws.iotcoredeviceadvisor.suite_definitions
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>suite_definition</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- suite_definition.iql (required properties only)
INSERT INTO aws.iotcoredeviceadvisor.suite_definitions (
 SuiteDefinitionConfiguration,
 region
)
SELECT 
'{{ SuiteDefinitionConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- suite_definition.iql (all properties)
INSERT INTO aws.iotcoredeviceadvisor.suite_definitions (
 SuiteDefinitionConfiguration,
 Tags,
 region
)
SELECT 
 '{{ SuiteDefinitionConfiguration }}',
 '{{ Tags }}',
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
  - name: suite_definition
    props:
      - name: SuiteDefinitionConfiguration
        value:
          DevicePermissionRoleArn: '{{ DevicePermissionRoleArn }}'
          Devices:
            - CertificateArn: '{{ CertificateArn }}'
              ThingArn: '{{ ThingArn }}'
          IntendedForQualification: '{{ IntendedForQualification }}'
          RootGroup: '{{ RootGroup }}'
          SuiteDefinitionName: '{{ SuiteDefinitionName }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.iotcoredeviceadvisor.suite_definitions
WHERE data__Identifier = '<SuiteDefinitionId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>suite_definitions</code> resource, the following permissions are required:

### Create
```json
iot:DescribeCertificate,
iot:DescribeThing,
iot:GetPolicy,
iot:ListAttachedPolicies,
iot:ListCertificates,
iot:ListPrincipalPolicies,
iot:ListTagsForResource,
iot:ListThingPrincipals,
iot:ListThings,
iotdeviceadvisor:CreateSuiteDefinition,
iotdeviceadvisor:TagResource,
iam:PassRole
```

### Delete
```json
iotdeviceadvisor:GetSuiteDefinition,
iotdeviceadvisor:DeleteSuiteDefinition
```

### List
```json
iotdeviceadvisor:ListSuiteDefinitions
```

