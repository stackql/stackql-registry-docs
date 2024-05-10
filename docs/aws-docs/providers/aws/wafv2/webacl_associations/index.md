---
title: webacl_associations
hide_title: false
hide_table_of_contents: false
keywords:
  - webacl_associations
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


Used to retrieve a list of <code>webacl_associations</code> in a region or to create or delete a <code>webacl_associations</code> resource, use <code>webacl_association</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webacl_associations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates WebACL to Application Load Balancer, CloudFront or API Gateway.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.webacl_associations" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="web_acl_arn" /></td><td><code>undefined</code></td><td></td></tr>
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
resource_arn,
web_acl_arn
FROM aws.wafv2.webacl_associations
;
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
 "ResourceArn": "{{ ResourceArn }}",
 "WebACLArn": null
}
>>>
--required properties only
INSERT INTO aws.wafv2.webacl_associations (
 ResourceArn,
 WebACLArn,
 region
)
SELECT 
{{ .ResourceArn }},
 {{ .WebACLArn }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "ResourceArn": "{{ ResourceArn }}",
 "WebACLArn": null
}
>>>
--all properties
INSERT INTO aws.wafv2.webacl_associations (
 ResourceArn,
 WebACLArn,
 region
)
SELECT 
 {{ .ResourceArn }},
 {{ .WebACLArn }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.wafv2.webacl_associations
WHERE data__Identifier = '<ResourceArn|WebACLArn>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>webacl_associations</code> resource, the following permissions are required:

### Create
```json
wafv2:AssociateWebACL,
wafv2:GetWebACLForResource,
wafv2:GetWebACL,
wafv2:DisassociateWebACL,
elasticloadbalancing:SetWebACL,
apigateway:SetWebACL,
appsync:SetWebACL,
cognito-idp:AssociateWebACL,
cognito-idp:DisassociateWebACL,
cognito-idp:GetWebACLForResource,
apprunner:AssociateWebAcl,
apprunner:DisassociateWebAcl,
apprunner:DescribeWebAclForService,
ec2:AssociateVerifiedAccessInstanceWebAcl,
ec2:DisassociateVerifiedAccessInstanceWebAcl,
ec2:DescribeVerifiedAccessInstanceWebAclAssociations,
ec2:GetVerifiedAccessInstanceWebAcl
```

### Delete
```json
wafv2:AssociateWebACL,
wafv2:GetWebACLForResource,
wafv2:GetWebACL,
wafv2:DisassociateWebACL,
elasticloadbalancing:SetWebACL,
apigateway:SetWebACL,
appsync:SetWebACL,
cognito-idp:AssociateWebACL,
cognito-idp:DisassociateWebACL,
cognito-idp:GetWebACLForResource,
apprunner:AssociateWebAcl,
apprunner:DisassociateWebAcl,
apprunner:DescribeWebAclForService,
ec2:AssociateVerifiedAccessInstanceWebAcl,
ec2:DisassociateVerifiedAccessInstanceWebAcl,
ec2:DescribeVerifiedAccessInstanceWebAclAssociations,
ec2:GetVerifiedAccessInstanceWebAcl
```

