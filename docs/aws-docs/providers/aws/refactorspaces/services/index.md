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

Creates, updates, deletes or gets a <code>service</code> resource or lists <code>services</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::RefactorSpaces::Service Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.refactorspaces.services" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="application_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_type" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="environment_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="lambda_endpoint" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="service_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="url_endpoint" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="vpc_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.</td></tr>
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
    <td><CopyableCode code="EnvironmentIdentifier, ApplicationIdentifier, EndpointType, Name, region" /></td>
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
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` examples
List all <code>services</code> in a region.
```sql
SELECT
region,
environment_identifier,
application_identifier,
service_identifier
FROM aws.refactorspaces.services
WHERE region = 'us-east-1';
```
Gets all properties from a <code>service</code>.
```sql
SELECT
region,
arn,
application_identifier,
description,
endpoint_type,
environment_identifier,
lambda_endpoint,
name,
service_identifier,
url_endpoint,
vpc_id,
tags
FROM aws.refactorspaces.services
WHERE region = 'us-east-1' AND data__Identifier = '<EnvironmentIdentifier>|<ApplicationIdentifier>|<ServiceIdentifier>';
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
INSERT INTO aws.refactorspaces.services (
 ApplicationIdentifier,
 EndpointType,
 EnvironmentIdentifier,
 Name,
 region
)
SELECT 
'{{ ApplicationIdentifier }}',
 '{{ EndpointType }}',
 '{{ EnvironmentIdentifier }}',
 '{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
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
 '{{ ApplicationIdentifier }}',
 '{{ Description }}',
 '{{ EndpointType }}',
 '{{ EnvironmentIdentifier }}',
 '{{ LambdaEndpoint }}',
 '{{ Name }}',
 '{{ UrlEndpoint }}',
 '{{ VpcId }}',
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
  - name: service
    props:
      - name: ApplicationIdentifier
        value: '{{ ApplicationIdentifier }}'
      - name: Description
        value: '{{ Description }}'
      - name: EndpointType
        value: '{{ EndpointType }}'
      - name: EnvironmentIdentifier
        value: '{{ EnvironmentIdentifier }}'
      - name: LambdaEndpoint
        value:
          Arn: '{{ Arn }}'
      - name: Name
        value: '{{ Name }}'
      - name: UrlEndpoint
        value:
          HealthUrl: '{{ HealthUrl }}'
          Url: '{{ Url }}'
      - name: VpcId
        value: '{{ VpcId }}'
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

### Read
```json
refactor-spacess:GetService,
refactor-spaces:ListTagsForResource
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

