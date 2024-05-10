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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';


Gets or updates an individual <code>landing_zone</code> resource, use <code>landing_zones</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>landing_zone</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ControlTower::LandingZone Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.controltower.landing_zone" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="landing_zone_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="arn" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="latest_available_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="drift_status" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="manifest" /></td><td><code>undefined</code></td><td></td></tr>
<tr><td><CopyableCode code="version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="tags" /></td><td><code>array</code></td><td></td></tr>
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
    <td><CopyableCode code="get_resource" /></td>
    <td><code>SELECT</code></td>
    <td><CopyableCode code="data__Identifier, region" /></td>
  </tr>
</tbody></table>

## `SELECT` Example
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
FROM aws.controltower.landing_zone
WHERE region = 'us-east-1' AND data__Identifier = '<LandingZoneIdentifier>';
```


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

