---
title: webacl_association
hide_title: false
hide_table_of_contents: false
keywords:
  - webacl_association
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

Gets or operates on an individual <code>webacl_association</code> resource, use <code>webacl_associations</code> to retrieve a list of resources or to create a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>webacl_association</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Associates WebACL to Application Load Balancer, CloudFront or API Gateway.</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.wafv2.webacl_association" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="resource_arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="web_acl_arn" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="update_resource" /></td>
    <td><code>UPDATE</code></td>
    <td><CopyableCode code="data__Identifier, data__PatchDocument, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="delete_resource" /></td>
    <td><code>DELETE</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
  <tr>
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
resource_arn,
web_acl_arn
FROM aws.wafv2.webacl_association
WHERE data__Identifier = '<ResourceArn>|<WebACLArn>';
```

## Permissions

To operate on the <code>webacl_association</code> resource, the following permissions are required:

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

### Read
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

### Update
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

