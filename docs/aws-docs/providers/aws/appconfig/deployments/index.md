---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - appconfig
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

Creates, updates, deletes or gets a <code>deployment</code> resource or lists <code>deployments</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::AppConfig::Deployment</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.appconfig.deployments" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="deployment_strategy_id" /></td><td><code>string</code></td><td>The deployment strategy ID.</td></tr>
<tr><td><CopyableCode code="configuration_profile_id" /></td><td><code>string</code></td><td>The configuration profile ID.</td></tr>
<tr><td><CopyableCode code="environment_id" /></td><td><code>string</code></td><td>The environment ID.</td></tr>
<tr><td><CopyableCode code="kms_key_identifier" /></td><td><code>string</code></td><td>The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>A description of the deployment.</td></tr>
<tr><td><CopyableCode code="configuration_version" /></td><td><code>string</code></td><td>The configuration version to deploy. If deploying an AWS AppConfig hosted configuration version, you can specify either the version number or version label. For all other configurations, you must specify the version number.</td></tr>
<tr><td><CopyableCode code="deployment_number" /></td><td><code>string</code></td><td>The sequence number of the deployment.</td></tr>
<tr><td><CopyableCode code="application_id" /></td><td><code>string</code></td><td>The application ID.</td></tr>
<tr><td><CopyableCode code="dynamic_extension_parameters" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appconfig-deployment.html"><code>AWS::AppConfig::Deployment</code></a>.

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
    <td><CopyableCode code="ApplicationId, ConfigurationProfileId, DeploymentStrategyId, EnvironmentId, ConfigurationVersion, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>deployments</code> in a region.
```sql
SELECT
region,
deployment_strategy_id,
configuration_profile_id,
environment_id,
kms_key_identifier,
description,
configuration_version,
deployment_number,
application_id,
dynamic_extension_parameters,
tags
FROM aws.appconfig.deployments
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>deployment</code>.
```sql
SELECT
region,
deployment_strategy_id,
configuration_profile_id,
environment_id,
kms_key_identifier,
description,
configuration_version,
deployment_number,
application_id,
dynamic_extension_parameters,
tags
FROM aws.appconfig.deployments
WHERE region = 'us-east-1' AND data__Identifier = '<ApplicationId>|<EnvironmentId>|<DeploymentNumber>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>deployment</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.appconfig.deployments (
 DeploymentStrategyId,
 ConfigurationProfileId,
 EnvironmentId,
 ConfigurationVersion,
 ApplicationId,
 region
)
SELECT 
'{{ DeploymentStrategyId }}',
 '{{ ConfigurationProfileId }}',
 '{{ EnvironmentId }}',
 '{{ ConfigurationVersion }}',
 '{{ ApplicationId }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.appconfig.deployments (
 DeploymentStrategyId,
 ConfigurationProfileId,
 EnvironmentId,
 KmsKeyIdentifier,
 Description,
 ConfigurationVersion,
 ApplicationId,
 DynamicExtensionParameters,
 Tags,
 region
)
SELECT 
 '{{ DeploymentStrategyId }}',
 '{{ ConfigurationProfileId }}',
 '{{ EnvironmentId }}',
 '{{ KmsKeyIdentifier }}',
 '{{ Description }}',
 '{{ ConfigurationVersion }}',
 '{{ ApplicationId }}',
 '{{ DynamicExtensionParameters }}',
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
  - name: deployment
    props:
      - name: DeploymentStrategyId
        value: '{{ DeploymentStrategyId }}'
      - name: ConfigurationProfileId
        value: '{{ ConfigurationProfileId }}'
      - name: EnvironmentId
        value: '{{ EnvironmentId }}'
      - name: KmsKeyIdentifier
        value: '{{ KmsKeyIdentifier }}'
      - name: Description
        value: '{{ Description }}'
      - name: ConfigurationVersion
        value: '{{ ConfigurationVersion }}'
      - name: ApplicationId
        value: '{{ ApplicationId }}'
      - name: DynamicExtensionParameters
        value:
          - ParameterValue: '{{ ParameterValue }}'
            ExtensionReference: '{{ ExtensionReference }}'
            ParameterName: '{{ ParameterName }}'
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
DELETE FROM aws.appconfig.deployments
WHERE data__Identifier = '<ApplicationId|EnvironmentId|DeploymentNumber>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>deployments</code> resource, the following permissions are required:

### Read
```json
appconfig:GetDeployment,
appconfig:ListTagsForResource
```

### Create
```json
appconfig:StartDeployment,
appconfig:GetDeployment,
appconfig:TagResource,
appconfig:ListTagsForResource,
kms:GenerateDataKey
```

### List
```json
appconfig:ListDeployments
```

### Delete
```json
appconfig:StopDeployment
```
