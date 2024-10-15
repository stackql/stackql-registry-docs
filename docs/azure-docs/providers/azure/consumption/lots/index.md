---
title: lots
hide_title: false
hide_table_of_contents: false
keywords:
  - lots
  - consumption
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

Creates, updates, deletes, gets or lists a <code>lots</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>lots</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.consumption.lots" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource Id. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="eTag" /> | `string` | eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not. |
| <CopyableCode code="properties" /> | `object` | The lot properties. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_by_billing_account" /> | `SELECT` | <CopyableCode code="billingAccountId" /> | Lists all Microsoft Azure consumption commitments for a billing account. The API is only supported for Microsoft Customer Agreements (MCA) and Direct Enterprise Agreement (EA)  billing accounts. |
| <CopyableCode code="list_by_billing_profile" /> | `SELECT` | <CopyableCode code="billingAccountId, billingProfileId" /> | Lists all Azure credits for a billing account or a billing profile. The API is only supported for Microsoft Customer Agreements (MCA) billing accounts. |
| <CopyableCode code="list_by_customer" /> | `SELECT` | <CopyableCode code="billingAccountId, customerId" /> | Lists all Azure credits for a customer. The API is only supported for Microsoft Partner  Agreements (MPA) billing accounts. |

## `SELECT` examples

Lists all Microsoft Azure consumption commitments for a billing account. The API is only supported for Microsoft Customer Agreements (MCA) and Direct Enterprise Agreement (EA)  billing accounts.


```sql
SELECT
id,
name,
eTag,
properties,
type
FROM azure.consumption.lots
WHERE billingAccountId = '{{ billingAccountId }}';
```