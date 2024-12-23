---
title: resource_quotas
hide_title: false
hide_table_of_contents: false
keywords:
  - Databricks
  - resource_quotas
  - unitycatalog
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

Operations on a <code>resource_quotas</code> resource.  

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource_quotas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="databricks_workspace.unitycatalog.resource_quotas" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="last_refreshed_at" /> | `integer` |
| <CopyableCode code="parent_full_name" /> | `string` |
| <CopyableCode code="parent_securable_type" /> | `string` |
| <CopyableCode code="quota_count" /> | `integer` |
| <CopyableCode code="quota_limit" /> | `integer` |
| <CopyableCode code="quota_name" /> | `string` |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getquota" /> | `SELECT` | <CopyableCode code="parent_full_name, parent_securable_type, quota_name, deployment_name" /> | The GetQuota API returns usage information for a single resource quota, defined as a child-parent pair. This API also refreshes the quota count if it is out of date. Refreshes are triggered asynchronously. The updated count might not be returned in the first call. |
| <CopyableCode code="listquotas" /> | `SELECT` | <CopyableCode code="deployment_name" /> | ListQuotas returns all quota values under the metastore. There are no SLAs on the freshness of the counts returned. This API does not trigger a refresh of quota counts. |

## `SELECT` examples

<Tabs
    defaultValue="listquotas"
    values={[
        { label: 'resource_quotas (listquotas)', value: 'listquotas' },
        { label: 'resource_quotas (getquota)', value: 'getquota' }
    ]
}>
<TabItem value="listquotas">

```sql
SELECT
last_refreshed_at,
parent_full_name,
parent_securable_type,
quota_count,
quota_limit,
quota_name
FROM databricks_workspace.unitycatalog.resource_quotas
WHERE deployment_name = '{{ deployment_name }}';
```

</TabItem>
<TabItem value="getquota">

```sql
SELECT
last_refreshed_at,
parent_full_name,
parent_securable_type,
quota_count,
quota_limit,
quota_name
FROM databricks_workspace.unitycatalog.resource_quotas
WHERE parent_full_name = '{{ parent_full_name }}' AND
parent_securable_type = '{{ parent_securable_type }}' AND
quota_name = '{{ quota_name }}' AND
deployment_name = '{{ deployment_name }}';
```

</TabItem>
</Tabs>
