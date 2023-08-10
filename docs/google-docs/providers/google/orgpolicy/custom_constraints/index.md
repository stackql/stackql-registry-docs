---
title: custom_constraints
hide_title: false
hide_table_of_contents: false
keywords:
  - custom_constraints
  - orgpolicy
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>custom_constraints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.orgpolicy.custom_constraints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. Name of the constraint. This is unique within the organization. Format of the name should be * `organizations/&#123;organization_id&#125;/customConstraints/&#123;custom_constraint_id&#125;` Example: `organizations/123/customConstraints/custom.createOnlyE2TypeVms` The max length is 70 characters and the minimum length is 1. Note that the prefix `organizations/&#123;organization_id&#125;/customConstraints/` is not counted. |
| `description` | `string` | Detailed information about this custom policy constraint. The max length of the description is 2000 characters. |
| `updateTime` | `string` | Output only. The last time this custom constraint was updated. This represents the last time that the `CreateCustomConstraint` or `UpdateCustomConstraint` RPC was called |
| `actionType` | `string` | Allow or deny type. |
| `condition` | `string` | Org policy condition/expression. For example: `resource.instanceName.matches("[production\|test]_.*_(\d)+")` or, `resource.management.auto_upgrade == true` The max length of the condition is 1000 characters. |
| `displayName` | `string` | One line display name for the UI. The max length of the display_name is 200 characters. |
| `methodTypes` | `array` | All the operations being applied for this constraint. |
| `resourceTypes` | `array` | Immutable. The resource instance type on which this policy applies. Format will be of the form : `/` Example: * `compute.googleapis.com/Instance`. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_custom_constraints_get` | `SELECT` | `customConstraintsId, organizationsId` | Gets a custom constraint. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the custom constraint does not exist. |
| `organizations_custom_constraints_list` | `SELECT` | `organizationsId` | Retrieves all of the custom constraints that exist on a particular organization resource. |
| `organizations_custom_constraints_create` | `INSERT` | `organizationsId` | Creates a custom constraint. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the organization does not exist. Returns a `google.rpc.Status` with `google.rpc.Code.ALREADY_EXISTS` if the constraint already exists on the given organization. |
| `organizations_custom_constraints_delete` | `DELETE` | `customConstraintsId, organizationsId` | Deletes a custom constraint. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. |
| `_organizations_custom_constraints_list` | `EXEC` | `organizationsId` | Retrieves all of the custom constraints that exist on a particular organization resource. |
| `organizations_custom_constraints_patch` | `EXEC` | `customConstraintsId, organizationsId` | Updates a custom constraint. Returns a `google.rpc.Status` with `google.rpc.Code.NOT_FOUND` if the constraint does not exist. Note: the supplied policy will perform a full overwrite of all fields. |
