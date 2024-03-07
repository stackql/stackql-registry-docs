---
title: landing_zone
hide_title: false
hide_table_of_contents: false
keywords:
  - landing_zone
  - controltower
  - aws
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage AWS resources using SQL
custom_edit_url: null
image: /img/providers/aws/stackql-aws-provider-featured-image.png
---
Gets an individual <code>landing_zone</code> resource

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>landing_zone</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>landing_zone</td></tr>
<tr><td><b>Id</b></td><td><code>awscc.controltower.landing_zone</code></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><code>landing_zone_identifier</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>arn</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>latest_available_version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>drift_status</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>manifest</code></td><td><code>undefined</code></td><td></td></tr>
<tr><td><code>version</code></td><td><code>string</code></td><td></td></tr>
<tr><td><code>tags</code></td><td><code>array</code></td><td></td></tr>
<tr><td><code>region</code></td><td><code>string</code></td><td>AWS region.</td></tr>

</tbody></table>

## Methods
Currently only <code>SELECT</code> is supported for this resource resource.

## Permissions

To operate on the <code>landing_zone</code> resource, the following permissions are required:

### Read
```json
controltower:GetLandingZone,
controltower:ListTagsForResource
```

### Update
```json
controltower:UpdateLandingZone,
controltower:GetLandingZoneOperation,
controltower:ListTagsForResource,
controltower:TagResource,
controltower:GetLandingZone,
controltower:UntagResource,
cloudformation:DescribeOrganizationsAccess,
servicecatalog:AssociatePrincipalWithPortfolio,
servicecatalog:AssociateProductWithPortfolio,
servicecatalog:CreatePortfolio,
servicecatalog:CreateProduct,
servicecatalog:CreateProvisioningArtifact,
servicecatalog:ListPortfolios,
servicecatalog:ListProvisioningArtifacts,
servicecatalog:SearchProductsAsAdmin,
servicecatalog:UpdatePortfolio,
servicecatalog:UpdateProvisioningArtifact,
servicecatalog:ListPrincipalsForPortfolio,
organizations:CreateOrganizationalUnit,
organizations:CreateOrganization,
organizations:UpdatePolicy,
organizations:CreatePolicy,
organizations:AttachPolicy,
organizations:DetachPolicy,
organizations:DeletePolicy,
organizations:EnablePolicyType,
organizations:EnableAWSServiceAccess,
organizations:ListRoots,
sso:GetPeregrineStatus,
sso:ListDirectoryAssociations,
sso:StartPeregrine,
sso:RegisterRegion
```

### Delete
```json
controltower:DeleteLandingZone,
controltower:GetLandingZone,
controltower:GetLandingZoneOperation,
cloudformation:DescribeOrganizationsAccess,
servicecatalog:ListPortfolios,
servicecatalog:ListProvisioningArtifacts,
servicecatalog:SearchProductsAsAdmin,
servicecatalog:DeleteProvisioningArtifact,
servicecatalog:ListPrincipalsForPortfolio,
servicecatalog:DeleteProduct,
servicecatalog:DisassociatePrincipalFromPortfolio,
servicecatalog:DisassociateProductFromPortfolio,
servicecatalog:DeletePortfolio,
organizations:AttachPolicy,
organizations:DetachPolicy,
organizations:DeletePolicy,
organizations:ListRoots,
sso:GetPeregrineStatus,
sso:ListDirectoryAssociations,
iam:DeleteRolePolicy,
iam:DetachRolePolicy,
iam:DeleteRole
```


## Example
```sql
SELECT
region,
landing_zone_identifier,
arn,
status,
latest_available_version,
drift_status,
manifest,
version,
tags
FROM awscc.controltower.landing_zone
WHERE region = 'us-east-1'
AND data__Identifier = '&lt;LandingZoneIdentifier&gt;'
```
