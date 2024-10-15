---
title: deny_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - deny_assignments
  - authorization
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

Creates, updates, deletes, gets or lists a <code>deny_assignments</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deny_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.authorization.deny_assignments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The deny assignment ID. |
| <CopyableCode code="name" /> | `string` | The deny assignment name. |
| <CopyableCode code="properties" /> | `object` | Deny assignment properties. |
| <CopyableCode code="type" /> | `string` | The deny assignment type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="denyAssignmentId, scope" /> | Get the specified deny assignment. |
| <CopyableCode code="get_by_id" /> | `SELECT` | <CopyableCode code="denyAssignmentId" /> | Gets a deny assignment by ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all deny assignments for the subscription. |
| <CopyableCode code="list_for_resource" /> | `SELECT` | <CopyableCode code="parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId" /> | Gets deny assignments for a resource. |
| <CopyableCode code="list_for_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Gets deny assignments for a resource group. |
| <CopyableCode code="list_for_scope" /> | `SELECT` | <CopyableCode code="scope" /> | Gets deny assignments for a scope. |

## `SELECT` examples

Gets deny assignments for a scope.


```sql
SELECT
id,
name,
properties,
type
FROM azure.authorization.deny_assignments
WHERE scope = '{{ scope }}';
```