---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - apprunner
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

Creates, updates, deletes or gets a <code>service</code> resource or lists <code>services</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AppRunner::Service resource specifies an AppRunner Service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apprunner.services" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="service_name" /></td><td><code>string</code></td><td>The AppRunner Service Name.</td></tr>
<tr><td><CopyableCode code="service_id" /></td><td><code>string</code></td><td>The AppRunner Service Id</td></tr>
<tr><td><CopyableCode code="service_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AppRunner Service.</td></tr>
<tr><td><CopyableCode code="service_url" /></td><td><code>string</code></td><td>The Service Url of the AppRunner Service.</td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td>AppRunner Service status.</td></tr>
<tr><td><CopyableCode code="source_configuration" /></td><td><code>object</code></td><td>Source Code configuration</td></tr>
<tr><td><CopyableCode code="instance_configuration" /></td><td><code>object</code></td><td>Instance Configuration</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="encryption_configuration" /></td><td><code>object</code></td><td>Encryption configuration (KMS key)</td></tr>
<tr><td><CopyableCode code="health_check_configuration" /></td><td><code>object</code></td><td>Health check configuration</td></tr>
<tr><td><CopyableCode code="observability_configuration" /></td><td><code>object</code></td><td>Service observability configuration</td></tr>
<tr><td><CopyableCode code="auto_scaling_configuration_arn" /></td><td><code>string</code></td><td>Autoscaling configuration ARN</td></tr>
<tr><td><CopyableCode code="network_configuration" /></td><td><code>object</code></td><td>Network configuration</td></tr>
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
    <td><CopyableCode code="SourceConfiguration, region" /></td>
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
Gets all <code>services</code> in a region.
```sql
SELECT
region,
service_name,
service_id,
service_arn,
service_url,
status,
source_configuration,
instance_configuration,
tags,
encryption_configuration,
health_check_configuration,
observability_configuration,
auto_scaling_configuration_arn,
network_configuration
FROM aws.apprunner.services
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>service</code>.
```sql
SELECT
region,
service_name,
service_id,
service_arn,
service_url,
status,
source_configuration,
instance_configuration,
tags,
encryption_configuration,
health_check_configuration,
observability_configuration,
auto_scaling_configuration_arn,
network_configuration
FROM aws.apprunner.services
WHERE region = 'us-east-1' AND data__Identifier = '<ServiceArn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>service</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.apprunner.services (
 SourceConfiguration,
 region
)
SELECT 
'{{ SourceConfiguration }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.apprunner.services (
 ServiceName,
 SourceConfiguration,
 InstanceConfiguration,
 Tags,
 EncryptionConfiguration,
 HealthCheckConfiguration,
 ObservabilityConfiguration,
 AutoScalingConfigurationArn,
 NetworkConfiguration,
 region
)
SELECT 
 '{{ ServiceName }}',
 '{{ SourceConfiguration }}',
 '{{ InstanceConfiguration }}',
 '{{ Tags }}',
 '{{ EncryptionConfiguration }}',
 '{{ HealthCheckConfiguration }}',
 '{{ ObservabilityConfiguration }}',
 '{{ AutoScalingConfigurationArn }}',
 '{{ NetworkConfiguration }}',
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
  - name: service
    props:
      - name: ServiceName
        value: '{{ ServiceName }}'
      - name: SourceConfiguration
        value:
          CodeRepository:
            RepositoryUrl: '{{ RepositoryUrl }}'
            SourceCodeVersion:
              Type: '{{ Type }}'
              Value: '{{ Value }}'
            CodeConfiguration:
              ConfigurationSource: '{{ ConfigurationSource }}'
              CodeConfigurationValues:
                Runtime: '{{ Runtime }}'
                BuildCommand: '{{ BuildCommand }}'
                StartCommand: '{{ StartCommand }}'
                Port: '{{ Port }}'
                RuntimeEnvironmentVariables:
                  - Name: '{{ Name }}'
                    Value: '{{ Value }}'
                RuntimeEnvironmentSecrets:
                  - null
            SourceDirectory: '{{ SourceDirectory }}'
          ImageRepository:
            ImageIdentifier: '{{ ImageIdentifier }}'
            ImageConfiguration:
              StartCommand: '{{ StartCommand }}'
              Port: '{{ Port }}'
              RuntimeEnvironmentVariables:
                - null
              RuntimeEnvironmentSecrets:
                - null
            ImageRepositoryType: '{{ ImageRepositoryType }}'
          AutoDeploymentsEnabled: '{{ AutoDeploymentsEnabled }}'
          AuthenticationConfiguration:
            ConnectionArn: '{{ ConnectionArn }}'
            AccessRoleArn: '{{ AccessRoleArn }}'
      - name: InstanceConfiguration
        value:
          Cpu: '{{ Cpu }}'
          Memory: '{{ Memory }}'
          InstanceRoleArn: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: EncryptionConfiguration
        value:
          KmsKey: '{{ KmsKey }}'
      - name: HealthCheckConfiguration
        value:
          Protocol: '{{ Protocol }}'
          Path: '{{ Path }}'
          Interval: '{{ Interval }}'
          Timeout: '{{ Timeout }}'
          HealthyThreshold: '{{ HealthyThreshold }}'
          UnhealthyThreshold: '{{ UnhealthyThreshold }}'
      - name: ObservabilityConfiguration
        value:
          ObservabilityEnabled: '{{ ObservabilityEnabled }}'
          ObservabilityConfigurationArn: '{{ ObservabilityConfigurationArn }}'
      - name: AutoScalingConfigurationArn
        value: '{{ AutoScalingConfigurationArn }}'
      - name: NetworkConfiguration
        value:
          EgressConfiguration:
            EgressType: '{{ EgressType }}'
            VpcConnectorArn: '{{ VpcConnectorArn }}'
          IngressConfiguration:
            IsPubliclyAccessible: '{{ IsPubliclyAccessible }}'
          IpAddressType: '{{ IpAddressType }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.apprunner.services
WHERE data__Identifier = '<ServiceArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>services</code> resource, the following permissions are required:

### Create
```json
apprunner:CreateService,
apprunner:TagResource,
iam:PassRole,
iam:CreateServiceLinkedRole,
logs:CreateLogGroup,
logs:PutRetentionPolicy,
logs:CreateLogStream,
logs:PutLogEvents,
logs:DescribeLogStreams,
events:PutRule,
events:PutTargets
```

### Read
```json
apprunner:DescribeService
```

### Update
```json
apprunner:UpdateService,
iam:PassRole
```

### Delete
```json
apprunner:DeleteService
```

### List
```json
apprunner:ListServices,
iam:PassRole
```

