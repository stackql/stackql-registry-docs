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


Used to retrieve a list of <code>containers</code> in a region or to create or delete a <code>containers</code> resource, use <code>container</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource Type definition for AWS::Lightsail::Container</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lightsail.containers" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="service_name" /></td><td><code>string</code></td><td>The name for the container service.</td></tr>
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
service_name
FROM aws.lightsail.containers
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
 "ServiceName": "{{ ServiceName }}",
 "Power": "{{ Power }}",
 "Scale": "{{ Scale }}"
}
>>>
--required properties only
INSERT INTO aws.lightsail.containers (
 ServiceName,
 Power,
 Scale,
 region
)
SELECT 
{{ ServiceName }},
 {{ Power }},
 {{ Scale }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ServiceName": "{{ ServiceName }}",
 "Power": "{{ Power }}",
 "Scale": "{{ Scale }}",
 "PublicDomainNames": [
  {
   "CertificateName": "{{ CertificateName }}",
   "DomainNames": [
    "{{ DomainNames[0] }}"
   ]
  }
 ],
 "ContainerServiceDeployment": {
  "Containers": [
   {
    "ServiceName": "{{ ServiceName }}",
    "Power": "{{ Power }}",
    "Scale": "{{ Scale }}",
    "PublicDomainNames": [
     null
    ],
    "ContainerServiceDeployment": null,
    "IsDisabled": "{{ IsDisabled }}",
    "PrivateRegistryAccess": {
     "EcrImagePullerRole": {
      "IsActive": "{{ IsActive }}",
      "PrincipalArn": "{{ PrincipalArn }}"
     }
    },
    "Tags": [
     {
      "Key": "{{ Key }}",
      "Value": "{{ Value }}"
     }
    ]
   }
  ],
  "PublicEndpoint": {
   "ContainerName": "{{ ContainerName }}",
   "ContainerPort": "{{ ContainerPort }}",
   "HealthCheckConfig": {
    "HealthyThreshold": "{{ HealthyThreshold }}",
    "IntervalSeconds": "{{ IntervalSeconds }}",
    "Path": "{{ Path }}",
    "SuccessCodes": "{{ SuccessCodes }}",
    "TimeoutSeconds": "{{ TimeoutSeconds }}",
    "UnhealthyThreshold": "{{ UnhealthyThreshold }}"
   }
  }
 },
 "IsDisabled": "{{ IsDisabled }}",
 "PrivateRegistryAccess": null,
 "Tags": [
  null
 ]
}
>>>
--all properties
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
 {{ ServiceName }},
 {{ Power }},
 {{ Scale }},
 {{ PublicDomainNames }},
 {{ ContainerServiceDeployment }},
 {{ IsDisabled }},
 {{ PrivateRegistryAccess }},
 {{ Tags }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

### Delete
```json
lightsail:DeleteContainerService,
lightsail:GetContainerServices
```

### List
```json
lightsail:GetContainerServices
```

