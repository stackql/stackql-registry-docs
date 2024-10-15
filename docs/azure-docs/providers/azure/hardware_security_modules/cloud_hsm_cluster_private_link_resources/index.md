---
title: cloud_hsm_cluster_private_link_resources
hide_title: false
hide_table_of_contents: false
keywords:
  - cloud_hsm_cluster_private_link_resources
  - hardware_security_modules
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

Creates, updates, deletes, gets or lists a <code>cloud_hsm_cluster_private_link_resources</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cloud_hsm_cluster_private_link_resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.hardware_security_modules.cloud_hsm_cluster_private_link_resources" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}" |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | Properties of a private link resource. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_cloud_hsm_cluster" /> | `SELECT` | <CopyableCode code="cloudHsmClusterName, resourceGroupName, subscriptionId" /> | Gets the private link resources supported for the Cloud Hsm Cluster. |

## `SELECT` examples

Gets the private link resources supported for the Cloud Hsm Cluster.


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.hardware_security_modules.cloud_hsm_cluster_private_link_resources
WHERE cloudHsmClusterName = '{{ cloudHsmClusterName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```