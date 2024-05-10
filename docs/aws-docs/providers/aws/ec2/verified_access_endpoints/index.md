---
title: verified_access_endpoints
hide_title: false
hide_table_of_contents: false
keywords:
  - verified_access_endpoints
  - ec2
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


Used to retrieve a list of <code>verified_access_endpoints</code> in a region or to create or delete a <code>verified_access_endpoints</code> resource, use <code>verified_access_endpoint</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>verified_access_endpoints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The AWS::EC2::VerifiedAccessEndpoint resource creates an AWS EC2 Verified Access Endpoint.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ec2.verified_access_endpoints" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="verified_access_endpoint_id" /></td><td><code>string</code></td><td>The ID of the AWS Verified Access endpoint.</td></tr>
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
verified_access_endpoint_id
FROM aws.ec2.verified_access_endpoints
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>verified_access_endpoint</code> resource, using <a ref="https://pypi.org/project/stack-deploy/" target="_blank"><code><b>stack-deploy</b></code></a>.

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
-- verified_access_endpoint.iql (required properties only)
INSERT INTO aws.ec2.verified_access_endpoints (
 VerifiedAccessGroupId,
 EndpointType,
 EndpointDomainPrefix,
 DomainCertificateArn,
 AttachmentType,
 ApplicationDomain,
 region
)
SELECT 
'{{ VerifiedAccessGroupId }}',
 '{{ EndpointType }}',
 '{{ EndpointDomainPrefix }}',
 '{{ DomainCertificateArn }}',
 '{{ AttachmentType }}',
 '{{ ApplicationDomain }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
-- verified_access_endpoint.iql (all properties)
INSERT INTO aws.ec2.verified_access_endpoints (
 VerifiedAccessGroupId,
 SecurityGroupIds,
 NetworkInterfaceOptions,
 LoadBalancerOptions,
 EndpointType,
 EndpointDomainPrefix,
 DomainCertificateArn,
 AttachmentType,
 ApplicationDomain,
 Description,
 PolicyDocument,
 PolicyEnabled,
 Tags,
 SseSpecification,
 region
)
SELECT 
 '{{ VerifiedAccessGroupId }}',
 '{{ SecurityGroupIds }}',
 '{{ NetworkInterfaceOptions }}',
 '{{ LoadBalancerOptions }}',
 '{{ EndpointType }}',
 '{{ EndpointDomainPrefix }}',
 '{{ DomainCertificateArn }}',
 '{{ AttachmentType }}',
 '{{ ApplicationDomain }}',
 '{{ Description }}',
 '{{ PolicyDocument }}',
 '{{ PolicyEnabled }}',
 '{{ Tags }}',
 '{{ SseSpecification }}',
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
  - name: verified_access_endpoint
    props:
      - name: VerifiedAccessGroupId
        value: '{{ VerifiedAccessGroupId }}'
      - name: SecurityGroupIds
        value:
          - '{{ SecurityGroupIds[0] }}'
      - name: NetworkInterfaceOptions
        value:
          NetworkInterfaceId: '{{ NetworkInterfaceId }}'
          Port: '{{ Port }}'
          Protocol: '{{ Protocol }}'
      - name: LoadBalancerOptions
        value:
          LoadBalancerArn: '{{ LoadBalancerArn }}'
          Port: '{{ Port }}'
          Protocol: '{{ Protocol }}'
          SubnetIds:
            - '{{ SubnetIds[0] }}'
      - name: EndpointType
        value: '{{ EndpointType }}'
      - name: EndpointDomainPrefix
        value: '{{ EndpointDomainPrefix }}'
      - name: DomainCertificateArn
        value: '{{ DomainCertificateArn }}'
      - name: AttachmentType
        value: '{{ AttachmentType }}'
      - name: ApplicationDomain
        value: '{{ ApplicationDomain }}'
      - name: Description
        value: '{{ Description }}'
      - name: PolicyDocument
        value: '{{ PolicyDocument }}'
      - name: PolicyEnabled
        value: '{{ PolicyEnabled }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: SseSpecification
        value:
          KmsKeyArn: '{{ KmsKeyArn }}'
          CustomerManagedKeyEnabled: '{{ CustomerManagedKeyEnabled }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.ec2.verified_access_endpoints
