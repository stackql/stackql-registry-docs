---
title: job_compliance
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - job_compliance
  - workflows
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

Operations on a <code>job_compliance</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>job_compliance</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.workflows.job_compliance" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="is_compliant" /> | `boolean` |
| <CopyableCode code="job_id" /> | `integer` |
| <CopyableCode code="violations" /> | `object` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getcompliance" /> | `SELECT` | <CopyableCode code="job_id, deployment_name" /> | Returns the policy compliance status of a job. Jobs could be out of compliance if a cluster policy they use was updated after the job was last edited and some of its job clusters no longer comply with their updated policies. |
| <CopyableCode code="listcompliance" /> | `SELECT` | <CopyableCode code="policy_id, deployment_name" /> | Returns the policy compliance status of all jobs that use a given policy. Jobs could be out of compliance if a cluster policy they use was updated after the job was last edited and its job clusters no longer comply with the updated policy. |
| <CopyableCode code="enforcecompliance" /> | `REPLACE` | <CopyableCode code="deployment_name" /> | Updates a job so the job clusters that are created when running the job (specified in |

## `SELECT` examples

<Tabs
    defaultValue="getcompliance"
    values={[
        { label: 'job_compliance (getcompliance)', value: 'getcompliance' },
        { label: 'job_compliance (listcompliance)', value: 'listcompliance' }
    ]
}>
<TabItem value="getcompliance">

```sql
SELECT
is_compliant,
job_id,
violations
FROM databricks_workspace.workflows.job_compliance
WHERE job_id = '{{ job_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="listcompliance">

```sql
SELECT
is_compliant,
job_id,
violations
FROM databricks_workspace.workflows.job_compliance
WHERE policy_id = '{{ policy_id }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>

## `REPLACE` example

Replaces a <code>job_compliance</code> resource.

```sql
/*+ update */
-- replace field1, field2, etc. with the fields you want to update
REPLACE databricks_workspace.workflows.job_compliance
SET field1 = '{ value1 }',
field2 = '{ value2 }', ...
WHERE deployment_name = '{{ deployment_name }}';
```
