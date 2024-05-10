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


Used to retrieve a list of <code>listener_rules</code> in a region or to create or delete a <code>listener_rules</code> resource, use <code>listener_rule</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>listener_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Specifies a listener rule. The listener must be associated with an Application Load Balancer. Each rule consists of a priority, one or more actions, and one or more conditions.&lt;br&#x2F;&gt; For more information, see &#91;Quotas for your Application Load Balancers&#93;(https:&#x2F;&#x2F;docs.aws.amazon.com&#x2F;elasticloadbalancing&#x2F;latest&#x2F;application&#x2F;load-balancer-limits.html) in the *User Guide for Application Load Balancers*.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.elasticloadbalancingv2.listener_rules" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="rule_arn" /></td><td><code>string</code></td><td></td></tr>
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
rule_arn
FROM aws.elasticloadbalancingv2.listener_rules
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
 "Actions": [
  {
   "Order": "{{ Order }}",
   "TargetGroupArn": "{{ TargetGroupArn }}",
   "FixedResponseConfig": {
    "ContentType": "{{ ContentType }}",
    "StatusCode": "{{ StatusCode }}",
    "MessageBody": "{{ MessageBody }}"
   },
   "AuthenticateCognitoConfig": {
    "OnUnauthenticatedRequest": "{{ OnUnauthenticatedRequest }}",
    "UserPoolClientId": "{{ UserPoolClientId }}",
    "UserPoolDomain": "{{ UserPoolDomain }}",
    "SessionTimeout": "{{ SessionTimeout }}",
    "Scope": "{{ Scope }}",
    "SessionCookieName": "{{ SessionCookieName }}",
    "UserPoolArn": "{{ UserPoolArn }}",
    "AuthenticationRequestExtraParams": {}
   },
   "Type": "{{ Type }}",
   "RedirectConfig": {
    "Path": "{{ Path }}",
    "Query": "{{ Query }}",
    "Port": "{{ Port }}",
    "Host": "{{ Host }}",
    "Protocol": "{{ Protocol }}",
    "StatusCode": "{{ StatusCode }}"
   },
   "ForwardConfig": {
    "TargetGroupStickinessConfig": {
     "Enabled": "{{ Enabled }}",
     "DurationSeconds": "{{ DurationSeconds }}"
    },
    "TargetGroups": [
     {
      "TargetGroupArn": "{{ TargetGroupArn }}",
      "Weight": "{{ Weight }}"
     }
    ]
   },
   "AuthenticateOidcConfig": {
    "OnUnauthenticatedRequest": "{{ OnUnauthenticatedRequest }}",
    "TokenEndpoint": "{{ TokenEndpoint }}",
    "SessionTimeout": "{{ SessionTimeout }}",
    "Scope": "{{ Scope }}",
    "Issuer": "{{ Issuer }}",
    "ClientSecret": "{{ ClientSecret }}",
    "UserInfoEndpoint": "{{ UserInfoEndpoint }}",
    "ClientId": "{{ ClientId }}",
    "AuthorizationEndpoint": "{{ AuthorizationEndpoint }}",
    "SessionCookieName": "{{ SessionCookieName }}",
    "UseExistingClientSecret": "{{ UseExistingClientSecret }}",
    "AuthenticationRequestExtraParams": {}
   }
  }
 ],
 "Priority": "{{ Priority }}",
 "Conditions": [
  {
   "Field": "{{ Field }}",
   "Values": [
    "{{ Values[0] }}"
   ],
   "HttpRequestMethodConfig": {
    "Values": [
     "{{ Values[0] }}"
    ]
   },
   "PathPatternConfig": {
    "Values": [
     "{{ Values[0] }}"
    ]
   },
   "HttpHeaderConfig": {
    "Values": [
     "{{ Values[0] }}"
    ],
    "HttpHeaderName": "{{ HttpHeaderName }}"
   },
   "SourceIpConfig": {
    "Values": [
     "{{ Values[0] }}"
    ]
   },
   "HostHeaderConfig": {
    "Values": [
     "{{ Values[0] }}"
    ]
   },
   "QueryStringConfig": {
    "Values": [
     {
      "Value": "{{ Value }}",
      "Key": "{{ Key }}"
     }
    ]
   }
  }
 ]
}
>>>
--required properties only
INSERT INTO aws.elasticloadbalancingv2.listener_rules (
 Actions,
 Priority,
 Conditions,
 region
)
SELECT 
{{ Actions }},
 {{ Priority }},
 {{ Conditions }},
