---
title: web_acls
hide_title: false
hide_table_of_contents: false
keywords:
  - web_acls
  - wafv2
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

Creates, updates, deletes or gets a <code>web_acl</code> resource or lists <code>web_acls</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>web_acls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Contains the Rules that identify the requests that you want to allow, block, or count. In a WebACL, you also specify a default action (ALLOW or BLOCK), and the action for each Rule that you add to a WebACL, for example, block requests from specified IP addresses or block requests from specified referrers. You also associate the WebACL with a CloudFront distribution to identify the requests that you want AWS WAF to filter. If you add more than one Rule to a WebACL, a request needs to match only one of the specifications to be allowed, blocked, or counted.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.web_acls" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="capacity" /></td><td><code>integer</code></td><td></td></tr>
<tr><td><CopyableCode code="default_action" /></td><td><code>object</code></td><td>Default Action WebACL will take against ingress traffic when there is no matching Rule.</td></tr>
<tr><td><CopyableCode code="description" /></td><td><code>string</code></td><td>Description of the entity.</td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Name of the WebACL.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td>Id of the WebACL</td></tr>
<tr><td><CopyableCode code="scope" /></td><td><code>string</code></td><td>Use CLOUDFRONT for CloudFront WebACL, use REGIONAL for Application Load Balancer and API Gateway.</td></tr>
<tr><td><CopyableCode code="rules" /></td><td><code>array</code></td><td>Collection of Rules.</td></tr>
<tr><td><CopyableCode code="visibility_config" /></td><td><code>object</code></td><td>Visibility Metric of the WebACL.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
<tr><td><CopyableCode code="label_namespace" /></td><td><code>string</code></td><td>Name of the Label.</td></tr>
<tr><td><CopyableCode code="custom_response_bodies" /></td><td><code>object</code></td><td>Custom response key and body map.</td></tr>
<tr><td><CopyableCode code="captcha_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="challenge_config" /></td><td><code>object</code></td><td></td></tr>
<tr><td><CopyableCode code="token_domains" /></td><td><code>array</code></td><td>List of domains to accept in web request tokens, in addition to the domain of the protected resource.</td></tr>
<tr><td><CopyableCode code="association_config" /></td><td><code>object</code></td><td>AssociationConfig for body inspection</td></tr>
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
    <td><CopyableCode code="DefaultAction, Scope, VisibilityConfig, region" /></td>
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
Gets all <code>web_acls</code> in a region.
```sql
SELECT
region,
arn,
capacity,
default_action,
description,
name,
id,
scope,
rules,
visibility_config,
tags,
label_namespace,
custom_response_bodies,
captcha_config,
challenge_config,
token_domains,
association_config
FROM aws.wafv2.web_acls
;
```
Gets all properties from an individual <code>web_acl</code>.
```sql
SELECT
region,
arn,
capacity,
default_action,
description,
name,
id,
scope,
rules,
visibility_config,
tags,
label_namespace,
custom_response_bodies,
captcha_config,
challenge_config,
token_domains,
association_config
FROM aws.wafv2.web_acls
WHERE data__Identifier = '<Name>|<Id>|<Scope>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>web_acl</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.wafv2.web_acls (
 DefaultAction,
 Scope,
 VisibilityConfig,
 region
)
SELECT 
'{{ DefaultAction }}',
 '{{ Scope }}',
 '{{ VisibilityConfig }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.wafv2.web_acls (
 DefaultAction,
 Description,
 Name,
 Scope,
 Rules,
 VisibilityConfig,
 Tags,
 CustomResponseBodies,
 CaptchaConfig,
 ChallengeConfig,
 TokenDomains,
 AssociationConfig,
 region
)
SELECT 
 '{{ DefaultAction }}',
 '{{ Description }}',
 '{{ Name }}',
 '{{ Scope }}',
 '{{ Rules }}',
 '{{ VisibilityConfig }}',
 '{{ Tags }}',
 '{{ CustomResponseBodies }}',
 '{{ CaptchaConfig }}',
 '{{ ChallengeConfig }}',
 '{{ TokenDomains }}',
 '{{ AssociationConfig }}',
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
  - name: web_acl
    props:
      - name: DefaultAction
        value:
          Allow:
            CustomRequestHandling:
              InsertHeaders:
                - Name: '{{ Name }}'
                  Value: '{{ Value }}'
          Block:
            CustomResponse:
              ResponseCode: '{{ ResponseCode }}'
              CustomResponseBodyKey: '{{ CustomResponseBodyKey }}'
              ResponseHeaders:
                - null
      - name: Description
        value: '{{ Description }}'
      - name: Name
        value: '{{ Name }}'
      - name: Scope
        value: '{{ Scope }}'
      - name: Rules
        value:
          - Name: null
            Priority: '{{ Priority }}'
            Statement:
              ByteMatchStatement:
                SearchString: '{{ SearchString }}'
                SearchStringBase64: '{{ SearchStringBase64 }}'
                FieldToMatch:
                  SingleHeader:
                    Name: '{{ Name }}'
                  SingleQueryArgument:
                    Name: '{{ Name }}'
                  AllQueryArguments: {}
                  UriPath: {}
                  QueryString: {}
                  Body:
                    OversizeHandling: '{{ OversizeHandling }}'
                  Method: {}
                  JsonBody:
                    MatchPattern:
                      All: {}
                      IncludedPaths:
                        - '{{ IncludedPaths[0] }}'
                    MatchScope: '{{ MatchScope }}'
                    InvalidFallbackBehavior: '{{ InvalidFallbackBehavior }}'
                    OversizeHandling: null
                  Headers:
                    MatchPattern:
                      All: {}
                      IncludedHeaders:
                        - '{{ IncludedHeaders[0] }}'
                      ExcludedHeaders:
                        - '{{ ExcludedHeaders[0] }}'
                    MatchScope: '{{ MatchScope }}'
                    OversizeHandling: null
                  Cookies:
                    MatchPattern:
                      All: {}
                      IncludedCookies:
                        - '{{ IncludedCookies[0] }}'
                      ExcludedCookies:
                        - '{{ ExcludedCookies[0] }}'
                    MatchScope: null
                    OversizeHandling: null
                  JA3Fingerprint:
                    FallbackBehavior: '{{ FallbackBehavior }}'
                TextTransformations:
                  - Priority: '{{ Priority }}'
                    Type: '{{ Type }}'
                PositionalConstraint: '{{ PositionalConstraint }}'
              SqliMatchStatement:
                FieldToMatch: null
                TextTransformations:
                  - null
                SensitivityLevel: '{{ SensitivityLevel }}'
              XssMatchStatement:
                FieldToMatch: null
                TextTransformations:
                  - null
              SizeConstraintStatement:
                FieldToMatch: null
                ComparisonOperator: '{{ ComparisonOperator }}'
                Size: null
                TextTransformations:
                  - null
              GeoMatchStatement:
                CountryCodes:
                  - '{{ CountryCodes[0] }}'
                ForwardedIPConfig:
                  HeaderName: '{{ HeaderName }}'
                  FallbackBehavior: '{{ FallbackBehavior }}'
              RuleGroupReferenceStatement:
                Arn: '{{ Arn }}'
                ExcludedRules:
                  - Name: null
                RuleActionOverrides:
                  - Name: null
                    ActionToUse:
                      Allow: null
                      Block: null
                      Count:
                        CustomRequestHandling: null
                      Captcha:
                        CustomRequestHandling: null
                      Challenge:
                        CustomRequestHandling: null
              IPSetReferenceStatement:
                Arn: null
                IPSetForwardedIPConfig:
                  HeaderName: '{{ HeaderName }}'
                  FallbackBehavior: '{{ FallbackBehavior }}'
                  Position: '{{ Position }}'
              RegexPatternSetReferenceStatement:
                Arn: null
                FieldToMatch: null
                TextTransformations:
                  - null
              ManagedRuleGroupStatement:
                Name: null
                VendorName: '{{ VendorName }}'
                Version: '{{ Version }}'
                ExcludedRules:
                  - null
                ScopeDownStatement: null
                ManagedRuleGroupConfigs:
                  - LoginPath: '{{ LoginPath }}'
                    PayloadType: '{{ PayloadType }}'
                    UsernameField:
                      Identifier: '{{ Identifier }}'
                    PasswordField: null
                    AWSManagedRulesBotControlRuleSet:
                      InspectionLevel: '{{ InspectionLevel }}'
                      EnableMachineLearning: '{{ EnableMachineLearning }}'
                    AWSManagedRulesATPRuleSet:
                      LoginPath: '{{ LoginPath }}'
                      EnableRegexInPath: '{{ EnableRegexInPath }}'
                      RequestInspection:
                        PayloadType: '{{ PayloadType }}'
                        UsernameField: null
                        PasswordField: null
                      ResponseInspection:
                        StatusCode:
                          SuccessCodes:
                            - '{{ SuccessCodes[0] }}'
                          FailureCodes:
                            - '{{ FailureCodes[0] }}'
                        Header:
                          Name: '{{ Name }}'
                          SuccessValues:
                            - '{{ SuccessValues[0] }}'
                          FailureValues:
                            - '{{ FailureValues[0] }}'
                        BodyContains:
                          SuccessStrings:
                            - '{{ SuccessStrings[0] }}'
                          FailureStrings:
                            - '{{ FailureStrings[0] }}'
                        Json:
                          Identifier: '{{ Identifier }}'
                          SuccessValues:
                            - '{{ SuccessValues[0] }}'
                          FailureValues:
                            - '{{ FailureValues[0] }}'
                    AWSManagedRulesACFPRuleSet:
                      CreationPath: '{{ CreationPath }}'
                      RegistrationPagePath: '{{ RegistrationPagePath }}'
                      RequestInspection:
                        PayloadType: '{{ PayloadType }}'
                        UsernameField: null
                        PasswordField: null
                        EmailField: null
                        PhoneNumberFields:
                          - null
                        AddressFields:
                          - null
                      ResponseInspection: null
                      EnableRegexInPath: '{{ EnableRegexInPath }}'
                RuleActionOverrides:
                  - null
              RateBasedStatement:
                Limit: '{{ Limit }}'
                EvaluationWindowSec: '{{ EvaluationWindowSec }}'
                AggregateKeyType: '{{ AggregateKeyType }}'
                CustomKeys:
                  - Cookie:
                      Name: '{{ Name }}'
                      TextTransformations:
                        - null
                    ForwardedIP: {}
                    Header:
                      Name: '{{ Name }}'
                      TextTransformations:
                        - null
                    HTTPMethod: {}
                    IP: {}
                    LabelNamespace:
                      Namespace: '{{ Namespace }}'
                    QueryArgument:
                      Name: '{{ Name }}'
                      TextTransformations:
                        - null
                    QueryString:
                      TextTransformations:
                        - null
                    UriPath:
                      TextTransformations:
                        - null
                ScopeDownStatement: null
                ForwardedIPConfig: null
              AndStatement:
                Statements:
                  - null
              OrStatement:
                Statements:
                  - null
              NotStatement:
                Statement: null
              LabelMatchStatement:
                Scope: '{{ Scope }}'
                Key: '{{ Key }}'
              RegexMatchStatement:
                RegexString: '{{ RegexString }}'
                FieldToMatch: null
                TextTransformations:
                  - null
            Action: null
            OverrideAction:
              Count: {}
              None: {}
            RuleLabels:
              - Name: '{{ Name }}'
            VisibilityConfig:
              SampledRequestsEnabled: '{{ SampledRequestsEnabled }}'
              CloudWatchMetricsEnabled: '{{ CloudWatchMetricsEnabled }}'
              MetricName: '{{ MetricName }}'
            CaptchaConfig:
              ImmunityTimeProperty:
                ImmunityTime: '{{ ImmunityTime }}'
            ChallengeConfig:
              ImmunityTimeProperty: null
      - name: VisibilityConfig
        value: null
      - name: Tags
        value:
          - Key: '{{ Key }}'
            Value: '{{ Value }}'
      - name: CustomResponseBodies
        value: {}
      - name: CaptchaConfig
        value: null
      - name: ChallengeConfig
        value: null
      - name: TokenDomains
        value:
          - '{{ TokenDomains[0] }}'
      - name: AssociationConfig
        value:
          RequestBody: {}

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.wafv2.web_acls
WHERE data__Identifier = '<Name|Id|Scope>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>web_acls</code> resource, the following permissions are required:

### Create
```json
wafv2:CreateWebACL,
wafv2:GetWebACL,
wafv2:ListTagsForResource
```

### Delete
```json
wafv2:DeleteWebACL,
wafv2:GetWebACL
```

### Read
```json
wafv2:GetWebACL,
wafv2:ListTagsForResource
```

### Update
```json
wafv2:UpdateWebACL,
wafv2:GetWebACL,
wafv2:ListTagsForResource
```

### List
```json
wafv2:listWebACLs
```

