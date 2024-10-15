---
title: detailed_cost_reports
hide_title: false
hide_table_of_contents: false
keywords:
  - detailed_cost_reports
  - cost_management
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

Creates, updates, deletes, gets or lists a <code>detailed_cost_reports</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>detailed_cost_reports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.cost_management.detailed_cost_reports" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_operation" /> | `INSERT` | <CopyableCode code="scope" /> | Generates the detailed cost report for provided date range, billing period(only enterprise customers) or Invoice ID asynchronously at a certain scope. Call returns a 202 with header Azure-Consumption-AsyncOperation providing a link to the operation created. A call on the operation will provide the status and if the operation is completed the blob file where generated detailed cost report is being stored. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>detailed_cost_reports</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.cost_management.detailed_cost_reports (
scope,
metric,
timePeriod,
billingPeriod,
invoiceId,
customerId
)
SELECT 
'{{ scope }}',
'{{ metric }}',
'{{ timePeriod }}',
'{{ billingPeriod }}',
'{{ invoiceId }}',
'{{ customerId }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: metric
      value: string
    - name: timePeriod
      value:
        - name: start
          value: string
        - name: end
          value: string
    - name: billingPeriod
      value: string
    - name: invoiceId
      value: string
    - name: customerId
      value: string

```
</TabItem>
</Tabs>
