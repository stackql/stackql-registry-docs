---
title: private_store_approval_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - private_store_approval_requests
  - marketplace
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

Creates, updates, deletes, gets or lists a <code>private_store_approval_requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>private_store_approval_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace.private_store_approval_requests" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="privateStoreId, requestApprovalId" /> | Create approval request |

## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>private_store_approval_requests</code> resource.

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
INSERT INTO azure_extras.marketplace.private_store_approval_requests (
privateStoreId,
requestApprovalId,
properties
)
SELECT 
'{{ privateStoreId }}',
'{{ requestApprovalId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: []
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedAt
          value: string
    - name: properties
      value:
        - name: offerId
          value: string
        - name: offerDisplayName
          value: string
        - name: publisherId
          value: string
        - name: plansDetails
          value:
            - - name: planId
                value: string
              - name: status
                value: string
              - name: requestDate
                value: string
              - name: justification
                value: string
              - name: subscriptionId
                value: string
              - name: subscriptionName
                value: string
        - name: isClosed
          value: boolean
        - name: messageCode
          value: integer

```
</TabItem>
</Tabs>
