---
title: containers
hide_title: false
hide_table_of_contents: false
keywords:
  - containers
  - lightsail
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

Creates, updates, deletes or gets a <code>container</code> resource or lists <code>containers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Container</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.containers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="service_name" /></td><td><code>string</code></td><td>The name for the container service.</td></tr>
<tr><td><CopyableCode code="power" /></td><td><code>string</code></td><td>The power specification for the container service.</td></tr>
<tr><td><CopyableCode code="container_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="scale" /></td><td><code>integer</code></td><td>The scale specification for the container service.</td></tr>
<tr><td><CopyableCode code="public_domain_names" /></td><td><code>array</code></td><td>The public domain names to use with the container service, such as example.com and www.example.com.</td></tr>
<tr><td><CopyableCode code="container_service_deployment" /></td><td><code>object</code></td><td>Describes a container deployment configuration of an Amazon Lightsail container service.</td></tr>
<tr><td><CopyableCode code="is_disabled" /></td><td><code>boolean</code></td><td>A Boolean value to indicate whether the container service is disabled.</td></tr>
<tr><td><CopyableCode code="private_registry_access" /></td><td><code>object</code></td><td>A Boolean value to indicate whether the container service has access to private container image repositories, such as Amazon Elastic Container Registry (Amazon ECR) private repositories.</td></tr>
<tr><td><CopyableCode code="url" /></td><td><code>string</code></td><td>The publicly accessible URL of the container service.</td></tr>
<tr><td><CopyableCode code="principal_arn" /></td><td><code>string</code></td><td>The principal ARN of the container service.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>An array of key-value pairs to apply to this resource.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lightsail-container.html"><code>AWS::Lightsail::Container</code></a>.

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
    <td><CopyableCode code="ServiceName, Power, Scale, region" /></td>
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
Gets all <code>containers</code> in a region.
```sql
SELECT
region,
service_name,
power,
container_arn,
scale,
public_domain_names,
container_service_deployment,
is_disabled,
private_registry_access,
url,
principal_arn,
tags
FROM aws.lightsail.containers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>container</code>.
```sql
SELECT
region,
service_name,
power,
container_arn,
scale,
public_domain_names,
container_service_deployment,
is_disabled,
private_registry_access,
url,
principal_arn,
tags
FROM aws.lightsail.containers
WHERE region = 'us-east-1' AND data__Identifier = '<ServiceName>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>container</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.lightsail.containers (
 ServiceName,
 Power,
 Scale,
 region
)
SELECT 
'{{ ServiceName }}',
 '{{ Power }}',
 '{{ Scale }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.lightsail.containers (
 ServiceName,
 Power,
 Scale,
 PublicDomainNames,
 ContainerServiceDeployment,
 IsDisabled,
 PrivateRegistryAccess,
 Tags,
 region
)
SELECT 
 '{{ ServiceName }}',
 '{{ Power }}',
 '{{ Scale }}',
 '{{ PublicDomainNames }}',
 '{{ ContainerServiceDeployment }}',
 '{{ IsDisabled }}',
 '{{ PrivateRegistryAccess }}',
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
  - name: container
    props:
      - name: ServiceName
        value: '{{ ServiceName }}'
      - name: Power
        value: '{{ Power }}'
      - name: Scale
        value: '{{ Scale }}'
      - name: PublicDomainNames
        value:
          - CertificateName: '{{ CertificateName }}'
            DomainNames:
              - '{{ DomainNames[0] }}'
      - name: ContainerServiceDeployment
        value:
          Containers:
            - ServiceName: '{{ ServiceName }}'
              Power: '{{ Power }}'
              Scale: '{{ Scale }}'
              PublicDomainNames:
                - null
              ContainerServiceDeployment: null
              IsDisabled: '{{ IsDisabled }}'
              PrivateRegistryAccess:
                EcrImagePullerRole:
                  IsActive: '{{ IsActive }}'
                  PrincipalArn: '{{ PrincipalArn }}'
              Tags:
                - Key: '{{ Key }}'
                  Value: '{{ Value }}'
          PublicEndpoint:
            ContainerName: '{{ ContainerName }}'
            ContainerPort: '{{ ContainerPort }}'
            HealthCheckConfig:
              HealthyThreshold: '{{ HealthyThreshold }}'
              IntervalSeconds: '{{ IntervalSeconds }}'
              Path: '{{ Path }}'
              SuccessCodes: '{{ SuccessCodes }}'
              TimeoutSeconds: '{{ TimeoutSeconds }}'
              UnhealthyThreshold: '{{ UnhealthyThreshold }}'
      - name: IsDisabled
        value: '{{ IsDisabled }}'
      - name: PrivateRegistryAccess
        value: null
      - name: Tags
        value:
          - null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.lightsail.containers
WHERE data__Identifier = '<ServiceName>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>containers</code> resource, the following permissions are required:

### Create
```json
lightsail:CreateContainerService,
lightsail:CreateContainerServiceDeployment,
lightsail:GetContainerServices,
lightsail:TagResource,
lightsail:UntagResource,
lightsail:UpdateContainerService
```

### Read
```json
lightsail:GetContainerServices
```

### Delete
```json
lightsail:DeleteContainerService,
lightsail:GetContainerServices
```

### List
```json
lightsail:GetContainerServices
```

### Update
```json
lightsail:CreateContainerServiceDeployment,
lightsail:GetContainerServices,
lightsail:TagResource,
lightsail:UntagResource,
lightsail:UpdateContainerService
```
