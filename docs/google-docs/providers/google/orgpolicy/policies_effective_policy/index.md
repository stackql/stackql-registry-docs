---
title: policies_effective_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - policies_effective_policy
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

Creates, updates, deletes or gets an <code>policies_effective_policy</code> resource or lists <code>policies_effective_policy</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies_effective_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.orgpolicy.policies_effective_policy" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Immutable. The resource name of the policy. Must be one of the following forms, where `constraint_name` is the name of the constraint which this policy configures: * `projects/{project_number}/policies/{constraint_name}` * `folders/{folder_id}/policies/{constraint_name}` * `organizations/{organization_id}/policies/{constraint_name}` For example, `projects/123/policies/compute.disableSerialPortAccess`. Note: `projects/{project_id}/policies/{constraint_name}` is also an acceptable name for API requests, but responses will return the name using the equivalent project number. |
| <CopyableCode code="alternate" /> | `object` | Similar to PolicySpec but with an extra 'launch' field for launch reference. The PolicySpec here is specific for dry-run/darklaunch. |
| <CopyableCode code="dryRunSpec" /> | `object` | Defines a Google Cloud policy specification which is used to specify constraints for configurations of Google Cloud resources. |
| <CopyableCode code="etag" /> | `string` | Optional. An opaque tag indicating the current state of the policy, used for concurrency control. This 'etag' is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. |
| <CopyableCode code="spec" /> | `object` | Defines a Google Cloud policy specification which is used to specify constraints for configurations of Google Cloud resources. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="folders_policies_get_effective_policy" /> | `SELECT` | <CopyableCode code="foldersId, policiesId" /> | Gets the effective policy on a resource. This is the result of merging policies in the resource hierarchy and evaluating conditions. The returned policy will not have an `etag` or `condition` set because it is an evaluated policy across multiple resources. Subtrees of Resource Manager resource hierarchy with 'under:' prefix will not be expanded. |
| <CopyableCode code="organizations_policies_get_effective_policy" /> | `SELECT` | <CopyableCode code="organizationsId, policiesId" /> | Gets the effective policy on a resource. This is the result of merging policies in the resource hierarchy and evaluating conditions. The returned policy will not have an `etag` or `condition` set because it is an evaluated policy across multiple resources. Subtrees of Resource Manager resource hierarchy with 'under:' prefix will not be expanded. |
| <CopyableCode code="projects_policies_get_effective_policy" /> | `SELECT` | <CopyableCode code="policiesId, projectsId" /> | Gets the effective policy on a resource. This is the result of merging policies in the resource hierarchy and evaluating conditions. The returned policy will not have an `etag` or `condition` set because it is an evaluated policy across multiple resources. Subtrees of Resource Manager resource hierarchy with 'under:' prefix will not be expanded. |

## `SELECT` examples

Gets the effective policy on a resource. This is the result of merging policies in the resource hierarchy and evaluating conditions. The returned policy will not have an `etag` or `condition` set because it is an evaluated policy across multiple resources. Subtrees of Resource Manager resource hierarchy with 'under:' prefix will not be expanded.

```sql
SELECT
name,
alternate,
dryRunSpec,
etag,
spec
FROM google.orgpolicy.policies_effective_policy
WHERE foldersId = '{{ foldersId }}'
AND policiesId = '{{ policiesId }}'; 
```