WHERE data__Identifier = '<VerifiedAccessEndpointId>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>verified_access_endpoints</code> resource, the following permissions are required:

### Create
```json
ec2:CreateVerifiedAccessEndpoint,
ec2:DescribeVerifiedAccessEndpoints,
ec2:CreateTags,
ec2:DescribeTags,
iam:CreateServiceLinkedRole,
iam:ListRoles,
acm:GetCertificateWithPK,
acm:DescribeCertificate,
acm:CreateCertificateRelation,
sso:GetManagedApplicationInstance,
sso:GetPeregrineStatus,
sso:GetSharedSsoConfiguration,
sso:CreateManagedApplicationInstance,
ec2:DescribeSubnets,
ec2:DescribeSecurityGroups,
ec2:DescribeNetworkInterfaces,
ec2:DescribeAccountAttributes,
elasticloadbalancing:DescribeLoadBalancers,
elasticloadbalancing:DescribeListeners,
elasticloadbalancing:DescribeListenerCertificates,
acm:DeleteCertificateRelation,
ec2:DeleteTags,
ec2:DeleteVerifiedAccessEndpoint,
ec2:GetVerifiedAccessEndpointPolicy,
ec2:ModifyVerifiedAccessEndpoint,
ec2:ModifyVerifiedAccessEndpointPolicy,
sso:DeleteManagedApplicationInstance,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

### Delete
```json
ec2:DescribeVerifiedAccessEndpoints,
ec2:DescribeTags,
ec2:DeleteVerifiedAccessEndpoint,
ec2:DeleteTags,
sso:DeleteManagedApplicationInstance,
acm:DeleteCertificateRelation,
acm:DescribeCertificate,
acm:CreateCertificateRelation,
acm:GetCertificateWithPK,
ec2:CreateTags,
ec2:CreateVerifiedAccessEndpoint,
ec2:DescribeAccountAttributes,
ec2:DescribeNetworkInterfaces,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:GetVerifiedAccessEndpointPolicy,
ec2:ModifyVerifiedAccessEndpoint,
ec2:ModifyVerifiedAccessEndpointPolicy,
elasticloadbalancing:DescribeListenerCertificates,
elasticloadbalancing:DescribeListeners,
elasticloadbalancing:DescribeLoadBalancers,
iam:CreateServiceLinkedRole,
iam:ListRoles,
sso:CreateManagedApplicationInstance,
sso:GetManagedApplicationInstance,
sso:GetPeregrineStatus,
sso:GetSharedSsoConfiguration,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

### List
```json
ec2:DescribeVerifiedAccessEndpoints,
ec2:DescribeTags,
acm:CreateCertificateRelation,
acm:DeleteCertificateRelation,
acm:DescribeCertificate,
acm:GetCertificateWithPK,
ec2:CreateTags,
ec2:CreateVerifiedAccessEndpoint,
ec2:DeleteTags,
ec2:DeleteVerifiedAccessEndpoint,
ec2:DescribeAccountAttributes,
ec2:DescribeNetworkInterfaces,
ec2:DescribeSecurityGroups,
ec2:DescribeSubnets,
ec2:GetVerifiedAccessEndpointPolicy,
ec2:ModifyVerifiedAccessEndpoint,
ec2:ModifyVerifiedAccessEndpointPolicy,
elasticloadbalancing:DescribeListenerCertificates,
elasticloadbalancing:DescribeListeners,
elasticloadbalancing:DescribeLoadBalancers,
iam:CreateServiceLinkedRole,
iam:ListRoles,
sso:CreateManagedApplicationInstance,
sso:DeleteManagedApplicationInstance,
sso:GetManagedApplicationInstance,
sso:GetPeregrineStatus,
sso:GetSharedSsoConfiguration,
kms:DescribeKey,
kms:RetireGrant,
kms:CreateGrant,
kms:GenerateDataKey,
kms:Decrypt
```

