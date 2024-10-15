---
title: policies_by_customers
hide_title: false
hide_table_of_contents: false
keywords:
  - policies_by_customers
  - billing
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

Creates, updates, deletes, gets or lists a <code>policies_by_customers</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>policies_by_customers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.policies_by_customers" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="billingAccountName, billingProfileName, customerName" /> | Updates the policies for a customer. This operation is supported only for billing accounts with agreement type Microsoft Partner Agreement. |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>policies_by_customers</code> resource.

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
INSERT INTO azure.billing.policies_by_customers (
billingAccountName,
billingProfileName,
customerName,
tags,
properties
)
SELECT 
'{{ billingAccountName }}',
'{{ billingProfileName }}',
'{{ customerName }}',
'{{ tags }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: tags
      value: object
    - name: properties
      value:
        - name: provisioningState
          value: string
        - name: viewCharges
          value: string
        - name: policies
          value:
            - - name: name
                value: string
              - name: value
                value: string
              - name: policyType
                value: string
              - name: scope
                value: string

```
</TabItem>
</Tabs>