'us-east-1';
```

</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ListenerArn": "{{ ListenerArn }}",
 "Actions": [
  {
   "Order": "{{ Order }}",
   "TargetGroupArn": "{{ TargetGroupArn }}",
   "FixedResponseConfig": {
    "ContentType": "{{ ContentType }}",
    "StatusCode": "{{ StatusCode }}",
    "MessageBody": "{{ MessageBody }}"
   },
   "AuthenticateCognitoConfig": {
    "OnUnauthenticatedRequest": "{{ OnUnauthenticatedRequest }}",
    "UserPoolClientId": "{{ UserPoolClientId }}",
    "UserPoolDomain": "{{ UserPoolDomain }}",
    "SessionTimeout": "{{ SessionTimeout }}",
    "Scope": "{{ Scope }}",
    "SessionCookieName": "{{ SessionCookieName }}",
    "UserPoolArn": "{{ UserPoolArn }}",
    "AuthenticationRequestExtraParams": {}
   },
   "Type": "{{ Type }}",
   "RedirectConfig": {
    "Path": "{{ Path }}",
    "Query": "{{ Query }}",
    "Port": "{{ Port }}",
    "Host": "{{ Host }}",
    "Protocol": "{{ Protocol }}",
    "StatusCode": "{{ StatusCode }}"
   },
   "ForwardConfig": {
    "TargetGroupStickinessConfig": {
     "Enabled": "{{ Enabled }}",
     "DurationSeconds": "{{ DurationSeconds }}"
    },
    "TargetGroups": [
     {
      "TargetGroupArn": "{{ TargetGroupArn }}",
      "Weight": "{{ Weight }}"
     }
    ]
   },
   "AuthenticateOidcConfig": {
    "OnUnauthenticatedRequest": "{{ OnUnauthenticatedRequest }}",
    "TokenEndpoint": "{{ TokenEndpoint }}",
    "SessionTimeout": "{{ SessionTimeout }}",
    "Scope": "{{ Scope }}",
    "Issuer": "{{ Issuer }}",
    "ClientSecret": "{{ ClientSecret }}",
    "UserInfoEndpoint": "{{ UserInfoEndpoint }}",
    "ClientId": "{{ ClientId }}",
    "AuthorizationEndpoint": "{{ AuthorizationEndpoint }}",
    "SessionCookieName": "{{ SessionCookieName }}",
    "UseExistingClientSecret": "{{ UseExistingClientSecret }}",
    "AuthenticationRequestExtraParams": {}
   }
  }
 ],
 "Priority": "{{ Priority }}",
 "Conditions": [
  {
   "Field": "{{ Field }}",
   "Values": [
    "{{ Values[0] }}"
   ],
   "HttpRequestMethodConfig": {
    "Values": [
     "{{ Values[0] }}"
    ]
   },
   "PathPatternConfig": {
    "Values": [
     "{{ Values[0] }}"
    ]
   },
   "HttpHeaderConfig": {
    "Values": [
     "{{ Values[0] }}"
    ],
    "HttpHeaderName": "{{ HttpHeaderName }}"
   },
   "SourceIpConfig": {
    "Values": [
     "{{ Values[0] }}"
    ]
   },
   "HostHeaderConfig": {
    "Values": [
     "{{ Values[0] }}"
    ]
   },
   "QueryStringConfig": {
    "Values": [
     {
      "Value": "{{ Value }}",
      "Key": "{{ Key }}"
     }
    ]
   }
  }
 ]
}
>>>
--all properties
INSERT INTO aws.elasticloadbalancingv2.listener_rules (
 ListenerArn,
 Actions,
 Priority,
 Conditions,
 region
)
SELECT 
 {{ ListenerArn }},
 {{ Actions }},
 {{ Priority }},
 {{ Conditions }},
 'us-east-1';
```

</TabItem>
</Tabs>

## `DELETE` Example

```sql
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

