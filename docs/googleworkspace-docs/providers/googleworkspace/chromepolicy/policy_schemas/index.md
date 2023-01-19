---
title: policy_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - policy_schemas
  - chromepolicy
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policy_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.chromepolicy.policy_schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Format: name=customers/&#123;customer&#125;/policySchemas/&#123;schema_namespace&#125; |
| `accessRestrictions` | `array` | Output only. Specific access restrictions related to this policy. |
| `additionalTargetKeyNames` | `array` | Output only. Additional key names that will be used to identify the target of the policy value. When specifying a `policyTargetKey`, each of the additional keys specified here will have to be included in the `additionalTargetKeys` map. |
| `policyApiLifeycle` | `object` |  |
| `definition` | `object` | Describes a complete .proto file. |
| `fieldDescriptions` | `array` | Output only. Detailed description of each field that is part of the schema. |
| `schemaName` | `string` | Output only. The fully qualified name of the policy schema. This value is used to fill the field `policy_schema` in PolicyValue when calling BatchInheritOrgUnitPolicies BatchModifyOrgUnitPolicies BatchModifyGroupPolicies or BatchDeleteGroupPolicies. |
| `notices` | `array` | Output only. Special notice messages related to setting certain values in certain fields in the schema. |
| `policyDescription` | `string` | Output only. Description about the policy schema for user consumption. |
| `validTargetResources` | `array` | Output only. Information about applicable target resources for the policy. |
| `supportUri` | `string` | Output only. URI to related support article for this schema. |
| `categoryTitle` | `string` | Title of the category in which a setting belongs. |
| `policyApiLifecycle` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `customers_policySchemas_get` | `SELECT` | `customersId, policySchemasId` | Get a specific policy schema for a customer by its resource name. |
| `customers_policySchemas_list` | `SELECT` | `customersId` | Gets a list of policy schemas that match a specified filter value for a given customer. |
