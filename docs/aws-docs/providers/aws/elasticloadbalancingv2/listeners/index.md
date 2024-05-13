---
title: listeners
hide_title: false
hide_table_of_contents: false
keywords:
  - listeners
  - elasticloadbalancingv2
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


Used to retrieve a list of <code>listeners</code> in a region or to create or delete a <code>listeners</code> resource, use <code>listener</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listeners</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a listener for an Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticloadbalancingv2.listeners" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="listener_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="LoadBalancerArn, DefaultActions, region" /></td>
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
listener_arn
FROM aws.elasticloadbalancingv2.listeners
WHERE region = 'us-east-1';
```

## `INSERT` Example

Use the following StackQL query and manifest file to create a new <code>listener</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.elasticloadbalancingv2.listeners (
 LoadBalancerArn,
 DefaultActions,
 region
)
SELECT 
'{{ LoadBalancerArn }}',
 '{{ DefaultActions }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.elasticloadbalancingv2.listeners (
 SslPolicy,
 LoadBalancerArn,
 DefaultActions,
 Port,
 Certificates,
 Protocol,
 AlpnPolicy,
 MutualAuthentication,
 region
)
SELECT 
 '{{ SslPolicy }}',
 '{{ LoadBalancerArn }}',
 '{{ DefaultActions }}',
 '{{ Port }}',
 '{{ Certificates }}',
 '{{ Protocol }}',
 '{{ AlpnPolicy }}',
 '{{ MutualAuthentication }}',
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
  - name: listener
    props:
      - name: SslPolicy
        value: '{{ SslPolicy }}'
      - name: LoadBalancerArn
        value: '{{ LoadBalancerArn }}'
      - name: DefaultActions
        value:
          - Order: '{{ Order }}'
            TargetGroupArn: '{{ TargetGroupArn }}'
            FixedResponseConfig:
              ContentType: '{{ ContentType }}'
              StatusCode: '{{ StatusCode }}'
              MessageBody: '{{ MessageBody }}'
            AuthenticateCognitoConfig:
              OnUnauthenticatedRequest: '{{ OnUnauthenticatedRequest }}'
              UserPoolClientId: '{{ UserPoolClientId }}'
              UserPoolDomain: '{{ UserPoolDomain }}'
              SessionTimeout: '{{ SessionTimeout }}'
              Scope: '{{ Scope }}'
              SessionCookieName: '{{ SessionCookieName }}'
              UserPoolArn: '{{ UserPoolArn }}'
              AuthenticationRequestExtraParams: {}
            Type: '{{ Type }}'
            RedirectConfig:
              Path: '{{ Path }}'
              Query: '{{ Query }}'
              Port: '{{ Port }}'
              Host: '{{ Host }}'
              Protocol: '{{ Protocol }}'
              StatusCode: '{{ StatusCode }}'
            ForwardConfig:
              TargetGroupStickinessConfig:
                Enabled: '{{ Enabled }}'
                DurationSeconds: '{{ DurationSeconds }}'
              TargetGroups:
                - TargetGroupArn: '{{ TargetGroupArn }}'
                  Weight: '{{ Weight }}'
            AuthenticateOidcConfig:
              OnUnauthenticatedRequest: '{{ OnUnauthenticatedRequest }}'
              TokenEndpoint: '{{ TokenEndpoint }}'
              SessionTimeout: '{{ SessionTimeout }}'
              Scope: '{{ Scope }}'
              Issuer: '{{ Issuer }}'
              ClientSecret: '{{ ClientSecret }}'
              UserInfoEndpoint: '{{ UserInfoEndpoint }}'
              ClientId: '{{ ClientId }}'
              AuthorizationEndpoint: '{{ AuthorizationEndpoint }}'
              SessionCookieName: '{{ SessionCookieName }}'
              UseExistingClientSecret: '{{ UseExistingClientSecret }}'
              AuthenticationRequestExtraParams: {}
      - name: Port
        value: '{{ Port }}'
      - name: Certificates
        value:
          - CertificateArn: '{{ CertificateArn }}'
      - name: Protocol
        value: '{{ Protocol }}'
      - name: AlpnPolicy
        value:
          - '{{ AlpnPolicy[0] }}'
      - name: MutualAuthentication
        value:
          Mode: '{{ Mode }}'
          TrustStoreArn: '{{ TrustStoreArn }}'
          IgnoreClientCertificateExpiry: '{{ IgnoreClientCertificateExpiry }}'

```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
/*+ delete */
DELETE FROM aws.elasticloadbalancingv2.listeners
WHERE data__Identifier = '<ListenerArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>listeners</code> resource, the following permissions are required:

### Create
```json
elasticloadbalancing:CreateListener,
elasticloadbalancing:DescribeListeners,
cognito-idp:DescribeUserPoolClient
```

### Delete
```json
elasticloadbalancing:DeleteListener,
elasticloadbalancing:DescribeListeners
```

### List
```json
elasticloadbalancing:DescribeListeners
```

