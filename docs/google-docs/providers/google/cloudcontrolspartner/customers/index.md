
---
title: customers
hide_title: false
hide_table_of_contents: false
keywords:
  - customers
  - cloudcontrolspartner
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

Creates, updates, deletes or gets an <code>customer</code> resource or lists <code>customers</code> in a region

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>customers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="google.cloudcontrolspartner.customers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Identifier. Format: `organizations/{organization}/locations/{location}/customers/{customer}` |
| <CopyableCode code="customerOnboardingState" /> | `object` | Container for customer onboarding steps |
| <CopyableCode code="displayName" /> | `string` | Required. Display name for the customer |
| <CopyableCode code="isOnboarded" /> | `boolean` | Output only. Indicates whether a customer is fully onboarded |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="customersId, locationsId, organizationsId" /> | Gets details of a single customer |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists customers of a partner identified by its Google Cloud organization ID |

## `SELECT` examples

Lists customers of a partner identified by its Google Cloud organization ID

```sql
SELECT
name,
customerOnboardingState,
displayName,
isOnboarded
FROM google.cloudcontrolspartner.customers
WHERE locationsId = '{{ locationsId }}'
AND organizationsId = '{{ organizationsId }}'; 
```
