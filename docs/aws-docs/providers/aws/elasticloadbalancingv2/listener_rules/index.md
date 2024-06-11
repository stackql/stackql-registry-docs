---
title: listener_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - listener_rules
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

Creates, updates, deletes or gets a <code>listener_rule</code> resource or lists <code>listener_rules</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listener_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a listener rule. The listener must be associated with an Application Load Balancer. Each rule consists of a priority, one or more actions, and one or more conditions.<br/> For more information, see &#91;Quotas for your Application Load Balancers&#93;(https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html) in the *User Guide for Application Load Balancers*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticloadbalancingv2.listener_rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="listener_arn" /></td><td><code>string</code></td><td>The Amazon Resource Name (ARN) of the listener.</td></tr>
<tr><td><CopyableCode code="rule_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="actions" /></td><td><code>array</code></td><td>The actions.<br/> The rule must include exactly one of the following types of actions: <code>forward</code>, <code>fixed-response</code>, or <code>redirect</code>, and it must be the last action to be performed. If the rule is for an HTTPS listener, it can also optionally include an authentication action.</td></tr>
<tr><td><CopyableCode code="priority" /></td><td><code>integer</code></td><td>The rule priority. A listener can't have multiple rules with the same priority.<br/> If you try to reorder rules by updating their priorities, do not specify a new priority if an existing rule already uses this priority, as this can cause an error. If you need to reuse a priority with a different rule, you must remove it as a priority first, and then specify it in a subsequent update.</td></tr>
<tr><td><CopyableCode code="conditions" /></td><td><code>array</code></td><td>The conditions.<br/> The rule can optionally include up to one of each of the following conditions: <code>http-request-method</code>, <code>host-header</code>, <code>path-pattern</code>, and <code>source-ip</code>. A rule can also optionally include one or more of each of the following conditions: <code>http-header</code> and <code>query-string</code>.</td></tr>
<tr><td><CopyableCode code="is_default" /></td><td><code>boolean</code></td><td></td></tr>
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
    <td><CopyableCode code="Actions, Priority, Conditions, region" /></td>
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
List all <code>listener_rules</code> in a region.
```sql
SELECT
region,
rule_arn
FROM aws.elasticloadbalancingv2.listener_rules
WHERE region = 'us-east-1';
```
Gets all properties from a <code>listener_rule</code>.
```sql
SELECT
region,
listener_arn,
rule_arn,
actions,
priority,
conditions,
is_default
FROM aws.elasticloadbalancingv2.listener_rules
WHERE region = 'us-east-1' AND data__Identifier = '<RuleArn>';
```


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>listener_rule</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.elasticloadbalancingv2.listener_rules (
 Actions,
 Priority,
 Conditions,
 region
)
SELECT 
'{{ Actions }}',
 '{{ Priority }}',
 '{{ Conditions }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.elasticloadbalancingv2.listener_rules (
 ListenerArn,
 Actions,
 Priority,
 Conditions,
 region
)
SELECT 
 '{{ ListenerArn }}',
 '{{ Actions }}',
 '{{ Priority }}',
 '{{ Conditions }}',
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
  - name: listener_rule
    props:
      - name: ListenerArn
        value: '{{ ListenerArn }}'
      - name: Actions
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
      - name: Priority
        value: '{{ Priority }}'
      - name: Conditions
        value:
          - Field: '{{ Field }}'
            Values:
              - '{{ Values[0] }}'
            HttpRequestMethodConfig:
              Values:
                - '{{ Values[0] }}'
            PathPatternConfig:
              Values:
                - '{{ Values[0] }}'
            HttpHeaderConfig:
              Values:
                - '{{ Values[0] }}'
              HttpHeaderName: '{{ HttpHeaderName }}'
            SourceIpConfig:
              Values:
                - '{{ Values[0] }}'
            HostHeaderConfig:
              Values:
                - '{{ Values[0] }}'
            QueryStringConfig:
              Values:
                - Value: '{{ Value }}'
                  Key: '{{ Key }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.elasticloadbalancingv2.listener_rules
WHERE data__Identifier = '<RuleArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>listener_rules</code> resource, the following permissions are required:

### Create
```json
elasticloadbalancing:CreateRule,
elasticloadbalancing:DescribeRules,
cognito-idp:DescribeUserPoolClient
```

### Delete
```json
elasticloadbalancing:DeleteRule,
elasticloadbalancing:DescribeRules
```

### List
```json
elasticloadbalancing:DescribeRules
```

### Read
```json
elasticloadbalancing:DescribeRules
```

### Update
```json
elasticloadbalancing:ModifyRule,
elasticloadbalancing:SetRulePriorities,
elasticloadbalancing:DescribeRules
```

