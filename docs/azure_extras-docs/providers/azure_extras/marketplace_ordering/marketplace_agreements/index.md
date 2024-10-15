---
title: marketplace_agreements
hide_title: false
hide_table_of_contents: false
keywords:
  - marketplace_agreements
  - marketplace_ordering
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

Creates, updates, deletes, gets or lists a <code>marketplace_agreements</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>marketplace_agreements</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.marketplace_ordering.marketplace_agreements" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_marketplace_agreements', value: 'view', },
        { label: 'marketplace_agreements', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Resource ID. |
| <CopyableCode code="name" /> | `text` | Resource name. |
| <CopyableCode code="accepted" /> | `text` | field from the `properties` object |
| <CopyableCode code="license_text_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="marketplace_terms_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="offerId" /> | `text` | field from the `properties` object |
| <CopyableCode code="offerType" /> | `text` | field from the `properties` object |
| <CopyableCode code="plan" /> | `text` | field from the `properties` object |
| <CopyableCode code="planId" /> | `text` | field from the `properties` object |
| <CopyableCode code="privacy_policy_link" /> | `text` | field from the `properties` object |
| <CopyableCode code="product" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisher" /> | `text` | field from the `properties` object |
| <CopyableCode code="publisherId" /> | `text` | field from the `properties` object |
| <CopyableCode code="retrieve_datetime" /> | `text` | field from the `properties` object |
| <CopyableCode code="signature" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Resource type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="properties" /> | `object` | Agreement Terms definition |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Resource type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="offerId, offerType, planId, publisherId, subscriptionId" /> | Get marketplace terms. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | List marketplace agreements in the subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="offerId, offerType, planId, publisherId, subscriptionId" /> | Save marketplace terms. |
| <CopyableCode code="cancel" /> | `EXEC` | <CopyableCode code="offerId, planId, publisherId, subscriptionId" /> | Cancel marketplace terms. |
| <CopyableCode code="sign" /> | `EXEC` | <CopyableCode code="offerId, planId, publisherId, subscriptionId" /> | Sign marketplace terms. |

## `SELECT` examples

List marketplace agreements in the subscription.

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_marketplace_agreements', value: 'view', },
        { label: 'marketplace_agreements', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accepted,
license_text_link,
marketplace_terms_link,
offerId,
offerType,
plan,
planId,
privacy_policy_link,
product,
publisher,
publisherId,
retrieve_datetime,
signature,
subscriptionId,
system_data,
type
FROM azure_extras.marketplace_ordering.vw_marketplace_agreements
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure_extras.marketplace_ordering.marketplace_agreements
WHERE subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>marketplace_agreements</code> resource.

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
INSERT INTO azure_extras.marketplace_ordering.marketplace_agreements (
offerId,
offerType,
planId,
publisherId,
subscriptionId,
properties
)
SELECT 
'{{ offerId }}',
'{{ offerType }}',
'{{ planId }}',
'{{ publisherId }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: publisher
          value: string
        - name: product
          value: string
        - name: plan
          value: string
        - name: licenseTextLink
          value: string
        - name: privacyPolicyLink
          value: string
        - name: marketplaceTermsLink
          value: string
        - name: retrieveDatetime
          value: string
        - name: signature
          value: string
        - name: accepted
          value: boolean
    - name: systemData
      value:
        - name: createdBy
          value: string
        - name: createdByType
          value: string
        - name: createdAt
          value: string
        - name: lastModifiedBy
          value: string
        - name: lastModifiedByType
          value: string
        - name: lastModifiedAt
          value: string
    - name: id
      value: string
    - name: name
      value: string
    - name: type
      value: string

```
</TabItem>
</Tabs>
