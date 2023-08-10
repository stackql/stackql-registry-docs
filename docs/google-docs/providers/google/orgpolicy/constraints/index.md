---
title: constraints
hide_title: false
hide_table_of_contents: false
keywords:
  - constraints
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
<tr><td><b>Name</b></td><td><code>constraints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.orgpolicy.constraints</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Immutable. The resource name of the constraint. Must be in one of the following forms: * `projects/&#123;project_number&#125;/constraints/&#123;constraint_name&#125;` * `folders/&#123;folder_id&#125;/constraints/&#123;constraint_name&#125;` * `organizations/&#123;organization_id&#125;/constraints/&#123;constraint_name&#125;` For example, "/projects/123/constraints/compute.disableSerialPortAccess". |
| `description` | `string` | Detailed description of what this constraint controls as well as how and where it is enforced. Mutable. |
| `supportsDryRun` | `boolean` | Shows if dry run is supported for this constraint or not. |
| `booleanConstraint` | `object` | A constraint that is either enforced or not. For example, a constraint `constraints/compute.disableSerialPortAccess`. If it is enforced on a VM instance, serial port connections will not be opened to that instance. |
| `constraintDefault` | `string` | The evaluation behavior of this constraint in the absence of a policy. |
| `displayName` | `string` | The human readable name. Mutable. |
| `listConstraint` | `object` | A constraint that allows or disallows a list of string values, which are configured by an Organization Policy administrator with a policy. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `folders_constraints_list` | `SELECT` | `foldersId` |
| `organizations_constraints_list` | `SELECT` | `organizationsId` |
| `projects_constraints_list` | `SELECT` | `projectsId` |
| `_folders_constraints_list` | `EXEC` | `foldersId` |
| `_organizations_constraints_list` | `EXEC` | `organizationsId` |
| `_projects_constraints_list` | `EXEC` | `projectsId` |
