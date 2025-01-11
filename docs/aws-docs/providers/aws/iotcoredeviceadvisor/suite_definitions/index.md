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

Creates, updates, deletes or gets a <code>suite_definition</code> resource or lists <code>suite_definitions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>suite_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>An example resource schema demonstrating some basic constructs and validation rules.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.iotcoredeviceadvisor.suite_definitions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="suite_definition_configuration" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="suite_definition_id" /></td><td><code>string</code></td><td>The unique identifier for the suite definition.</td></tr>
<tr><td><CopyableCode code="suite_definition_arn" /></td><td><code>string</code></td><td>The Amazon Resource name for the suite definition.</td></tr>
<tr><td><CopyableCode code="suite_definition_version" /></td><td><code>string</code></td><td>The suite definition version of a test suite.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html"><code>AWS::IoTCoreDeviceAdvisor::SuiteDefinition</code></a>.

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
    <td><CopyableCode code="SuiteDefinitionConfiguration, region" /></td>
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
    <td><CopyableCode code="list_resources" /></td>
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
Gets all <code>suite_definitions</code> in a region.
```sql
SELECT
region,
suite_definition_configuration,
suite_definition_id,
suite_definition_arn,
suite_definition_version,
tags
FROM aws.iotcoredeviceadvisor.suite_definitions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>suite_definition</code>.
```sql
SELECT
region,
suite_definition_configuration,
suite_definition_id,
suite_definition_arn,
suite_definition_version,
tags
FROM aws.iotcoredeviceadvisor.suite_definitions
WHERE region = 'us-east-1' AND data__Identifier = '<SuiteDefinitionId>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>suite_definition</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
/*+ create */
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

## `DELETE` example

```sql
/*+ delete */
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
iot:ListThingPrincipals,
iot:ListThings,
iotdeviceadvisor:CreateSuiteDefinition,
iotdeviceadvisor:TagResource,
iam:PassRole
```

### Read
```json
iotdeviceadvisor:GetSuiteDefinition,
iot:ListTagsForResource
```

### Update
```json
iot:DescribeCertificate,
iot:DescribeThing,
iot:GetPolicy,
iot:ListAttachedPolicies,
iot:ListCertificates,
iot:ListPrincipalPolicies,
iot:ListThingPrincipals,
iot:ListThings,
iotdeviceadvisor:UpdateSuiteDefinition,
iotdeviceadvisor:GetSuiteDefinition,
iotdeviceadvisor:UntagResource,
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
