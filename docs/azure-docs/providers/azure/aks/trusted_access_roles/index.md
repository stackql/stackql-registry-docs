---
title: trusted_access_roles
hide_title: false
hide_table_of_contents: false
keywords:
  - trusted_access_roles
  - aks
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

Creates, updates, deletes, gets or lists a <code>trusted_access_roles</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>trusted_access_roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aks.trusted_access_roles" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of role, name is unique under a source resource type |
| <CopyableCode code="rules" /> | `array` | List of rules for the role. This maps to 'rules' property of [Kubernetes Cluster Role](https://kubernetes.io/docs/reference/kubernetes-api/authorization-resources/cluster-role-v1/#ClusterRole). |
| <CopyableCode code="sourceResourceType" /> | `string` | Resource type of Azure resource |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> |  |

## `SELECT` examples




```sql
SELECT
name,
rules,
sourceResourceType
FROM azure.aks.trusted_access_roles
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```