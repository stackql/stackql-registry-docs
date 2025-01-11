---
title: servers
hide_title: false
hide_table_of_contents: false
keywords:
  - servers
  - transfer
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

Creates, updates, deletes or gets a <code>server</code> resource or lists <code>servers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::Transfer::Server Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.transfer.servers" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="as2_service_managed_egress_ip_addresses" /></td><td><code>array</code></td><td>The list of egress IP addresses of this server. These IP addresses are only relevant for servers that use the AS2 protocol. They are used for sending asynchronous MDNs. These IP addresses are assigned automatically when you create an AS2 server. Additionally, if you update an existing server and add the AS2 protocol, static IP addresses are assigned as well.</td></tr>
<tr><td><CopyableCode code="certificate" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="domain" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_details" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="endpoint_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_provider_details" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="identity_provider_type" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="logging_role" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="post_authentication_login_banner" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="pre_authentication_login_banner" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="protocol_details" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="protocols" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="s3_storage_options" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="security_policy_name" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="server_id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="state" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="structured_log_destinations" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="workflow_details" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html"><code>AWS::Transfer::Server</code></a>.

## Methods

<table><tbody>
  <tr>
    <th>Name</th>
    <th>Accessible by</th>
    <th>Required Params</th>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="create_resource" /></td>
    <td><code>INSERT</code></td>
    <td><CopyableCode code="region" /></td>
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
Gets all <code>servers</code> in a region.
```sql
SELECT
region,
arn,
as2_service_managed_egress_ip_addresses,
certificate,
domain,
endpoint_details,
endpoint_type,
identity_provider_details,
identity_provider_type,
logging_role,
post_authentication_login_banner,
pre_authentication_login_banner,
protocol_details,
protocols,
s3_storage_options,
security_policy_name,
server_id,
state,
structured_log_destinations,
tags,
workflow_details
FROM aws.transfer.servers
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>server</code>.
```sql
SELECT
region,
arn,
as2_service_managed_egress_ip_addresses,
certificate,
domain,
endpoint_details,
endpoint_type,
identity_provider_details,
identity_provider_type,
logging_role,
post_authentication_login_banner,
pre_authentication_login_banner,
protocol_details,
protocols,
s3_storage_options,
security_policy_name,
server_id,
state,
structured_log_destinations,
tags,
workflow_details
FROM aws.transfer.servers
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>server</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.transfer.servers (
 Certificate,
 Domain,
 EndpointDetails,
 EndpointType,
 IdentityProviderDetails,
 IdentityProviderType,
 LoggingRole,
 PostAuthenticationLoginBanner,
 PreAuthenticationLoginBanner,
 ProtocolDetails,
 Protocols,
 S3StorageOptions,
 SecurityPolicyName,
 StructuredLogDestinations,
 Tags,
 WorkflowDetails,
 region
)
SELECT 
'{{ Certificate }}',
 '{{ Domain }}',
 '{{ EndpointDetails }}',
 '{{ EndpointType }}',
 '{{ IdentityProviderDetails }}',
 '{{ IdentityProviderType }}',
 '{{ LoggingRole }}',
 '{{ PostAuthenticationLoginBanner }}',
 '{{ PreAuthenticationLoginBanner }}',
 '{{ ProtocolDetails }}',
 '{{ Protocols }}',
 '{{ S3StorageOptions }}',
 '{{ SecurityPolicyName }}',
 '{{ StructuredLogDestinations }}',
 '{{ Tags }}',
 '{{ WorkflowDetails }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.transfer.servers (
 Certificate,
 Domain,
 EndpointDetails,
 EndpointType,
 IdentityProviderDetails,
 IdentityProviderType,
 LoggingRole,
 PostAuthenticationLoginBanner,
 PreAuthenticationLoginBanner,
 ProtocolDetails,
 Protocols,
 S3StorageOptions,
 SecurityPolicyName,
 StructuredLogDestinations,
 Tags,
 WorkflowDetails,
 region
)
SELECT 
 '{{ Certificate }}',
 '{{ Domain }}',
 '{{ EndpointDetails }}',
 '{{ EndpointType }}',
 '{{ IdentityProviderDetails }}',
 '{{ IdentityProviderType }}',
 '{{ LoggingRole }}',
 '{{ PostAuthenticationLoginBanner }}',
 '{{ PreAuthenticationLoginBanner }}',
 '{{ ProtocolDetails }}',
 '{{ Protocols }}',
 '{{ S3StorageOptions }}',
 '{{ SecurityPolicyName }}',
 '{{ StructuredLogDestinations }}',
 '{{ Tags }}',
 '{{ WorkflowDetails }}',
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
  - name: server
    props:
      - name: Certificate
        value: '{{ Certificate }}'
      - name: Domain
        value: '{{ Domain }}'
      - name: EndpointDetails
        value:
          AddressAllocationIds:
            - '{{ AddressAllocationIds[0] }}'
          SubnetIds:
            - '{{ SubnetIds[0] }}'
          VpcEndpointId: '{{ VpcEndpointId }}'
          VpcId: '{{ VpcId }}'
          SecurityGroupIds:
            - '{{ SecurityGroupIds[0] }}'
      - name: EndpointType
        value: '{{ EndpointType }}'
      - name: IdentityProviderDetails
        value:
          Url: '{{ Url }}'
          InvocationRole: '{{ InvocationRole }}'
          DirectoryId: '{{ DirectoryId }}'
          Function: '{{ Function }}'
          SftpAuthenticationMethods: '{{ SftpAuthenticationMethods }}'
      - name: IdentityProviderType
        value: '{{ IdentityProviderType }}'
      - name: LoggingRole
        value: '{{ LoggingRole }}'
      - name: PostAuthenticationLoginBanner
        value: '{{ PostAuthenticationLoginBanner }}'
      - name: PreAuthenticationLoginBanner
        value: '{{ PreAuthenticationLoginBanner }}'
      - name: ProtocolDetails
        value:
          PassiveIp: '{{ PassiveIp }}'
          TlsSessionResumptionMode: '{{ TlsSessionResumptionMode }}'
          SetStatOption: '{{ SetStatOption }}'
          As2Transports:
            - '{{ As2Transports[0] }}'
      - name: Protocols
        value:
          - '{{ Protocols[0] }}'
      - name: S3StorageOptions
        value:
          DirectoryListingOptimization: '{{ DirectoryListingOptimization }}'
      - name: SecurityPolicyName
        value: '{{ SecurityPolicyName }}'
      - name: StructuredLogDestinations
        value:
          - '{{ StructuredLogDestinations[0] }}'
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: WorkflowDetails
        value:
          OnUpload:
            - WorkflowId: '{{ WorkflowId }}'
              ExecutionRole: '{{ ExecutionRole }}'
          OnPartialUpload:
            - null

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.transfer.servers
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>servers</code> resource, the following permissions are required:

