---
title: enabled_baseline
hide_title: false
hide_table_of_contents: false
keywords:
  - enabled_baseline
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


Gets or updates an individual <code>enabled_baseline</code> resource, use <code>enabled_baselines</code> to retrieve a list of resources or to create or delete a resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enabled_baseline</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ControlTower::EnabledBaseline Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.controltower.enabled_baseline" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="baseline_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="baseline_version" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="enabled_baseline_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="target_identifier" /></td><td><code>string</code></td><td></td></tr>
<tr><td><CopyableCode code="parameters" /></td><td><code>array</code></td><td></td></tr>
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
baseline_identifier,
baseline_version,
enabled_baseline_identifier,
target_identifier,
parameters,
tags
FROM aws.controltower.enabled_baseline
WHERE region = 'us-east-1' AND data__Identifier = '<EnabledBaselineIdentifier>';
```


## Permissions

To operate on the <code>enabled_baseline</code> resource, the following permissions are required:

### Read
```json
controltower:GetEnabledBaseline,
controltower:ListEnabledBaselines,
controltower:ListTagsForResource
```

### Update
```json
controltower:UpdateEnabledBaseline,
controltower:GetBaselineOperation,
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
servicecatalog:DeleteProvisioningArtifact,
controltower:TagResource,
controltower:ListTagsForResource,
controltower:GetEnabledBaseline
```

