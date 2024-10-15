---
title: managed_clusters_kubernetes_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_clusters_kubernetes_versions
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

Creates, updates, deletes, gets or lists a <code>managed_clusters_kubernetes_versions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managed_clusters_kubernetes_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.aks.managed_clusters_kubernetes_versions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="values" /> | `array` | Array of AKS supported Kubernetes versions. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="location, subscriptionId" /> | Contains extra metadata on the version, including supported patch versions, capabilities, available upgrades, and details on preview status of the version |

## `SELECT` examples

Contains extra metadata on the version, including supported patch versions, capabilities, available upgrades, and details on preview status of the version


```sql
SELECT
values
FROM azure.aks.managed_clusters_kubernetes_versions
WHERE location = '{{ location }}'
AND subscriptionId = '{{ subscriptionId }}';
```