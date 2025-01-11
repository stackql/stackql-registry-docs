---
title: resource_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - resource_shares
  - ram
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

Creates, updates, deletes or gets a <code>resource_share</code> resource or lists <code>resource_shares</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Resource type definition for AWS::RAM::ResourceShare</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.ram.resource_shares" /></td></tr>
</tbody></table>

## Fields
<table><tbody><tr><th>Name</th><th>Datatype</th><th>Description</th></tr><tr><td><CopyableCode code="allow_external_principals" /></td><td><code>boolean</code></td><td>Specifies whether principals outside your organization in AWS Organizations can be associated with a resource share. A value of `true` lets you share with individual AWS accounts that are not in your organization. A value of `false` only has meaning if your account is a member of an AWS Organization. The default value is `true`.</td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="name" /></td><td><code>string</code></td><td>Specifies the name of the resource share.</td></tr>
<tr><td><CopyableCode code="permission_arns" /></td><td><code>array</code></td><td>Specifies the &#91;Amazon Resource Names (ARNs)&#93;(https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the AWS RAM permission to associate with the resource share. If you do not specify an ARN for the permission, AWS RAM automatically attaches the default version of the permission for each resource type. You can associate only one permission with each resource type included in the resource share.</td></tr>
<tr><td><CopyableCode code="principals" /></td><td><code>array</code></td><td>Specifies the principals to associate with the resource share. The possible values are:<br />- An AWS account ID<br />- An Amazon Resource Name (ARN) of an organization in AWS Organizations<br />- An ARN of an organizational unit (OU) in AWS Organizations<br />- An ARN of an IAM role<br />- An ARN of an IAM user</td></tr>
<tr><td><CopyableCode code="resource_arns" /></td><td><code>array</code></td><td>Specifies a list of one or more ARNs of the resources to associate with the resource share.</td></tr>
<tr><td><CopyableCode code="sources" /></td><td><code>array</code></td><td>Specifies from which source accounts the service principal has access to the resources in this resource share.</td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td>Specifies one or more tags to attach to the resource share itself. It doesn't attach the tags to the resources associated with the resource share.</td></tr>
<tr><td><CopyableCode code="region" /></td><td><code>string</code></td><td>AWS region.</td></tr>
</tbody></table>

For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ram-resourceshare.html"><code>AWS::RAM::ResourceShare</code></a>.

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
    <td><CopyableCode code="Name, region" /></td>
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
Gets all <code>resource_shares</code> in a region.
```sql
SELECT
region,
allow_external_principals,
arn,
name,
permission_arns,
principals,
resource_arns,
sources,
tags
FROM aws.ram.resource_shares
WHERE region = 'us-east-1';
```
Gets all properties from an individual <code>resource_share</code>.
```sql
SELECT
region,
allow_external_principals,
arn,
name,
permission_arns,
principals,
resource_arns,
sources,
tags
FROM aws.ram.resource_shares
WHERE region = 'us-east-1' AND data__Identifier = '<Arn>';
```

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>resource_share</code> resource, using [__`stack-deploy`__](https://pypi.org/project/stack-deploy/).

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
INSERT INTO aws.ram.resource_shares (
 Name,
 region
)
SELECT 
'{{ Name }}',
'{{ region }}';
```
</TabItem>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO aws.ram.resource_shares (
 AllowExternalPrincipals,
 Name,
 PermissionArns,
 Principals,
 ResourceArns,
 Sources,
 Tags,
 region
)
SELECT 
 '{{ AllowExternalPrincipals }}',
 '{{ Name }}',
 '{{ PermissionArns }}',
 '{{ Principals }}',
 '{{ ResourceArns }}',
 '{{ Sources }}',
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
  - name: resource_share
    props:
      - name: AllowExternalPrincipals
        value: '{{ AllowExternalPrincipals }}'
      - name: Name
        value: '{{ Name }}'
      - name: PermissionArns
        value:
          - '{{ PermissionArns[0] }}'
      - name: Principals
        value:
          - '{{ Principals[0] }}'
      - name: ResourceArns
        value:
          - '{{ ResourceArns[0] }}'
      - name: Sources
        value:
          - '{{ Sources[0] }}'
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
DELETE FROM aws.ram.resource_shares
WHERE data__Identifier = '<Arn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>resource_shares</code> resource, the following permissions are required:

### Create
```json
ram:CreateResourceShare,
ram:TagResource
```

### Read
```json
ram:GetResourceShares
```

### Update
```json
ram:GetPermission,
ram:GetResourceShares,
ram:GetResourceShareAssociations,
ram:ListResourceSharePermissions,
ram:UpdateResourceShare,
ram:AssociateResourceSharePermission,
ram:AssociateResourceShare,
ram:DisassociateResourceShare,
ram:UntagResource,
ram:TagResource
```

### Delete
```json
ram:DeleteResourceShare,
ram:GetResourceShares
```

### List
```json
ram:GetResourceShares
```
