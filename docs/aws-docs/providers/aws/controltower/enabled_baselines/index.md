---
title: enabled_baselines
hide_title: false
hide_table_of_contents: false
keywords:
  - enabled_baselines
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


Used to retrieve a list of <code>enabled_baselines</code> in a region or to create or delete a <code>enabled_baselines</code> resource, use <code>enabled_baseline</code> to read or update an individual resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>enabled_baselines</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Description</b></td><td>Definition of AWS::ControlTower::EnabledBaseline Resource Type</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="aws.controltower.enabled_baselines" /></td></tr>
</tbody></table>

## Fields
<table><tbody>
<tr><th>Name</th><th>Datatype</th><th>Description</th></tr>
<tr><td><CopyableCode code="enabled_baseline_identifier" /></td><td><code>string</code></td><td></td></tr>
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
enabled_baseline_identifier
FROM aws.controltower.enabled_baselines
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
 "BaselineIdentifier": "{{ BaselineIdentifier }}",
 "BaselineVersion": "{{ BaselineVersion }}",
 "TargetIdentifier": "{{ TargetIdentifier }}"
}
>>>
--required properties only
INSERT INTO aws.controltower.enabled_baselines (
 BaselineIdentifier,
 BaselineVersion,
 TargetIdentifier,
 region
)
SELECT 
{{ .BaselineIdentifier }},
 {{ .BaselineVersion }},
 {{ .TargetIdentifier }},
'us-east-1';
```
</TabItem>
<TabItem value="all">

```sql
<<<json
{
 "BaselineIdentifier": "{{ BaselineIdentifier }}",
 "BaselineVersion": "{{ BaselineVersion }}",
 "TargetIdentifier": "{{ TargetIdentifier }}",
 "Parameters": [
  {
   "Key": "{{ Key }}",
   "Value": null
  }
 ],
 "Tags": [
  {
   "Key": "{{ Key }}",
   "Value": "{{ Value }}"
  }
 ]
}
>>>
--all properties
INSERT INTO aws.controltower.enabled_baselines (
 BaselineIdentifier,
 BaselineVersion,
 TargetIdentifier,
 Parameters,
 Tags,
 region
)
SELECT 
 {{ .BaselineIdentifier }},
 {{ .BaselineVersion }},
 {{ .TargetIdentifier }},
 {{ .Parameters }},
 {{ .Tags }},
 'us-east-1';
```
</TabItem>
</Tabs>

## `DELETE` Example

```sql
DELETE FROM aws.controltower.enabled_baselines
WHERE data__Identifier = '<EnabledBaselineIdentifier>'
AND region = 'us-east-1';
```

## Permissions

To operate on the <code>enabled_baselines</code> resource, the following permissions are required:

### Create
```json
controltower:EnableBaseline,
controltower:TagResource,
controltower:GetBaselineOperation,
controltower:GetEnabledBaseline,
controltower:ListTagsForResource,
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
servicecatalog:DeleteProvisioningArtifact
```

### Delete
```json
controltower:DisableBaseline,
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
servicecatalog:DeleteProvisioningArtifact
```

### List
```json
controltower:ListEnabledBaselines
```

