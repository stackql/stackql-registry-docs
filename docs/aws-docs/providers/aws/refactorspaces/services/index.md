---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - refactorspaces
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
<tr><td><b>Description</b></td><td>Definition of AWS::RefactorSpaces::Service Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.refactorspaces.services" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="environment_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_identifier" /></td><td><code>string</code></td><td></td></tr>
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
environment_identifier,
application_identifier,
service_identifier
FROM aws.refactorspaces.services
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
 "ApplicationIdentifier": "{{ ApplicationIdentifier }}",
 "EndpointType": "{{ EndpointType }}",
 "EnvironmentIdentifier": "{{ EnvironmentIdentifier }}",
 "Name": "{{ Name }}"
}
>>>
--required properties only
INSERT INTO aws.refactorspaces.services (
 ApplicationIdentifier,
 EndpointType,
 EnvironmentIdentifier,
 Name,
 region
)
SELECT 
{{ .ApplicationIdentifier }},
 {{ .EndpointType }},
 {{ .EnvironmentIdentifier }},
 {{ .Name }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ApplicationIdentifier": "{{ ApplicationIdentifier }}",
 "Description": "{{ Description }}",
 "EndpointType": "{{ EndpointType }}",
 "EnvironmentIdentifier": "{{ EnvironmentIdentifier }}",
 "LambdaEndpoint": {
  "Arn": "{{ Arn }}"
 },
 "Name": "{{ Name }}",
 "UrlEndpoint": {
  "HealthUrl": "{{ HealthUrl }}",
  "Url": "{{ Url }}"
 },
 "VpcId": "{{ VpcId }}",
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.refactorspaces.services (
 ApplicationIdentifier,
 Description,
 EndpointType,
 EnvironmentIdentifier,
 LambdaEndpoint,
 Name,
 UrlEndpoint,
 VpcId,
 Tags,
 region
)
SELECT 
 {{ .ApplicationIdentifier }},
 {{ .Description }},
 {{ .EndpointType }},
 {{ .EnvironmentIdentifier }},
 {{ .LambdaEndpoint }},
 {{ .Name }},
 {{ .UrlEndpoint }},
 {{ .VpcId }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.refactorspaces.services
WHERE data__Identifier = '<EnvironmentIdentifier|ApplicationIdentifier|ServiceIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>services</code> resource, the following permissions are required:

### Create
```json
refactor-spaces:CreateService,
refactor-spaces:GetService,
refactor-spaces:TagResource,
ec2:DescribeVpcs,
ec2:DescribeSubnets,
ec2:DescribeRouteTables,
ec2:CreateTags,
ec2:CreateTransitGatewayVpcAttachment,
ec2:DescribeTransitGatewayVpcAttachments,
ec2:CreateSecurityGroup,
ec2:AuthorizeSecurityGroupIngress,
ec2:CreateRoute,
lambda:GetFunctionConfiguration
```

### Delete
```json
refactor-spaces:DeleteService,
refactor-spaces:GetService,
refactor-spaces:UntagResource,
ram:DisassociateResourceShare,
ec2:DescribeNetworkInterfaces,
ec2:DescribeRouteTables,
ec2:DescribeTransitGatewayVpcAttachments,
ec2:DescribeSecurityGroups,
ec2:DeleteSecurityGroup,
ec2:DeleteRoute,
ec2:RevokeSecurityGroupIngress,
ec2:DeleteTransitGatewayVpcAttachment,
ec2:DeleteTags
```

### List
```json
refactor-spaces:ListServices,
refactor-spaces:ListTagsForResource
```

