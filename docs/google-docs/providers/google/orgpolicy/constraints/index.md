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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>constraints</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>constraints</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.orgpolicy.constraints" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the constraint. Must be in one of the following forms: * `projects/{project_number}/constraints/{constraint_name}` * `folders/{folder_id}/constraints/{constraint_name}` * `organizations/{organization_id}/constraints/{constraint_name}` For example, "/projects/123/constraints/compute.disableSerialPortAccess". |
| <CopyableCode code="description" /> | `string` | Detailed description of what this constraint controls as well as how and where it is enforced. Mutable. |
| <CopyableCode code="booleanConstraint" /> | `object` | A constraint that is either enforced or not. For example, a constraint `constraints/compute.disableSerialPortAccess`. If it is enforced on a VM instance, serial port connections will not be opened to that instance. |
| <CopyableCode code="constraintDefault" /> | `string` | The evaluation behavior of this constraint in the absence of a policy. |
| <CopyableCode code="displayName" /> | `string` | The human readable name. Mutable. |
| <CopyableCode code="listConstraint" /> | `object` | A constraint that allows or disallows a list of string values, which are configured by an Organization Policy administrator with a policy. |
| <CopyableCode code="supportsDryRun" /> | `boolean` | Shows if dry run is supported for this constraint or not. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_constraints_list" /> | `SELECT` | <CopyableCode code="foldersId" /> | Lists constraints that could be applied on the specified resource. |
| <CopyableCode code="organizations_constraints_list" /> | `SELECT` | <CopyableCode code="organizationsId" /> | Lists constraints that could be applied on the specified resource. |
| <CopyableCode code="projects_constraints_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists constraints that could be applied on the specified resource. |

## `SELECT` examples

Lists constraints that could be applied on the specified resource.

```sql
SELECT
name,
description,
booleanConstraint,
constraintDefault,
displayName,
listConstraint,
supportsDryRun
FROM google.orgpolicy.constraints
WHERE foldersId = '{{ foldersId }}'; 
```
