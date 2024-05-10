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


Used to retrieve a list of <code>services</code> in a region or to create or delete a <code>services</code> resource, use <code>service</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::AppRunner::Service resource specifies an AppRunner Service.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.apprunner.services" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="service_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the AppRunner Service.</td></tr>
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
service_arn
FROM aws.apprunner.services
WHERE region = 'us-east-1';
```

## `INSERT` Example

<Tabs
    defaultValue="required"
    values={[
      { label: 'Required Properties', value: 'required', },
      { label: 'All Properties', value: 'all', },
    ]
}>
<TabItem value="required">

```sql
<<<json
{
 "SourceConfiguration": {
  "CodeRepository": {
   "RepositoryUrl": "{{ RepositoryUrl }}",
   "SourceCodeVersion": {
    "Type": "{{ Type }}",
    "Value": "{{ Value }}"
   },
   "CodeConfiguration": {
    "ConfigurationSource": "{{ ConfigurationSource }}",
    "CodeConfigurationValues": {
     "Runtime": "{{ Runtime }}",
     "BuildCommand": "{{ BuildCommand }}",
     "StartCommand": "{{ StartCommand }}",
     "Port": "{{ Port }}",
     "RuntimeEnvironmentVariables": [
      {
       "Name": "{{ Name }}",
       "Value": "{{ Value }}"
      }
     ],
     "RuntimeEnvironmentSecrets": [
      null
     ]
    }
   },
   "SourceDirectory": "{{ SourceDirectory }}"
  },
  "ImageRepository": {
   "ImageIdentifier": "{{ ImageIdentifier }}",
   "ImageConfiguration": {
    "StartCommand": "{{ StartCommand }}",
    "Port": "{{ Port }}",
    "RuntimeEnvironmentVariables": [
     null
    ],
    "RuntimeEnvironmentSecrets": [
     null
    ]
   },
   "ImageRepositoryType": "{{ ImageRepositoryType }}"
  },
  "AutoDeploymentsEnabled": "{{ AutoDeploymentsEnabled }}",
  "AuthenticationConfiguration": {
   "ConnectionArn": "{{ ConnectionArn }}",
   "AccessRoleArn": "{{ AccessRoleArn }}"
  }
 }
}
>>>
--required properties only
INSERT INTO aws.apprunner.services (
 SourceConfiguration,
 region
)
SELECT 
{{ .SourceConfiguration }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ServiceName": "{{ ServiceName }}",
 "SourceConfiguration": {
  "CodeRepository": {
   "RepositoryUrl": "{{ RepositoryUrl }}",
   "SourceCodeVersion": {
    "Type": "{{ Type }}",
    "Value": "{{ Value }}"
   },
   "CodeConfiguration": {
    "ConfigurationSource": "{{ ConfigurationSource }}",
    "CodeConfigurationValues": {
     "Runtime": "{{ Runtime }}",
     "BuildCommand": "{{ BuildCommand }}",
     "StartCommand": "{{ StartCommand }}",
     "Port": "{{ Port }}",
     "RuntimeEnvironmentVariables": [
      {
       "Name": "{{ Name }}",
       "Value": "{{ Value }}"
      }
     ],
     "RuntimeEnvironmentSecrets": [
      null
     ]
    }
   },
   "SourceDirectory": "{{ SourceDirectory }}"
  },
  "ImageRepository": {
   "ImageIdentifier": "{{ ImageIdentifier }}",
   "ImageConfiguration": {
    "StartCommand": "{{ StartCommand }}",
    "Port": "{{ Port }}",
    "RuntimeEnvironmentVariables": [
     null
    ],
    "RuntimeEnvironmentSecrets": [
     null
    ]
   },
   "ImageRepositoryType": "{{ ImageRepositoryType }}"
  },
  "AutoDeploymentsEnabled": "{{ AutoDeploymentsEnabled }}",
  "AuthenticationConfiguration": {
   "ConnectionArn": "{{ ConnectionArn }}",
   "AccessRoleArn": "{{ AccessRoleArn }}"
  }
 },
 "InstanceConfiguration": {
  "Cpu": "{{ Cpu }}",
  "Memory": "{{ Memory }}",
  "InstanceRoleArn": null
 },
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ],
 "EncryptionConfiguration": {
  "KmsKey": "{{ KmsKey }}"
 },
 "HealthCheckConfiguration": {
  "Protocol": "{{ Protocol }}",
  "Path": "{{ Path }}",
  "Interval": "{{ Interval }}",
  "Timeout": "{{ Timeout }}",
  "HealthyThreshold": "{{ HealthyThreshold }}",
  "UnhealthyThreshold": "{{ UnhealthyThreshold }}"
 },
 "ObservabilityConfiguration": {
  "ObservabilityEnabled": "{{ ObservabilityEnabled }}",
  "ObservabilityConfigurationArn": "{{ ObservabilityConfigurationArn }}"
 },
 "AutoScalingConfigurationArn": "{{ AutoScalingConfigurationArn }}",
 "NetworkConfiguration": {
  "EgressConfiguration": {
   "EgressType": "{{ EgressType }}",
   "VpcConnectorArn": "{{ VpcConnectorArn }}"
  },
  "IngressConfiguration": {
   "IsPubliclyAccessible": "{{ IsPubliclyAccessible }}"
  },
  "IpAddressType": "{{ IpAddressType }}"
 }
}
>>>
--all properties
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
 {{ .ServiceName }},
 {{ .SourceConfiguration }},
 {{ .InstanceConfiguration }},
 {{ .Tags }},
 {{ .EncryptionConfiguration }},
 {{ .HealthCheckConfiguration }},
 {{ .ObservabilityConfiguration }},
 {{ .AutoScalingConfigurationArn }},
 {{ .NetworkConfiguration }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
apprunner:DeleteService
```

### List
```json
apprunner:ListServices,
iam:PassRole
```

