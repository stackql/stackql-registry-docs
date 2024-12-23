---
title: cluster_policy_compliance
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - cluster_policy_compliance
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

Operations on a <code>cluster_policy_compliance</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_policy_compliance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.compute.cluster_policy_compliance" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="is_compliant" /> | `boolean` |
| <CopyableCode code="violations" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getcompliance" /> | `SELECT` | <CopyableCode code="cluster_id, deployment_name" /> | Returns the policy compliance status of a cluster. Clusters could be out of compliance if their policy was updated after the cluster was last edited. |
| <CopyableCode code="enforcecompliance" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | Updates a cluster to be compliant with the current version of its policy. A cluster can be updated if it is in a |

## `SELECT` examples

```sql
SELECT
is_compliant,
violations
FROM databricks_workspace.compute.cluster_policy_compliance
WHERE cluster_id = '{{ cluster_id }}' AND
deployment_name = '{{ deployment_name }}';
```

## `REPLACE` example

Replaces a <code>cluster_policy_compliance</code> resource.

```sql
/*+ update */
REPLACE databricks_workspace.compute.cluster_policy_compliance
SET { field = value }
WHERE deployment_name = '{{ deployment_name }}';
```
