---
title: provisioned_cluster_instances_user_kubeconfigs
hide_title: false
hide_table_of_contents: false
keywords:
  - provisioned_cluster_instances_user_kubeconfigs
  - hybrid_aks
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

Creates, updates, deletes, gets or lists a <code>provisioned_cluster_instances_user_kubeconfigs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>provisioned_cluster_instances_user_kubeconfigs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hybrid_aks.provisioned_cluster_instances_user_kubeconfigs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Operation Id |
| <CopyableCode code="name" /> | `string` | Operation Name |
| <CopyableCode code="error" /> | `object` |  |
| <CopyableCode code="properties" /> | `object` |  |
| <CopyableCode code="resourceId" /> | `string` | ARM Resource Id of the provisioned cluster instance |
| <CopyableCode code="status" /> | `string` | Provisioning state of the resource |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="connectedClusterResourceUri" /> | Lists the user credentials of the provisioned cluster (can only be used within private network) |

## `SELECT` examples

Lists the user credentials of the provisioned cluster (can only be used within private network)


```sql
SELECT
id,
name,
error,
properties,
resourceId,
status
FROM azure.hybrid_aks.provisioned_cluster_instances_user_kubeconfigs
WHERE connectedClusterResourceUri = '{{ connectedClusterResourceUri }}';
```