### Create
```json
apigateway:GET,
ds:AuthorizeApplication,
ds:DescribeDirectories,
ec2:AssociateAddress,
ec2:CreateVpcEndpoint,
ec2:DescribeAddresses,
ec2:DescribeNetworkInterfaces,
ec2:DescribeVpcEndpoints,
iam:PassRole,
logs:CreateLogDelivery,
logs:DeleteLogDelivery,
logs:DescribeLogGroups,
logs:DescribeResourcePolicies,
logs:GetLogDelivery,
logs:ListLogDeliveries,
logs:PutResourcePolicy,
logs:UpdateLogDelivery,
transfer:CreateServer,
transfer:DescribeServer,
transfer:StartServer,
transfer:StopServer,
transfer:TagResource,
transfer:UpdateServer
```

### Read
```json
ec2:DescribeVpcEndpoints,
transfer:DescribeServer
```

### Update
```json
apigateway:GET,
ec2:AssociateAddress,
ec2:CreateVpcEndpoint,
ec2:DeleteVpcEndpoints,
ec2:DescribeAddresses,
ec2:DescribeNetworkInterfaces,
ec2:DescribeVpcEndpoints,
ec2:DisassociateAddress,
ec2:ModifyVpcEndpoint,
iam:PassRole,
logs:CreateLogDelivery,
logs:DeleteLogDelivery,
logs:DescribeLogGroups,
logs:DescribeResourcePolicies,
logs:GetLogDelivery,
logs:ListLogDeliveries,
logs:PutResourcePolicy,
logs:UpdateLogDelivery,
transfer:DescribeServer,
transfer:StartServer,
transfer:StopServer,
transfer:TagResource,
transfer:UnTagResource,
transfer:UpdateServer
```

### Delete
```json
ds:DescribeDirectories,
ds:UnauthorizeApplication,
ec2:DeleteVpcEndpoints,
ec2:DescribeAddresses,
ec2:DescribeNetworkInterfaces,
ec2:DescribeVpcEndpoints,
ec2:DisassociateAddress,
logs:DeleteLogDelivery,
logs:GetLogDelivery,
logs:ListLogDeliveries,
transfer:DeleteServer
```

### List
```json
transfer:ListServers
```
