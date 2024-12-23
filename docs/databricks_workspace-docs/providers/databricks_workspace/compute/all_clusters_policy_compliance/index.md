---
title: all_clusters_policy_compliance
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - all_clusters_policy_compliance
  - compute
  - databricks_workspace
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Databricks resources using SQL
custom_edit_url: null
image: /img/providers/databricks_workspace/stackql-databricks-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Operations on a <code>all_clusters_policy_compliance</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>all_clusters_policy_compliance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.all_clusters_policy_compliance" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="cluster_id" /> | `string` |
| <CopyableCode code="is_compliant" /> | `boolean` |
| <CopyableCode code="violations" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="listcompliance" /> | `SELECT` | <CopyableCode code="policy_id, deployment_name" /> | Returns the policy compliance status of all clusters that use a given policy. Clusters could be out of compliance if their policy was updated after the cluster was last edited. |

## `SELECT` examples

```sql
SELECT
cluster_id,
is_compliant,
violations
FROM databricks_workspace.compute.all_clusters_policy_compliance
WHERE policy_id = '{{ policy_id }}' AND
deployment_name = '{{ deployment_name }}';
```
