---
title: permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - permissions
  - lambda
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

Creates, updates, deletes or gets a <code>permission</code> resource or lists <code>permissions</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>The <code>AWS::Lambda::Permission</code> resource grants an AWS service or another account permission to use a function. You can apply the policy at the function level, or specify a qualifier to restrict access to a single version or alias. If you use a qualifier, the invoker must use the full Amazon Resource Name (ARN) of that version or alias to invoke the function.<br />To grant permission to another account, specify the account ID as the <code>Principal</code>. To grant permission to an organization defined in AOlong, specify the organization ID as the <code>PrincipalOrgID</code>. For AWS services, the principal is a domain-style identifier defined by the service, like <code>s3.amazonaws.com</code> or <code>sns.amazonaws.com</code>. For AWS services, you can also specify the ARN of the associated resource as the <code>SourceArn</code>. If you grant permission to a service principal without specifying the source, other accounts could potentially configure resources in their account to invoke your Lambda function.<br />If your function has a function URL, you can specify the <code>FunctionUrlAuthType</code> parameter. This adds a condition to your permission that only applies when your function URL's <code>AuthType</code> matches the specified <code>FunctionUrlAuthType</code>. For more information about the <code>AuthType</code> parameter, see &#91;Security and auth model for function URLs&#93;(https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html).<br />This resource adds a statement to a resource-based permission policy for the function. For more information about function policies, see &#91;Lambda Function Policies&#93;(https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html).</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.lambda.permissions" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="function_name" /></td><td><code>string</code></td><td>The name or ARN of the Lambda function, version, or alias.<br />**Name formats**<br />+ *Function name* – <code>my-function</code> (name-only), <code>my-function:v1</code> (with alias).<br />+ *Function ARN* – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.<br />+ *Partial ARN* – <code>123456789012:function:my-function</code>.<br /><br />You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</td></tr>
<tr><td><CopyableCode code="action" /></td><td><code>string</code></td><td>The action that the principal can use on the function. For example, <code>lambda:InvokeFunction</code> or <code>lambda:GetFunction</code>.</td></tr>
<tr><td><CopyableCode code="event_source_token" /></td><td><code>string</code></td><td>For Alexa Smart Home functions, a token that the invoker must supply.</td></tr>
<tr><td><CopyableCode code="function_url_auth_type" /></td><td><code>string</code></td><td>The type of authentication that your function URL uses. Set to <code>AWS_IAM</code> if you want to restrict access to authenticated users only. Set to <code>NONE</code> if you want to bypass IAM authentication to create a public endpoint. For more information, see &#91;Security and auth model for Lambda function URLs&#93;(https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html).</td></tr>
<tr><td><CopyableCode code="source_arn" /></td><td><code>string</code></td><td>For AWS-services, the ARN of the AWS resource that invokes the function. For example, an Amazon S3 bucket or Amazon SNS topic.<br />Note that Lambda configures the comparison using the <code>StringLike</code> operator.</td></tr>
<tr><td><CopyableCode code="source_account" /></td><td><code>string</code></td><td>For AWS-service, the ID of the AWS-account that owns the resource. Use this together with <code>SourceArn</code> to ensure that the specified account owns the resource. It is possible for an Amazon S3 bucket to be deleted by its owner and recreated by another account.</td></tr>
<tr><td><CopyableCode code="principal_org_id" /></td><td><code>string</code></td><td>The identifier for your organization in AOlong. Use this to grant permissions to all the AWS-accounts under this organization.</td></tr>
<tr><td><CopyableCode code="id" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="principal" /></td><td><code>string</code></td><td>The AWS-service, AWS-account, IAM user, or IAM role that invokes the function. If you specify a service, use <code>SourceArn</code> or <code>SourceAccount</code> to limit who can invoke the function through that service.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html"><code>AWS::Lambda::Permission</code></a>.

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
    <td><CopyableCode code="FunctionName, Action, Principal, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
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
Gets all <code>permissions</code> in a region.
```sql
SELECT
region,
function_name,
action,
event_source_token,
function_url_auth_type,
source_arn,
source_account,
principal_org_id,
id,
principal
FROM aws.lambda.permissions
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>permission</code>.
```sql
SELECT
region,
function_name,
action,
event_source_token,
function_url_auth_type,
source_arn,
source_account,
principal_org_id,
id,
principal
FROM aws.lambda.permissions
WHERE region = 'us-east-1' AND data__Identifier = '<FunctionName>|<Id>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>permission</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.lambda.permissions (
 FunctionName,
 Action,
 Principal,
 region
)
SELECT 
'{{ FunctionName }}',
 '{{ Action }}',
 '{{ Principal }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.lambda.permissions (
 FunctionName,
 Action,
 EventSourceToken,
 FunctionUrlAuthType,
 SourceArn,
 SourceAccount,
 PrincipalOrgID,
 Principal,
 region
)
SELECT 
 '{{ FunctionName }}',
 '{{ Action }}',
 '{{ EventSourceToken }}',
 '{{ FunctionUrlAuthType }}',
 '{{ SourceArn }}',
 '{{ SourceAccount }}',
 '{{ PrincipalOrgID }}',
 '{{ Principal }}',
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
  - name: permission
    props:
      - name: FunctionName
        value: '{{ FunctionName }}'
      - name: Action
        value: '{{ Action }}'
      - name: EventSourceToken
        value: '{{ EventSourceToken }}'
      - name: FunctionUrlAuthType
        value: '{{ FunctionUrlAuthType }}'
      - name: SourceArn
        value: '{{ SourceArn }}'
      - name: SourceAccount
        value: '{{ SourceAccount }}'
      - name: PrincipalOrgID
        value: '{{ PrincipalOrgID }}'
      - name: Principal
        value: '{{ Principal }}'

```
</TabItem>
</Tabs>

## `DELETE` example

```sql
/*+ delete */
DELETE FROM aws.lambda.permissions
WHERE data__Identifier = '<FunctionName|Id>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>permissions</code> resource, the following permissions are required:

### Read
```json
lambda:GetPolicy
```

### Create
```json
lambda:AddPermission
```

### List
```json
lambda:GetPolicy
```

### Delete
```json
lambda:RemovePermission
```
