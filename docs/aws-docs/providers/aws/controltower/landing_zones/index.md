---
title: landing_zones
hide_title: false
hide_table_of_contents: false
keywords:
  - landing_zones
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';

Used to retrieve a list of <code>landing_zones</code> in a region or create a <code>landing_zones</code> resource, use <code>landing_zone</code> to operate on an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>landing_zones</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ControlTower::LandingZone Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.controltower.landing_zones" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="landing_zone_identifier" /></td><td><code>string</code></td><td></td></tr>
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
    <td><CopyableCode code="list_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
```sql
SELECT
region,
landing_zone_identifier
FROM aws.controltower.landing_zones
WHERE region = 'us-east-1'
```

## Permissions

To operate on the <code>landing_zones</code> resource, the following permissions are required:

### Create
```json
controltower:CreateLandingZone,
controltower:GetLandingZoneOperation,
controltower:ListTagsForResource,
controltower:TagResource,
controltower:GetLandingZone,
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

### List
```json
controltower:ListLandingZones
```

