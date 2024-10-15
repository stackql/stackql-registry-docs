---
title: requests
hide_title: false
hide_table_of_contents: false
keywords:
  - requests
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

Creates, updates, deletes, gets or lists a <code>requests</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.billing.requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | A request submitted by a user to manage billing. Users with an owner role on the scope can approve or decline these requests. |
| <CopyableCode code="tags" /> | `object` | Dictionary of metadata associated with the resource. It may not be populated for all resource types. Maximum key/value length supported of 256 characters. Keys/value should not empty value nor null. Keys can not contain < > % & \ ? / |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="billingRequestName" /> | Gets a billing request by its ID. |
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountName" /> | The list of billing requests submitted for the billing account. |
| <CopyableCode code="list_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName" /> | The list of billing requests submitted for the billing profile. |
| <CopyableCode code="list_by_customer" /> | `SELECT` | <CopyableCode code="billingAccountName, billingProfileName, customerName" /> | The list of billing requests submitted for the customer. |
| <CopyableCode code="list_by_user" /> | `SELECT` | <CopyableCode code="" /> | The list of billing requests submitted by a user. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="billingRequestName" /> | Create or update a billing request. |

## `SELECT` examples

The list of billing requests submitted by a user.


```sql
SELECT
properties,
tags
FROM azure.billing.requests
;
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>requests</code> resource.

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
INSERT INTO azure.billing.requests (
billingRequestName,
tags,
properties
)
SELECT 
'{{ billingRequestName }}',
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
        - name: additionalInformation
          value: object
        - name: reviewedBy
          value: string
        - name: reviewalDate
          value: string
        - name: billingAccountId
          value: string
        - name: billingAccountName
          value: string
        - name: billingAccountDisplayName
          value: string
        - name: billingAccountPrimaryBillingTenantId
          value: string
        - name: billingProfileId
          value: string
        - name: billingProfileName
          value: string
        - name: billingProfileDisplayName
          value: string
        - name: createdBy
          value: string
        - name: creationDate
          value: string
        - name: expirationDate
          value: string
        - name: decisionReason
          value: string
        - name: invoiceSectionId
          value: string
        - name: invoiceSectionName
          value: string
        - name: invoiceSectionDisplayName
          value: string
        - name: customerId
          value: string
        - name: customerName
          value: string
        - name: customerDisplayName
          value: string
        - name: subscriptionId
          value: string
        - name: subscriptionName
          value: string
        - name: subscriptionDisplayName
          value: string
        - name: justification
          value: string
        - name: recipients
          value:
            - - name: tenantId
                value: string
              - name: objectId
                value: string
              - name: upn
                value: string
        - name: requestScope
          value: string
        - name: billingScope
          value: string
        - name: status
          value: string
        - name: type
          value: string
        - name: lastUpdatedBy
          value: string
        - name: lastUpdatedDate
          value: string

```
</TabItem>
</Tabs>
